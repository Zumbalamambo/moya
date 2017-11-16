#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
import sys, select, termios, tty
import cv2
import numpy as np
import time as time
from numpy.linalg import inv

#8.15 edit: Fixed speed, added adjusting speed function for hard turns. Added feature so
#           robot doesn't go straight when it detects no line (remembers old value)
#           Fixed bug in which program crashed due to exceeding range and empty arrays
#8.17 edit: Fixed bug where another lane was detected (Added simple break for now)
#8.21 edit: deleted some lines
#print velocities
def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

controlSpeed=0
controlTurn=0
targetSpeed=0
targetTurn=0

def publishTwist():
    # if targetSpeed > controlSpeed:
    #     controlSpeed = min( targetSpeed, controlSpeed + 0.02 )
    # elif targetSpeed < controlSpeed:
    #     controlSpeed = max( targetSpeed, controlSpeed - 0.02 )
    # if targetTurn > controlTurn:
    #     controlTurn = min( targetTurn, controlTurn + 0.1 )
    # elif targetTurn < controlTurn:
    #     controlTurn = max( targetTurn, controlTurn - 0.1 )
    controlTurn=targetTurn;controlSpeed=targetSpeed
    twist=Twist()
    twist.linear.x=controlSpeed;twist.linear.y=0;twist.linear.z=0
    twist.angular.x=0;twist.angular.y=0;twist.angular.z=controlTurn
    twistPub.publish(twist)

def eStop():
    twist=Twist()
    twist.linear.x=0;twist.linear.y=0;twist.linear.z=0
    twist.angular.x=0;twist.angular.y=0;twist.angular.z=0
    twistPub.publish(twist)

#define search y pixel value
ypixel = 440
#homography matrix found using the eigenvector method. Converts pixel data for our setup to real life coordinates
homography = [[1.43267564599360e-05, 0.000137246685914842, 0.820559009050558],
            [-0.00127160762630245,-2.31921046236619e-05,0.571559600076394],
            [-1.49366228754847e-07,9.53570215882248e-06,-0.000948456529749349]]

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 864)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)


#Find all edges on the line of y=ypixel using the canny edge image. Input is canny edge image
def edgefinder(img):
    #initialize empty array and counter
    array1 = []
    counter=0
    for x in range(0,864):
        if img[ypixel,x] == 255:
            if len(array1)==0:
                array1.append(x)
            elif abs(x-array1[-1])<=1+counter:
                counter+=1
            else:
                array1.append(x)
    return array1

#check for white on the left side of an edge detected in edgefinder(), and yellow on the right side.
#uses a sample of 3x3 pixels
def checkcolor(edgearray, hsvimage):
    #define color ranges
    whiteline = 0
    yellowline=0
    lower_white = np.array([0,0,100],np.uint8)
    upper_white = np.array([180,100,255],np.uint8)
    lower_yellow = np.array([15,50,100],np.uint8)
    upper_yellow = np.array([40,255,255],np.uint8)

    maskyellow = cv2.inRange(hsvimage, lower_yellow, upper_yellow)

    cv2.imshow('maskyellow',maskyellow)
    for yellow in edgearray:
        colorboolean = []
        counter = 0
        # left side first
        for x in range(3):
            for y in range(3):
                if yellow-3>=0:
                    hsv=np.asarray(hsvimage[ypixel-x,yellow-y])
                    bool1= np.array_equiv(np.less_equal(hsv,upper_yellow),[True, True, True])
                    bool2 = np.array_equiv(np.greater_equal(hsv,lower_yellow),[True, True, True])
                    if bool1 and bool2:
                        counter+=1
        if counter >=7:
            yellowline = yellow

    for whites in edgearray:
        colorboolean = []
        counter = 0
        # left side first
        for x in range(3):
            for y in range(3):
                if whites+8 <= 864:
                    hsv=np.asarray(hsvimage[ypixel-1+x,whites+5+y])
                    bool1= np.array_equiv(np.less_equal(hsv,upper_white),[True, True, True])
                    bool2 = np.array_equiv(np.greater_equal(hsv,lower_white),[True, True, True])
                    if bool1 and bool2:
                        counter+=1
        if counter >=8:
            if whites>yellowline:
                whiteline = whites
                break

    return whiteline,yellowline

#return list of point to line distances
def point_to_line_distance_white(x1,y1,x2,y2,white_x):
    white_distance = abs(x1-white_x)+abs(y1-ypixel)+abs(x2-white_x)+abs(y2-ypixel)
    return white_distance

def point_to_line_distance_yellow(x1,y1,x2,y2, yellow_x):
    yellow_distance = abs(x1-yellow_x)+abs(y1-ypixel)+abs(x2-yellow_x)+abs(y2-ypixel)
    return yellow_distance

def pixel2realcoordinate(point1, point2):
    point1.append(1)
    point2.append(1)
    point1_real_raw = np.matmul(homography, point1)
    point1_real = np.divide(point1_real_raw,point1_real_raw[2])
    point2_real_raw = np.matmul(homography,point2)
    point2_real = np.divide(point2_real_raw,point2_real_raw[2])
    return point1_real, point2_real

def goalpoint(point1, point2, projectionpoint, isleft):
    #point 2 is further point on coordinate system. Input is in real coordinate system. Isleft is Boolean
    deltaX = point2[0]-point1[0]
    deltaY = point2[1]-point1[1]
    angle = math.atan2(deltaY,deltaX)
    if isleft:
        angle = angle-(math.pi)/2.
    else:
        angle = angle+(math.pi)/2.
    addX = 130.*math.cos(angle)
    addY = 130.*math.sin(angle)
    goalpoint = [projectionpoint[0]+addX, projectionpoint[1]+addY]
    return goalpoint

def realcoordinate2pixel(point1):
    point1.append(1)
    nphomography = np.array(homography)
    point1_pixel_raw = np.matmul(inv(np.matrix(nphomography)),point1)
    point1_pixel_real = np.divide(point1_pixel_raw, point1_pixel_raw[0,2])
    return point1_pixel_real

def getCoordinates():

    _, img = cap.read()
    #start timer
    startingtime = time.time()
    #resize image
    #img = cv2.resize(imgs,None,fx=1, fy=1, interpolation = cv2.INTER_AREA)

    hsvimage=cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #don't know why it's RGB, not BGR
    edges = cv2.Canny(img,100,200,apertureSize = 3)
    cv2.imshow('canny',edges)
    #cv2.imshow('canny', edges)
    array2 = edgefinder(edges)
    white_x_value, yellow_x_value=checkcolor(array2,hsvimage)
    #get image size. xsize is width, ysize is height. This can be reduced when video frame is set with constant values
    image_data = edges.shape
    ysize = int(image_data[0])
    xsize = int(image_data[1])

    pixel_offset = 30
    edges_roi1 = edges[ypixel-pixel_offset:ypixel+pixel_offset, 0:xsize]
    #Probabilistic hough transform method
    lines = cv2.HoughLinesP(edges_roi1,1,np.pi/180,10,minLineLength=5,maxLineGap=10)

    #initialize distance array for sorting
    distance_white = []
    distance_yellow = []

    #make array of distances between point and hough lines
    try:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            distance_white.append(point_to_line_distance_white(x1,y1,x2,y2,white_x_value))
            distance_yellow.append(point_to_line_distance_yellow(x1,y1,x2,y2,yellow_x_value))
    except TypeError:
           pass

    #tune the value 2000
    white_x_point_real, yellow_x_point_real = pixel2realcoordinate([white_x_value,ypixel],[yellow_x_value, ypixel])
    if len(distance_white) !=0:
        if min(distance_white)<2000 and white_x_value!=0:
            minimum_index_white = distance_white.index(min(distance_white))
            line_data = lines[minimum_index_white]
            x1_minw,y1_minw,x2_minw,y2_minw = line_data[0]
            cv2.line(img,(x1_minw,y1_minw+ypixel-pixel_offset),(x2_minw,y2_minw+ypixel-pixel_offset),(255,255,255),2)
            if y2_minw >= y1_minw:
                point1_white = [x2_minw,y2_minw+ypixel-pixel_offset]
                point2_white = [x1_minw,y1_minw+ypixel-pixel_offset]
            else:
                point1_white = [x1_minw,y1_minw+ypixel-pixel_offset]
                point2_white = [x2_minw,y2_minw+ypixel-pixel_offset]
            point1_real_white, point2_real_white = pixel2realcoordinate(point1_white, point2_white)
            goalpoint_right = goalpoint(point1_real_white, point2_real_white, white_x_point_real, False)
            goalpoint_right_pixel = realcoordinate2pixel(goalpoint_right)
            cv2.circle(img,(int(goalpoint_right_pixel[0,0]),int(goalpoint_right_pixel[0,1])), 7, (255,255,255), -1)
        else:
            goalpoint_right = [-10000,0]
    else:
        goalpoint_right = [-10000,0]

    if len(distance_yellow) !=0:
        if min(distance_yellow)<2000 and yellow_x_value!=0:
            minimum_index_yellow = distance_yellow.index(min(distance_yellow))
            line_data1 = lines[minimum_index_yellow]
            x1_miny,y1_miny,x2_miny,y2_miny = line_data1[0]
            cv2.line(img,(x1_miny,y1_miny+ypixel-pixel_offset),(x2_miny,y2_miny+ypixel-pixel_offset),(0,255,255),2)
            if y2_miny >= y1_miny:
                point1_yellow = [x2_miny,y2_miny+ypixel-pixel_offset]
                point2_yellow = [x1_miny,y1_miny+ypixel-pixel_offset]
            else:
                point1_yellow = [x1_miny,y1_miny+ypixel-pixel_offset]
                point2_yellow = [x2_miny,y2_miny+ypixel-pixel_offset]
            point1_real_yellow, point2_real_yellow = pixel2realcoordinate(point1_yellow, point2_yellow)
            goalpoint_left = goalpoint(point1_real_yellow, point2_real_yellow, yellow_x_point_real, True)
            goalpoint_left_pixel = realcoordinate2pixel(goalpoint_left)
            cv2.circle(img,(int(goalpoint_left_pixel[0,0]),int(goalpoint_left_pixel[0,1])), 6, (0,255,255), -1)
        else:
            goalpoint_left = [-10000,0]
    else:
        goalpoint_left = [-10000,0]

    if goalpoint_left[0] > goalpoint_right[0]:
        goalpoint_final = goalpoint_left
    else:
        goalpoint_final = goalpoint_right


    finishtime = time.time()

    print("Time taken to process:")
    print(finishtime-startingtime)
    print(goalpoint_final)
    # cv2.imshow('houghlines5.jpg',img)
    return goalpoint_final[0]/1000., goalpoint_final[1]/1000.,img

    #     k = cv2.waitKey(5) & 0xFF
    #     if k==27:
    #         break
    #
    # cv2.destroyAllWindows()
    # cap.release()
if __name__ == '__main__':
    rospy.init_node('practice_teleop')
    twistPub=rospy.Publisher('/cmd_vel',Twist,queue_size=5)
    rate=rospy.Rate(10) #10Hz
    x=0;y=0
    prevX=0;prevY=0
    errorNumber=0
    while(1):
        prevX=x;prevY=y

        x,y,img=getCoordinates()
        if x==-10:
            print (x)
            x=prevX;y=prevY;errorNumber=errorNumber+1
        else:
            errorNumber=0

        targetSpeed=0.2

        if y==0:
            targetTurn=0
            R=0
        else:
            R=(x*x+y*y)/2/y
            if abs(R)<0.7:
                targetSpeed=0.15
                R=R/1.2

            targetTurn=targetSpeed/R


        publishTwist()
        print vels(targetSpeed,targetTurn)
        print ("x %s\ty %s\tR %s " % (x,y,R))
        cv2.imshow('img',img)
        # cv2.waitKey(100)
        #cv2.destroyAllWindows()
        rate.sleep()

        k = cv2.waitKey(5) & 0xFF
        if k==27:
            eStop()
            break

    cv2.destroyAllWindows()
    cap.release()
    out.release()

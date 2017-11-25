# MOYA - Deep Learning 기반 사물인식 기술을 이용한 언어학습 보조로봇

<img align="center" width="537" height="311"
     title="moya logo" src="./moya.PNG">

## SNU 로봇인공지능만들기 Code for MOYA Robot


Install Tensorflow with GPU support using virtual env:
https://www.tensorflow.org/install/install_linux

Setup CUDA for Tensorflow GPU support:
http://docs.nvidia.com/cuda/cuda-installation-guide-linux/#axzz4VZnqTJ2A

## TO-DO:
### - [] Controlling Robot wheels
     -[] Rosserial + Arduino
     -[] Teleop
### - [] Object Recognition
    - [x] Train images by retraining Mobilenet
    - [x] Capture image with webcam and classify using retrained model
    - [] Output identified object to main
### - [] Hand Motion Detection
    - [x] Python wrapper for Intel RealSense + OpenCV
    - [] Calculate direction of hand
### - [] UI integration
    - [] Make everything work smoothly with UI
    - [] (Optional) Quiz Mode for users
    




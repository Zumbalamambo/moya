# Tensorflow Retrained Model

Retrained object recognition for Moya Project using TensorFlow and MobileNet. We are identifying: Apples, Flower Vase, Glasses, Remote Control, Shoes, Telephone, and Trump
Refer to: https://codelabs.developers.google.com/codelabs/tensorflow-for-poets 

## How To Retrain

Clone tensorflow for poets repository:
```
git clone https://github.com/googlecodelabs/tensorflow-for-poets-2
cd tensorflow-for-poets-2/tf_files
```
Download and extract training images from:
```
https://drive.google.com/file/d/1kQ5iSv5z1cFUyrcuzmON8OthHXl4kQML/view?usp=sharing
```
and test images from:
```
https://drive.google.com/file/d/1uWS6EZ7w-QfZLe1nkk3ZMpBy1W0Nt7bT/view?usp=sharing
```

Retrain the model with Mobilenet:

```
cd ..
python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/"$mobilenet_0.50_224" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture="mobilenet_0.50_224" \
  --image_dir=tf_files/images
```

Lastly, test the trained model.

```
python label_images.py
```

## On Raspberry Pi:
Running label_images.py doesn't do anything until it is triggered by a message on topic /capture_image. 
Publishes the highest matching result to /classify_image, which should be subscribed to by the UI




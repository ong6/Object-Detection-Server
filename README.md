# Deploy an Object-Detection-Server

![sample_website](./website_sample.jpg)
![sample_result](./sample/car_processed.jpg)
## Deploying an Object Detection Tool/Service

Implemented with a Client-Server Architecture

### Setup

- Clone into local directory
- Object detection is supported by mobilenet_v2/1 from google open images.
- Ensure that relevant dependencies that are needed are installed such as flask, numpy, pillow, matplotlib and tensorflow_hub.
- Start the server by running `python objectServer.py`
- Navigate to frontend by going to "http://127.0.0.1:5000/"
- The first image may take more time than the rest as it will have to load the model first.

### User Guide

A quick demo is shown here:
![Demo](./objectdetectiondemo.gif)

- Choose a picture file (must be jpg or png) and click submit.
- The image with a box applied will be shown to the user.
- To test another image just click choose file and upload again.
- Inference times are show on the website.

### Inference Times

Sample images and sample outputs are in the sample folder.

- Car = 0.0530s
- Cat = 0.0580s
- Dog = 0.0539s

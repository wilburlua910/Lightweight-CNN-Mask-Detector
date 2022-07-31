# Project Information 
##### This repository contains the source code, training scripts, and contents that is used to build, deploy the Capstone Project and the Conference papers.

## Capstone Project Title
![Alt text](https://media.giphy.com/media/2zsuidAcMx8gEDZCjS/giphy-downsized-large.gif)

### Real-Time Covid-19 Face mask detection: Edge Intelligence with Convolutional Neural Network (CNN) and Single Shot Detectors
Paper can be found here: ```./papers/(CSC3001_Capstone_Report__Final_Trimeter__Wilbur_Lua_Kai_Heng(1901839)```

## Conference Title (Accepted into 2022 IEEE 5th International Conference on Pattern Recognition and Artificial Intelligence)
### Deep Learning in IoT and Edge Computing for Safety Applications
Paper can be found here: ```./papers/PRAI.pdf```



## Motivation
- Current "Traditional" detectors (E.g. VGG-16, VGG-19, ResNet-50) have high amounts of trainable parameters leading to high computations, memory and power consumption (CPU, GPU, Network). 
- Contribute to Public Health and Safety applications by researching, experimenting and deploying an FMD system that can be deployed on the Edge (NVIDIA Jetson Nano)
- Edge Intelligence, bring Deep Learning onto Internet of Things (IoT) devices.

## Model training script are placed in ```/scripts/<Script_name>```

1. YOLOv5s Mask Detection Script -> ```/scripts/YOLOv5_TrainingScript.ipynb```
2. EfficientDet Mask Detection Script -> ```/scripts/EfficientDet_TrainingScript.ipynb```
3. Model Compression and Sparse Transfer Learning Script -> ```/scripts/Sparse_TransferLearning.ipynb```

## (Required) Installing PyTorch, Torch vision and OpenCV
### Scripts required to install dependencies on Edge Device - NVIDIA Jetson Nano
1. PyTorch installation Script -> ```/scripts/PyTorch_Torchvision.txt```
2. TorchVision installation Script -> ```/scripts/PyTorch_Torchvision.txt```
3. OpenCV installation Script (Requires to make SwapFile and Compile on-device) -> ```/scripts/OpenCV.txt```

## Miscellaneous scripts 
#### These are the scripts I wrote to help with Data-preprocessing.
1. Utils ```./utils/*```

### How to run the models on the Edge 
#### YOLOv5s model 

```python
cd ./yolov5-master
python3 detect.py --weights ./weights/CMFD_Best02.pt --source 0 
```
#### EfficientDet model
```python
cd ./EfficientDet
python3 efficientdet_test_videos.py
```






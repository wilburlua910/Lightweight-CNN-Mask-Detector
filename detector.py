
# import the opencv library
import cv2
import numpy as np
from time import time 
import torch
import os
  
class MaskDetector:

    def __init__(self, captureIndex, modelWeight):
        """
        :param CaptureIndex -> Index of camera (0,1,-1)
        :param modelWeight -> Path to the PyTorch pt E.g. CMFD_best02.pt
        """

        #User will pass camera index and model weights
        self.captureIndex = captureIndex
        self.modelWeight = modelWeight

        projectDir = "directory to yolov5"
    
        self.model = self.loadModel(modelWeight)
        self.classes = self.model.names

        print("Classes:" + str(self.classes))
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

        print("Using Device: ", self.device)

    def getVideoCapture(self):

        #Need to return a camera object 
        return cv2.VideoCapture(self.captureIndex)

    def loadModel(self, model_weight_path):

        print("Model weights path: " + model_weight_path)

        dirPath = os.path.join(os.getcwd(), "yolov5-master")
        print(dirPath)
        model = torch.hub.load(repo_or_dir=dirPath,model='custom', path= model_weight_path, source= 'local', force_reload=True)

        return model

    def scoreFrame(self, frame):

        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)

        print(results)

        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord

    def classToLabel(self, x):
        #Get the class string from the classess array 

        # E.g. ['dog', 'cat'] --> Pos 0 returns 'dog'
        return self.classes[int(x)]
    
    def plotBoxes(self, results, frame):

        labels, cord = results
        #Number of output labels
        n = len(labels)

        x_shape, y_shape = frame.shape[1], frame.shape[0]

        for i in range(n):
            row = cord[i]
            if row[4] >= 0.1:
                x1, y1, x2, y2 = int(row[0] *x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.classToLabel(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)

        return frame

    def __call__(self):
        cap = self.getVideoCapture()
        #assert cap.isOpened()
        while(True):
            ret, frame = cap.read()
            frame = cv2.resize(frame, (416, 416))

            #Calculate FPS
            startTime = time()
            results = self.scoreFrame(frame)
            frame = self.plotBoxes(results, frame)

            endTime = time()

            fps = 1/ np.round(endTime - startTime, 2)
            cv2.putText(frame, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)
            
            cv2.imshow('YOLOv5 Detection', frame)

            if cv2.waitKey(5) & 0xFF == 27:
                break
        
        #Clean up
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
    

pathToWeights = "./yolov5-master/weights/CMFD_best02.pt"

modelWeightPath = os.path.abspath(path = pathToWeights)

currentPath = os.path.join(os.getcwd(), "yolov5-master")
print(currentPath)

print("Path to weights: " + pathToWeights)
print("Abs path to weights: " + modelWeightPath)

maskDetector = MaskDetector(captureIndex= 0, modelWeight= modelWeightPath)
maskDetector()
# #Call it 

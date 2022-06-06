import torch
import os
#Get the current path 
dir = os.getcwd()

pt_weights = os.path.join(dir, "yolov5_kaggle.pt")
model = torch.hub.load('.', 'custom', path= pt_weights , source='local')


img = os.path.join(dir, "data/images/00000/00000_Mask.jpg")


results = model(img)

results.save()
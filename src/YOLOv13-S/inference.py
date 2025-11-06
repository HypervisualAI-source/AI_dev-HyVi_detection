import os                                                                      
import sys                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                         
sys.path.append(os.path.abspath('../../third_party_libraries'))  
                                                                                                                                                                                             
from ultralytics import YOLO                                                      
                                                                                                                          
# model weight and configration                                                                                                                      
base_path = os.path.dirname(__file__)                                                                                             
model_weight = os.path.join(base_path, 'models', 'yolov13s.pt')                                       
                                                                                                                                                                                                                                     
# loading YOLOv13-S                                                                                                                                                                                                                                                                                                                  
model = YOLO(model_weight)                                                                                                                                                                     
                                                                               
                                                                                                                                                                                                                                                                                                             
# calculating MAP                                                                                                                                                                                                   
metrics = model.val(data='coco.yaml')                                                    
print("\n")                                                                                                                                                              
print("metrics/mAP50(B):", metrics.results_dict["metrics/mAP50(B)"])
print("metrics/mAP75(B):", metrics.results_dict["metrics/mAP75(B)"])
print("metrics/mAP50-95(B):", metrics.results_dict["metrics/mAP50-95(B)"])
                                                                                                         
# inferencing model                                                                                                                                     
results = model("test.jpg")                                                                      
results[0].show()                                                                                                                                                                 
                                                                              
                                                                                                        

import os                                                                      
import sys                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                         
sys.path.append(os.path.abspath('../../third_party_libraries'))  
                                                                                                                                                                                             
from ultralytics import YOLO                                                      
                                                                                                                                                                                                    
# model weight and configration                                                                                                                      
base_path = os.path.dirname(__file__)                                                                                             
model_weight = os.path.join(base_path, 'models', 'yolov13s.pt')                                       
                                                                                                                                                                                                                                     
# loading YOLOv13-S                                                                                                                                                                                                                                                                                                                  
model = YOLO(model_weight)                                                                                                                                                                                                                                                                                                                                     
                                                                               
                                                                                                  
# inferencing model                                                                                                                                     
results = model("test.jpg")                                                                      
results[0].show()                                                                                                                                                                 
                                                                              
                                                                                                        

import os                                                                      
import sys                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                         
sys.path.append(os.path.abspath('../../third_party_libraries'))                                                                        
                                                                                                                                                                                             
from ultralytics import YOLO                                                                             
                                                                                                                                                                                                                              
base_path = os.path.dirname(__file__)                                                                                             
model_weight = os.path.join(base_path, 'models', 'yolov13n.pt')                                       

model = YOLO(model_weight)                                                                                  
                                                                                    
results = model("test.jpg")                                                             
results[0].show()   
                                                                                                                                         

                                                                                                                                                         
                                                                              
                                                                                                        

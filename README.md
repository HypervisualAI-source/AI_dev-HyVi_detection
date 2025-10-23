### AI dev - HyVi detection                                                                                        
Hypervisual AI is currently developing a project that incorporates YOLOv13-N, with plans to integrate ViT-B-16 in future iterations.
                                                                                                    
### Install Dependencies                                                                            
1. git clone https://github.com/HypervisualAI-source/AI_dev-HyVi_detection.git                               
2. cd AI_dev-HyVi_detection
3. python3 -m venv venv_benchmark
4. source venv_benchmark/bin/activate
5. pip3 install -r requirements_benchmark.txt
6. python3 -m venv venv
7. source venv/bin/activate
8. pip3 install -r requirements.txt
                             
### Usage Guide                                                                     
                                                                                                                                                                                                                                                
1. Training Model                           
                                                                                                                                                                   
    cd ./src/YOLOv13-N/
   
	python3 train.py      
	                                                                                           
2. Inferencing Model
   
    cd ./src/YOLOv13-N/
                                             
	python3 inference.py
	                                                     
3. Comparing with benchmark
                                                                                                                                                                                                                       
    cd ./src/YOLOv13-N/

	3.1 For YOLOv8
   																								
    python3 comparison_yolov8.py

    3.2 For YOLOv9

	python3 comparison_yolov9.py

5. Demonstrating YOLOv13-N

    cd ./demos/YOLOv13-N/
   
	python3 demo.py 

    4.1 Demonstrating YOLOv13-N in shell script file
   
        cd ./demos/YOLOv13-N/
   
        chmod +x demo.sh
   
	    ./demo.sh

6. Demonstrating ViT-B-16
   
    cd ./demos/ViT-B-16/
   
	python3 demo.py                  
                                       
    5.1 Demonstrating ViT-B-16 in shell script file
   
        cd ./demos/ViT-B-16/
   
        chmod +x demo.sh
   
	    ./demo.sh
                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                   
### Benchmark                                                                                                                                                             
| Model | Parameters(M) | FLOPs(G) | Latency(ms)<br><sup>640(pixel)<br><sup>CPU(12th Gen Intel(R) Core(TM) i5-12400)| mAP50_95<br><sup>coco(val)|  
|-------|-----|----------|---------------------------- |-----------------|                                                                                                            
| [YOLOv8n](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt) | 3.2 | 8.9 | 26.00 | 44.8 |                      
| [YOLOv8s](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt) | 11.2 | 28.8 | 57.00 | 58.8 |
| [YOLOv8m](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8m.pt) | 25.9 | 79.3 | 136.00 | 61.1 |
| [YOLOv8l](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8l.pt) | 43.7 | 165.7 | 256.00 | 65.9 |
| [YOLOv8x](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x.pt) | 68.2 | 258.5 | 401.00 | 66.7 |
| [YOLOv9t](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov9t.pt) | 2.1 | 8.5 | 39.00 | 37.8 |               
| [YOLOv9s](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov9s.pt)| 7.3 | 27.6 | 76.00 | 46.4 |                   
| [YOLOv9m](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov9m.pt) | 20.2 | 77.9 | 160.00 | 51.5 |
| [YOLOv9c](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov9c.pt) | 25.6 | 104.0 | 202.00 | 52.9 |
| [YOLOv9e](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov9) | 58.2 | 193.0 | 401.00 | 55.3 |                                                                                  
| **yolov13n** | **2.5** | **6.5** | **43.35** | **41.4** |                                                                                                                                 
                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                            
### Demos                                                                                                                                                             
#### Features                        
| Model | Frame size | Display  | Inference time (average/ms) | FPS (average/s) |   CPU   |
|-------|-----|----------|---------------------------- |-----------------|---------|
| YOLOv-13-N|(3, 640, 640) | 1920 x 1080  | 39 | 13 | 12th Gen Intel(R) Core(TM) i5-12400 |
| ViT-B-16|(3, 224, 224) | 1920 x 1080  | 95 | 8 | 12th Gen Intel(R) Core(TM) i5-12400 |

                            
#### YOLOv13-N for detection (30ms/frame)
![Image](demos/YOLOv13-N/source/yolo_output.gif)

#### ViT-B-16 for classification (30ms/frame)
![Image](demos/ViT-B-16/source/vit_output.gif)
                    
### Improvements                       
#### v0.0.rc4
Compared to the version (v0.0.rc3), the improvements of the version (v0.0.rc4) are:
1. Compared with benchmarks: YOLOv9t,YOLOv9s,YOLOv9m,YOLOv9c,YOLOv9e 
                                                                                                                                              
### TO DO                                         
1. Make a comparison between YOLOv13-N and YOLOv10(YOLOv10n,YOLOv10s,YOLOv10m,YOLOv10b,YOLOv10l,YOLOv10x)                                                                                                   


































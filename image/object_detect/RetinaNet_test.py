# ref:https://mp.weixin.qq.com/s/zTHtkuA5SyptwrrEepGtzg
# ref:https://github.com/OlafenwaMoses/ImageAI/tree/master/imageai/Detection
"""
2012年深度学习技术的突破性进展，催生了一大批高度精准的目标检测算法，
比如R-CNN，Fast-RCNN，Faster-RCNN，RetinaNet和既快又准的SSD及YOLO。
"""



from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()   # 定义了目标检测类
detector.setModelTypeAsYOLOv3()  # 将模型的类型设置为 Yolo3
# detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "1.jpg"), output_image_path=os.path.join(execution_path , "1_new.jpg"), extract_detected_objects=False)  # extract_detected_objects参数是保存提取对象到文件夹

for eachObject in detections:
    print(eachObject["name"] + " : ", eachObject["percentage_probability"] )




# Jordanian ALPR
The objective of this project is to create a system that employs object detection and character recognition techniques to detect and recognize license plates from images.

# Introduction
As the number of cars in Jordan keeps going up, it becomes increasingly difficult to manually control and improve traffic congestion, public security, law enforcement, and vehicle identification in the country. In order to address these challenges, it becomes necessary to leverage the power of artificial intelligence, such as using deep learning algorithms to build and develop a robust, real-time automatic license plate recognition (ALPR) system. This system can process input images of various sizes and lighting conditions, accurately identify vehicle license plates, and convert the recognized license plate numbers into digital text. Moreover, it will help to improve traffic management and enhance public security as it can be used to track vehicles for public security purposes, such as identifying suspicious vehicles involved in criminal activity. Furthermore, it can improve law enforcement, by monitoring and enforcing speed limits, and providing faster and more accurate vehicle identification.

# Approach
To detect the license plate number, the following things need to be done:

     1.The license plate needs to be detected and extracted from the overall image. This is done by using object detection method like using You-Only-Look-Once (YOLO).
     2. After extracting the license plate, individual characters of LP number need to be recognized, this is done by using Optical Character Recognition Techique (OCR).
     3. The last phase is to retrieve the Owner's and Vehicle's information of the recognized LP by connecting it to the database.
# Dataset
The following datasets have been used for different purposes:

    1.For license plate detection (YOLO): The dataset contains approximately 1300 annotated images of vehicle with license plates.The dataset can be found in folder "OpenSooq
    dataset" which includes the images of JPEG format and the annotated text files.
    2.For character recognition(OCR): The dataset contains approximately 508 cropped license plate that was previously detected and extracted by YOLO. The dataset can be found 
    in  folder named "OCR LP".
    3.For testing the whole model: The dataset contains about 250 images of vehicle's with license plates that was collected from Roboflow. The dataset can be found in folder
    named "Online Dataset".
    
    
# Technologies/Languages Used


Python: This is the most sought language for implementing AI projects.
IDE: We used Jupter Notebook for this project.
OpenCV: OpenCV is a library of programming functions mainly aimed at real-time computer vision. It eases the work when projects are based primarily on images or videos.
Tensorflow: TensorFlow is a free and open-source software library for machine learning. It can be used across a range of tasks but has a particular focus on training and inference of deep neural networks.
Keras: Keras is an open-source software library that provides a Python interface for artificial neural networks. Keras acts as an interface for the TensorFlow library.
YOLOv5: YOLOv5 (You Only Look Once, Version 5) is a real-time object detection algorithm that identifies specific objects in videos, live feeds, or images.
Scikit-Learn: It is a free software machine learning library for the Python programming language.
Matplotlib: Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.
Imutils: A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, displaying Matplotlib images, sorting contours, detecting edges, and much more easier with OpenCV.
Tkinter: is a standard Python library used for creating graphical user interfaces (GUIs). It provides a set of tools and widgets for building interactive applications. Tkinter is based on the Tk GUI toolkit, which originated as a part of the Tcl scripting language.

# Methodolgy



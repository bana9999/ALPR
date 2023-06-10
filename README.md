# Jordanian ALPR
The objective of this project is to create a system that employs object detection and character recognition techniques to detect and recognize license plates from images.
![Empty_recog_page](https://github.com/bana9999/ALPR/assets/129235769/38974949-a84e-461a-9151-f1141a721ec8)

# Introduction
As the number of cars in Jordan keeps going up, it becomes increasingly difficult to manually control and improve traffic congestion, public security, law enforcement, and vehicle identification in the country. In order to address these challenges, it becomes necessary to leverage the power of artificial intelligence, such as using deep learning algorithms to build and develop a robust, real-time automatic license plate recognition (ALPR) system. This system can process input images of various sizes and lighting conditions, accurately identify vehicle license plates, and convert the recognized license plate numbers into digital text. Moreover, it will help to improve traffic management and enhance public security as it can be used to track vehicles for public security purposes, such as identifying suspicious vehicles involved in criminal activity. Furthermore, it can improve law enforcement, by monitoring and enforcing speed limits, and providing faster and more accurate vehicle identification.

# Approach
The ALPR project approach is to detect and recognize the license plate number, the following things need to be done:

1.The license plate needs to be detected and extracted from the overall image. This is done by using an object detection method like using You-Only-Look-Once version 
5(YOLOv5).
2. After extracting the license plate, individual characters of the LP number need to be recognized, this is done by integrating the ALPR model with Nanonets, which is a  
website that provides a variety of AI tools and APIs for image extraction and enables the use of OCR technology, was used in order to complete the objective of the project 
by recognizing license plate characters.
3. The last phase is to retrieve the Owner's and Vehicle's information of the recognized LP by integrating the ALPR system with a database.
4. 
# Dataset
The following datasets have been used for different purposes:

1.For license plate detection (YOLOv5) model : The dataset, which contains approximately 1300 images, was divided into two parts: one for training, which contains the annotated images in JPEG format with their annotated text files.
The dataset for training can be found at the following link:https://drive.google.com/drive/folders/1cVbuLZmEtlzywJprHiOJ6iYwP5k9u6Ec?usp=sharing
The second part of the data is for testing and contains images in JPEG format.
The dataset for testing can be found at the following link:https://drive.google.com/drive/folders/1tJC01XPuNkAqGy6Nfds_K898_qPularK?usp=sharing

2.For Nanonets optical character  recognition (OCR)  model: The dataset contains approximately 508 cropped license plates that were previously detected and extracted by YOLOv5. 
 The dataset can be found at the following link: https://drive.google.com/drive/folders/1GUijXI5YcMgm8AR1X8dYW3M4hyvmW3r_?usp=sharing

# Programming Language used
The ALPR system utilizes Python as its programming language, benefiting from Python's reputation for simplicity, readability, and a wide range of libraries. Python's versatility allows it to address various tasks, including application development, data processing, and automation, making it a suitable choice for the ALPR system.
# Libraries Used
OpenCV: is a library of programming functions mainly aimed at real-time computer vision. It eases the work when projects are based primarily on images or videos.
PyTorch: is a popular open-source machine learning framework widely used for various artificial intelligence and deep learning tasks. PyTorch provides a flexible and dynamic programming interface that allows developers to efficiently build and train neural networks.
Tensorflow: is a free and open-source software library for machine learning. It can be used across a range of tasks, but has a particular focus on training and inference of deep neural networks.
Keras: is an open-source software library that provides a Python interface for artificial neural networks. Keras acts as an interface for the TensorFlow library.
Python Imaging Library(PIL): is a popular Python library used for image processing and manipulation. PIL provides comprehensive functions and methods for opening, manipulating, and saving many different image file formats.
Torchvision: is a module in the PyTorch ecosystem specifically designed for computer vision tasks. It provides a wide range of utility functions, datasets, and pre-trained models to simplify and accelerate the development of computer vision models using PyTorch.
Openpyxl: is used for working with Microsoft Excel files. It provides a convenient and efficient way to read, write, and modify Excel spreadsheets.
Requests: used for making HTTP requests and working with web APIs. It provides a simple and intuitive interface to send HTTP requests.
Torch: is a popular open-source machine learning framework primarily used for deep learning tasks. It provides a flexible and efficient platform for building, training, and deploying various neural network models.
Tkinter: is a standard Python library used for creating graphical user interfaces (GUIs). It provides a set of tools and widgets for building interactive applications.`

# Main Technologies used
For license plate detection: YOLOv5 is used, which is an upgraded version of the YOLO (You Only Look Once) models. In YOLOv5, a single neural network directly predicts bounding boxes for objects in an image, leading to high accuracy and speedy inference times. YOLOv5 is characterized by its unique architecture and uses a modified version of the Darknet backbone network named CSPDarknet, which is built up of multiple layers to extract high-level features from the input image. It introduces a neck module known as PANet (Path Aggregation Network), which creates a feature pyramid that incorporates features from different scales and aids in the detection of objects of varied sizes. As a result of this feature pyramid, YOLOv5 is able to detect license plates of different sizes and aspect ratios with ease. YOLOv5's detection head has multiple detection layers, and in each detection layer, bounding boxes and probability distributions are predicted at a different scale. These detection layers generate predictions of bounding boxes for objects based on input from the neck module. The bounding box prediction consists of four coordinates: the x and y coordinates of the box's center, its width, and its height. Apart from bounding boxes, YOLOv5 also predicts class probabilities. Depending on the context of the ALPR system, the model assigns class probabilities to indicate the presence of vehicles license plates. After obtaining the bounding box and classification predictions, YOLOv5 applies a non-maximum suppression (NMS) post-processing step. Through the NMS, redundant bounding boxes of license plates are eliminated by suppressing those that have low confidence scores and overlap with other boxes, providing cleaner final predictions. In order to ensure that only confident license plate detections are considered, a threshold is applied to filter out low-confidence predictions. Finally, the YOLOv5 engine outputs bounding boxes, along with class probabilities, that represent the detected license plates in the input images.
Furthermore, Yolov5 differs from other versions in having multiple variants to cover different model sizes, from the small model size (Yolov5s) to the largest model size (Yolov5x).
Overall, with the YOLOv5 architecture, the model is able to effectively capture and interpret visual information from input images, resulting in accurate and efficient license plate detection. By processing the image through the various layers of the network, the model predicts it based on regression and classification techniques.\\


For Character recognition: incorporating the trained optical character recognition model via Nanonets, which is a platform that provides a variety of AI tools and APIs for image extraction and enables the use of OCR technology, was done in order to complete the objective of the project by recognizing the detected license plate characters. Looking at how nanonets work, little steps are applied to produce the result of the recognized license plate characters. It begins with the collection of labeled data specifically needed for the task; in the ALPR context, license plates are the required labeled data. This labeled data will serve as the basis for training the nanonets optical character recognition model. The next step is to extract the characters from the license plates using the data collected so far. Following character extraction, the OCR model is trained with labeled data. Using this technology, the ALPR system is able to recognize the characters in the detected license plate image.

# Testing the ALPR system 
To test the ALPR system , first install and run the ALPR system , so please refer to the following guide:
Step 1:Download and install the Visual Studio Integrated Development Environment (IDE), from the following link:{https://code.visualstudio.com/download}.
Step 2: Download and install Git from the following link:{https://git-scm.com/downloads}.
Step 3: Open the previously installed Visual Studio code, navigate to the left-hand side of the VS Code window, and access the Extensions Marketplace. Install the Python support and Git support extensions.
Step 4: click on the "Code" button and select "Download ZIP" to download the ALPR project locally on your desktop.
Step 5: Navigate to the left-hand side of the VS code window and access "SOURCE CONTROL", next select either "Open Folder" or "Clone Repository". If you have chosen "Open Folder", locate the folder of the ALPR project that you have previously downloaded and select it. Else, copy the following GitHub link:{https://github.com/bana9999/ALPR} and paste it in the "Clone Repository" button. Finally, you have successfully cloned the ALPR system.
Step 6: Access the ALPR-model Juypter notebook in the ALPR-GUI folder of the cloned ALPR system  and run the entire notebook. 
Step 7: Enter the username: "admin" and password: "$12345$" in the ALPR Login page.
![ALPR_Login_page](https://github.com/bana9999/ALPR/assets/129235769/d13ed245-a045-4a57-9aa9-1d7a25e0b73a)
Step 8: Finally, you can click on the "Start" button to initialize the ALPR system, which will directly display the detected cropped license plate images along with the digital text of each image  Then, if you want to retrieve information about a specific detected cropped license plate image, you can just manually enter the LP number by clicking on the "Enter License Plate" button, selecting either "Retrieve Owner's Information" or "Retrieve Vehicle's Information from the selection box, and clicking on the "Check" button.
![LP_Recognition_page](https://github.com/bana9999/ALPR/assets/129235769/35147b34-0712-45be-a4fa-2d248c2ff7cb)
![owner_info_page](https://github.com/bana9999/ALPR/assets/129235769/19a2a224-e8dd-40c0-9bbf-55495decb4e4)
![Vehicle_info_page](https://github.com/bana9999/ALPR/assets/129235769/1e85f7d2-83e2-4a11-a22b-6e434a032976)








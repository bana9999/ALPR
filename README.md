# Jordanian ALPR
The objective of this project is to create a system that employs object detection and character recognition techniques to detect and recognize license plates from images. The main ALPR GUI is as shown in this Figure :
![Empty_recog_page](https://github.com/bana9999/ALPR/assets/129235769/e0065839-8d44-4e54-9f74-3e64e7e9d357)

# Introduction
As the number of cars in Jordan keeps going up, it becomes increasingly difficult to manually control and improve traffic congestion, public security, law enforcement, and vehicle identification in the country. In order to address these challenges, it becomes necessary to leverage the power of artificial intelligence, such as using deep learning algorithms to build and develop a robust, real-time automatic license plate recognition (ALPR) system. This system can process input images of various sizes and lighting conditions, accurately identify vehicle license plates, and convert the recognized license plate numbers into digital text. Moreover, it will help to improve traffic management and enhance public security as it can be used to track vehicles for public security purposes, such as identifying suspicious vehicles involved in criminal activity. Furthermore, it can improve law enforcement, by monitoring and enforcing speed limits, and providing faster and more accurate vehicle identification.

# Approach
The ALPR project approach is to detect and recognize the license plate number, the following things need to be done:
1. The license plate needs to be detected and extracted from the overall image. This is done by using an object detection method like using You-Only-Look-Once version 5(YOLOv5).
2. After extracting the license plate, individual characters of the LP number need to be recognized, this is done by integrating the ALPR model with Nanonets, which is a website that provides a variety of AI tools and APIs for image extraction and enables the use of OCR technology, was used in order to complete the objective of the project by recognizing license plate characters.
3. The last phase is to retrieve the Owner's and Vehicle's information of the recognized LP by integrating the ALPR system with a database.



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
Overall, with the YOLOv5 architecture, the model is able to effectively capture and interpret visual information from input images, resulting in accurate and efficient license plate detection. By processing the image through the various layers of the network, the model predicts it based on regression and classification techniques.


For Character recognition: incorporating the trained optical character recognition model via Nanonets, which is a platform that provides a variety of AI tools and APIs for image extraction and enables the use of OCR technology, was done in order to complete the objective of the project by recognizing the detected license plate characters. Looking at how nanonets work, little steps are applied to produce the result of the recognized license plate characters. It begins with the collection of labeled data specifically needed for the task; in the ALPR context, license plates are the required labeled data. This labeled data will serve as the basis for training the nanonets optical character recognition model. The next step is to extract the characters from the license plates using the data collected so far. Following character extraction, the OCR model is trained with labeled data. Using this technology, the ALPR system is able to recognize the characters in the detected license plate image.

# The ALPR project consists of the following directories:
1. The "Applying_Noises" directory which includes the "applying_noise_functions.py" Python file. This file contains the code responsible for applying noises to a sample of 50 images from the ALPR dataset. Additionally, within the "Applying_Noises" directory, there is a folder called "noise images" which holds the collection of the 50 images after the noise has been applied to them.
2. The "Image_preprocessing" directory that contains the "image_preprocessing.py" Python file. This file includes the necessary code for applying image preprocessing techniques to prepare the images for license plate detection and recognition.
3. The "Test_detection_model" directory which consists of the "testing detection model.ipynb" notebook. This notebook contains the code for the YOLOV5 detection model and is used for testing purposes. Additionally, within the "Test_detection_model" directory, there is a folder called "testing images" that contains the images from the ALPR dataset on which the model is tested.
4. The "Train_YOLOv5_on_custom_data" directory that contains several essential files: firstly, the "train_YOLOv5.ipynb" notebook is included, which was utilized for training YOLOv5 on our specific ALPR dataset. This notebook holds the code and instructions for the training process. Additionally, within the same directory, you will find the "yolov5s.pt" weights file. These weights were employed during the training to initialize the YOLOv5 model. Lastly, the "new1coco128.yaml" configuration file is also present. This file was used to configure the training settings and parameters for our custom dataset. 
5. The "main" directory serves as the central location for the ALPR project. It contains the primary ALPR Graphical User Interface (GUI) implemented in the "ALPR_model.ipynb" notebook. This notebook incorporates the code responsible for integrating the YOLOv5 detection model and the Optical Character Recognition (OCR) model within the GUI. Within the "main" directory, you can find the following essential components: "ALPR_model.ipynb" notebook: this notebook houses the ALPR GUI code, allowing users to interact with the system. It provides functionalities for license plate detection, recognition, and information retrieval. "Input_camera-images" folder: This folder is intended for storing input images captured from cameras. These images can be utilized for testing and evaluating the ALPR system. "yolov5" folder: This folder contains the YOLOv5 model implementation, it includes necessary scripts and configurations for executing the model. "best8.pt" customized weights file: This file contains the trained weights specific to the YOLOv5 model for license plate detection.  "coco128.yaml" configuration file: This file holds the configuration settings required by the YOLOv5 model, such as the model architecture, anchor sizes, and classes. "Database.xlsx": This Excel file acts as a database, connecting it to the ALPR GUI. It stores relevant information associated with license plates, allowing the GUI to retrieve and display the required data during the ALPR process.


# To run the ALPR system
1. Clone the ALPR GitHub project using any Integrated Development Environment (IDE) like Visual Studio Code, PyCharm, etc.
2. Navigate to the "main" directory in the cloned project.
3. Locate the "Input_camera_images" folder and insert the desired test images. Remember that this folder can hold a maximum of three images. Alternatively, you can use the three  test_example images already present in the "Input_camera_images" folder for evaluating the ALPR system.
4. Open the "ALPR_model.ipynb" notebook.
5. In the notebook, go to the third code section called the "detect_license_plate()" function. Replace the "model" variable with the correct path to the "yolov5" folder.
6. In the notebook, go to the fifth code section called the "search_vehicle_information()" function. Also, go to the sixth code section called the "search_owner_information()"    function. Replace the "workbook" variable in both sections with the correct path to the "database.xlsx" file.
7. In the notebook, find the "start_license_plate_detection()" function. Replace the "folder_path" variable with the correct path to the "Input_camera_images" folder.           Additionally, update the "config_path" variable with the path to the "coco128.yaml" configuration file, and set the "weights_path" variable to the path of the "best8.pt" file.
8. Finally, run the entire "ALPR_model.ipynb" notebook to access the ALPR GUI and evaluate the system.  


# Evaluating the ALPR system example
1. Run the ALPR system: Follow the instructions provided in the previous "To run the ALPR system" section to start the ALPR system. This will launch the "ALPR Login" page.
2. Enter login credentials: On the "ALPR Login" page, enter the username as "admin" and the password as "$12345$". This will grant access to the ALPR system.
![ALPR_Login_page](https://github.com/bana9999/ALPR/assets/129235769/73c14738-0920-4883-9639-3729ee404c96)
3. After logging in, you will be redirected to the "license_plate_recognition" page.
4. On the "license_plate_recognition" page, click on the "Start" button to initialize the ALPR system. This will trigger the license plate detection process.
5. As the ALPR system is running, the screen will display the detected cropped license plate images. These images are sourced from the "Input_camera_images" folder. Alongside each license plate image, the system will also display the corresponding digital text associated with that particular license plate.
![LP_Recognition_page](https://github.com/bana9999/ALPR/assets/129235769/c7fed261-1a4a-42ff-bd60-aec0da4105ee)
6. Retrieve information for a specific license plate: If you want to retrieve information about a particular detected license plate image, click on the "Enter License Plate" button. Manually enter the license plate number in the provided field.
7. Select information retrieval type: Choose either "Retrieve Owner's Information" or "Retrieve Vehicle's Information" from the selection box based on the desired information.
8. After selecting the information retrieval type, click on the "Check" button. The ALPR system will retrieve and display the requested information related to the specific license plate.

![owner_info_page](https://github.com/bana9999/ALPR/assets/129235769/67b305a7-79d6-42d8-bdc3-7ba9e28c83f3)

![Vehicle_info_page](https://github.com/bana9999/ALPR/assets/129235769/e19b3fdc-f3d5-47d7-9ebb-b9d4cedcfeb9)








# Jordanian ALPR
The objective of this project is to create a system that employs object detection and character recognition techniques to detect and recognize license plates from images.
![Empty_recog_page](https://github.com/bana9999/ALPR/assets/129235769/38974949-a84e-461a-9151-f1141a721ec8)

# Introduction
As the number of cars in Jordan keeps going up, it becomes increasingly difficult to manually control and improve traffic congestion, public security, law enforcement, and vehicle identification in the country. In order to address these challenges, it becomes necessary to leverage the power of artificial intelligence, such as using deep learning algorithms to build and develop a robust, real-time automatic license plate recognition (ALPR) system. This system can process input images of various sizes and lighting conditions, accurately identify vehicle license plates, and convert the recognized license plate numbers into digital text. Moreover, it will help to improve traffic management and enhance public security as it can be used to track vehicles for public security purposes, such as identifying suspicious vehicles involved in criminal activity. Furthermore, it can improve law enforcement, by monitoring and enforcing speed limits, and providing faster and more accurate vehicle identification.

# Approach
The ALPR project approach is to detect and recognize the license plate number, the following things need to be done:

     1.The license plate needs to be detected and extracted from the overall image. This is done by using object detection method like using You-Only-Look-Once version 
     5(YOLOv5).
     
     2. After extracting the license plate, individual characters of LP number need to be recognized, this is done by integrating the ALPR model with Nanonets, which is a  
     website that provides a variety of AI tools and APIs for image extraction and enables the use of OCR technology, was used in order to complete the objective of the project 
     by recognizing license plate characters.
     
     3. The last phase is to retrieve the Owner's and Vehicle's information of the recognized LP by integrating the ALPR system with a database.
# Dataset
The following datasets have been used for different purposes:

    1.For license plate detection (YOLOv5) model : The dataset contains approximately 1300 annotated images of vehicle with license plates.The dataset can be found in the 
    following link: which includes the images of JPEG format and the annotated text files.
    
    2.For Nanonets optical character recognition(OCR) model: The dataset contains approximately 508 cropped license plate that was previously detected and extracted by YOLOv5. 
    The dataset can be found in the following link

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

# Testing the ALPR system 
To test the ALPR system , first install and run the ALPR system , so please refer to the following guide:
Step 1:Download and install the Visual Studio Integrated Development Environment (IDE), from the following link:{https://code.visualstudio.com/download}.
Step 2: Download and install Git from the following link:{https://git-scm.com/downloads}.
Step 3: Open the previously installed Visual Studio code, navigate to the left-hand side of the VS Code window, and access the Extensions Marketplace. Install the Python support and Git support extensionsز
Step 4: click on the "Code" button and select "Download ZIP" to download the ALPR project locally on your desktop.
Step 5: Navigate to the left-hand side of the VS code window and access "SOURCE CONTROL", next select either "Open Folder" or "Clone Repository". If you have chosen "Open Folder", locate the folder of the ALPR project that you have previously downloaded and select it. Else, copy the following GitHub link:{https://github.com/bana9999/ALPR} and paste it in the "Clone Repository" button. Finally, you have successfully cloned the ALPR system.
Step 6: Access the ALPR-model Juypter notebook in the ALPR-GUI folder of the cloned ALPR system as shown in Figure \ref{fig:Access ALPR-model} and run the entire notebook. 
Step 7: Enter the username: "admin" and password: "$12345$" in the ALPR Login page.
Step 8: Finally, you can click on the "Start" button to initialize the ALPR system, which will directly display the detected cropped license plate images along with the digital text of each image  Then, if you want to retrieve information about a specific detected cropped license plate image, you can just manually enter the LP number by clicking on the "Enter License Plate" button, selecting either "Retrieve Owner's Information" or "Retrieve Vehicle's Information from the selection box, and clicking on the "Check" button.







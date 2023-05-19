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
    
    2.For character recognition(OCR): The dataset contains approximately 508 cropped license plate that was previously detected and extracted by YOLO. The dataset can be found in
    folder named "OCR LP".
    
    3.For testing the whole model: The dataset contains about 250 images of vehicle's with license plates that was collected from Roboflow. The dataset can be found in folder
    named "Online Dataset".
    
    
# Technologies/Languages Used

# Methodolgy



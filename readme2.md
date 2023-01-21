Motion is a interactive display system that can translate gestures that a user provides it , provides feedback through an array of mechanical flowers.
# Softwares that are required
A python ide <br>
An Arduino <br>
Iriun Webcam<br>
## Setting everything up
 all the code can be pulled from this github repo [https://github.com/alkrona/blooming_project.git](https://github.com/alkrona/blooming_project.git " bloom project repository")
<br>
1. Open the python code in an ide and create a virtual enviorment
<br>
**One of the libraries used mediapipe at the moment of making this doc is not compatiple with python3.9 or higher. So make sure your python version is lower than 3.9.**
<!--Code bloacks-->
```
python3 -m venv venv
source venv/bin/activate
```

2. All the required libraries are in the requirements.txt file

<!--Code bloacks-->
```
pip install -r requirements.txt
```
3. Install Iriun webcam on both your phone and your pc [link here]( https://iriun.com "link to download") . This enabes you to make your phone into a webcam. Make sure both devices operate on the same wifi network.
 * Now the program should be running properly. If something goes wrong check the following.
    *  if the error message is related to camera footage. Check if there are multiple or no cameras in your device.
    <!--Code bloacks-->
```python
import cv2 as cv
import mediapipe as mp
import posemodule as pm
import time 
import testing_wave_menu_integration
import testing_push_menu_integration
import testing_push_menu_intergration_version2
import arduino_sender
import circle_pattern
import circular_pattern
import random
import analytical_wave_speed_test
import pythonToFirebasesender
mode=1
cap = cv.VideoCapture(1)
cap.set(3,680)
cap.set(4,480)
```

* this is the file main2.py. here change the parameter of the VideoCapture function.
## Setting the wire connections


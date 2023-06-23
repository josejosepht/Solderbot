# Solderbot
This repo contains the RoboDK workstation with associated tree objects, including a camera object which takes snapshots of a PCB to detect viases to solder it. A python script uses the RoboDK API and OpenCV's template matching to detect the viases and execute a solder tool execution path.

The below is the workstation with the PCB to be soldered, the camera object above the PCB and the uFactory uArm robot model(available in the RoboDK library for import) with a custom tool tip of a solder:

![image](https://github.com/josejosepht/Solderbot/assets/97187460/1b1304b1-ff40-4403-a271-65bf6d5a6015)

The workstation tree is as shown below, which includes the pre-defined program for solder tip tool path execution through the different detected and placed PCB vias targets:

![image](https://github.com/josejosepht/Solderbot/assets/97187460/01096888-e2cb-4bfc-a24e-5b7d708d2ed5)

Here is a demo video showing the execution of the vias_detect.py script using the RoboDK API to connect to the workstation and use OpenCV's template matching to detect the vias positions on the image captured from the camera object in the workstation:

https://github.com/josejosepht/Solderbot/assets/97187460/0f9fa5a4-e1ca-4654-bd8a-2f6181ba726e

This project received collaborative support from Athul Rajeev on the design of the custom solder tool using CAD (https://github.com/athularr)

Link to published paper: https://www.ijsr.net/archive/v10i6/SR21529115123.pdf

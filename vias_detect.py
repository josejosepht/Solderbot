from robolink import Robolink,ITEM_TYPE_CAMERA
import time
import cv2
import numpy as np

# Load the template image
template_path = "path/to/template_image.png"
template_image = cv2.imread(template_path, cv2.IMREAD_COLOR)

# Create a Robolink instance
RDK = Robolink()

# Get the current active RoboDK station/workspace
station = RDK.ActiveStation()

#The below is a work in progress on placing target positions on PCB
# Check if the station is valid
if station.Valid():
    # Get a list of all the items in the station
    all_items = station.Childs()

    program_item = RDK.Item('Prog1')
    
    # Find the camera object and get its image
    for item in all_items:
        print(item.Name())
        if item.Name() == 'Camera 1':  # Replace 'Camera1' with the actual camera name
            #camera_item = RDK.Cam2D_Add(item_object=RDK.Item("eezybot_mark1"),cam_params="FOCAL_LENGTH=5.0 FOV=30.0 SIZE=640x480")
            camera_item = RDK.Cam2D_Add(item_object=RDK.Item("Matrox Iris GTR"),cam_params="FOCAL_LENGTH=5.0 FOV=30.0 SIZE=640x480")
            break
    time.sleep(0.2)
    filename = "path/to/save/workstation_PCB_image.png"
    RDK.Cam2D_Snapshot(file_save_img=filename)
    print("saved image1.png")
    if program_item.Valid():
    # Run the program once
        program_item.RunProgram()
        print("Program 'Prog1' executed successfully.")
    else:
        print("Program 'Prog1' not found.")
    
else:
    print('No active RoboDK station found.')

# Load the source image
source_path = "C:/Users/josei/OneDrive/Documents/project/Capstone/robot files/camera1 images from code/image1.png"
source_image = cv2.imread(source_path, cv2.IMREAD_COLOR)

# Perform template matching
result = cv2.matchTemplate(source_image, template_image, cv2.TM_CCOEFF_NORMED)

# Define a threshold for the template matching result
threshold = 0.65

# Find locations where the template matches with high confidence
locations = np.where(result > threshold)

# Convert the locations to a list of (x, y) coordinates
locations = list(zip(locations[1], locations[0]))

# Iterate over the found locations and draw bounding boxes around each match
if locations:
    for loc in locations:
        # Retrieve the position of each match
        x, y = loc

        # Calculate the coordinates for the bounding box
        width, height = template_image.shape[:2]
        top_left = (x, y)
        bottom_right = (x + width, y + height)

        # Draw the bounding box on the source image
        cv2.rectangle(source_image, top_left, bottom_right, (0, 0, 255), 2)

    # Show the image with bounding boxes
    cv2.imshow("Source Image", source_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"Found {len(locations)} instances of the template image.")
else:
    print("Template image not found in the source image.")

# Get the item by name
pcb_name = "eezybot_pcb_1connectorhead v1"
pcb = RDK.Item(pcb_name)

# Check if the item is valid
if pcb.Valid():
    # Get the list of targets associated with the item
    targets = pcb.Childs()
    
    # Print the names of the targets
    for target in targets:
        print(target.Name())
else:
    print("Item '{}' not found.".format(pcb_name))

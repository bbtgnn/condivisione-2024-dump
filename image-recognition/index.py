import cv2
from ultralytics import YOLO

import os
import random
import shutil
import csv

#

source_folder_path = '/Users/giovanniabbatepaolo/Downloads/progetto_finale/2-libri/0-jpg/hotel_images'
subject = 59 # bed

dest_folder_path = "dest/images"

# 

def predict(chosen_model:YOLO, img:cv2.typing.MatLike, classes=[], conf=0.5):
    if classes:
        results = chosen_model.predict(img, classes=classes, conf=conf)
    else:
        results = chosen_model.predict(img, conf=conf)

    return results


def predict_and_detect(chosen_model, img:cv2.typing.MatLike, classes=[], conf=0.5):
    results = predict(chosen_model, img, classes, conf=conf)
    # for result in results:
    #     for box in result.boxes:
    #         cv2.rectangle(img, (int(box.xyxy[0][0]), int(box.xyxy[0][1])),
    #                       (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (255, 0, 0), 2)
            # cv2.putText(img, f"{result.names[int(box.cls[0])]}",
            #             (int(box.xyxy[0][0]), int(box.xyxy[0][1]) - 10),
            #             cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
    return results

def find_first_at_symbol_filename(filenames):
    for filename in filenames:
        if "@" in filename:
            return filename
    return None

def pick_random_images(source_folder):
    selected_images = []

    # Loop through each subfolder in the source folder
    for subfolder in os.listdir(source_folder):
        subfolder_path = os.path.join(source_folder, subfolder)
        
        # Check if it's a directory
        if os.path.isdir(subfolder_path):
            # List all files in the subfolder
            file_names = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
            file = find_first_at_symbol_filename(file_names)
            
            if file:
                source_file_path = os.path.join(subfolder_path, file)
                selected_images.append(source_file_path)
    
    return selected_images

# 

if not os.path.exists(dest_folder_path):
    os.makedirs(dest_folder_path)

file = open("res.csv", mode='w', newline='')
writer = csv.writer(file)

model = YOLO("yolov8n.pt")

selected_images = pick_random_images(source_folder_path)

for image_path in selected_images:
    img = cv2.imread(image_path)
    result = predict(model, img, [59], 0.5)

    box = []
    if (len(result) >0 ):
        box = result[0].boxes.xywh.numpy().flatten().tolist()[:4]
    if (len(box) == 0):
        box = [0,0,0,0]

    image_name = image_path.split("/")[-1]
    shutil.copy(image_path, dest_folder_path)

    row = [image_name]
    row.extend(box)
    writer.writerow(row)


file.close()
    
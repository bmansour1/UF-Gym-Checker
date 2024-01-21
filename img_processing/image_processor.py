from ultralytics import YOLO

def process_image(image_path, model_path="yolov8m.pt"):
    model = YOLO(model_path)
    results = model.predict(image_path)
    result = results[0]
    person_counter = 0
    for box in result.boxes:
        class_id = result.names[box.cls[0].item()]
        if class_id == "person":
            person_counter += 1
    return person_counter


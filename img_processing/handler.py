from image_fetcher import fetch_camera_image
from image_processor import process_image

def handler(event, context):
    camera_urls = {
        "weight_room_1": "http://recsports.ufl.edu/cam/cam1.jpg",
        "weight_room_2": "http://recsports.ufl.edu/cam/cam4.jpg",
        "cardio" : "http://recsports.ufl.edu/cam/cam5.jpg",
        "bball_1_2" : "http://recsports.ufl.edu/cam/cam3.jpg",
        "bball_3_4" : "http://recsports.ufl.edu/cam/cam2.jpg"
     }

    counts = {}

    for key, url in camera_urls.items():
        image_data = fetch_camera_image(url)
        if image_data:
            tmp_image_path = f'/tmp/{key}.jpg'
            with open(tmp_image_path, 'wb') as file:
                file.write(image_data)
            counts[key] = process_image(tmp_image_path)

    # Combine counts for specific areas if needed
    # e.g., combine weight room 1 and 2
    weight_room_count = counts.get("weight_room_1", 0) + counts.get("weight_room_2", 0)
    cardio_count = counts.get("cardio", 0)
    basketball_courts_1_2_count = counts.get("bball_courts_1_2", 0)
    basketball_courts_3_4_count = counts.get("bball_courts_3_4", 0)

    
    # Return the combined counts or individual counts as required
    return {
        "statusCode": 200,
        "body": {
            "weight_room_count": weight_room_count,
            "cardio_count" : cardio_count,
            "basketball_courts_1_2_count" : basketball_courts_1_2_count,
            "basketball_courts_3_4_count" : basketball_courts_3_4_count
        }
    }

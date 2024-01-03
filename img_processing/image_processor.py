import requests
def handler(event, context):
    return {"statusCode": 200, "body": "Hello World!"}

def fetch_camera_image(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to fetch image. HTTP status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error occurred during fetching image: {e}")
        return None

# URL of the camera feed
camera_url = "http://recsports.ufl.edu/cam/cam1.jpg"

# Call the function to fetch the image
image_data = fetch_camera_image(camera_url)

if image_data:
    # Note the change in file path to '/tmp/test_image.jpg'
    with open('/tmp/test_image.jpg', 'wb') as file:
        file.write(image_data)
    print("Image written to '/tmp/test_image.jpg'.")
else:
    print("Failed to fetch the image. Check the URL or your network connection.")

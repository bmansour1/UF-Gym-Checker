import requests

def fetch_camera_image(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to fetch image from {url}. HTTP status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error occurred during fetching image from {url}: {e}")
        return None

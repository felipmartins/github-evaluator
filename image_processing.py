from face_detection import FaceDetector
from profile_handler import get_image_url
from time import sleep
from requests import get
from PIL import Image


def has_photo(selector, username):
    image_url = get_image_url(selector)
    sleep(2)
    img_data = get(image_url).content
    with open("photos/" + username + "_image.jpg", "wb") as handler:
        handler.write(img_data)
    return FaceDetector.find_faces("photos/" + username + "_image.jpg")

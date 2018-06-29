from picamera import PiCamera
from time import sleep

camera=PiCamera()
"""camera.rotation=180"""
"""camera.start_preview(alpha=100"""
"""alpha is used t o set the tranparency"""
camera.start_preview()
for x in range (5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg'%x)
camera.stop_preview()

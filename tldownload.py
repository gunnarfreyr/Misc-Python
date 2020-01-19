"""
    Quick and dirty way to grab images from ip cameras to make a time lapes video
    I wrote this to use with IP Webcam for Android , but it should work with any
    cameras that have a single frame output.


    ### Usage : Just run tldownload.py , then it will ask you for url and settings

    IP Webcam for android has these urls :

    - http://<your-ip>:8080/photo.jpg     Takes a regular photo with the camera
    - http://<your-ip>:8080/photoaf.jpg   This one focuses first, then takes the photo (slower)
    - http://<your-ip>:8080/shot.jpg      Grabs latest frame from video feed, with overlays etc

    - Download IP Webcam for android : https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en

"""

import os
import urllib.request
import time

imageUrl = str(input("Image url : "))
totalImages = int(input("\nHow many images ? "))
imageDelay = int(input("How many sec between images ? "))

def download_image(url, imageNumber):
    outputImage = "images\\" + "Image-" + str(imageNumber) + ".jpg"
    urllib.request.urlretrieve(url, outputImage)


def startTimelapse():
    totalRuntime = totalImages * imageDelay / 60
    imageNumber = 0

    try:
        os.mkdir("images")
        print("Image folder created")
    except FileExistsError:
        pass

    print("\nNow downloading images for timelapse\n")
    print("Fetching : " + str(totalImages) + " images with " + str(imageDelay) + "sec delay")
    print("Total runtime : " + str(totalRuntime) + " mins\n")

    while imageNumber < totalImages:
        download_image(imageUrl, imageNumber)
        print("downloaded : Image-" + str(imageNumber))
        imageNumber += 1
        time.sleep(imageDelay)

    else:
        print("\nAll images downloaded !\n")

startTimelapse()

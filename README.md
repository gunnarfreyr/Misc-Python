# Just misc things that dont get their own repo 

## tldownload.py

    Quick and dirty way to grab images from ip cameras to make a time lapes video
    I wrote this to use with IP Webcam for Android , but it should work with any
    cameras that have a single frame output.

    ### Usage : Just run tldownload.py , then it will ask you for url and settings

    IP Webcam for android has these urls :

    - http://<your-camera-ip>:8080/photo.jpg     Takes a regular photo with the camera
    - http://<your-camera-ip>:8080/photoaf.jpg   This one focuses first, then takes the photo (slower)
    - http://<your-camera-ip>:8080/shot.jpg      Grabs latest frame from video feed, with overlays etc

    - Download IP Webcam for android : https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en

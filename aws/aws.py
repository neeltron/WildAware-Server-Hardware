# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 12:51:22 2021

@author: Neel
"""

import cv2
import random
import os
import boto3

def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def detect_labels(photo, bucket):
    client=boto3.client('rekognition')
    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}}, MaxLabels=10)
    print('Detected labels for ' + photo) 
    print()
    i = 0
    labelperm = ""
    for label in response['Labels']:
        i += 1
        if i == 1:
            labelperm = label['Name']
        print ("Label: " + label['Name'])
    return labelperm

num = random.randint(0, 1000)
imgname = "image" + str(num) + ".jpg"

videoCaptureObject = cv2.VideoCapture(0)
result = True

while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite(imgname, frame)
    result = False
    
videoCaptureObject.release()
cv2.destroyAllWindows()

upload_file(imgname, 'wildaware')

label = detect_labels(imgname, 'wildaware')

print(label)

animal = label
imageurl = 'https://wildaware.s3.ap-south-1.amazonaws.com/' + imgname

payload = bytes(animal + ' ' + imageurl, 'utf-8')

print(payload)

import serial
s = serial.Serial('COM4')
s.write(payload)
s.close()

# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 03:05:36 2021

@author: Neel
"""

#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

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


def main():
    photo='NewPicture.jpg'
    bucket='wildaware'
    label_count=detect_labels(photo, bucket)
    print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    main()

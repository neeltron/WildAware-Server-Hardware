# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 12:59:46 2021

@author: Neel
"""

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

upload_file('image39.jpg', 'wildaware')

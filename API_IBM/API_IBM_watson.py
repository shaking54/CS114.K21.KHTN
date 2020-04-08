import json
import os
from ibm_watson import VisualRecognitionV4
from ibm_watson.visual_recognition_v4 import FileWithMetadata, TrainingDataObject, Location, AnalyzeEnums
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='XiwANQts_kQ6ZeGtK2IXkdI6IJ2ubtER8NZPkRewIvJM')

with open('/content/CS114.K21.KHTN/test set/cat_test6.jpeg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
	classifier_ids='default').get_result()
print(json.dumps(classes['images'][0]['classifiers'][0]['classes'], indent=2))

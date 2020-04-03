import json
import os
from ibm_watson import VisualRecognitionV4
from ibm_watson.visual_recognition_v4 import FileWithMetadata, TrainingDataObject, Location, AnalyzeEnums
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator('P25ojmx0GDFuNUemlfT1-mbW9H89wZSgpyKJxrjVbvLD')
visual_recognition = VisualRecognitionV4(
    version='2019-02-11',
    authenticator=authenticator
)

visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/8344294d-ae94-4dc3-901b-5aa57b7e01b8')


print("enter test file path: ")
n = input()

with open(n, 'rb') as cat:
    result = visual_recognition.analyze(
        collection_ids=["656bca73-b606-4d88-90c2-cb221d3667a9"],
        features=[AnalyzeEnums.Features.OBJECTS.value],
        images_file=[
            FileWithMetadata(cat),
        ]).get_result()
    print(json.dumps(result, indent=2))

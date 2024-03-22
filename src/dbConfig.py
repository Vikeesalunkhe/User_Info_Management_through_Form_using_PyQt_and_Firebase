from google.cloud import firestore
import json
#firestore database configuration

credentials_path = './setup/c2w-demo-1343e-firebase-adminsdk-o45qj-c4ec3873ed.json'

with open(credentials_path) as json_file:
    credentials_info = json.load(json_file)
    db = firestore.Client.from_service_account_info(credentials_info)
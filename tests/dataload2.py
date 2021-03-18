import boto3
import json
from datetime import datetime
#import time

dynamodb = boto3.client('dynamodb')

for i in range(1,10):
    orderdatetime = str(datetime.now())
    for j in range(1,10):
        productKey = 'PROD#000' + str(j)
        item = {
        "pk1": {
            "S": productKey
        },
        "sk1": {
            "S": orderdatetime 
        }
        }
        response = dynamodb.put_item(
            TableName='sam-streamsdemo5-DynamoDBTable-1SFVAPD7TM9WQ',
            Item=item
            )
        #time.sleep(1)
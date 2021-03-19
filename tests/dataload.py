import boto3
import json
from datetime import datetime
#import time

dynamodb = boto3.client('dynamodb')
tableName = 'streamsdemo'

for i in range(1,11):
    orderdatetime = str(datetime.now())
    for j in range(1,11):
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
            TableName=tableName,
            Item=item
            )
        #time.sleep(1)

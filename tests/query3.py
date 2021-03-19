import boto3
import json
from datetime import datetime
#import time

dynamodb = boto3.client('dynamodb')

tableName = 'streamsdemo'

print('query1 start' + str(datetime.now()))
response = dynamodb.describe_table(
    TableName=tableName
)
print('query1 end' + str(datetime.now()))
print(response)

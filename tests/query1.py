import boto3
import json
from datetime import datetime
#import time

dynamodb = boto3.client('dynamodb')

tableName = 'sam-streamsdemo5-DynamoDBTable-1SFVAPD7TM9WQ'

print('query1 start' + str(datetime.now()))
response = dynamodb.query(
    TableName=tableName,
    KeyConditionExpression='pk1 = :name AND sk1 = :startdate',
    ExpressionAttributeValues={
        ':name':{'S':'PROD#0001'},
        ':startdate':{'S':'2021-03-00'}
        }
)
print('query1 end' + str(datetime.now()))
print(response)
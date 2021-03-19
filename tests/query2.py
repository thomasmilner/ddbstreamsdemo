import boto3
import json
from datetime import datetime
#import time

dynamodb = boto3.client('dynamodb')

tableName = 'streamsdemo'

print('query2 start' + str(datetime.now()))
response = dynamodb.query(
    TableName=tableName,
    KeyConditionExpression='pk1 = :name AND sk1 BETWEEN :startdate and :enddate',
    ExpressionAttributeValues={
        ':name':{'S':'PROD#0001'},
        ':startdate':{'S':'2021-03-01 00:00:00.000000'},
        ':enddate':{'S':'2021-03-31 23:59:59.999999'}
        }
)
print('query2 end' + str(datetime.now()))
print(response)

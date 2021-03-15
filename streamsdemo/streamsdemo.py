import json
import boto3
import traceback
from botocore.exceptions import ClientError

#print('Loading function')

def updateDDBTable(tableName,pkValue,counterKey,counter):
    dynamodb = boto3.resource('dynamodb')
     
    #Get table name from stream. Updates will be written back to same table
    dynamodb_table = dynamodb.Table(tableName)
    
    #loop through collection
    for i in counterKey:
        dynamodb_table.update_item(
                Key={
                        'pk1': pkValue,
                        'sk1': i,
                    },
                UpdateExpression="set sales_cnt = ((if_not_exists(sales_cnt,:init)) + :num)", #if record doesn't exist, create it
                ExpressionAttributeValues={
                        ':init': 0, #new record will be created with 0 + num value
                        ':num': counter
                    },
                ReturnValues="NONE"
                )
                
def updateCounter(tableName,pkValue,skValue,counter):
    #always increment 0000 entry
    counterKey = [skValue[0:10], skValue[0:8]+ "00",skValue[0:5]+ "00-00","0000-00-00"]
    #persist changes to table
    updateDDBTable(tableName,pkValue,counterKey,counter)
            
def parseStreamArn(streamARN):
    tableName = streamARN.split(':')[5].split('/')[1]
    return(tableName)
    
def _lambda_handler(event, context):

    records = event['Records']

    record1 = records[0]
    tableName = parseStreamArn(record1['eventSourceARN'])
 
    for record in records:

        event_name = record['eventName'].upper()  # INSERT, MODIFY, REMOVE
        pkValue = record['dynamodb']['Keys']['pk1']['S']
        skValue = record['dynamodb']['Keys']['sk1']['S']
        #print(keyValue)
            
        if (event_name == 'INSERT') and "sales_cnt" not in record['dynamodb']["NewImage"]:
            updateCounter(tableName,pkValue,skValue,1)

        #if (event_name == 'REMOVE') and "sales_cnt" not in record['dynamodb']["NewImage"]:
        #    updateCounter(tableName,pkValue,skValue,-1)
            
    return 'Successfully processed {} records.'.format(len(event['Records']))
    
def lambda_handler(event, context):
    try:
        return _lambda_handler(event, context)
    except Exception:
        print (traceback.format_exc())
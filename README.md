# DyanamoDB Streams Tutorial

AWS SAM application that processes events from a DynamoDB stream and writes them back to a DynamoDB table.

'''
            ┌──────────────┐          ┌─────────────┐
            │   DynamoDB   │          │             │
───────────►│    Table     ├─────────►│    Streams  │
            │              │          │             │
            └──────▲───────┘          └──────┬──────┘
                   │                         │
                   │                         │
                   │                         ▼
                   │                  ┌──────────────┐
                   │                  │              │
                   └──────────────────┤    Lambda    │
                                      │              │
                                      └──────────────┘
'''

##Files
../ddbstreamsdemo/template.yml - SAM template to create DynamoDB table, stream and Lambda to process stream. Lambda is written in Python 3.8 runtime
../ddbstreamsdemo/streamsdemo/streamsdemo.py - Lambda code

../ddbstreamsdemo/tests/dataload.py - generate data and insert into table

../ddbstreamsdemo/tests/query1.py - query aggregation record
../ddbstreamsdemo/tests/query2.py - count range of records
../ddbstreamsdemo/tests/query3.py - describe table

##Blog
Read this article to walk through tutorial and details/learnings on how I built this application


import csv
import json

import boto3

STREAM_NAME = "ExampleInputStream"

def generate(stream_name, kinesis_client):
    counter = 0
    with open("./sample.csv", encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            #limit the number of records being sent to Kinesis
            # included sample file contains 100,000 row in total
            if (counter >= 10):
                break
            counter = counter + 1
            print(json.dumps(rows))
            # kinesis_client.put_record(StreamName=stream_name,
            #                           Data=json.dumps(rows),
            #                           PartitionKey="partitionkey")


if __name__ == '__main__':
    generate(STREAM_NAME, boto3.client('kinesis'))

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentData')

def lambda_handler(event, context):

    student_id = event['studentId']
    name = event['name']

    table.put_item(
        Item={
            'studentId': student_id,
            'name': name
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Student Added')
    }
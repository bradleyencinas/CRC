import json
import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Get the table name
table = dynamodb.Table('bradleyencinaswebsite')


def lambda_handler(event, context):

    # Get the current visit count
    response = table.get_item(
        Key={
            'ID': 'viewcount'
        }
    )
    
    visit_count = response['Item']['viewcount']
    visit_count = int(visit_count) + 1
    
    # Update the visit count in DynamoDB
    table.put_item(
        Item={
            'ID': 'viewcount',
            'viewcount': visit_count
        }
    )
    
    # Return the updated visit count as JSON
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': json.dumps({'counter': visit_count})
    }
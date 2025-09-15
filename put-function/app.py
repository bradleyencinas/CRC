import json
import boto3


dynamodb = boto3.resource('dynamodb')

# import requests


def lambda_handler(event, context):
    table_name = 'bradleyencinaswebsite'
    table = dynamodb.Table(table_name)

    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    try:
        item_to_put = {
            'id': 'visitors',
            'name': 'Example Item',
            'description': 'This is a test item.'
        }
        table.put_item(Item=item_to_put)
        print(f"Successfully put item: {item_to_put}")
    except Exception as e:
        print(f"Error putting item: {e}")
        return {
            "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*"
            },
            'statusCode': 500,
            'body': json.dumps(f"Error putting item: {str(e)}")
        }

    
           # "location": ip.text.replace("\n", "")
    

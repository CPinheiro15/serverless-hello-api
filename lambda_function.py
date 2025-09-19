import json
from datetime import datetime

def lambda_handler(event, context):
    # Log the incoming request in CloudWatch
    print("Received event:", json.dumps(event))

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from AWS Lambda!',
            'timestamp': str(datetime.now())
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
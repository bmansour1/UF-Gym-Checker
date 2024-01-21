import boto3
import os
import json
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

# Initialize the Boto3 Lambda client
lambda_client = boto3.client('lambda')

@app.get("/process-image")
def process_image():
    try:
        # Invoke the image processing Lambda function
        response = lambda_client.invoke(
            FunctionName=os.environ["IMG_PROCESSING_FUNCTION_ARN"],
            InvocationType='RequestResponse'
        )

        # Parse the Lambda response
        response_payload = json.load(response['Payload'])
        return response_payload

    except Exception as e:
        return {"error": str(e)}

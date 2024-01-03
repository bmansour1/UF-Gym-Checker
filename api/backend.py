def handler(event, context):
    

import os
import boto3
from fastapi import FASTAPI
from mangum import Mangum


app = FASTAPI()
handler = Mangum(app)


@app.get("/")
def root():
    return {"statusCode": 200, "body": "Hello World!"}
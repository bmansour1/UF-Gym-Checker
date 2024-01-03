import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from "aws-cdk-lib/aws-lambda";
import { CfnOutput } from 'aws-cdk-lib';

export class GymInfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

   

   const imgProcessing = new lambda.Function(this, "ImgProcessing", {
    runtime: lambda.Runtime.PYTHON_3_9,
    code: lambda.Code.fromAsset("../UF-Gym-Checker/lambda_function_api.zip"),
    handler: "image_processor.handler",
   });

   const api = new lambda.Function(this, "API", {
    runtime: lambda.Runtime.PYTHON_3_9,
    code: lambda.Code.fromAsset("../api/lambda_function_img.zip"),
    handler: "backend.handler",
    environment: {
      IMG_PROCESSING_FUNCTION_ARN: imgProcessing.functionArn,
    },
   });
   
   const backendFunctionUrl = api.addFunctionUrl({
    authType: lambda.FunctionUrlAuthType.NONE,
    cors: {
      allowedOrigins: ["*"],
      allowedMethods: [lambda.HttpMethod.ALL],
      allowedHeaders: ["*"],
    },
   });

   const imgProcessingFunctionUrl = imgProcessing.addFunctionUrl({
    authType: lambda.FunctionUrlAuthType.NONE,
    cors: {
      allowedOrigins: ["*"],
      allowedMethods: [lambda.HttpMethod.ALL],
      allowedHeaders: ["*"],
    },
   });

   new CfnOutput(this, "backendUrl",{
    value: backendFunctionUrl.url,
   });
   
   new CfnOutput(this, "imgProcessingUrl", {
    value: imgProcessingFunctionUrl.url,
   });

   imgProcessing.grantInvoke(api);

  }
}

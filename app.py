#!/usr/bin/env python3

from aws_cdk import core

from cdk_s3_notification_lambda.cdk_s3_notification_lambda_stack import CdkS3NotificationLambdaStack


app = core.App()
CdkS3NotificationLambdaStack(app, "cdk-s3-notification-lambda")

app.synth()

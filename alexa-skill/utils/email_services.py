import os
import boto3
from botocore.exceptions import ClientError
from utils.api_services import ApiServices

SENDER = os.getenv("SENDER")
RECIPIENT = os.getenv("RECIPIENT")
AWS_REGION = "eu-west-1"

CHARSET = "UTF-8"

SUBJECT = "Record"


class EmailServices:
    def __init__(self):
        self.client = boto3.client('ses', region_name=AWS_REGION)
        self.api_services = ApiServices()

    def send_mail(self):
        csv = self.api_services.get_csv()

        BODY_HTML = """<html>
            <head></head>
            <body>
            <h1>Record</h1>
            <p>Here is a record</p>
            RECORD
            </body>
            </html>
                        """

        print(csv)
        BODY_HTML.replace("RECORD", csv)

        try:
            response = self.client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER
            )
            print(response)
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])

import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import uuid
import time

# Inicializando conexión con DynamoDB (usando Boto3 para AWS)
dynamodb = boto3.resource('dynamodb')

class CorporateLog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CorporateLog, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.table = dynamodb.Table('CorporateLog')

    def post(self, session_uuid, method_name):
        try:
            log_entry = {
                'uuid': session_uuid,
                'cpu_uuid': str(uuid.getnode()),
                'method': method_name,
                'timestamp': int(time.time())
            }
            self.table.put_item(Item=log_entry)
            return {"status": "log saved"}
        except ClientError as e:
            return {"error": str(e)}

    def list(self, cpu_uuid, session_uuid=None):
        try:
            if session_uuid:
                response = self.table.query(KeyConditionExpression=boto3.dynamodb.conditions.Key('cpu_uuid').eq(cpu_uuid))
            else:
                response = self.table.scan()
            return response.get('Items', [])
        except ClientError as e:
            return {"error": str(e)}

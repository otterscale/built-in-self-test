import boto3
import sys

from botocore.exceptions import ClientError, EndpointConnectionError


def check_backend(host, access_key, secret_key):
    s3 = boto3.client(
            's3',
            endpoint_url = "http://"+host,
            aws_access_key_id = access_key,
            aws_secret_access_key = secret_key
            )
    try:
        s3.list_buckets()
        return True
    except EndpointConnectionError as e:
        print(f"{e}")
        sys.exit(1)
        return False
    except ClientError as e:
        print(f"{e}")
        sys.exit(1)
        return False


def initialize(warp_config):
    return check_backend(warp_config['host'] , warp_config['access_key'], warp_config['secret_key'])
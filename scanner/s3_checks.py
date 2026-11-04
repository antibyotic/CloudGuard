import boto3

def check_s3_buckets():
    s3 = boto3.client('s3')
    findings = []

    response = s3.list_buckets()
    buckets = response['Buckets']

    for bucket in buckets:
        bucket_name = bucket['Name']

        try:
            result = s3.get_public_access_block(Bucket=bucket_name)
            config = result['PublicAccessBlockConfiguration']

            if config['BlockPublicAcls'] and config['BlockPublicPolicy']:
                findings.append({"resource": bucket_name, "check": "s3_public_access", "status": "PASS"})
            else:
                findings.append({"resource": bucket_name, "check": "s3_public_access", "status": "FAIL", "detail": "Block Public Access exists but not fully enabled"})

        except s3.exceptions.ClientError as error:
            error_code = error.response['Error']['Code']
            if error_code == 'NoSuchPublicAccessBlockConfiguration':
                findings.append({"resource": bucket_name, "check": "s3_public_access", "status": "FAIL", "detail": "No Block Public Access configuration"})
            else:
                findings.append({"resource": bucket_name, "check": "s3_public_access", "status": "ERROR", "detail": error_code})

    return findings

if __name__ == "__main__":
    results = check_s3_buckets()
    print(results)
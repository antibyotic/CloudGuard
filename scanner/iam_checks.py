import boto3

def check_iam_policies():
    iam = boto3.client('iam')
    findings = []

    policies = iam.list_policies(Scope='Local')['Policies']

    for policy in policies:
        policy_name = policy['PolicyName']
        policy_arn = policy['Arn']
        version_id = policy['DefaultVersionId']

        version = iam.get_policy_version(PolicyArn=policy_arn, VersionId=version_id)
        document = version['PolicyVersion']['Document']

        statements = document['Statement']

        if isinstance(statements, dict):
            statements = [statements]

        for statement in statements:
            sid = statement.get('Sid', 'unnamed-statement')
            effect = statement.get('Effect')
            action = statement.get('Action')
            resource = statement.get('Resource')

            if effect == 'Allow' and action == '*' and resource == '*':
                findings.append({"resource": f"{policy_name} / {sid}", "check": "iam_wildcard_policy", "status": "FAIL", "detail": "Full admin access granted"})
            else:
                findings.append({"resource": f"{policy_name} / {sid}", "check": "iam_wildcard_policy", "status": "PASS"})


    return findings

if __name__ == "__main__":
    results = check_iam_policies()
    print(results)
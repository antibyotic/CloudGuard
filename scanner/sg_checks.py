import boto3

def check_security_groups():
    ec2 = boto3.client('ec2')
    findings = []

    response = ec2.describe_security_groups()
    security_groups = response['SecurityGroups']

    for sg in security_groups:
        group_id = sg['GroupId']
        group_name = sg.get('GroupName', 'unnamed')

        for rule in sg['IpPermissions']:
            from_port = rule.get('FromPort')

            for ip_range in rule.get('IpRanges', []):
                cidr = ip_range.get('CidrIp')

                if cidr == '0.0.0.0/0' and from_port in [22, 3389, 5432]:
                    findings.append({"resource": f"{group_name} ({group_id})", "check": "sg_open_ingress", "status": "FAIL", "detail": f"Port {from_port} open to the internet"})
                else:
                    findings.append({"resource": f"{group_name} ({group_id})", "check": "sg_open_ingress", "status": "PASS"})

    return findings

if __name__ == "__main__":
    results = check_security_groups()
    print(results)
    
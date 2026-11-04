from s3_checks import check_s3_buckets
from iam_checks import check_iam_policies
from sg_checks import check_security_groups
import json

all_findings = []

all_findings.extend(check_s3_buckets())
all_findings.extend(check_iam_policies())
all_findings.extend(check_security_groups())

print(json.dumps(all_findings, indent=2))
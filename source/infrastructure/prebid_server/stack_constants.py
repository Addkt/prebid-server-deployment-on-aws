# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

CUSTOM_RESOURCES_PATH = Path(__file__).absolute().parents[1] / "custom_resources"

X_SECRET_HEADER_NAME = "X-Header-Secret"

PVT_SUBNET_NAME = "Prebid-Private"
PUB_SUBNET_NAME = "Prebid-Public"
VPC_CIDR = "10.8.0.0/16"
CIDR_MASK = 20
MAX_AZS = 2
NAT_GATEWAYS = 2

CONTAINER_PORT = 8080
MEMORY_LIMIT_MIB = 1024
VCPU = 512

HEALTH_URL_DOMAIN = "http://localhost:8080"
HEALTH_PATH = "/status"
HEALTH_ENDPOINT = HEALTH_URL_DOMAIN + HEALTH_PATH
HEALTH_CHECK_INTERVAL_SECS = 120
HEALTH_CHECK_TIMEOUT_SECS = 5

EFS_VOLUME_NAME = "prebid-efs-volume"
EFS_PORT = 2049
EFS_MOUNT_PATH = "/mnt/efs"
EFS_METRICS = "metrics"
EFS_LOGS = "logs"

# Configure for container autoscaling
CPU_TARGET_UTILIZATION_PCT = 62
MEMORY_TARGET_UTILIZATION_PCT = 55
REQUESTS_PER_TARGET = 4000
TASK_MIN_CAPACITY = 2
TASK_MAX_CAPACITY = 300

FARGATE_RESERVED_WEIGHT = 1
FARGATE_SPOT_WEIGHT = 20
FARGATE_MIN_HEALTHY_PERCENT = 100
FARGATE_MAX_HEALTHY_PERCENT = 200
HEALTH_CHECK_GRACE_PERIOD = 120

DATASYNC_DISABLE=True
DATASYNC_METRICS_SCHEDULE = "cron(30 * * * ? *)"  # hourly on the half hour
DATASYNC_LOGS_SCHEDULE = "cron(30 * * * ? *)"  # hourly on the half hour
DATASYNC_REPORT_LIFECYCLE_DAYS = 1

GLUE_MAX_CONCURRENT_RUNS = 10
GLUE_TIMEOUT_MINS = 120
GLUE_ATHENA_OUTPUT_LIFECYCLE_DAYS = 1

# CloudFront managed headers policy CORS-with-preflight-and-SecurityHeadersPolicy
RESPONSE_HEADERS_POLICY_ID = "eaab4381-ed33-4a86-88ca-d9558dc6cd63"

CLOUDWATCH_ALARM_TYPE = "AWS::CloudWatch::Alarm"
CLOUDWATCH_ALARM_NAMESPACE = "AWS/ApplicationELB"

# Anomaly detection with 2 stdev (medium band)
ANOMALY_DETECTION_BAND_2 = "ANOMALY_DETECTION_BAND(m1, 2)"

CLOUD_FRONT_NAMESPACE = "AWS/CloudFront"
RESOURCE_NAMESPACE = "aws:ResourceAccount"

# CloudFront settings
SSL_CERTIFICATE_ARN = "arn:aws:acm:us-east-1:463470947511:certificate/e5848f93-debb-473d-a307-97b8d1fabe75"
DOMAIN_NAMES = ["s2s.lngtd.com"]
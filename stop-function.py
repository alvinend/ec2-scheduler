import boto3
import os
import requests
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

region = 'ap-southeast-1'
instances = [
    'i-0b6aa1851340e829a',
    'i-0aed08b7cd1b32c4d'
]
instances_names = ['grand-admin', 'grand-salary']
ec2 = boto3.client('ec2', region_name=region)

text = '*Stopped Instances ' + current_time + '* :octagonal_sign: \n'
text = text + '```\n'

for i, id in enumerate(instances):
    name = instances_names[i]
    text = text + name + '(' + id + ')\n'
text = text + '```\n'

data = {"text": text }
url = os.environ.get('SLACK_WEBHOOK')

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
    res = requests.post(url, json = data)
    return 200

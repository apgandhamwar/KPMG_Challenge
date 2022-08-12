from typing import List
import requests

response = requests.post('http://169.254.169.254/latest/api/token" --header "X-aws-ec2-metadata-token-ttl-seconds: 21600')

response1= response.json()

token = response['Token']

list=["ami-id",
"ami-launch-index",
"ami-manifest-path",
"block-device-mapping/",
"hostname",
"instance-action",
"instance-id",
"instance-type",
"kernel-id",
"local-hostname",
"local-ipv4",
"mac",
"metrics/",
"network/",
"placement/",
"profile",
"public-",
"public-ipv4",
"public-keys/",
"reservation-id",
"security-groups"]

print (list)

val = input("Enter your MetadataKey: ")

headersVal = {
    'X-aws-ec2-metadata-token': token,
    'Accept': 'application/json',
}

responseMeta = requests.get(url="http://169.254.169.254/latest/meta-data/{}".format(val),headers=headersVal)

print(responseMeta)




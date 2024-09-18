import urllib.request
import json
import ipaddress
import sys

def download_aws_ip_set():
  """Downloads the AWS IP range JSON file and returns it as a dictionary."""

  # URL of the AWS IP range JSON file
  aws_ip_range_url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'

  # Download the JSON file
  with urllib.request.urlopen(aws_ip_range_url) as url:
    aws_ip_range_data = json.load(url)

  return aws_ip_range_data['prefixes']

# Find ip given IP belongs to any AWS Service
def find_aws_ip(aws_ip_range_data, ip_to_find):
  """Finds the AWS IP range that contains the given IP address."""
  return [prefix for prefix in aws_ip_range_data if ipaddress.ip_address(ip_to_find) in ipaddress.ip_network(prefix['ip_prefix'])]

sys.stdout.write(json.dumps(find_aws_ip(download_aws_ip_set(), sys.argv[1]),indent=2))
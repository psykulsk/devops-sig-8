import yaml
import os

vals = dict()

try:
    vals['MAGIC'] = os.environ['MAGIC']
except KeyError:
    vals['MAGIC'] = 'Magic val not found in the environment variables'

with open('/etc/app/config.yml', 'w') as f:
    yaml.safe_dump(vals, f)

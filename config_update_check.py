#!/usr/bin/env python
import os

CONFIGS_DIR = '/etc/app'
TMP_FILE = '/tmp/config_change_time'

current_config_m_time = int(os.path.getmtime(CONFIGS_DIR))

# Try to read last save config dir modification time
try:
    with open(TMP_FILE, 'r') as f:
        last_config_m_time = int(f.readline())
except FileNotFoundError:
    last_config_m_time = None

# Write current config dir modification time
with open(TMP_FILE, 'w') as f:
    f.write(str(current_config_m_time))

if last_config_m_time and current_config_m_time > last_config_m_time:
    print("Config dir was modified since last check. Exiting with non-zero code.")
    exit(1)
else:
    exit(0)




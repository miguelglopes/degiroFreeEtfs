import logging
import os
import json

config=None
full_config_dir = "C:\\Miguel\\Nextcloud\\projetos\\etfs\\"
config_file_name = "config.json"
config_file = os.path.join(full_config_dir, config_file_name)
logger = logging.getLogger('log1')

with open(config_file) as config_file:
    config = json.load(config_file)
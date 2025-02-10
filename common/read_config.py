import yaml

from constants.path import config_path

with open(config_path, 'r') as file:
    config_path = 'config.yml'
    config = yaml.safe_load(file)
GENAI_CONFIG = config.get('genai', {}).get('ollama', {})

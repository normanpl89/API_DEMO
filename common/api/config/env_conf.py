import os


class SplunkEnvironmentConfig:
    ENVIRONMENT = os.getenv('ENV', 'TEST')
    ENVIRONMENT_PARAMS = {
        'TEST': {
            'API_HOST': 'https://cat-fact.herokuapp.com/facts'
        }
    }


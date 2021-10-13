from tests.api import constant
from requests import get
from common.api.config.env_conf import SplunkEnvironmentConfig as ApiHost

api_host = ApiHost.ENVIRONMENT_PARAMS[ApiHost.ENVIRONMENT]['API_HOST']


class FactHelper:

    @staticmethod
    def get_fact_random_results():
        endpoint = constant.API_ENDPOINTS['GET_RANDOM_FACTS']
        response = get(api_host + endpoint)
        return response

    @staticmethod
    def get_fact_random_by_amount(amount):
        endpoint = constant.API_ENDPOINTS['GET_RANDOM_FACTS']

        param = {
            'animal_type': 'cat',
            'amount': amount
        }

        response = get(api_host + endpoint, param)
        return response

    @staticmethod
    def get_fact_by_id(fact_id):
        endpoint = constant.API_ENDPOINTS['GET_FACT_BY_ID'].format(fact_id=fact_id)

        response = get(api_host + endpoint)
        return response


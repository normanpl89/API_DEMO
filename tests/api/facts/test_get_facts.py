import pytest as pytest
from hamcrest import assert_that, equal_to, less_than_or_equal_to
from common.api.helpers.fact_api_helper import FactHelper
from tests.api import constant
import allure


@pytest.mark.get_random_fact
@pytest.mark.parametrize('expected_response_code, expected_response_time, expected_type',
                         [(constant.STATUS_CODE_200_OK, constant.DEFAULT_RESPONSE_TIME, 'cat')])
@allure.title('Retrieve random results from cat-facts api')
def test_get_random_fact_items(expected_response_code, expected_response_time, expected_type):

    # ARRANGE #
    response = FactHelper.get_fact_random_results()

    # ASSERT #
    assert_that(response.status_code, equal_to(expected_response_code), 'Verify the response status code')
    assert_that(response.elapsed.microseconds, less_than_or_equal_to(expected_response_time), 'Verify response time')
    assert_that(response.json()['type'], equal_to(expected_type), 'Verify Type match with the one provided')


@pytest.mark.get_random_by_amount
@pytest.mark.parametrize('expected_response_code, expected_response_time, expected_type, amount',
                         [(constant.STATUS_CODE_200_OK, constant.DEFAULT_RESPONSE_TIME, 'cat', 5)])
@allure.title('Retrieve random results by amount from cat-facts api')
def test_get_random_fact_by_amount(expected_response_code, expected_response_time, expected_type, amount):

    # ARRANGE #
    response = FactHelper.get_fact_random_by_amount(amount)

    # ASSERT #
    assert_that(response.status_code, equal_to(expected_response_code), 'Verify the response status code')
    assert_that(response.elapsed.microseconds, less_than_or_equal_to(expected_response_time), 'Verify response time')
    assert_that(len(response.json()), equal_to(amount), 'The provided amount does not match')


@pytest.mark.get_empty_fact
@pytest.mark.parametrize('expected_response_code, expected_response_time, expected_type, amount',
                         [(constant.STATUS_CODE_200_OK, constant.DEFAULT_RESPONSE_TIME, 'cat', 0)])
@allure.title('Verify if we pass Amount = 0 the cat-facts api does not return any response')
def test_get_random_fact_w_zero_amount(expected_response_code, expected_response_time, expected_type, amount):

    # ARRANGE #
    response = FactHelper.get_fact_random_by_amount(amount)

    # ASSERT #
    assert_that(response.status_code, equal_to(expected_response_code), 'Verify the response status code')
    assert_that(response.elapsed.microseconds, less_than_or_equal_to(expected_response_time), 'Verify response time')
    assert_that(len(response.json()), equal_to(amount), 'The provided amount does not match')


@pytest.mark.get_fact_result_by_id
@pytest.mark.parametrize('expected_response_code, expected_response_time, expected_type, fact_id, amount',
                         [(constant.STATUS_CODE_200_OK, constant.DEFAULT_RESPONSE_TIME, 'cat',
                           '591f97b4ccb34a14d3f7dc94', 1)])
@allure.title('Verify if cat-facts api return a valid record by ID')
def test_get_fact_by_id(expected_response_code, expected_response_time, expected_type, fact_id, amount):

    # ARRANGE #
    response = FactHelper.get_fact_by_id(fact_id)

    # ASSERT #
    assert_that(response.status_code, equal_to(expected_response_code), 'Verify the response status code')
    assert_that(response.elapsed.microseconds, less_than_or_equal_to(expected_response_time), 'Verify response time')
    assert_that(response.json()['type'], equal_to(expected_type), 'Verify Type match with the one provided')
    assert_that(response.json()['_id'], equal_to(fact_id), 'Verify the provided id')


@pytest.mark.get_fact_result_invalid_id
@pytest.mark.parametrize('expected_response_code, expected_response_time, expected_type, fact_id, amount',
                         [(constant.STATUS_CODE_404_NOT_FOUND, constant.DEFAULT_RESPONSE_TIME, 'cat',
                           'aa1f97b4ccb34a14d3f7dc94', 1)])
@allure.title('Verify the cat-facts api return an error using an invalid record by ID')
def test_get_fact_invalid_id(expected_response_code, expected_response_time, expected_type, fact_id, amount):

    # ARRANGE #
    response = FactHelper.get_fact_by_id(fact_id)

    # ASSERT #
    assert_that(response.status_code, equal_to(expected_response_code), 'Verify the response status code')
    assert_that(response.elapsed.microseconds, less_than_or_equal_to(expected_response_time), 'Verify response time')
    assert_that(response.json()['message'], equal_to('Fact not found'), 'Verify the error message.')


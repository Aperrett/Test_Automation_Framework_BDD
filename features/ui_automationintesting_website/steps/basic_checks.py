from lib.webdriver.page import BrowserPage
from lib.webdriver.automationintesting import BasicChecks
from selenium.webdriver.common.by import By
from behave import when, then


@when('the user navigates to "{url}"')
def step_impl(context, url):
    BrowserPage(context.browser).visit(url)


@then('the browser title is "{browser_title}"')
def step_impl(context, browser_title):
    current_title = context.browser.driver.title
    assert BasicChecks(context.browser).title_is(browser_title),\
        f'got Title: {current_title}, expected Title: {browser_title}'


@then('the url is "{url}"')
def step_impl(context, url):
    current_url = context.browser.driver.current_url
    assert BasicChecks(context.browser).url_is(url),\
        f'got URL: {current_url}, expected URL: {url}'


@then('the h2 title is "{h2_tag}"')
def step_impl(context, h2_tag):
    assert BasicChecks(context.browser).h2_is(h2_tag)


@when('the user inputs Name "{text_value}"')
def step_impl(context, text_value):
    id = 'name'
    BasicChecks(context.browser).input_field_by_id(id, text_value)


@when('the user inputs Email "{text_value}"')
def step_impl(context, text_value):
    id = 'email'
    BasicChecks(context.browser).input_field_by_id(id, text_value)


@when('the user inputs Phone "{text_value}"')
def step_impl(context, text_value):
    id = 'phone'
    BasicChecks(context.browser).input_field_by_id(id, text_value)


@when('the user inputs Subject "{text_value}"')
def step_impl(context, text_value):
    id = 'subject'
    BasicChecks(context.browser).input_field_by_id(id, text_value)


@when('the user inputs Message "{text_value}"')
def step_impl(context, text_value):
    id = 'description'
    BasicChecks(context.browser).input_field_by_id(id, text_value)


@when('the user clicks on submit button')
def step_impl(context):
    BasicChecks(context.browser).click_submit_button()


@then('the user should see a h2 message "{message}"')
def step_impl(context, message):
    path = '//*[@id="root"]/div/div/div[5]/div[2]/div/h2'
    check1 = context.browser.driver.find_element(By.XPATH, path).text

    assert (message in check1), \
        f'Got Message: {check1}, Expected Message: {message}'

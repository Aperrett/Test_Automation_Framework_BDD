from behave import use_fixture

from lib.webdriver.behave_hooks import start_browser, screenshot_on_fail


def after_step(context, step):
    screenshot_on_fail(context, step)


def before_feature(context, feature):
    use_fixture(start_browser, context)


def before_scenario(context, scenario):
    context.browser.driver.get('https://automationintesting.online/')
    context.browser.driver.delete_all_cookies()

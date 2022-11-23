import os
import re

from behave import fixture
from selenium.common.exceptions import WebDriverException

from lib.webdriver.context import BrowserContext


@fixture
def start_browser(context):
    context.browser = BrowserContext()
    yield
    context.browser.driver.quit()


def screenshot_on_fail(context, step):
    if step.status != 'failed' \
            or not isinstance(step.exception, WebDriverException):
        return

    # Save a screenshot of the current page if the failing test is using a
    # browser and the error corresponds to an element not being found.
    feature_file = os.path.basename(context.feature.filename)
    scenario_name = re.sub(r'[^a-zA-Z_0-9]', '_', context.scenario.name)
    step_name = re.sub(r'[^a-zA-Z_0-9]', '_', step.name)

    location = f'{os.getcwd()}/screenshots/{feature_file}/{scenario_name}'

    os.makedirs(location, mode=0o755, exist_ok=True)

    filename = f'{location}/{step_name}.png'

    print(f'Failed to find element. Saving screenshot to {filename}')

    success = context.browser.driver.save_screenshot(filename)

    if not success:
        print('Failed to save screenshot')

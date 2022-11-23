import os
import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class BrowserContext():
    def __init__(self):
        if "browser=firefox" in sys.argv:
            self.firefox_browser()
        elif "browser=chrome" in sys.argv:
            self.chrome_browser()
        elif "browser=zap" in sys.argv:
            self.zap_browser()
        else:
            self.headless_browser()

    def headless_browser(self):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.add_argument('--ignore-certificate-errors')
        chrome_opts.add_argument('--headless')
        chrome_opts.add_argument('--no-sandbox')
        chrome_opts.add_argument('--window-size=1920,1080')
        chrome_opts.add_argument('--disable-gpu')

        if os.path.exists('/usr/bin/chromedriver'):
            self.driver = webdriver.Chrome(
                executable_path='/usr/bin/chromedriver',
                options=chrome_opts
            )
        else:
            self.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=chrome_opts
            )

        self.driver.implicitly_wait(60)

    def firefox_browser(self):
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        options = Options()
        self.driver = webdriver.Firefox(
            firefox_profile=profile,
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)

    def chrome_browser(self):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.add_argument('--start-fullscreen')
        chrome_opts.add_argument('--ignore-certificate-errors')

        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_opts
        )
        self.driver.implicitly_wait(60)

    def zap_browser(self):
        zap_ip = os.environ['ZAP_CONTAINER_IP']
        port = os.environ['OWASP_PORT']
        PROXY = f"{zap_ip}:{port}"
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.add_argument('--ignore-certificate-errors')
        chrome_opts.add_argument('--headless')
        chrome_opts.add_argument('--no-sandbox')
        chrome_opts.add_argument('--window-size=1920,1080')
        chrome_opts.add_argument('--disable-gpu')
        chrome_opts.add_argument('--proxy-server=http://%s' % PROXY)

        self.driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver',
            options=chrome_opts
        )

        self.driver.implicitly_wait(60)

from selenium.webdriver import Remote as RemoteWebDriver

class BasePage():
    def __init__(self, browser: RemoteWebDriver, url):
        """Конструктор класса.
        :param browser:
        :param url:
        """
        self.browser = browser
        self.url = url

    def open(self):
        #метод открывает нужную страницу, используя метод get()
        self.browser.get(self.url)

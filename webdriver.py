from selenium import webdriver

class Driver:
    def __init__(self):
        self.chromedriver_loc = 'D:\Projects\PythonProjects\SeleniumAutomationFramework\chromedriver'
        self.instance = webdriver.Chrome(executable_path=self.chromedriver_loc)

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string")
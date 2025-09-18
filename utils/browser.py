from selenium import webdriver

def get_driver(browser='chrome'):
    if browser == 'chrome':
        return webdriver.Chrome()
    elif browser == 'firefox':
        return webdriver.Firefox()
    else:
        raise ValueError('Unsupported browser')

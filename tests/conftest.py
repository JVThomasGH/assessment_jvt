import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = None


@pytest.fixture
def base_uri():
    return "https://dog.ceo/"


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get("http://www.way2automation.com/angularjs-protractor/webtables/")
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(params=[{"first_name": "FName1", "last_name": "LName1", "user_name": "User1", "password": "Pass1",
                         "customer": "CompanyAAA", "role": "Admin", "email": "admin@mail.com", "cell": "082555"},
                        {"first_name": "FName2", "last_name": "LName2", "user_name": "User2", "password": "Pass2",
                         "customer": "CompanyBBB",
                         "role": "Customer", "email": "customer@mail.com", "cell": "083444"}])
def data_set(request):
    return request.param


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """Extends the Pytest Plugin to take and embed screenshot in html report upon test failure"""
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

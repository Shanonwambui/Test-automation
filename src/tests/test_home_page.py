# Python
import pytest
from src.pages.BasePage import BasePage
from src.utils.helpers import get_driver
from src.utils.config import BASE_URL

class TestHomePage:
    @pytest.fixture
    def home(self, base_driver):
        base_page = BasePage(base_driver)
        return base_page

    @pytest.fixture
    def base_driver(self):
        driver = get_driver()  # replace with your actual driver setup code
        yield driver
        driver.quit()  # replace with your actual driver teardown code

    def test_home_page_loads(self, home):
        assert "Automation Exercise" in home.driver.title
    
import allure
import pytest


class Test_01(object):
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="测试步骤01_用例1")
    def test_01(self):
        allure.attach("描述1","用例步骤1")
        allure.attach("描述1","用例步骤2")
        allure.attach("描述1","用例步骤3")
        assert 0


    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="测试步骤_用例2")
    def test_02(self):
        allure.attach("描述2","用例步骤1")
        allure.attach("描述2","用例步骤2")
        allure.attach("描述2","用例步骤3")
        assert 1
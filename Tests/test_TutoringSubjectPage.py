import pytest
from Config.configuration import TestData
from Pages.HomePage import HomePage
from Pages.addsubjectpage import SubjectPage
from Tests.test_base import BaseTest
from ddt import ddt, data, file_data, unpack
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class Add_Subject:
    def test_add_subject_added(self):
        sp = SubjectPage(self.driver)
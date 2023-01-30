from lib2to3.pytree import convert
from packages.service import UserContactConverter


class TestUserContactConverter:

    converter = UserContactConverter("", "", "")
    test_data = {
        "firstName": " LOREM",
        "lastName": "  IPSUM  ",
        "dateOfBirth": "31-01-1986",
        "lifetime_value": "$125500.00",
    }

    def test_clean_data(self):

        firstname, lastname = self.converter.data_cleaner(
            self.test_data["firstName"], self.test_data["lastName"]
        )

        assert firstname == "LOREM"
        assert lastname == "IPSUM"
        assert firstname != " LOREM"
        assert lastname != "  IPSUM  "

    def test_transform_data(self):

        birth, liftime = self.converter.transfor_data(
            self.test_data["dateOfBirth"], self.test_data["lifetime_value"]
        )

        assert birth == "1986-01-31"
        assert liftime == 125500.00

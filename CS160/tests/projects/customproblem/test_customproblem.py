#!/usr/bin/env python3
"""
Testing custom problem
@author: Isaac List
@updated: 2019
"""

import pytest
from src.projects.customproblem import (
    Language,
    Country,
    Resident,
    Tourist,
    Local
)

class TestCustomProblemMethods:
    """Testing module customproblem"""

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self):
        """Setting up"""
        pass

    def test_Language(self):
        """Testing Language"""
        german = Language("German", "Hallo", "Danke")
        assert german.greeting == "Hallo"
        french = Language("French", "Bonjour", "Merci")
        assert french.thanks == "Merci"
        assert french.__str__() == "In French, people say Bonjour"

    def test_Country(self):
        """Testing Country"""
        german = Language("German", "Hallo", "Danke")
        Germany = Country("Germany", german)
        assert Germany.name == "Germany"
        assert Germany.language.greeting == "Hallo"

    def test_Resident(self):
        """
        Testing Resident
        
        Scream and cry, IDK how to do this
        """
        pass

    def test_Tourist(self):
        """Testing Tourist"""
        english = Language("English", "Hello", "Thanks")
        america = Country("America", english)
        american_tourist = Tourist("Dwayne", america, "Berlin")
        assert american_tourist.destination == "Berlin"
        assert american_tourist.__str__() == \
            "Hello, Dwayne is from America"
        assert american_tourist.ask_for_directions == "Can you give me \
            directions to Berlin? Thanks!"
        american_tourist.destination = "Oslo"
        assert american_tourist.destination == "Oslo"

    def test_Local(self):
        """Testing Local"""
        chinese = Language("中文", "你好", "谢谢")
        china = Country("China", chinese)
        chinese_local = Local("李爱克", china, True)
        assert chinese_local.name == "李爱克"
        assert chinese_local.offer_directions == \
            "I can give you directions"
        assert chinese_local.say_hello == "李爱克 says 你好"

    def test_f(self):
        """Testing something"""
        pass

    def test_g(self):
        """Testing something"""
        pass

    def test_h(self):
        """Testing something"""
        pass

    def test_i(self):
        """Testing something"""
        pass

    def test_j(self):
        """Testing something"""
        pass


if __name__ == "__main__":
    pytest.main(["-vv", "test_customproblem.py"])

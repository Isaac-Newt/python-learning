#!/usr/bin/env python3
"""
Isaac List - CS160
March 16, 2019

customproblem classes
"""

from abc import ABC, abstractmethod

# Country has a...
class Language:
    """Define how to greet someone in a language [Name]"""

    def __init__(self, Name: str, Greeting: str):
        """__init__"""
        self._name = Name
        self._greeting = Greeting

    def get_name(self):
        """Name Getter"""
        return self._name

    name = property(get_name)

    def get_greeting(self):
        """Greeting Getter"""
        return self._greeting

    greeting = property(get_greeting)


class Country:
    """
    Every citizen has a country

    Takes a country name and a language object
    """

    def __init__(self, Country_Name: str, Country_Language: object):
        """__init__"""
        self._name = Country_Name
        self._language = Country_Language

    def get_name(self):
        """Getter"""
        return self._name

    name = property(get_name)

    def get_language(self):
        """Getter"""
        return self._language

    language = property(get_language)


class Nationality(ABC):
    """
    Base class, extended by American and German

    Takes a person's name, and a country object
    """

    def __init__(self, Persons_Name: str, Persons_Country: object):
        """__init__"""
        self._name = Persons_Name
        self._country = Persons_Country

    def get_name(self):
        """Getter"""
        return self._name

    name = property(get_name)

    def get_country(self):
        """Getter"""
        return self._country

    country = property(get_country)

    @abstractmethod
    def __str__(self):
        """Abstract Method for __str__"""
        pass

    def __eq__(self, other):
        """Equal if from same country"""
        return self.country == other.country


class American(Nationality):
    """An American Citizen"""

    def __init__(self, Persons_Name: str, Persons_Country: object, State: str):
        """__init__"""
        super().__init__(Persons_Name, Persons_Country)
        self._state = State

    def get_state(self):
        """Getter"""
        return self._state

    def set_state(self, value: str):
        """Setter"""
        self._state = value

    state = property(get_state, set_state)

    def __str__(self):
        """__str__"""
        return f"{self.country.language.greeting}, {self.name} is from \
                {self.country}, and live in {self.state}"

    def __eq__(self, other):
        """Same if live in same state"""
        return self.state == other.state

    def move(self, new_state: str):
        """Change State"""
        self.state = new_state


class German(Nationality):
    """A German Person"""

    def __init__(self, Persons_Name: str, Persons_Country: object, Oktoberfest: bool):
        """__init__"""
        super().__init__(Persons_Name, Persons_Country)
        self._attends_oktoberfest = Oktoberfest

    def get_att_okt(self):
        """Getter"""
        return self._attends_oktoberfest

    oktoberfest = property(get_att_okt)

    def __str__(self):
        """__str__"""
        if self.oktoberfest:
            string = f"{self.country.language.greeting}, {self.name} is from \
                {self.country}, and attends Oktoberfest"
        else:
            string = f"{self.country.language.greeting}, {self.name} is from \
                {self.country}, and does not attend Oktoberfest"
        return string

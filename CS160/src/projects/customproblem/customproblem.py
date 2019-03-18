#!/usr/bin/env python3
"""
Isaac List - CS160
March 16, 2019

customproblem classes
"""

from abc import ABC, abstractmethod

# Country has a...
class Language:
    """Define how to say things in a language"""

    def __init__(self, Name: str, Greeting: str, Phrase: str):
        """__init__"""
        self._name = Name
        self._greeting = Greeting
        self._other_phrase = Phrase

    def get_name(self):
        """Name Getter"""
        return self._name

    name = property(get_name)

    def get_greeting(self):
        """Greeting Getter"""
        return self._greeting

    greeting = property(get_greeting)

    def get_other_phrase(self):
        """Phrase Getter"""
        return self._other_phrase

    phrase = property(get_other_phrase)


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


class Resident(ABC):
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
    
    def say_hello(self):
        return f"{self.name} says {self.country.language.greeting}!"


class Tourist(Resident):
    """
    A Tourist
    
    Extends Resident with methods ask_for_directions, travel
    """

    def __init__(self, Persons_Name: str, Persons_Country: object, Destination: str):
        """__init__"""
        super().__init__(Persons_Name, Persons_Country)
        self._destination = Destination

    def get_destination(self):
        """Getter"""
        return self._destination

    def set_destination(self, value: str):
        """Setter"""
        self._destination = value

    destination = property(get_destination, set_destination)

    def __str__(self):
        """__str__"""
        return f"{self.country.language.greeting}, {self.name} is from \
                {self.country}, and is going to {self.destination}"

    def __eq__(self, other):
        """__eq"""

    def ask_for_directions(self):
        return f"Can you give me directions to {self.destination}?"

    def travel(self, new_destination: str):
        """Change Destination"""
        self.destination = new_state


class Local(Resident):
    """A Local Person"""

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

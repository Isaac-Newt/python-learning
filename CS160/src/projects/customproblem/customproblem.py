#!/usr/bin/env python3
"""
Isaac List - CS160
March 18, 2019

Classes for Residents
"""

from abc import ABC, abstractmethod

# Country has a...
class Language:
    """Define how to say things in a language"""

    def __init__(self, Name: str, Greeting: str, Thanks: str):
        """__init__"""
        self._name = Name
        self._greeting = Greeting
        self._thanks = Thanks

    def get_name(self):
        """Name Getter"""
        return self._name

    name = property(get_name)

    def __eq__(self, other):
        """__eq__"""
        return self.name == other.name

    def __str__(self):
        """__str__"""
        return f"In {self.name}, people say {self.greeting}."

    def get_greeting(self):
        """Greeting Getter"""
        return self._greeting

    greeting = property(get_greeting)

    def get_thanks(self):
        """Thanks Getter"""
        return self._thanks

    thanks = property(get_thanks)


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
        """
        __eq__
        Equal if from the same country and going to the same place
        """
        eq = False
        if self.country == other.country:
            if self.destination == other.destination:
                eq = True
        return eq

    def ask_for_directions(self):
        return f"Can you give me directions to {self.destination}? \
            {self.country.language.thanks}!"

    def travel(self, new_destination: str):
        """Change Destination"""
        self.destination = new_state


class Local(Resident):
    """A Local Person"""

    def __init__(self, Persons_Name: str, Persons_Country: object, Helpful: bool):
        """__init__"""
        super().__init__(Persons_Name, Persons_Country)
        self._helpful

    def get_helpful(self):
        return self._helpful

    helpful = property(get_helpful)

    def __str__(self):
        """__str__"""
        return f"{self.country.language.greeting}, {self.name} \
            is from {self.country}"

    def offer_directions(self):
        """Offer directions if helpful"""
        if self.helpful:
            string = f"I can give you directions"
        else:
            string = f"I can't help you"
        return string

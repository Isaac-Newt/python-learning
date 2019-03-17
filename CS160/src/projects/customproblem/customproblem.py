#!/usr/bin/env python3
"""
Isaac List - CS160
March 16, 2019

customproblem classes
"""

from abc import ABC, abstractmethod

# Country has a...
class Language():
    def __init__(self, Name: str, Greeting: str):
        self._name = Name
        self._greeting = Greeting

    def get_name(self):
        return self._name

    name = property(get_name)

    def get_greeting(self):
        return self._greeting

    greeting = property(get_greeting)


# Citizen has (a)... 
class Country():
    def __init__(self, Name: str, Language: object):
        self._name = Name
        self._language = Language

    def get_name(self):
        return self._name

    name = property(get_name)

    def get_language(self):
        return self._language

    language = property(get_language)


class Nationality(ABC):
    def __init__(self, Name: str, Country: object):
        self._name = Name
        self._country = Country

    def get_name(self):
        return self._name

    name = property(get_name)

    @abstractmethod
    def __str__(self):
        pass

    def __eq__(self, other):
        return self._country == other._country


class American(Country):
    def __init__(self, Name: str, Country: object, State: str):
        super.__init__(Name, Country)
        self._state = State

    def get_state(self):
        return self._state

    def set_state(self, value: str)

    state = property(get_state, set_state)

    def __str__(self):
        return f"{self.language.greeting}, {self.name} is from \
                {self.country}, and live in {self.state}"

    def __eq__(self, other):
        return self._state == other._state


class German(Country):
    def __init__(self, Name: str, Country: object, Oktoberfest: bool):
        super.__init__(Name, Country)
        self._attends_oktoberfest = Oktoberfest

    def get_att_okt(self):
        return self._attends_oktoberfest

    oktoberfest = property(get_att_okt)

    def __str__(self):
        if self.oktoberfest:
            return f"{self.language.greeting}, {self.name} is from \
                {self.country}, and attends Oktoberfest"
        else:
            return f"{self.language.greeting}, {self.name} is from \
                {self.country}, and does not attend Oktoberfest"
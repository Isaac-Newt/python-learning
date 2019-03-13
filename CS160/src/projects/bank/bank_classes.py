#!/usr/bin/env python3
"""
Banking classes implementation

Isaac List - CS160
March 12, 2019
"""

from abc import ABC, abstractmethod


class Address:
    """Address class"""

    def __init__(
        self, street_init: str, city_init: str, state_init: str, zip_init: str
    ):
        """__init__"""
        self._street = street_init
        self._city = city_init
        self._state = state_init
        self._zip = zip_init

    def __eq__(self, other: object):
        """Compare 2 addresses"""
        equal = False
        if self._street == other._street:
            if self._city == other._city:
                if self._state == other._state:
                    if self._zip == other._zip:
                        equal = True
        return equal

    def get_street(self):
        """Get Street"""
        return self._street

    def set_street(self, value: str):
        """Set Street"""
        self._street = value

    street = property(get_street, set_street)

    def get_city(self):
        """Get City"""
        return self._city

    def set_city(self, value: str):
        """Set City"""
        self._city = value

    city = property(get_city, set_city)

    def get_state(self):
        """Get State"""
        return self._state

    def set_state(self, value: str):
        """Set State"""
        self._state = value

    state = property(get_state, set_state)

    def get_zip(self):
        """Get Zip"""
        return self._zip

    def set_zip(self, value: str):
        """Set Zip"""
        self._zip = value

    zip = property(get_zip, set_zip)

    def __str__(self):
        """__str__ method"""
        return f"{self.street}\n{self.city}, {self.state} {self.zip}"


class Customer:
    """Customer class"""

    def __init__(self, name_init: str, dob_init: str, address_init: object):
        """Constructor"""
        self._name = name_init
        self._dob = dob_init
        self._address = address_init

    def get_name(self):
        """Get Name"""
        return self._name

    def set_name(self, value: str):
        """Set Name"""
        self._name = value

    name = property(get_name, set_name)

    def get_dob(self):
        """Get DOB"""
        return self._dob

    def set_dob(self, value: str):
        """Set DOB"""
        self._dob = value

    dob = property(get_dob, set_dob)

    def get_address(self):
        """Get Address"""
        return self._address

    def set_address(self, value: object):
        """Set Address"""
        self.move(value)

    address = property(get_address, set_address)

    def move(self, new_address: object):
        """Change address"""
        self._address = new_address

    def __str__(self):
        """__str"""
        return f"{self.name} ({self.dob})\n{self.address}"


class Account(ABC):
    """Account class"""

    @abstractmethod
    def __init__(self, owner_init: object, balance_init: float = 0):
        """Constructor"""
        self._owner = owner_init
        self._balance = balance_init

    def get_owner(self):
        """Get Owner"""
        return self._owner

    def set_owner(self, value: object):
        """Set Owner"""
        self._owner = value

    owner = property(get_owner, set_owner)

    def get_balance(self):
        """Get Balance"""
        return self._balance

    def set_balance(self, value: float):
        """Set Balance"""
        self._balance = value

    balance = property(get_balance, set_balance)

    def deposit(self, amount: float):
        """Add money"""
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Must deposit positive amount")

    def close(self):
        """Close account"""
        self._balance = 0

    @abstractmethod
    def __str__(self):
        """__str__"""
        pass


class CheckingAccount(Account):
    """CheckingAccount class"""

    def __init__(self, owner_init: object, fee_init: float, balance_init: float = 0):
        """Constructor"""
        super().__init__(owner_init, balance_init)
        self._fee = fee_init

    def get_fee(self):
        """Get Fee"""
        return self._fee

    fee = property(get_fee)

    def process_check(self, amount: float):
        """Process a check"""
        if amount <= self.balance:
            self.balance -= amount
        else:
            self.balance -= self.fee

    def __str__(self):
        """__str__"""
        return f"Checking account\nOwner: {self.owner}\nBalance: {self.balance:.2f}"


class SavingsAccount(Account):
    """CheckingAccount class"""

    def __init__(
        self, owner_init: object, interest_rate_init: float, balance_init: float = 0
    ):
        """Constructor"""
        super().__init__(owner_init, balance_init)
        self._annual_interest_rate = interest_rate_init

    def yield_interest(self):
        """Yield annual interest"""
        self.balance += self._annual_interest_rate / 100 * self.balance

    def __str__(self):
        """__str__"""
        return f"Savings account\nOwner: {self.owner}\nBalance: {self.balance:.2f}"

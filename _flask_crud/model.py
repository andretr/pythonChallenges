import logging

# !/usr/bin/python
class FamilyMember:

    def __init__(self, name, accounts=None):
        self.name = name
        self.accounts = accounts
        self.hobbies = []

    def add_hobbies(self, *hobbiesList):
        for i in hobbiesList:
            self.hobbies.append(i)

    def get_cuenta(self, cuenta):
        print(cuenta)
        for key, val in self.accounts.items():
            print(key,"->", val)
        if cuenta in self.accounts:
            return cuenta
        else:
            raise Exception('El numero de cuenta no existe')

class Account:

    def __init__(self, total):
        self.total = total

    def log_withdrawal(func):
        def wrapper():
            logging.debug('Registrando retiro')
            func()
        return wrapper

    def deposit(self, amount):
        self.total += amount

    @log_withdrawal
    def withdrawal(self, amount):
        if(amount <= self.total):
            self.total -= amount
        else:
            raise Exception('La cuenta no tiene fondos suficientes para el retiro')

    def get_total(self):
        return  self.total





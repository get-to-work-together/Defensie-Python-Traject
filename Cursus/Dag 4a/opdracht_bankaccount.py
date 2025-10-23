class BankAccount:

    def __init__(self, accountnumber, holder, balance = 0.0):
        self._accountnumber = accountnumber
        self._holder = holder
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def info(self):
        print(f'Account {self._accountnumber} belongs to {self._holder} has a balance of €{self._balance:.2f}.')


# ------------------------------------------------------------------------

account = BankAccount('NL99ABCD0123454321', 'Peter', 1000)

account.info()

account.deposit(2000)
account.withdraw(23)
account.withdraw(110.25)
account.deposit(55)

account.info()

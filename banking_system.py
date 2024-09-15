from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

class Account(ABC):
    def __init__(self, account_number: int, balance: int, account_type: str) -> None:
        self._account_number = account_number
        self._balance = balance
        self._account_type = account_type

    def getBalance(self):
        return self._balance
    
    def setBalance(self, new_balance) -> None:
        self._balance = new_balance

    def getAccountType(self):
        return self._account_type
    
    def getAccountNumber(self):
        return self._account_number

    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    @abstractmethod
    def transfer(self, destination: "Account", amount: float) -> None:
        pass

    @abstractmethod
    def show_balance(self) -> None:
        pass

    @abstractmethod
    def get_account_type(self) -> str:
        pass

class CheckingAccount(Account):
    def __init__(self,account_number: int, balance: int, account_type: str, overdraft_limit: float):
        super().__init__(account_number, balance, "Checking")
        self._overdraft_limit = overdraft_limit
        
    def deposit(self, amount: float) -> None:
        self.setBalance(self.getBalance() + amount)

    def withdraw(self, amount: float) -> None:
        balance = self.getBalance()
        if amount <= balance + self._overdraft_limit:
            self.setBalance(self.getBalance() - amount)
        else:
            print("Withdraw amount exceedes balance.")

    def transfer(self, destination: "Account", amount: float) -> None:
        balance = self.getBalance()
        if amount <= balance + self._overdraft_limit:
            self.withdraw(amount)
            destination.deposit(amount)
        else:
            print("Transfer cannot be done.")

    def show_balance(self) -> None:
        print(self.getBalance())

    def get_account_type(self) -> str:
        print(self.getAccountType())

class SavingsAccount(Account):
    def __init__(self, account_number: int, balance: int, account_type: str, interest_rate):
        super().__init__(account_number, balance, "Savings") 
        self._interest_rate = interest_rate

    def deposit(self, amount: float) -> None:
        self.setBalance(self.getBalance() + amount)

    def withdraw(self, amount: float) -> None:
        balance = self.getBalance()
        if amount <= balance:
            self.setBalance(self.getBalance() - amount)
        else:
            print("Withdraw amount exceedes balance.")

    def transfer(self, destination: "Account", amount: float) -> None:
        balance = self.getBalance()
        if amount <= balance:
            self.withdraw(amount)
            destination.deposit(amount)
        else:
            print("Transfer cannot be done.")

    def show_balance(self) -> None:
        print(self.getBalance())

    def get_account_type(self) -> str:
        print(self.getAccountType())

class JointAccount(Account):
    def __init__(self, account_number, balance, account_type, joint_owners: List[str]):
        super().__init__(account_number, balance, "Joint")
        self._joint_owners = joint_owners

    def deposit(self, amount: float) -> None:
        self.setBalance(self.getBalance() + amount)

    def withdraw(self, amount: float) -> None:
        balance = self.getBalance()
        if amount <= balance:
            self.setBalance(self.getBalance() - amount)
        else:
            print("Withdraw amount exceedes balance.")

    def transfer(self, destination: "Account", amount: float) -> None:
        balance = self.getBalance()
        if amount <= balance:
            self.withdraw(amount)
            destination.deposit(amount)
        else:
            print("Transfer cannot be done.")

    def show_balance(self) -> None:
        print(self.getBalance())

    def get_account_type(self) -> str:
        print(self.getAccountType())

    def add_owner(self, customer_name: str) -> None:
        if customer_name not in self._joint_owners:
            self._joint_owners.append(customer_name)

# this is an interface,it doesn't have properties
class TransactionManager:
    @abstractmethod
    def log_transaction(self, transaction_type: str, amount: float) -> None:
        pass

    @abstractmethod
    def show_transaction_history(self) -> None:
        pass

class Transaction:
    def __init__(self, from_account: Account, to_account: Optional['Account'], amount: float, transaction_type: str) -> None:
        self._from_account = from_account
        self._to_account = to_account
        self._amount = amount
        self._transaction_type = transaction_type
        self._timestamp = datetime.now()
    
    def log(self) -> None:
        print(f"From: {self.__from_account} | To: {self.__to_account} | {self.__amount} | {self.__transaction_type} | {self.__timestamp}")

class Customer:
    def __init__(self, name: str, contact_info: str):
        self._name: str = name
        self._contact_info: str = contact_info
        self._accounts: List[Account] = []

    def add_account(self, account: Account) -> None:
        self._accounts.append(account)

    def view_accounts(self) -> None:
        for account in self._accounts:
            print(account)

    def view_transactions(self) -> None:
        pass

    def view_transactions_history(self) -> None:
        pass
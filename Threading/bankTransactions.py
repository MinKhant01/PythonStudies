import threading
import random
import time

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            old_balance = self.balance
            self.balance += amount
            print(f"{threading.current_thread().name} deposited ${amount}."
                  f"Balance: ${old_balance} -> ${self.balance}")
    
    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                old_balance = self.balance
                self.balance -= amount
                print(f"{threading.current_thread().name} withdraws ${amount}."
                      f"Balance: ${old_balance} -> ${self.balance}")
            else:
                print(f"{threading.current_thread().name} faild to withdraw ${amount}."
                      f"Insufficient funds: balance remains ${self.balance}.")
                

def perform_transactions(account: BankAccount):
    for _ in range(10):
        action = random.choice(['deposit','withdraw'])
        amount = random.randint(1,100)
        if action == 'deposit':
            account.deposit(amount)
        else:
            account.withdraw(amount)
        time.sleep(random.uniform(0.01,0.1))

myAcc = BankAccount(1000)
threads = []

for i in range(5):
    t = threading.Thread(target=perform_transactions, args = (myAcc,), name = f"Customer {i+1}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\nFinal account balance: ${myAcc.balance}"),
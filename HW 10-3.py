import threading

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        return self.balance + amount
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance - amount

account = BankAccount(1000)

lock = threading.Lock

print(account.deposit(350))
def deposit_task(amount):
    with lock:
        for _ in range(5):
            sum = account.deposit(amount)
            print(f'Deposited {amount}, new balance is {sum}')



def withdraw_task(amount):
    with lock:
        for _ in range(5):
            sum = account.withdraw(amount)
            print(f'Withdrew {amount}, new balance is {sum}')

deposit_thread = threading.Thread(target=deposit_task, args=(100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()



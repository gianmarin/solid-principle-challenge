# Here your solution
import datetime

class BankAccount:
    def __init__(self, account_number, balance = 0.0):
        self.account_number = account_number
        self.balance = balance
        
class DepositTransactionLogService:
    def __init__(self, bankAccount: BankAccount):
        self.bankAccount = bankAccount

    def execute(self, amount):
        with open("transactions.log", "a") as log_file:
            log_file.write( 
                f"{datetime.datetime.now()}: Deposited {amount} into {self.bankAccount.account_number}\n"
            )      

class WithDrawTransactionLogService:
    def __init__(self, bankAccount: BankAccount):
        self.bankAccount = bankAccount

    def execute(self, amount):
        with open("transactions.log", "a") as log_file:
            log_file.write(
                f"{datetime.datetime.now()}: Withdrew {amount} into {self.bankAccount.account_number}\n"
            )            

class GeneratedStatementLogService:
    def __init__(self, bankAccount: BankAccount):
        self.bankAccount = bankAccount

    def execute(self):
        with open("statements.log", "a") as stmt_file:
            stmt_file.write(
                f"{datetime.datetime.now()}: Generated statement for {self.bankAccount.account_number}\n"
            )  

class EmailNotificationService:
    def execute(self, description):
        print(description)

class DepositService:
    def __init__(self, bankAccount: BankAccount, transactionLog: DepositTransactionLogService):
        self.bankAccount = bankAccount
        self.transactionLog = transactionLog

    def execute(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.bankAccount.balance += amount
        self.transactionLog.execute(amount)
        self.emailNotification.execute(f"Sending email notification: {amount} deposited into account {self.bankAccount.account_number}.")
        return

class WithDrawService:
    def __init__(self, bankAccount: BankAccount, transactionLog: WithDrawTransactionLogService):
        self.bankAccount = bankAccount
        self.transactionLog = transactionLog

    def execute(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.bankAccount.balance:
            raise ValueError("Insufficient funds.")

        self.bankAccount.balance -= amount
        self.transactionLog.execute(amount)
        self.emailNotification.execute(f"Sending email notification: {amount} withdrawn from account {self.bankAccount.account_number}.")

class GenerateStatementService:
    def __init__(self, bankAccount: BankAccount, statementLog: GeneratedStatementLogService):
        self.bankAccount = bankAccount
        self.statementLog = statementLog

    def execute(self):
        statement = f"Statement for Account: {self.bankAccount.account_number}\nBalance: {self.bankAccount.balance}\n"
        self.statementLog.execute()
        print(statement)
        self.emailNotification.execute(f"Sending email with statement for account {self.bankAccount.account_number}...")
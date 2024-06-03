class  Account:
       def _init_(self,number,pin):
           self.number = number
           self._ _pin = pin
           self._ _balance = 0

        def show_balance(self,pin):
            if pin ==self._ _pin:
                return self._ _ _balance
            else:
                return "wrong pin"       
def account_statement(self, pin):
        if pin == self.__pin:
            transactions = ["Deposit $800", "Withdrawal $100"]
            return "\n".join(transactions)
        else:
            return "Wrong PIN"
    def set_overdraft_limit(self, limit, pin):
        if pin == self.__pin:
            self.__overdraft_limit = limit
            return f"Overdraft limit set to ${limit}."
        else:
            return "Wrong PIN"
    def calculate_interest(self, rate, pin):
        if pin == self.__pin:
            interest_amount = self.__balance * rate / 100
            self.__balance += interest_amount
            return f"Interest calculated. New balance: ${self.__balance}"
        else:
            return "Wrong PIN"
    def freeze_account(self, pin):
        if pin == self.__pin:
            self.__is_frozen = True
            return "Account frozen."
        else:
            return "Wrong PIN"
    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.__is_frozen = False
            return "Account unfrozen."
        else:
            return "Wrong PIN"
    def transaction_history(self, pin):
        if pin == self.__pin:
            return "\n".join(self.__transaction_history)
        else:
            return "Wrong PIN"
    def set_minimum_balance(self, min_balance, pin):
        if pin == self.__pin:
            self.__minimum_balance = min_balance
            return f"Minimum balance requirement set to ${min_balance}."
        else:
            return "Wrong PIN"
    def transfer_funds(self, amount, recipient_number, pin):
        if pin == self.__pin:
            if self.__balance >= amount:
                self.__balance -= amount
                self.__transaction_history.append(f"Withdrawal: ${amount} to {recipient_number}")
                return f"Funds transferred successfully. New balance: ${self.__balance}"
            else:
                return "Insufficient funds."
        else:
            return "Wrong PIN"
    def close_account(self, pin):
        if pin == self.__pin:
            return "Account closed."
        else:
            return "Wrong PIN"
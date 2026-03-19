# mutable value in the parent frame can maintain state for a local in function
def make_withdraw_account(initial):
    balance = [initial]
    def withdraw(amount):
        if balance[0] - amount < 0:
            return 'Insufficient funds'
        balance[0] -= amount
        return balance[0]
    
    return withdraw
    
withdraw = make_withdraw_account(100)
print(f'withdrew $25, balance = {withdraw(25)}')
print(f'withdrew $25, balance = {withdraw(25)}')
print(f'withdrew $60, balance = {withdraw(60)}')
#IF YOU WANT TO KEEP IT AROUND MAKE IT A LIST
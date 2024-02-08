from bankAcc import *

# Test Cases:

# Test Case 1: Nikhil's account
Nikhil = BankAccount(1000, "Nikhil")
Nikhil.get_balance()                                                      # Output: The current balance of Nikhil is $1000.00
Nikhil.deposit(1000)                                                      # Output: Successfully deposited ✅.!!!!!!
                                                                          #         You have successfully deposited $1000 on 'Nikhil' Account🏦. Your new balance is $2000.00.
Nikhil.withdraw(30000)                                                    # Output: ❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌ Unsufficient Balance. you only got 2000 in your bank account

# Test Case 2: Transferring from Nidhin to Nikhil
Nidhin = BankAccount(10000, "Nidhin")
Nidhin.transfer(700, Nikhil)
# Output:
# Transfer of 💸$700.00 from Nidhin ➡️ Nikhil completed successfully.
# Nikhil new balance is $2700.00.

# Test Case 3: Interest Reward Account (Neethu)
Neethu = InterestRewardAcc(1000, "Neethu")
Neethu.deposit(100)
# Output:
# The current balance of Neethu is $1050.00
# Rupees 💸 '100' with interest of 5.0 has been credited in 🤵‍♂️Neethu's Account

# Test Case 4: Savings Account (Leela)
Leela = SavingsAcc(5000, "Leela")
Leela.get_balance()                                                       # Output: The current balance of Leela is $5000.00
Leela.deposit(2005)                                                       # Output: Successfully deposited ✅.!!!!!!
                                                                          #         You have successfully deposited $2005 on 'Leela' Account🏦. Your new balance is $7005.00.
Leela.withdraw(1000)                                                        # Output: 
                                                                            # initializing-----------------------withdrawel -------------------
                                                                            # Unsufficient Balance. you only got 7005 in your bank account




Leela = SavingsAcc(5000, "Leela")
Leela.get_balance
Leela.deposit(2005)

Leela.withdraw(1000)
class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES Sent to {recipient} successful.")
        else:
            print("Insufficient Balance")


class Personal_Mpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_number):
        super().__init__(account_balance, phone_number)
        self.id_number = id_number

    def buy_airtime(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES airtime bought successfully.")
        else:
            print("Insufficient Balance")


class Business_Mpesa(Mpesa):
    def __init__(self, account_balance, phone_number, Business_name):
        super().__init__(account_balance, phone_number)
        self.Business_name = Business_name

    def receive_money(self, amount):
        self.account_balance += amount
        print(f"{amount} KES received successfully")


personal = Personal_Mpesa(2000, 721655711, 20755835)
personal.send_money(450, 729917590)
personal.buy_airtime(25)

business = Business_Mpesa(25000, 721655711,"Benaroma Industries")
business.receive_money(25000)



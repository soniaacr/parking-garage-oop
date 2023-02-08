class ParkingGarage():
    def __init__(self):
        self.tickets = 75
        self.parking_spaces = 75
        self.current_ticket = {}

    def takeTicket(self):
        self.tickets -= 1
        self.parking_spaces -= 1

    def payForParking(self):
        payment = input("Amount due is $15: ")
        if payment != '':
            print("Your ticket has been paid, please leave garage within 15 minutes, Thank you.")
            self.parking_spaces += 1
            self.current_ticket['paid'] = True

    def leaveGarage(self):
        payment = input('Please make payment: ')
        if payment != '':
                print('Thank you, have a nice day!')
        self.tickets += 1
        self.parking_spaces += 1 

def run():
    while True:
        response = input('Please enter: Take ticket/ Pay for parking/ Leave garage: ')
        if response.lower() == 'Take your ticket':
            garage.takeTicket()
        elif response.lower() == 'Pay for parking':
            garage.payForParking()
        elif response.lower() == 'Leave garage':
            garage.leaveGarage()
            break


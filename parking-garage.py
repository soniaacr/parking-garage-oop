class ParkingGarage():
    def __init__(self):
        self.tickets = 100
        self.parking_spaces = 100
        self.current_ticket = {}

    def takeTicket(self):
        self.tickets -= 1
        self.parking_spaces -= 1

    def payForParking(self):
        payment = input("Please make payment amount of $10: ")
        if payment != '':
            print("Your ticket has been paid, please leave garage within 15 minutes, Thank you.")
            self.parking_spaces += 1
            self.current_ticket['paid'] = True

    def leaveGarage(self):
        payment = input('Please make payment: ')
        if payment != '':
                print('Thank you.')
        self.tickets += 1
        self.parking_spaces += 1 

garage = ParkingGarage()

def run():
    while True:
        response = input('Please enter: Take ticket/ Pay for parking/ Leave garage: ')
        if response.lower() == 'take ticket':
            garage.takeTicket()
        elif response.lower() == 'pay for parking':
            garage.payForParking()
        elif response.lower() == 'leave garage':
            garage.leaveGarage()
            break
run()


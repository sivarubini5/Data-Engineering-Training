def calculate_booking(ticket_price, tickets):
    return ticket_price * tickets

def calculate_discount(amount):
    if amount >= 10000:
        return amount * 0.10
    else:
        return amount * 0.05

def check_capacity(capacity, registered):

    if capacity < 0 or registered < 0:
        return "Invalid Data"

    elif registered == capacity:
        return "Full"

    elif registered < capacity:
        return "Seats Available"

    else:
        return "Invalid Data"
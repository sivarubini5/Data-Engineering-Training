import event_utils
booking = event_utils.calculate_booking(2500, 4)
print("Booking Amount:", booking)
discount = event_utils.calculate_discount(booking)
print("Discount:", discount)
capacity_status = event_utils.check_capacity(500, 450)
print("Capacity Status:", capacity_status)

from event_utils import calculate_booking
print(calculate_booking(3500, 2))

import event_utils as eu
print(eu.calculate_discount(12000))
print(eu.check_capacity(200, 200))
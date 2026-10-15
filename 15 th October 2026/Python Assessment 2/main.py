
import shipment_utils

print(shipment_utils.calculate_shipping_cost(12.5, 68))

print(shipment_utils.shipment_category(22))

print(shipment_utils.calculate_cost_per_kg(850, 12.5))

from shipment_utils import shipment_category

print(shipment_category(18.5))

import shipment_utils as su

print(su.calculate_shipping_cost(10, 75))
import retail_utils

total = retail_utils.calculate_order_total(65000, 2)
print("Total:", total)

discount = retail_utils.calculate_discount(total)
print("Discount:", discount)

stock_status = retail_utils.check_stock(12)
print("Stock Status:", stock_status)


from retail_utils import calculate_order_total

print(calculate_order_total(3000, 4))

import retail_utils as ru
print(ru.check_stock(12))
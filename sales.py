import random

def daily_sales(available_items, inventory_records, current_day):
    if current_day % 7 != 0:
        sold_units = random.randint(1, 200)
        restocked_units = 0
        available_items -= sold_units
        inventory_records.append((current_day, sold_units, restocked_units, available_items))

    return available_items

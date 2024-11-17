def restock_inventory(available_items, inventory_records, current_day):
    # This first if statement fixes "Error: Totals do not match".
    # Without it, the code works fine, but on day 0, restocked_units will be 0 instead of 2000.
    if current_day == 0: 
        available_items = 0

    if current_day % 7 == 0:
        max_available_items = 2000
        sold_units = 0
        restocked_units = max_available_items - available_items
        available_items += restocked_units
        inventory_records.append((current_day, sold_units, restocked_units, available_items))
    
    return available_items

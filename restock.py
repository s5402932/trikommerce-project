def restock_inventory(available_items, inventory_records, current_day):
    if current_day % 7 == 0:
        max_available_items = 2000
        sold_units = 0
        restocked_units = max_available_items - available_items
        available_items += restocked_units
        inventory_records.append((current_day, sold_units, restocked_units, available_items))
    
    return available_items

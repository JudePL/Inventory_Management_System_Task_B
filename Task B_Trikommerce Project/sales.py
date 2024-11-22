import random

def daily_sales(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 

    '''

    sold_units = random.randint(0, 200) # Generates random sales (0 to 200 units)

    if current_day % 7 == 0: # Skip restocking days (only handle sales on non-restocking days)
        available_items -= sold_units # Deduct sold units from available stock.
        inventory_records.append([current_day, sold_units, 0, available_items]) # Appends inventory for daily sales and remaining stock
    
    return available_items # Return updated available items

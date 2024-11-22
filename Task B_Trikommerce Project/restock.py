def restock_inventory(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
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


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''

    if current_day == 0: # Initialize inventory on day 0
        inventory_records.append([0, 0, 2000, 2000]) # Sets inventory on day 0 full of stock (2000 items)
    elif current_day % 7 == 0: # Restock's every 7th Day
        inventory_records.append([current_day, 0,(2000 - available_items), 2000]) # Updates restocking to 2000

    available_items = 2000 # Sets available_items to 2000

    return available_items # Returns the updated "available_items" after restocking


class RestaurantTable:
    restaurant_name = "Taste of Tashkent"
    max_seats = 4
    total_tables = 0
    
    def __init__(self, table_number, section):
        self.table_number = table_number
        self.section = section
        self.diners = []
        RestaurantTable.total_tables += 1
        
    def seat_diner(self, name):
        if len(self.diners) < RestaurantTable.max_seats:
            self.diners.append(name)
            print(f"Seated {name} at Table {self.table_number}")
        else:
            print(f"Table is full")
                
    def unseat_diner(self, name):
       if name in self.diners:
           self.diners.remove(name)       
           print(f"Removed {name} from Table {self.table_number}")
       else:
           print(f"Diner not found")
               
    def display_table(self):
        print(f"Table {self.table_number} in {self.section} at {RestaurantTable.restaurant_name}")         
    
    
first = RestaurantTable(5, "Patio")

first.display_table()
first.seat_diner("Nodira")
first.seat_diner("Kamola")
first.seat_diner("Farhod")
first.seat_diner("Shavkat")
first.seat_diner("Dilshod")
first.unseat_diner("Kamola")
first.unseat_diner("Zafar")

print(f"Total tables: {RestaurantTable.total_tables}")
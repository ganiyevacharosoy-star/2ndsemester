class Warehouse:
    def __init__(self, name, total_capacity):
        self._name = name
        self.total_capacity = total_capacity
        self._stored_crates = 0
        
    @property
    def name(self):
        return self._name
        
    @property
    def total_capacity(self):
        return self._total_capacity
        
    @total_capacity.setter
    def total_capacity(self, value):
        if value < 1:
            raise ValueError(f"Total capacity must be at least 1")
        self._total_capacity = value
        
    @property
    def stored_crates(self):
        return self._stored_crates
        
    @stored_crates.setter
    def stored_crates(self, value):
        if value < 0:
            raise ValueError(f"Stored crates cannot be negative")
        if value > self.total_capacity:
            raise ValueError(f"Stored crates cannot exceed total capacity")
        self._stored_crates = value
        
    @property
    def free_space(self):
        return self.total_capacity - self.stored_crates
        
    @property
    def usage_rate(self):
        rate = (self.stored_crates / self.total_capacity) * 100
        return round(rate, 1)
   
    def store(self, crates):
        if crates < 0:
            raise ValueError(f"Number of crates must be positive")
        if crates > self.free_space:
            raise ValueError(f"Not enough free space")
        self.stored_crates += crates
        
    def ship(self, crates):
        if crates < 0:
            raise ValueError(f"Number of crates must be positive")
        if crates > self._stored_crates:
            raise ValueError(f"Cannot ship more than stored")
        self.stored_crates -= crates
                   
w = Warehouse("East", 500)
print(w.name, w.free_space, w.usage_rate)

w.store(350)
print(w.stored_crates, w.usage_rate)

w.ship(100)
print(w.free_space)

try:
    w.store(300)
except ValueError as e:
    print(e)

try:
    w.name = "X"
except AttributeError:
    print("Cannot change warehouse name")    
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[ACTION] {func.__name__} executed")
        result = func(*args, **kwargs)
        return result
    return wrapper
    
class Athlete:
    _total_athletes = 0
    def __init__(self, name, athlete_id):
        self.name = name
        self.athlete_id = athlete_id
        self._sessions = {}
        Athlete._total_athletes += 1
        
    @log_action    
    def add_session(self, exercise, intensity):
        exercise = exercise.upper()
        self._sessions[exercise] = intensity
        return f"{self.name} trained {exercise} at intensity {intensity}"
        
    def avg_intensity(self):
        if not self._sessions:
            return 0.0
        avg = sum(self._sessions.values()) / len(self._sessions)
        return float(round(avg,1))
        
    def hardest_session(self):
        if not self._sessions:
            return "No session"
            
        hardest_name, highest = None, 0
        for session, intensity in self._sessions.items():
            if highest < intensity:
                hardest_name, highest = session, intensity
        return hardest_name   
                
    @classmethod
    def from_roster(cls, data):
        name, id = data.split("-")
        return cls(name, id)
        
    @staticmethod
    def is_valid_id(athlete_id):
        return len(athlete_id) == 7 and athlete_id.isdigit()
        
    @classmethod
    def total_athletes(cls):
        return cls._total_athletes
        
        
a1 = Athlete("Bobur", "5501001")
a1.add_session("sprints", 95)
a1.add_session("weights", 80)
a1.add_session("swimming", 70)

a2 = Athlete.from_roster("Nilufar-5501002")
a2.add_session("Cycling", 82)
a2.add_session("sprints", 91)       
print(f"{a1.name}: Avg = {a1.avg_intensity()}, Hardest = {a1.hardest_session()}")
print(f"{a2.name}: Avg = {a2.avg_intensity()}, Hardest = {a2.hardest_session()}")

print(f"Valid ID '5501001': {Athlete.is_valid_id('5501001')}")
print(f"Valid ID '55X': {Athlete.is_valid_id('55X')}")
print(f"Total athletes: {Athlete.total_athletes()}")            
            
                       
       
                
        
                 
        
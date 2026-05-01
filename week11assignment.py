from dataclasses import dataclass, field

class WorkoutError(Exception):
    pass
@dataclass   
class Exercise:
    code: str
    name: str
    duration: int
    calories: int
    _label: str = field(init=False)
    
    def __post_init__(self):
        self._label = "PENDING"
        if self.duration <= 0:
            raise WorkoutError(f"Invalid duration for {self.code}")
    @property        
    def intensity(self) -> float:
        if self.duration == 0:
            return 0.0
        return round(self.calories / self.duration, 1)
        
    def __str__(self):
        return f"[{self.code}] {self.name} {self.duration}min {self.calories}cal ({self._label})"
        
    def __lt__(self, other) -> bool:
    #    if not isinstance(other, Exercise):
        #    return NotImplemented
        return self.calories < other.calories
        
class CalorieChecker:
    def __init__(self, exercises, max_cal):
        self.exercises = exercises
        self.max_cal = max_cal
        self.calling = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.calling >= len(self.exercises):
            raise StopIteration
            
        exer = self.exercises[self.calling]
        if exer.calories <= self.max_cal:
            exer._label = "APPROVED"
        else:
            exer._label  = "EXCESSIVE"
            
        self.calling += 1
        return exer
        
def workout_report(checker):
     approved = 0
     excessive = 0
     
     for exer in checker:
         if exer._label == "APPROVED":
             approved += 1
             
         else:
             excessive += 1
             
         yield str(exer)
     yield f"Summary: {approved} approved, {excessive} excessive"
     
class GymSession:
    def __init__(self, name):
        self.name = name
        self._exercises = []
    def __enter__(self):
        print(f"=== Start: {self.name} ===")
        return self
         
    def add(self, exercise):
        return self._exercises.append(exercise)
         
    def evaluate(self, max_cal):
        checker = CalorieChecker(self._exercises, max_cal)
        return workout_report(checker)
         
    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_val, WorkoutError):
            print(f"!!! Error: {exc_val}")
            print(f"=== End: {self.name} ({len(self._exercises)} exercises) ===")
            return True
             
        print(f"=== End: {self.name} ({len(self._exercises)} exercises) ===")
        return False
         


with GymSession("Cardio Plan") as gym:
    gym.add(Exercise("E01", "Running", 30, 250))
    gym.add(Exercise("E02", "Cycling", 45, 400))
    gym.add(Exercise("E03", "Swimming", 60, 650))

    for line in gym.evaluate(500):
        print(line)

    print(gym._exercises[0] < gym._exercises[1])

print()

with GymSession("Strength Plan") as gym:
    gym.add(Exercise("E04", "Deadlift", -10, 300))

        
        
       

from dataclasses import dataclass, field
@dataclass
class Student:
    name: str
    student_id: str
    assignments_done = int = 0
    scores: list[int] = field(default_factory=list)
    
    def submit(self, score: int):
        self.assignments_done += 1
        self.scores.append(score)
        
    def avg_score(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)
@dataclass        
class Course:
    course_name: str
    professor: str
    capacity: int
    students: list[Student] = field(default_factory=list)
    enrolled: int = field(init=False)
    
    def __post_init__(self):
        self.enrolled = 0
        
    def enroll(self, student: Student) -> bool:
        if self.enrolled >= self.capacity:
            return False
        self.students.append(student)
        self.enrolled += 1
        return True
        
        
    def top_student(self) -> str:
        if not self.students:
            return "No data"
            
        top_student = None
        best_avg = 0
        for s in self.students:
            avg = s.avg_score()
            if avg > best_avg:
                best_avg = avg
                top_student = s
                
        if top_student is None or best_avg == 0:
            return "No data"
            
        return top_student.name
        
        
    def course_stats(self) -> str:
        if not self.students:
            return f"{self.course_name} ({self.professor})\n Enrolled: 0/{self.capacity}\n No student enrolled."
            
        result = f"{self.course_name} ({self.professor}):\n"
        for s in self.students:
            avg = s.avg_score()
            result += f"  {s.name} - {s.assignments_done} assignmnets, avg {avg:.1f} pts\n"
            
        result += f"Enrolled: {self.enrolled}/{self.capacity}"
        return result
  
  
s1 = Student("Liam", "S101")
s2 = Student("Nora", "S102")
s3 = Student("Omar", "S103")

s1.submit(72)
s1.submit(88)
s1.submit(91)
s2.submit(95)
s2.submit(89)
s3.submit(60)

c = Course("Data Structures", "Prof. Kim", 3)
print(c.enroll(s1))
print(c.enroll(s2))
print(c.enroll(s3))
print(c.enroll(Student("Priya", "S104")))
print(c.enrolled)
print(c.top_student())
print(c.course_stats())
      
    
        
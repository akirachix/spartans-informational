class Student:
    school = "AkiraChix"  # Class attribute

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.year = 2025 - age  
        self.marks=[]

    def create_initials(self):
        
        return self.first_name[0].upper() + self.last_name[0].upper()

    
    def record_marks(self, points):
        self.marks.append(points)
        
        self.total= sum(self.marks)
        if  self.marks:
            return f"marks recorded. Total marks is {self.total}"

  




    

        
def hello():
    print("Hello AkiraChix!")

# hello()  

def say_hello(name):
    print(f"hello {name}")


def greet(name,age):
    year=2025-age
    print(f"hello {name},born in {year}")

def greeting (names):
    for name in names:
        print(f"hello {name}")

def year_of_birth(name, age):
    year= 2025 - age
    print(f"Hello {name} born in {year}")

def my_country(name="Uganda"):
    print(f"i love my country {name}")

def  welcome_student(** kwargs):
    print(kwargs)

def create_sentence(**words):
    sentence=" "
    for word in words.values():
        sentence +=word
        sentence +=" "
    return sentence

def exam_results(*args,**kwargs):
    name=kwargs.get("name")
    course=kwargs.get("course")
    if not args:
        return None
    total_score = sum(args)
    average_score = total_score/len(args)
    return f"hello {name}, your average exam score for{course} is {average_score}"



      
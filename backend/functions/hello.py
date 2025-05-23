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
        return f"Hello{name},we dont have your results for {course}"
    total_score = sum(args)
    average_score = total_score/len(args)
    return f"hello {name}, your average exam score for{course} is {average_score}"



def reversed_string(**kwargs):
    s="";
    
    return s

def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

sentence = "This is a sentence with some long words"
longest = find_longest_word(sentence)
print(len(longest))

# to check if a number 

arr = [1,2,3,4,5,6];
num = 5;
if num in arr:
    print("num exists")
else:
    print("num doesn't exist")   
    
      

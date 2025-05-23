# def add(a,b):
#     ans = a+b
#     return ans

# def subtract(a,b):
#     ans= a-b
#     return ans   

# def multiply(a,b):
#     ans = a*b
#     return ans   

# def divide(a,b):
#     ans = a/b
#     return ans

# def modulus(h):
#     remainder = h%2
#     return remainder

# def exponent(a,b):
#     z = a**b
#     return z
def fun(n):
    x=2
    count = 0
    while count < n:
        for d in range (2, int(x** 0.5) + 1):
            if x % d == 0:
                break
        else:
            print(x)
            count +=1
        x +=1
n = 10
fun(n)  

# def square_numbers(*args):
  
#     squared_numbers=[num **2 for square_numbers in args]
#     return squared_numbers
# numbers = [1,2,3,4,5]
# squares = square_numbers(numbers)
# print(squares)






 
# def sum(* numbers):

#     total=0
#     for num in numbers:
#         total +=num
#     return total       

# def summation(** numbers):
    
# def square(a):
#     d = a*a
#     return d

# def cube(a):
#     cubenum= a*a*a 
#     return cubenum   
  
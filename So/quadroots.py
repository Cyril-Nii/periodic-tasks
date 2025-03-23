
def nature_of_roots(a:float,b:float,c:float):
    
    discriminant = pow(b,2) - 4*a*c

    if(discriminant == 0):
        print("The equation has real and equal roots")
    elif(discriminant < 0):
        print("The equation has complex roots")
    elif(discriminant > 0):
        print("The equation has real and distinct roots")
    
    
print(f"""For a quadratic equation a(x^2) + bx + c,
Enter the coefficients a, b and c to recieve the nature of roots.""")

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : \n"))

nature_of_roots(a,b,c)
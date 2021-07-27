#quadratic equation is of form ax**2+bx+c=0
import cmath
a=float(input('Enter a: '))
b=float(input('Enter b: '))
c=float(input('Enter c: '))

d=(b**2)-(4*a*c) #discremenant

sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2)) 
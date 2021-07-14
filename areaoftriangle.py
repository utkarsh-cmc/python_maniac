side1=float(input('Enter first side: '))
side2=float(input('Enter second side: '))
side3=float(input('Enter third side: '))

s=(side1+side2+side3)/2 #semi-perimeter

area_triangle=(s*(s-side1)*(s-side2)*(s-side3))**0.5 #area of triangle by heron's formula

print('The area of the triangle is %0.2f'%area_triangle)
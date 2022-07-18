a=int(input('enter the wieght of first man  :'))
b=int(input('enter the wieght of second man :'))
c=int(input('enter the wieght of third  man :'))
d=int(input('enter the wieght of fourth man :'))
if a==b:
    print("first and second man added in the car 1")
    if c==d:
        print('third and fourth man added in the car 2')
    else:
        print('third and fourth man dont have any pair to be in car 2')

elif a==c:
    print("first and third man added in the car 1")
    if d==b:
        print("second and fourth man added in the car 2")
    else:
        print('second and fourth man dont have any pair to be in car 2')
elif a==d:
    print("first and fourth man added in the car 1")
    if c==b:
        print("second and third man added in the car 2")
    else:
        print('second and third man dont have any pair to be in car 2')
elif b==c:
    print("second and third man added in the car 1")
    if a==d:
        print("first and fourth man added in the car 2")
    else:
        print('first and fourth man dont have any pair to be in car 2')
elif b==d:
    print("second and fourth man added in the car 1")
    if a==c:
        print("first and third man added in the car 2")
    else:
        print('first and third man dont have any pair to be in car 2')
elif c==d:
    print("third and fourth man added in the car 1")
    if a==b:
        print("first and second man added in the car 2")
    else:
        print('first and second man dont have any pair to be in car 2')
else:
    print('no pair for both car 1 and 2')



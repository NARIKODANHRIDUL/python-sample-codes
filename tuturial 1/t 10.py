s=int(input('Enter your salary :'))
if s<250000:
    t=0
elif (s>=250000 and s<500000):
    t=s*0.1
elif (s>=500000 and s<1000000):
    t=s*0.2
elif (s>=100000 and s<2000000):
    t=s*0.25
else:
    t=s*0.3
print('You have to pay Rs.',t,'as Tax',)

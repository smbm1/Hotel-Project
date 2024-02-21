swimming=int(input('enter your swimming time'))
cycling=int(input('enter your cycling time'))
running=int(input('enter your running time'))

total= swimming + cycling + running
print(total)

if total <=100:
    print('you get the provincial colours award')
elif total >=101 and total <=105:
    print('you get the provincial half colours award')
elif total >=106 and total <=110:
    print('you get the provincial scroll award')
else:
    print('you get no award! try harder')
    
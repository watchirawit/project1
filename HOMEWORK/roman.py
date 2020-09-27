
roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
Number = int(input('Value: '))
N1 = Number // 1000
ronum1 = N1*roman[12]
Number = Number % 1000
N2 = Number // 900
ronum2 = N2*roman[11]
Number = Number % 900
N3 = Number // 500
ronum3 = N3*roman[10]
Number = Number % 500
N4 = Number // 400
ronum4 = N4*roman[9]
Number = Number % 400
N5 = Number // 100
ronum5 = N5*roman[8]
Number = Number % 100
N6 = Number // 90
ronum6 = N6*roman[7]
Number = Number % 90
N7 = Number // 50
ronum7 = N7*roman[6]
Number = Number % 50 
N8 = Number // 40
ronum8 = N8*roman[5]
Number = Number % 40
N9 = Number // 10
ronum9 = N9*roman[4]
Number = Number % 10
N10 = Number // 9
ronum10 = N10*roman[3]
Number = Number % 9
N11 = Number // 5
ronum11 = N11*roman[2]
Number = Number % 5
N12 = Number // 4
ronum12 = N12*roman[1]
Number = Number % 4
N13 = Number // 1
ronum13 = N13*roman[0]
Number = Number % 1
RomanNum = ronum1+ronum2+ronum3+ronum4+ronum5+ronum6+ronum7+ronum8+ronum9+ronum10+ronum11+ronum12+ronum13
print('RomanNo:',RomanNum)
   






A=float(input('enter A'))
B=float(input('enter B'))
C=float(input('enter C'))
if A + B > C and A + C > B and B + C > A:
    print('available')
else:
        print('unavailable')   

weight=float(input('enter weight'))
height=float(input('enter height'))
bmi=weight/(height*height)
if (bmi<18.5):
          print('underweight')
if              (18.5<=bmi<=24.9):
          print('normal')    
if      (25<=bmi<=29.9):
          print('overweight')
if (30<=bmi<=34.9):
          print('obese') 
if (bmi>=35):
          print('extremely obese')
                 
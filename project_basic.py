import random
l=["rock","scissor","paper"]
while True:
    ccount=0
    uccount=0
    uc=int(input('''
       Game Start....
       1: yes
       2:No|Exit                 
                 '''))
    if uc==1:
              for a in range(1,6):
                   userinput=int(input('''

1 Rock
2 scissor
3 paper                                                            
'''))
    if userinput ==1:
          ucchoice="rock"
    elif userinput==2:
          ucchoice="scissor"
    elif userinput==3:
          ucchoice="paper"
Cchoice=random.choice(l)
if Cchoice==ucchoice:
      print("computer value:",Cchoice)
      print("user value:",ucchoice)
      print("game over")
      uccount+=1
      ccount+=1
elif (ucchoice=="rock"and Cchoice=="scissor") or (
      ucchoice=="paper"and Cchoice=="rock") or(ucchoice=="scissor" and Cchoice=="paper"):
      print("computer value:",Cchoice)
      print("user value:",ucchoice)
      print("you win")
      uccount+=1
else:
       print("computer value:",Cchoice)
       print("user value:",ucchoice)
       print("computer win")
       ccount+=1

import os
def ijad():
    while(True):
        a = input('enter name of folder :')
        l = os.path.exists(a)
        if l == True:
            print('yes')
        else :
            print('no')
  
  
ijad()
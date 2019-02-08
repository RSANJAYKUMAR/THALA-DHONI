while True:
        try:
              t7=int(input())
              break
        except:
              print('invalid')
              break
if t7%400==0 or t7%4==0 and t7%100!=0:
       print('yes')
else:
       print('no')

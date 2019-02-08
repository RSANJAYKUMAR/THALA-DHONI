while True:
        try:
              t3=int(input())
              break
        except:
              print('invalid')
              break
if t3%400==0 or t3%4==0 and t3%100!=0:
       print('yes')
else:
       print('no')

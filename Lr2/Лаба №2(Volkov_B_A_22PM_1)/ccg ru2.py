s = input()
glasn = 'ауоыэяюёие'
flag = False
for i in range(len(glasn)):
    if s[-1] == glasn[i]:
        flag = True
        break
if flag == True:
    print('Слово с гласной на конце')
else:
    print('Слово с согласной на конце')


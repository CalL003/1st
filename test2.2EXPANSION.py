def computepay(hours, Rate) :
    print('in computepay', hours, Rate)

    if fh > 40 :
        print('overtime')
        regpay = fh * fr
        ovr = (fh - 40) * (fr + 0.5)
        finishedpay = regpay + ovr
    else :
        finishedpay = fr * fh
    print('returning', finishedpay)
    return finishedpay


hours = input('enter hours: ')
try :
    fh = float(hours)
except :
    print('please enter numeric values only! goodbye')
    quit()
Rate = input('enter Rate: ')

try :
    fr = float(Rate)
except :
    print('error please enter numeric values only!')
    quit()

finishedpay = computepay(fr,fh)  

print('pay', finishedpay)  
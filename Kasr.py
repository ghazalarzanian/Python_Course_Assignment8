def Mul(x,y):
    result={}
    result['s']=x['s']*y['s']
    result['m']=x['m']*y['m']
    return result
def Sum(x,y):
    result={}
    result['s']=x['s']*y['m']+x['m']*y['s']
    result['m']=x['m']*y['m']
    return result
def Minus(x,y):
    result={}
    result['s']=x['s']*y['m']-x['m']*y['s']
    result['m']=x['m']*y['m']
    return result
def Division(x,y):
    result={}
    Temp=y['s']
    y['s']=y['m']
    y['m']=Temp
    result=Mul(x,y)
    return result
def Show(x):
    print(x['s'],'/',x['m'])
a={'s':2,'m':3}
b ={'s':5,'m':4}
c=Mul(a,b)
d=Sum(a,b)
print('Minus:',end='')
Show(Minus(a,b))
print('Mul:',end='')
Show(c)
print('Sum:',end='')
Show(d)
print('Division:',end='')
Show(Division(a,b))
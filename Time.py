def Sum(x,y):
    result={'h':0,'m':0,'s':0}
    result['s']=x['s']+y['s']
    if result['s']>59:
        result['m']=int(result['s']/60)
        result['s']=result['s']%60
    result['m']+=x['m']
    result['m']+=y['m']
    if result['m']>59:
        result['h']=int(result['m']/60)
        result['m']=result['m']%60
    result['h']+=x['h']
    result['h']+=y['h']
    return result
def Minus(x,y):
    result={}
    if x['s']>=y['s']:
        result['s']=x['s']-y['s']
    else:
        x['s']+=60
        x['m']-=1
        result['s']=x['s']-y['s']
    if x['m']>=y['m']:
        result['m']=x['m']-y['m']
    else:
        x['m']+=60
        x['h']-=1
        result['m']=x['m']-y['m']
    result['h']=int(x['h']-y['h'])
    return result
def SecondToClock(x):
    result={}
    result['h']=int(x/3600)
    x=x-result['h']*3600
    result['m']=int(x/60)
    x=x-result['m']*60
    result['s']=int(x)
    return result
def ClockToSecond(x):
    result=int()
    result+=x['h']*3600
    result+=x['m']*60
    result+=x['s']
    return result
def Show(x):
    print(x['h'],':',x['m'],":",x['s'])
t1 ={'h':2,'m':50,'s':45}
t2 ={'h':3,'m':17,'s':40}
a=Sum(t1,t2)
b=Minus(t2,t1)
Show(a)
Show(b)
Show(SecondToClock(3669))
print(ClockToSecond(t1))
def Sum(x,y):
    result={}
    result['r']=x['r']+y['r']
    result['i']=x['i']+y['i']
    return result
def Minus(x,y):
    result={}
    result['r']=x['r']-y['r']
    result['i']=x['i']-y['i']
    return result
def Mul(x,y):
    result={}
    result['r']=x['r']*y['r']-x['i']*y['i']
    result['i']=x['i']*y['r']+x['r']*y['i']
    return result
def Show(x):
    print(x['r'],',',x['i'],'i')
Complex1={'r':4,'i':2}
Complex2={'r':1,'i':3}
Show(Complex1)
Show(Complex2)
print("Sum:",end='')
Show(Sum(Complex1,Complex2))
print("Mul:",end='')
Show(Mul(Complex1,Complex2))
print("Minus:",end='')
Show(Minus(Complex1,Complex2))
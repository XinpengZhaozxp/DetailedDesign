
def reNum(u, row=1.002, mu=1.89e-5 ,L=0.51184):
    return (row*u*L)/mu


def VelocityFromRe(Re, l, row=1.002, mu=1.89e-5):
    return (Re*mu)/(row*l)

def vConv(u,s1,s2):
    if s1=='ft':
        if s2 == 'm':
            return u*0.3048
        if s2 == 'kt':
            return u*0.592484
    elif s1 == 'm':
        if s2 == 'ft':
            return u*3.28084
        if s2 == 'kt':
            return u*1.943848
    else:
        if s2 == 'm':
            return u*0.51444
        if s2 == 'ft':
            return u*1.68781

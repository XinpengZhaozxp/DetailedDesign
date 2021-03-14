vlcal = 83.33
vlogis = 58.33
vtrans = 15
Re1 = 3e6  # local mission: 83.33m/s
Re2 = 2.1e6 # logistic mission 58.33m/s
Re3 = 407034 # potential transition speed 15m/s

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









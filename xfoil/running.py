import subprocess as sp
import os
import shutil
import sys
import string
import time


def running(airfoil, path, Re, a1=-17, a2=17, step=0.5):
    exepath = "D:\\Xinpeng Zhao\\Desktop\\XFOIL6.99\\XFOIL6.99\\" + "xfoil.exe"

    def cmd(process,cmd):
        process.stdin.write(str.encode(cmd + '\n'))
    try:
        os.remove(airfoil+"-Re{0}".format(Re)+'.txt')
    except:
        pass

    proc = sp.Popen(exepath , stdin=sp.PIPE, stderr=sp.PIPE, stdout=sp.PIPE,
                    cwd=r'C:\Users\Xinpeng Zhao\PycharmProjects\DetailedDesign\AirFoilCache')
    #proc.stderr.close()
    cmd(proc, 'load '+airfoil+'.dat')

    cmd(proc, 'OPER')

    cmd(proc, 'visc '+str(Re))
    cmd(proc, 'iter 400')
    cmd(proc, 'PACC')
    cmd(proc, airfoil+"-Re{0}".format(Re)+'.txt')
    cmd(proc, '')
    cmd(proc, 'aseq {0} {1} {2}'.format(a1, a2, step))
    # print(str(proc.communicate()[0])) for debug purpose
    cmd(proc, ' ')
    cmd(proc, 'quit')
    proc.stdout.close()
    proc.stdin.close()
    proc.wait()

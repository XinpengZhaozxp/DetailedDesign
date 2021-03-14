from pyxfoil.running import running
from pyxfoil.post_process import post_process
import os.path as path


def xfoil_analysis(airfoil, Re, cpath=None, xpath=None):

    if cpath is None:
        cachePath ='C:\\Users\\Xinpeng Zhao\\PycharmProjects\\DetailedDesign\\AirFoilCache'
    else:
        cachePath = cpath

    if xpath is None:
        xfpath = "D:\\Xinpeng Zhao\\Desktop\\XFOIL6.99\\XFOIL6.99\\" + "xfoil.exe"
    else:
        xfpath = xpath

    if path.exists(cachePath+'\\'+airfoil+"-Re{0}".format(Re)+'.txt'):
        print("The same analysis has previously done, .npy path returned\n")
        saved = cachePath+'\\'+airfoil+"-Re{0}".format(Re)+'.npy'
        return saved
    else:
        print("Running pyxfoil analysis=============================\n")
        running(xfpath, cachePath, airfoil, Re)
        print("Analysis completed, result file has been saved to cache\n")
        data_path=cachePath+'\\'+airfoil+"-Re{0}".format(Re)+'.txt'
        saved = post_process(data_path, cachePath, airfoil, Re)
        print("Processed .npy file saved, path returned for .npy file\n")
        return saved

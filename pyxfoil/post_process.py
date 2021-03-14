import numpy as np

def post_process(dpath,savepath,name,re):
    data = np.loadtxt(dpath, skiprows=12)
    # data = np.array(data)

    ind_0, dum = np.where(data[:, 0:1] == 0)
    alpha = np.array(data[:, 0])
    cl = np.array(data[:, 1])
    cd = np.array(data[:, 2])
    cdp = np.array(data[:, 3])
    cm = np.array(data[:, 4])
    xtr_t = np.array(data[:, 5])
    xtr_b = np.array(data[:, 6])

    C_l_alpha = (cl[ind_0 + 1] - cl[ind_0 - 1]) / np.deg2rad(alpha[ind_0 + 1] - alpha[ind_0 - 1])
    C_m_alpha = (cm[ind_0 + 1] - cm[ind_0 - 1]) / np.deg2rad(alpha[ind_0 + 1] - alpha[ind_0 - 1])
    X_ac_t = 0.25 - (C_m_alpha / C_l_alpha)

    result = np.array([(ind_0, alpha, cl, cd, cdp, cm, xtr_t, xtr_b, C_l_alpha, C_m_alpha, X_ac_t)],
                      dtype=[('ind_0', 'i8'), ('alpha', np.object_), ('cl', np.object_), ('cd', np.object_),
                             ('cdp', np.object_), ('cm', np.object_), ('xtr_t', np.object_), ('xtr_b', np.object_),
                             ('cl_alpha', '<f4'), ('cm_alpha', '<f4'), ('x_ac', '<f4')])
    sp = savepath+'\\'+name+"-Re{0}".format(re)+'.npy'
    np.save(sp, result)
    return sp

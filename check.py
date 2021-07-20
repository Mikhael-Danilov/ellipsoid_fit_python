import numpy as np
from ellipsoid_fit import ellipsoid_fit, data_regularize


if __name__=='__main__':

    data = np.loadtxt("mag_out_bck.txt", delimiter=",", skiprows=1)

    center, evecs, radii, v = ellipsoid_fit(data)

    d = data - center.T

    a, b, c = radii
    r = (a * b * c) ** (1. / 3.)
    D = np.array([[r/a, 0., 0.], [0., r/b, 0.], [0., 0., r/c]])
    #http://www.cs.brandeis.edu/~cs155/Lecture_07_6.pdf
    #affine transformation from ellipsoid to sphere (translation excluded)
    TR = evecs.dot(D).dot(evecs.T)

    t = [TR[0][0], TR[1][0], TR[1][1], TR[2][0], TR[2][1], TR[2][2]]

    print(TR[0][0],TR[0][1])
    print(t)

    dd = TR.dot(d.T).T

    for i in range(0,10):
        r = d[i]
        print([t[0] * r[0] + t[1] * r[1] + t[3] * r[2], t[1]*r[0] + t[2]*r[1] + t[4]*r[2], t[3] * r[0] + t[4]*r[1] + t[5]*r[2] ])
        print(dd[i])


    print(dd[0])

    print("transformation:\n",TR)

    np.savetxt('mag_out.txt', dd, delimiter=',', header='header')



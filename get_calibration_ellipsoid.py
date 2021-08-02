import sys

import numpy as np
from ellipsoid_fit import ellipsoid_fit as ellipsoid_fit, data_regularize


if __name__ == '__main__':

    data = np.loadtxt(sys.argv[1], delimiter=',', skiprows=1)
    # data2 = data_regularize(data)

    center, evecs, radii, v = ellipsoid_fit(data)

    a, b, c = radii
    r = (a * b * c) ** (1. / 3.)
    D = np.array([[r/a, 0., 0.], [0., r/b, 0.], [0., 0., r/c]])
    tr = evecs.dot(D).dot(evecs.T)
    
    # print('')
    # print('center: ', center)
    # print('radii: ', radii)
    # print('evecs: ', evecs)
    # print('transformation:')
    # print(tr)

    TR = tr
    t = [TR[0][0], TR[1][0], TR[1][1], TR[2][0], TR[2][1], TR[2][2]]

    print("Bias:")
    print(center)
    print("Rotate & Scale:")
    print(t)

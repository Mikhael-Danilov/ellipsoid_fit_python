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
    transformation = evecs.dot(D).dot(evecs.T)
    
    print('')
    print('center: ', center)
    print('radii: ', radii)
    print('evecs: ', evecs)
    print('transformation:')
    print(transformation)

    TR = transformation
    t = [TR[0][0], TR[1][0], TR[1][1], TR[2][0], TR[2][1], TR[2][2]]

    print("Hard & Soft correction:")
    print(f'gps2:upload_current_config({{address=6, magBias={{{center[1]},{center[2]},[0]={center[0]}}}, softIron={{{t[1]},{t[2]},{t[3]},{t[4]},{t[5]},[0]={t[0]}}}, gyroBias={{0,0,[0]=0}} }}) gps2:write_current_config()')
    print("Only Hard correction:")
    print(f'gps2:upload_current_config({{address=6, magBias={{{center[1]},{center[2]},[0]={center[0]}}}, softIron={{0,1,0,0,1,[0]=1}}, gyroBias={{0,0,[0]=0}} }}) gps2:write_current_config()')

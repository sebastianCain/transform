
from matrix import *
from math import sin, cos

def translate(m, a = 0, b = 0, c = 0):
    tm = identity_mtrx()
    print("*********")
    tm[0][3] += a
    tm[1][3] += b
    tm[2][3] += c
    print(str(tm[0][3]))
    print("*********")

    return mtrx_mult(m, tm)


def scale(m, a = 1, b = 1, c = 1):
    tm = identity_mtrx()
    tm[0][0] *= a
    tm[1][1] *= b
    tm[2][2] *= c

    return mtrx_mult(m, tm)


#all thetas are in radians
def rotateX(m, theta):
    tm = identity_mtrx()
    tm[0][0] = cos(theta)
    tm[0][1] = -(sin(theta))
    tm[1][0] = sin(theta)
    tm[1][1] = cos(theta)

    return mtrx_mult(m, tm)

def rotateY(m, theta):
    tm = identity_mtrx()
    tm[1][1] = cos(theta)
    tm[1][2] = -(sin(theta))
    tm[2][1] = sin(theta)
    tm[2][2] = cos(theta)

    return mtrx_mult(m, tm)

def rotateZ(m, theta):
    tm = identity_mtrx()
    tm[0][0] = cos(theta)
    tm[0][2] = sin(theta)
    tm[2][0] = -(sin(theta))
    tm[2][2] = cos(theta)

    return mtrx_mult(m, tm)

def cmbine_trnsfrms(transforms, m):
    for i in range(len(transforms)-1):
        mtrx_mult(transforms[i], transforms[i+1])
        #[i+1] now holds the values of the first two and will go on to multiply by the next matrix
        
    return matrix_mult(transforms[-1], m)

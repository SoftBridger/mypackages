"""
求两个离散随机变量的卷积的分布
"""
import numpy as np
from numpy import ndarray


def dis_convol(x:ndarray, fx:ndarray, y:ndarray, fy:ndarray):
    """
    求两个离散随机变量的卷积的分布
    :param fy: 随机变量各取值对应的频率
    :param y: 随机变量取值
    :param x: 随机变量取值
    :param fx: 随机变量各值对应的频率
    :return: z=x+y , fz
    """
    # z = x+y  求 z的概率分布 用卷积
    z = np.array([])
    for i in x:
        for j in y:
            zm = i + j
            if zm not in z:
                z = np.append(z, zm)
    fz = np.array([])
    for n in z:
        fzz = 0
        for i in x:
            if n - i in y:
                fzz = fzz + fx[np.where(x == i)] * fy[np.where(y == n - i)]
        fz = np.append(fz, fzz)

    return z, fz


if __name__ == '__main__':
    x1 = np.array([0, 1])
    fx1 = np.array([0.75, 0.25])
    y1 = np.array([0, 1, 2])
    fy1 = np.array([0.5, 0.25, 0.25])
    z1, fz1 = dis_convol(x1, fx1, y1, fy1)

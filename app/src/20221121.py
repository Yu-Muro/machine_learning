#coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("~/docs/20221121_exam.csv")

for i in range(1, 5):
    x = df["x{}".format(i)].values
    y = df["y{}".format(i)].values
    print(" ----- data{} ----- ".format(i))
    print("平均値\tx:{:.15f}\ty:{:.15f}".format(x.mean(), y.mean()))
    print("分散\tx:{:.15f}\ty:{:.15f}".format(x.var(), y.var()))
    print("共分散行列\n{}".format(np.cov(x, y, ddof = 0)))
    print("相関行列\n{}".format(np.corrcoef(x, y, ddof = 0)))
    plt.figure()
    plt.title("x{0}, y{0}".format(i))
    plt.xlim(0, 20)
    plt.ylim(0, 15)
    plt.scatter(x, y)
    plt.savefig("./img/20221121/data{}.png".format(i))

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import elice_utils as eu
elice_utils = eu.EliceUtils()

# 자료 읽어오는 함수
def read_data():
    X, Y = [], []
    with open("./data/input.txt") as f:
        for line in f:
            items = list(map(lambda x: float(x), line.split(",")))

            X.append(items[0:4])
            Y.append(items[4])

    X, Y = np.array(X), np.array(Y)
    return X, Y

def loss(X, Y, W):
    """
    Sum of Squared Error(SSE)를 기반으로 하여 손실함수를 구해봅시다.
    
    W는 A, B, C, D가 담겨있습니다.
    
    Y' = X.dot(W) 일 때, 손실값은 |Y - Y'|^2가 됩니다.
    
    손실값을 계산하여 돌려줍시다.
    
    아래 적당한 값을 리턴해주세요!
    """
    
    return np.sum((Y - X.dot(W)) ** 2)
    

def move(X, Y, W, epsilon=0.001):
    """    
    결과는 새로이 계산된 W를 돌려줍니다.
    
    W의 한 원소에 epsilon을 더하거나 뺀 계수들의 여러 셋을 준비하고,
    그 중 가장 작은 손실값의 W를 취하여 돌려줍시다.
    
    손실을 측정하는 함수는 위 loss함수를 이용합니다.
    """
    
    epsilons = np.vstack((np.eye(4) * epsilon, np.eye(4) * - epsilon))
    return W + epsilons[np.argmin([loss(X, Y, W + e) for e in epsilons])]

def main():
    X, Y = read_data()

    W = np.array([0, 0, 0, 0])
    W_history = []

    # 아래는 Regression하는 함수입니다.
    for i in range(2001):
        if i % 100 == 0:
            print("iter %d, loss = %f, P = %s" % (i, loss(X, Y, W), W))
            W_history.append(W)
        W = move(X, Y, W, epsilon=0.01)

    print("Rendering...")

    # 그래프 그리는 함수
    def update(i):
        W = W_history[i]
        line.set_ydata(X.dot(W))
        ax.set_xlabel("y = %.2lfx^3 + %.2lfx^2 + %.2lfx + %.2lf" % (W[0], W[1], W[2], W[3]))

        return line, ax

    Xs = X[:, 2]
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)
    ax.scatter(Xs, Y, s=3)
    line, = ax.plot(Xs, X.dot(W), c="r")
    anim = FuncAnimation(fig, update, frames=np.arange(0, len(W_history)), interval=200)
    anim.save("plot.gif", dpi=80, writer='imagemagick')
    elice_utils.send_image("plot.gif")

    return W

if __name__ == "__main__":
    main()
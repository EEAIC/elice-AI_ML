import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import elice_utils
import numpy as np
elice = elice_utils.EliceUtils()



def rabbit(P):
    th_hold = 0.03
    if np.abs((P[0] ** 2) / 12.25 + (P[1] ** 2 / 1) - 1) <= 0.01:
        if -1 <= P[1] <= 0:
        #턱
            return 0
    if np.abs((P[0] ** 2) / 0.1 + ((P[1] - 1.0) ** 2 / 0.04) - 1) <= th_hold:
        if -0.5 <= P[0] <= 0.5 and 0.8 <= P[1] <= 1.2: 
        #코
            return 0
    if np.abs(((P[0] + 0.5) ** 2) / 0.25 + ((P[1] - 0.8) ** 2 / 0.04) - 1) <= th_hold:
        if  -1 <= P[0] <= 0 and 0.6 <= P[1] <= 0.8:
        #왼쪽 입술
            return 0
    if np.abs(((P[0] - 0.5) ** 2) / 0.25 + ((P[1] - 0.8) ** 2 / 0.04) - 1) <= th_hold:
        if 0 <= P[0] <= 1 and 0.6 <= P[1] <= 0.8:
        #오른쪽 입술
            return 0
    if np.abs(P[0] ** 2 + (P[1] - 0.6) ** 2 - 0.25) <= 0.01:
        #입
        if 0 <= P[1] <= 0.6:
            return 0
    if np.abs((P[0] ** 2) / 6.25 + ((P[1] - 3) ** 2 / 1) - 1) <= 0.01:
        if 3 <= P[1] <= 4:
        #두피
            return 0
    if np.abs((-4 * P[0]) - P[1] + 13) <= th_hold:
        if  2.5 <= P[0] <= 3 and 1 <= P[1] <= 3:
        #오른쪽 위면
            return 0
    if np.abs((P[0] - 2.25) ** 2 + P[1] ** 2 - 1.56) <= 0.01:
        #오른쪽 아래면
        if 3 <= P[0] <= 3.5 and 0 <= P[1]:
            return 0
    if np.abs((4 * P[0]) - P[1] + 13) <= th_hold:
        if  -3 <= P[0] <= -2.5 and 1 <= P[1] <= 3:
        #완쪽 위면
            return 0
    if np.abs((P[0] + 2.25) ** 2 + P[1] ** 2 - 1.56) <= 0.01:
        if -3.5 <= P[0] <= -3 and 0 <= P[1]:  
        #왼쪽 아래면
            return 0
    if -1.01 <= P[0] <= 1.01 and 1.99 <= P[1] <= 2.01:
        #안경테
        return 0
    if 0.3 <= P[0] <= 1.3 and 4 <= P[1]:
        #오른쪽 귀 왼쪽
        pos = P - np.array([6.5, 4])
        return np.sqrt(np.sum(pos * pos)) - 6
    if 1.3 <= P[0] <= 2.3 and 3.5 <= P[1]:
        #오른쪽 귀 오른쪽
        pos = P - np.array([-3.9, 4])
        return np.sqrt(np.sum(pos * pos)) - 6
    if -1.3 <= P[0] <= -0.3 and 4 <= P[1]:
        #왼쪽 귀 오른쪽
        pos = P - np.array([-6.5, 4])
        return np.sqrt(np.sum(pos * pos)) - 6
    if -2.3 <= P[0] <= -1.3 and 3.5 <= P[1]:
        #왼쪽 귀 왼쪽
        pos = P - np.array([3.9, 4])
        return np.sqrt(np.sum(pos * pos)) - 6
    def left_eye(P):
        eye_pos = P - np.array([-1.5, 2])
        return np.sqrt(np.sum(eye_pos * eye_pos)) - 0.5
    def right_eye(P):
        eye_pos = P - np.array([1.5, 2])
        return np.sqrt(np.sum(eye_pos * eye_pos)) - 0.5
    return left_eye(P) * right_eye(P) 
    #return np.linalg.norm(P) - 1 # 밑의 코드와 동일하게 동작합니다.
    # return np.sqrt(np.sum(P * P)) - 1
    
def diamond(P):
    return np.abs(P[0]) + np.abs(P[1]) - 1
    
def smile(P):
    def left_eye(P):
        eye_pos = P - np.array([-0.5, 0.5])
        return np.sqrt(np.sum(eye_pos * eye_pos)) - 0.1
    
    def right_eye(P):
        eye_pos = P - np.array([0.5, 0.5])
        return np.sqrt(np.sum(eye_pos * eye_pos)) - 0.1
    
    def mouth(P):
        if P[1] < 0:
            return np.sqrt(np.sum(P * P)) - 0.7
        else:
            return 1
    
    return circle(P) * left_eye(P) * right_eye(P) * mouth(P)

def checker(P, shape, tolerance):
    return abs(shape(P)) < tolerance

def sample(num_points, xrange, yrange, shape, tolerance):
    accepted_points = []
    rejected_points = []
    
    for i in range(num_points):
        x = np.random.random() * (xrange[1] - xrange[0]) + xrange[0]
        y = np.random.random() * (yrange[1] - yrange[0]) + yrange[0]
        P = np.array([x, y])
        
        if (checker(P, shape, tolerance)):
            accepted_points.append(P)
        else:
            rejected_points.append(P)
    
    return np.array(accepted_points), np.array(rejected_points)

xrange = [-3.5, 3.5] # X축 범위입니다.
yrange = [-1, 7] # Y축 범위입니다.
accepted_points, rejected_points = sample(
    1000000, #  점의 개수를 줄이거나 늘려서 실행해 보세요. 너무 많이 늘리면 시간이 오래 걸리는 것에 주의합니다.
    xrange, 
    yrange, 
    rabbit, # smile을 circle 이나 diamond 로 바꿔서 실행해 보세요.
    0.01) # Threshold를 0.01이나 0.0001 같은 다른 값으로 변경해 보세요.

plt.figure(figsize=(xrange[1] - xrange[0], yrange[1] - yrange[0]), 
           dpi=100) # 그림이 제대로 로드되지 않는다면 DPI를 줄여보세요.
           
plt.scatter(rejected_points[:, 0], rejected_points[:, 1], c='lightgray', s=0.1)
plt.scatter(accepted_points[:, 0], accepted_points[:, 1], c='black', s=1)

plt.savefig("graph.png")
elice.send_image("graph.png")
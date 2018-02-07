import numpy as np

def main():
    print(matrix_tutorial())

def matrix_tutorial():
    A = np.array([[1,4,5,8], [2,1,7,3], [5,4,5,9]])

    # 1
    A = A / np.sum(A)
    # 2
    return np.var(A) 

if __name__ == "__main__":
    main()

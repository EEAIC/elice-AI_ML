import re
import math
import numpy as np

def main():
    M1 = {'r': 0.7, 'g': 0.2, 'b': 0.1} # M1 기계의 사탕 비율
    M2 = {'r': 0.3, 'g': 0.4, 'b': 0.3} # M2 기계의 사탕 비율
    
    test = {'r': 4, 'g': 3, 'b': 3}

    print(naive_bayes(M1, M2, test, 0.7, 0.3))

def naive_bayes(M1, M2, test, M1_prior, M2_prior):
    np_M1 = np.array(list(M1.values()))
    np_M2 = np.array(list(M2.values()))
    np_test = np.array(list(test.values()))
    np_result = np.array([np.prod(np_M1 ** np_test) * M1_prior, np.prod(np_M2 ** np_test) * M2_prior])
    np_normalized_result = np_result / np.sum(np_result)
    return np_normalized_result

if __name__ == "__main__":
    main()

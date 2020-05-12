import csv
import pandas as pd
import random
import numpy as np
from sklearn.linear_model import LogisticRegression


def get_samples(num_samples=1000, mode='train'):
    # x-coordinate
    x = np.random.uniform(0, 1, num_samples)

    # y-coordinate
    y = np.random.uniform(0.2, 1.0, num_samples)

    # color
    # 0 - Red, 1 - Blue
    c = np.zeros(num_samples)

    if mode == 'train':
        c[np.where(x < 0.5)] = 1
    elif mode == 'test':
        c = np.random.randint(2, size=num_samples)

    # success for task
    # set up all the blue samples for success
    output = np.zeros(num_samples)
    output[np.where(x < 0.5)] = 1

    dataset = pd.DataFrame({'x': x, 'y': y, 'c': c, 'output': output})
    return (dataset)



if __name__ == '__main__':

    df_train = get_samples(mode='train')
    df_test = get_samples(300, mode='test')

    # train logistic regression classifier
    y_train = df_train.iloc[:, -1]
    x_train = df_train.iloc[:, :-1]
    y_test = df_test.iloc[:, -1]
    x_test = df_test.iloc[:, :-1]

    LR = LogisticRegression(
        random_state=0, solver='lbfgs').fit(x_train, y_train)

    LR.predict(x_test)
    print(round(LR.score(x_test, y_test), 4))

    #print(y_train, x_train)

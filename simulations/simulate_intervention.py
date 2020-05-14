import csv, random
import torch
import pandas as pd
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(3, 100)
        # self.fc11 = nn.Linear(100, 100)
        # self.fc12 = nn.Linear(100, 100)
        # self.fc13 = nn.Linear(100, 100)
        self.fc2 = nn.Linear(100, 2)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        # x = F.relu(self.fc11(x))
        # x = F.relu(self.fc12(x))
        # x = F.relu(self.fc13(x))
        # x = self.fc1(x)
        x = self.fc2(x)
        return x


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

    x = np.expand_dims(x, axis=1)
    y = np.expand_dims(y, axis=1)
    c = np.expand_dims(c, axis=1)
    output =output.astype('int32')


    input = np.concatenate((x,y,c), axis=1).astype('float32')
    print(input.shape, y.shape)
    print(input.dtype, output.dtype)
    # dataset = pd.DataFrame({'x': x, 'y': y, 'c': c, 'output': output})
    # return (dataset)
    return input, output

if __name__ == '__main__':
    x_train, y_train = get_samples(mode='train')
    x_test, y_test = get_samples(300, mode='test')

    print(type(x_train))

    criterion = nn.CrossEntropyLoss()

    model=Net()

    optimizer = torch.optim.Adam(model.parameters(), 0.0001, weight_decay=1e-4)

    bs = 5

    intervent=True
    dorandom=False

    train_log=[]
    test_log = []
    ccc=0
    for epoch in range(50):
        all_iteration = int( x_train.shape[0] / bs)
        acc_cnt=0
        cnt = 0
        for each in range(all_iteration):
            ccc+=1

            if intervent:
                x_data = x_train[each * bs: (each + 1) * bs]
                y_data = y_train[each * bs: (each + 1) * bs]
                if dorandom or ccc<0:
                    r = random.sample([1,2,3], 1)[0]
                else:
                    x_data_t = torch.from_numpy(x_train[each * bs: (each + 1) * bs])
                    y_data_t = torch.from_numpy(y_train[each * bs: (each + 1) * bs]).long()
                    x_in = Variable(x_data_t, requires_grad=True)
                    out = model(x_in)
                    # print(out.size(), y_data.size())
                    loss = criterion(out, y_data_t)
                    loss.backward()
                    g = torch.abs(x_in.grad)
                    _, pred_g = g.topk(1, 1, True, True)
                    # print(pred_g.item())
                    ind = random.sample([0,1,2,3,4],1)[0]
                    pred_g = pred_g[ind]
                    r = pred_g.item() + 1
                    print(r)

                if r==1:
                    x_data[:, 0] = np.clip(x_data[:, 0] + np.random.normal(0, 1, size=x_data[:, 0].shape), 0, 1)
                    y_data = np.zeros_like(x_data[:, 0])
                    y_data[np.where(x_data[:, 0] < 0.5)] = 1
                elif r==2:
                    x_data[:, 1] = np.clip(x_data[:, 1] + np.random.normal(0, 1, size=x_data[:, 1].shape), 0, 1)
                elif r==3:
                    x_data[:, 2] = np.clip(x_data[:, 2] + np.random.normal(0, 1, size=x_data[:, 1].shape), 0, 1)

                x_data = torch.from_numpy(x_data)
                y_data = torch.from_numpy(y_data).long()
            else:
                x_data = torch.from_numpy(x_train[each * bs: (each + 1) * bs])
                y_data = torch.from_numpy(y_train[each * bs: (each + 1) * bs]).long()

            out = model(x_data)
            # print(out.size(), y_data.size())
            loss = criterion(out, y_data)

            _, pred = out.topk(1, 1, True, True)
            # print('p',pred, 'y',y_data)
            pred = pred[:, 0]
            equal = pred == y_data
            # print('equal', equal)
            cor_cnt = torch.sum(equal)

            acc_cnt += cor_cnt.item()
            cnt += x_data.size(0)

            # print("correct", cor_cnt)
            # print('p', pred.size(), 'y',y_data.size())

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            # print("loss {}".format(loss.item()))
            # print("acc {}".format(acc_cnt*1.0/cnt))
            train_log.append(acc_cnt*1.0/cnt)

            # TEST
            x_data = torch.from_numpy(x_test)
            y_data = torch.from_numpy(y_test).long()

            out = model(x_data)
            _, pred = out.topk(1, 1, True, True)
            # print('p',pred, 'y',y_data)
            pred = pred[:, 0]
            equal = pred == y_data
            # print('equal', equal)
            cor_cnt = torch.sum(equal)

            print("Test Acc {}".format(cor_cnt.item() * 1.0 / x_data.size(0)))
            test_log.append(cor_cnt.item() * 1.0 / x_data.size(0))




        # # test
        # x_data = torch.from_numpy(x_test)
        # y_data = torch.from_numpy(y_test).long()
        #
        # out = model(x_data)
        # _, pred = out.topk(1, 1, True, True)
        # # print('p',pred, 'y',y_data)
        # pred = pred[:, 0]
        # equal = pred == y_data
        # # print('equal', equal)
        # cor_cnt = torch.sum(equal)
        #
        # print("Test Acc {}".format(cor_cnt.item() * 1.0 / x_data.size(0)))

    import matplotlib.pyplot as plt

    plt.plot(train_log, ':', label="train")
    plt.plot(test_log, label="test")
    plt.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.xlabel("iterations")
    plt.ylabel("accuracy")
    plt.title("DNN")
    plt.show()





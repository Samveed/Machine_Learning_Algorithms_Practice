import numpy as np
import matplotlib.pyplot as plt


def update(x, y, alpha):

    theta_0 = np.random.rand(1,1)
    theta_1 = np.random.rand(1,1)

    epoch = 0
    while(epoch<5):

        h_x = theta_0 + theta_1*x
        error = h_x - y
        print("Error ", error)
        #print((error.T).shape)
        theta_0 = theta_0 - alpha*np.sum(error)
        print("Theta_0 ", np.asscalar(theta_0))
        theta_1 = theta_1 - alpha*((error).dot(x.T))
        print("Theta_1 ", (theta_1))
        epoch+=1

        if(epoch%10==0):
            print(error)
    
    return theta_0, theta_1
    

def main():
    # x = np.array([0,1,2,3,4,5,6,7,8,9])
    # print(x)
    # y = np.array([1,3,2,5,7,8,8,9,10,12])

    x = 2 * np.random.rand(1, 100)  
    y = 4 + 3 * x + np.random.randn(1, 100)

    plt.subplot(2,1,1)
    plt.scatter(x,y)

    #plt.show()

    learning_rate = 0.01
    theta_0, theta_1 = update(x,y,learning_rate)
    # print(theta_0, " ", theta_1)

    y_final = theta_0 + theta_1*x
    print("y_final ", y_final.shape)
    plt.subplot(2,1,2)

    plt.scatter(x,y_final)

    plt.show()

if __name__ == "__main__":
    main()

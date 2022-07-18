import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, multivariate_normal
#%matplotlib inline
"""
plt.rcParams['figure.figsize'] = 8, 6
plt.rcParams['font.size'] = 12
plt.show()

# gaussian distribution with different values of the mean and variance
x = np.linspace(start = -10, stop = 10, num = 200)
mean_opt = [0, 0, 2]
var_opt = [1, 4, 4]

for m, v in zip(mean_opt, var_opt):
    y = norm(m, np.sqrt(v)).pdf(x)
    plt.plot(x, y, label = '$\mu$ = {}, $\sigma^2$ = {}'.format(m, v))
    plt.legend()

plt.show()


np.random.seed(2)
x1 = np.random.normal(0, 2, size = 2000)
x2 = np.random.normal(5, 5, size = 2000)
print(len(x1))
data = [x1, x2]

def plot_hist(data):
    for x in data:
        plt.hist(x, bins = 80, density = True, alpha = 0.6)

    plt.xlim(-10, 20)

plot_hist(data)
plt.show()
"""
import numpy as np
a=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
#print(a)
print(a.shape[1])

a=a.reshape(a.shape[0],6)
print(a.shape)




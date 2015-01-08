#Use the iris dataset for PCA. It is included with scikit-learn
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets imort load_iris

#Load the dataset and initialize a PCA estimator.
#PCA takes a number of principal components to retain as hyperparameters.
#fit_transform() reutrns the reduced data matrix.
data = load_iris()
y = data.target
X = data.data
pca = PCA(n_components=2)
reduced_X = pca.fit_transform(X)

#Assemble and plot the reduced data.
red_x, red_y = [], []
blue_x, blue_y = [], []
green_x, green_y = [], []
for i in range(len(reduced_X)):
	if y[i] == 0:
		red_x.append(reduced_X[i][0])
		red_y.append(reduced_X[i][1])
	elif y[i] == 1:
		blue_x.append(reduced_X[i][0])
		blue_y.append(reduced_X[i][1])
	else:
		green_x.append(reduced_X[i][0])
		green_y.append(reduced_X[i][1])
plt.scatter(red_x, red_y, c='r', marker='X')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y, c='g', marker='.')
plt.show()
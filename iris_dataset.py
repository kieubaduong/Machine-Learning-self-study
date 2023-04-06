from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import matplotlib.pyplot as plt

iris_dataset = datasets.load_iris()

# iris_dataset.data contains the features
# iris_dataset.target contains the labels
# test_size=0.3 means 30% of the data will be used for testing
# random_state=0 means the data will be split randomly
x_train, x_test, y_train, y_test = train_test_split(
    iris_dataset.data, iris_dataset.target, test_size=0.3, random_state=0)

model = DecisionTreeClassifier()

trained_model = model.fit(x_train, y_train)

print(trained_model.score(x_test, y_test))  # 0.9777777777777777


# Plotting the accuracy of the model with different test sizes
size = np.array([])
accuracy = np.array([])

for i in range(0, 100, 5):
    i = i/100
    if i == 0:
        continue
    x_train, x_test, y_train, y_test = train_test_split(
        iris_dataset.data, iris_dataset.target, test_size=i, random_state=1)
    model = DecisionTreeClassifier()
    trained_model = model.fit(x_train, y_train)
    size = np.append(size, i)
    accuracy = np.append(accuracy, trained_model.score(x_test, y_test))

plt.plot(size, accuracy)

plt.get_current_fig_manager().set_window_title(
    'Accuracy of the model with different test sizes')
plt.xlabel('Test Size')
plt.ylabel('Accuracy')
plt.xticks(np.arange(size.min(), size.max()+0.1, step=0.1))


plt.show()

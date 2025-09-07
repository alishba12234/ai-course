from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = load_iris()

#features and target
X = iris.data      
y = iris.target   

# Create and train the Decision Tree model
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X, y)

# Predict a sample
print("Prediction for first sample:", clf.predict([X[0]]))

# Visualize the decision tree
plt.figure(figsize=(10, 6))
plot_tree(clf, filled=True,
          feature_names=iris.feature_names,
          class_names=iris.target_names)
plt.show()

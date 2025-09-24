from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
#features and labels
X = iris.data      
y = iris.target    

# Create and train decision tree
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Visualize the tree
plt.figure(figsize=(10, 6))
plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.show()

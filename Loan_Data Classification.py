import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn import metrics
from six import StringIO
from IPython.display import Image
import pydotplus

# Load your dataset
df = pd.read_csv("C:/Users/Lenovo/Documents/GitHub/ai-course/code test/loan_dataset.csv")

# Feature Selection
# Target variable
y = df["not.fully.paid"]

# Features (all except target)
X = df.drop("not.fully.paid", axis=1)

# For DecisionTree, we need to convert categorical feature 'purpose'
X = pd.get_dummies(X, columns=["purpose"], drop_first=True)


# Splitting Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1, stratify=y
)

# Building Decision Tree Model
clf = DecisionTreeClassifier(criterion="gini", random_state=42)
clf = clf.fit(X_train, y_train)

# Predictions
y_pred = clf.predict(X_test)

# Evaluating Model
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Visualizing Decision Tree
dot_data = StringIO()
export_graphviz(
    clf,
    out_file=dot_data,
    filled=True,
    rounded=True,
    special_characters=True,
    feature_names=X.columns,
    class_names=['Fully Paid (0)','Not Fully Paid (1)']
)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png("loan_tree.png")
Image(graph.create_png())

# Try with Pre-Pruning (max_depth=3, entropy)
clf2 = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=42)
clf2 = clf2.fit(X_train, y_train)
y_pred2 = clf2.predict(X_test)

print("Accuracy with max_depth=3:", metrics.accuracy_score(y_test, y_pred2))

dot_data = StringIO()
export_graphviz(
    clf2,
    out_file=dot_data,
    filled=True,
    rounded=True,
    special_characters=True,
    feature_names=X.columns,
    class_names=['Fully Paid (0)','Not Fully Paid (1)']
)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png("loan_tree_pruned.png")
Image(graph.create_png())

# from this data ,I learned how to build and evaluate a Decision Tree classifier using scikit-learn.It showed me how to load data, split it into training and testing sets, and train a model to make predictions. I also learned how to measure accuracy, handle categorical variables, and visualize the decision tree to better understand how decisions are made.
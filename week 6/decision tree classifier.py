import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
# Example of a Decision Tree Classifier with visualization
data = {
   'Age': [36, 42, 23, 52, 43, 44, 66, 35, 52, 35, 24, 18, 45],
    'Experience': [10, 12, 4, 4, 21, 14, 3, 14, 13, 5, 3, 3, 9],
    'Rank': [9, 4, 6, 4, 8, 5, 7, 9, 7, 9, 5, 7, 9],
    'Nationality': ['UK', 'USA', 'N', 'USA', 'USA', 'UK', 'N', 'UK', 'N', 'N', 'USA', 'UK', 'UK'],
    'Go': ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'YES', 'YES', 'YES', 'YES', 'NO', 'YES', 'YES']
}

df = pd.DataFrame(data)

# Encode categorical values
le_nationality = LabelEncoder()
df['Nationality'] = le_nationality.fit_transform(df['Nationality'])

le_go = LabelEncoder()
df['Go'] = le_go.fit_transform(df['Go'])  # YES=1, NO=0

# Features and target
X = df[['Age', 'Experience', 'Rank', 'Nationality']]
y = df['Go']

# Train decision tree
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X, y)

# Visualize
plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=['Age', 'Experience', 'Rank', 'Nationality'], class_names=['NO', 'YES'])
plt.show()

# Prediction example
sample = [[40, 10, 7, le_nationality.transform(['UK'])[0]]]
print("Prediction:", le_go.inverse_transform(clf.predict(sample)))

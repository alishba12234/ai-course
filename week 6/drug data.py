import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , classification_report
from sklearn.preprocessing import LabelEncoder

col_names = ['Age' , 'Sex' , 'BP' , 'Cholesterol' , 'Na_to_K' , 'Drug']

df = pd.read_csv("drug200.csv")

le = LabelEncoder()
for col in ['Sex', 'BP', 'Cholesterol']:
    df[col] = le.fit_transform(df[col])

# splitting dataset

X = df.drop('Drug', axis=1)
y = df['Drug']

print(X.shape)
print(y.shape)

# split into train\test sets

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#Train decision tree classifier

model = DecisionTreeClassifier()

model.fit(X_train , y_train)

y_pred = model.predict(X_test)

# Model accuracy

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:", classification_report(y_test, y_pred))
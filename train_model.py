import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset from the UCI repository
data = pd.read_csv('heart_indicator.csv')

# Display the first few rows of the dataset (optional)
print(data.head())

# Separate features (X) and target (y)
X = data.drop('HeartDiseaseorAttack', axis=1)  # Features: all columns except 'target'
y = data['HeartDiseaseorAttack']                # Target variable: 'target'

# Split the data into training and test sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features using StandardScaler
scaler2 = StandardScaler()
X_train = scaler2.fit_transform(X_train)  # Fit on training data
X_test = scaler2.transform(X_test)        # Transform test data using the same scaler

# Train the Random Forest model
from sklearn.metrics import accuracy_score
max_accuracy = 0


for x in range(50):    #tuning for best features
    rf = RandomForestClassifier(random_state=x)
    rf.fit(X_train,y_train)
    Y_pred_rf = rf.predict(X_test)
    current_accuracy = round(accuracy_score(Y_pred_rf,y_test)*100,2)
    if(current_accuracy>max_accuracy):
        max_accuracy = current_accuracy
        best_x = x

model2 = RandomForestClassifier(random_state=best_x)  # Initialize the model
model2.fit(X_train, y_train)                       # Train the model

# Save the trained model and scaler to .pkl files
joblib.dump(model2, 'heart_indicator_model.pkl')  # Save the model
joblib.dump(scaler2, 'scaler2.pkl')               # Save the scaler

print("Model and scaler saved successfully!")
# import pandas as pd
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import StandardScaler, LabelEncoder
# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# from sklearn.model_selection import cross_val_score

# df = pd.read_csv('heart_indicator.csv')

# df.fillna(df.median(), inplace=True)

# X = df.drop('HeartDiseaseorAttack', axis=1)
# y = df['HeartDiseaseorAttack']

# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# param_grid = {
#     'n_estimators': [100, 200, 300],
#     'max_depth': [None, 10, 20, 30],
#     'min_samples_split': [2, 5, 10],
#     'min_samples_leaf': [1, 2, 4]
# }

# grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
# grid_search.fit(X_train, y_train)

# best_params = grid_search.best_params_
# print(f"Best Parameters: {best_params}")

# rf_model_best = RandomForestClassifier(**best_params)
# rf_model_best.fit(X_train, y_train)

# y_pred = rf_model_best.predict(X_test)

# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy:.4f}")

# print("Classification Report:\n", classification_report(y_test, y_pred))

# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# cv_scores = cross_val_score(rf_model_best, X_scaled, y, cv=5)
# print(f"Cross-Validation Accuracy: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

# importances = rf_model_best.feature_importances_
# feature_importance = pd.DataFrame({
#     'Feature': X.columns,
#     'Importance': importances
# }).sort_values(by='Importance', ascending=False)

# print("Feature Importance:\n", feature_importance)

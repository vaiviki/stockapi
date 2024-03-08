import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV, train_test_split


def generateModel(df):
    # Define features (X) and target variable (y)
    features = [ 'Open', 'High',
           'Low', 'Close', 'Shares Traded',
            'Turnover','Weekday']
    X = df[features]
    y = df['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
    # Create an XGBClassifier model
    model = XGBClassifier(n_estimators=100, random_state=48)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.2f}')

    # Display classification report
    print(classification_report(y_test, y_pred))
    # Define the grid of parameters to search
    param_grid = {
        'learning_rate': [0.01, 0.05, 0.1,0.15, 0.2, 0.3,0.35,0.4],
        'n_estimators': [10,15,25,50,75, 100,110,115, 200],
        'gamma':[0.5,1,0.05,0.1]
        # Add other hyperparameters as needed
    }

    print("generating grid search...")
    # Perform grid search using cross-validation
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, scoring='accuracy', cv=5)
    grid_result = grid_search.fit(X_train, y_train)

    # Display the best parameters and corresponding accuracy
    print("Best Parameters: ", grid_result.best_params_)
    print("Best Accuracy: ", grid_result.best_score_)

    # Evaluate the model with the best parameters on the test set
    best_model = grid_result.best_estimator_
    y_pred = best_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy on Test Set: {accuracy:.2f}')
    return best_model


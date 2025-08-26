import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

def task4():
    """
    Performs Task 4: Feature Normalization and KNN.
    1. Reads the urbansound8k_features_small.csv dataset.
    2. Applies MinMax feature scaling to the data.
    3. Splits the data into training and testing sets.
    4. Trains a new KNeighborsClassifier on the scaled training data.
    5. Evaluates the model's accuracy on the scaled test data and saves
       the result to task4_summary.json.
    """
    file_path = "urbansound8k_features_small.csv"
    
    # Load the dataset
    df = pd.read_csv(file_path)

    # Separate features (X) and target (y)
    X = df.drop(columns=['class', 'classID'])
    y = df['classID']

    # 1. Apply MinMax feature normalization
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)

    # Split the scaled data into training and testing sets
    X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(
        X_scaled_df, y, 
        test_size=0.2, 
        random_state=77, 
        shuffle=True, 
        stratify=y
    )

    # 2. Train a new KNeighborsClassifier on the scaled training data
    knn_scaled = KNeighborsClassifier(n_neighbors=5)
    knn_scaled.fit(X_train_scaled, y_train)

    # 3. Evaluate the model on the scaled test data
    y_pred_scaled = knn_scaled.predict(X_test_scaled)
    accuracy_scaled = accuracy_score(y_test, y_pred_scaled)
    
    # Round the accuracy to two decimal places
    accuracy_scaled_rounded = round(accuracy_scaled, 2)

    # Prepare the output dictionary
    output_data = {
        "The accuracy of KNN (scaled data, n_neighbors=5):": accuracy_scaled_rounded
    }
    
    # Write the output to a JSON file
    output_file_name = "task4_summary.json"
    with open(output_file_name, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4)

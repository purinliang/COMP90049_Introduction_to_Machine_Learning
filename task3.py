import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def task3():
    """
    Task 3: Data Splitting and K-Nearest Neighbors (KNN).
    """
    file_path = "urbansound8k_features_small.csv"

    # 1. Read the dataset into a DataFrame
    df = pd.read_csv(file_path)

    # 2. Separate features (X) and target (y)
    # Drop 'class' and 'classID' as they are the targets. The rest are features.
    X = df.drop(columns=['class', 'classID'])
    y = df['classID']

    # 3. Split the data into training and testing sets with stratification
    # Ensure random_state and shuffle are set for reproducibility
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=0.2, 
        random_state=77, 
        shuffle=True, 
        stratify=y
    )

    # 4. Train the KNeighborsClassifier on the unscaled data
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    # 5. Test the model's accuracy on the unscaled test data
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    # 6. Round the accuracy to two decimal places
    accuracy_rounded = round(accuracy, 2)

    # 7. Prepare the output dictionary
    output_data = {
        "The accuracy of KNN (unscaled data, n_neighbors=5):": accuracy_rounded
    }
    
    # 8. Save the output to a JSON file
    output_file_name = "task3_summary.json"
    with open(output_file_name, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4)

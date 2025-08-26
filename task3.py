import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def task3():
    """
    Performs Task 3: Data Splitting and KNN.
    1. Reads the urbansound8k_features_small.csv dataset.
    2. Splits the data into training (80%) and testing (20%) sets using a
       stratified strategy.
    3. Trains a KNeighborsClassifier on the unscaled training data.
    4. Evaluates the model's accuracy on the unscaled test data and saves
       the result to task3_summary.json.
    """
    file_path = "urbansound8k_features_small.csv"
    
    try:
        # Load the dataset
        df = pd.read_csv(file_path)

        # Separate features (X) and target (y)
        # Drop 'class' and 'classID' as they are the targets. The rest are features.
        X = df.drop(columns=['class', 'classID'])
        y = df['classID']

        # 1. Split the data into training and testing sets with stratification
        # Ensure random_state and shuffle are set for reproducibility
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, 
            test_size=0.2, 
            random_state=77, 
            shuffle=True, 
            stratify=y
        )

        # 2. Train the KNeighborsClassifier on the unscaled data
        knn = KNeighborsClassifier(n_neighbors=5)
        knn.fit(X_train, y_train)

        # 3. Test the model's accuracy on the unscaled test data
        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # Round the accuracy to two decimal places
        accuracy_rounded = round(accuracy, 2)

        # Prepare the output dictionary
        output_data = {
            "Accuracy of KNN on unscaled test data:": accuracy_rounded
        }
        
        # Write the output to a JSON file
        output_file_name = "task3_summary.json"
        with open(output_file_name, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=4)
        
        print(f"Task 3 summary successfully saved to {output_file_name}")
        print(f"Accuracy of KNN (unscaled) on test data: {accuracy_rounded}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    task3()
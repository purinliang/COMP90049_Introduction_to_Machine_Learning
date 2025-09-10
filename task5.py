import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def task5():
    """
    Performs Task 5: Naive Bayes.
    1. Reads the urbansound8k_features_small.csv dataset.
    2. Splits the data into training (80%) and testing (20%) sets.
    3. Trains a GaussianNB classifier on the unscaled training data.
    4. Evaluates the model's accuracy on the unscaled test data and saves
       the result to task5_summary.json.
    """
    file_path = "urbansound8k_features_small.csv"

    # Load the dataset
    df = pd.read_csv(file_path)

    # Separate features (X) and target (y)
    X = df.drop(columns=['class', 'classID'])
    y = df['classID']

    # Split the unscaled data into training and testing sets with stratification
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=77,
        shuffle=True,
        stratify=y
    )

    # Train a GaussianNB classifier on the unscaled training data
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)

    # Evaluate the model's accuracy on the unscaled test data
    y_pred = gnb.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Round the accuracy to two decimal places
    accuracy_rounded = round(accuracy, 2)

    # Prepare the output dictionary
    output_data = {
        "The accuracy of GaussianNB (unscaled data)": accuracy_rounded
    }

    # Write the output to a JSON file
    output_file_name = "task5_summary.json"
    with open(output_file_name, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4)
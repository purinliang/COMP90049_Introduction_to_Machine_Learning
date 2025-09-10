import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def task6():
    """
    Performs Task 6: Decision Tree.
    1. Reads the urbansound8k_features_small.csv dataset.
    2. Splits the data into training and testing sets.
    3. Trains a DecisionTreeClassifier on the unscaled training data,
       using Information Gain as the splitting criterion.
    4. Reports accuracy, tree depth, and the root node feature in a JSON file.
    5. Visualizes the top 3 levels of the tree and saves it to a PNG file.
    """
    file_path = "urbansound8k_features_small.csv"

    # Load the dataset
    df = pd.read_csv(file_path)

    # Separate features (X) and target (y)
    X = df.drop(columns=['class', 'classID'])
    y = df['classID']
    feature_names = X.columns.tolist()
    class_names = [str(c) for c in sorted(df['class'].unique())]

    # Split the data into training and testing sets with stratification
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=77,
        shuffle=True,
        stratify=y
    )

    # 1. Train the DecisionTreeClassifier
    # Use 'entropy' for Information Gain
    dt_classifier = DecisionTreeClassifier(
        criterion='entropy',
        random_state=77
    )
    dt_classifier.fit(X_train, y_train)

    # Predict and calculate accuracy
    y_pred = dt_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # 2. Get the depth of the trained tree
    tree_depth = dt_classifier.get_depth()

    # 3. Identify the feature at the root node
    # The root node's feature index is stored at position 0
    root_feature_index = dt_classifier.tree_.feature[0]
    root_feature_name = feature_names[root_feature_index]

    # Prepare the output dictionary
    output_data = {
        "The accuracy of Decision Tree (default max_depth)": round(accuracy, 2),
        "The depth of trained Decision Tree": tree_depth,
        "The feature at the root of the tree": root_feature_name
    }

    # Write the output to a JSON file
    output_file_name = "task6_summary.json"
    with open(output_file_name, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4)

    # 4. Draw the plot to visualise the top three levels of the tree
    plt.figure(figsize=(25, 15))
    plot_tree(
        dt_classifier,
        max_depth=2,  # Visualise top 3 levels (root + 2 more)
        feature_names=feature_names,
        class_names=class_names,
        filled=True,
        rounded=True,
        fontsize=10
    )
    plt.title("Top 3 Levels of the Decision Tree", fontsize=15)
    
    # Save the plot
    plot_file_name = "task6_plot.png"
    plt.savefig(plot_file_name, dpi=300, bbox_inches='tight')

    print(f"Task 6 completed. Summary saved to {output_file_name} and plot to {plot_file_name}.")
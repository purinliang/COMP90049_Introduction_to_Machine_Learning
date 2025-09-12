import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

def task7():
    """
    Task 7: Support Vector Machines.
    """
    file_path = "urbansound8k_features_small.csv"

    # 1. Read the dataset into a DataFrame
    df = pd.read_csv(file_path)

    # 2. Separate features (X) and target (y)
    X = df.drop(columns=['class', 'classID'])
    y = df['classID']

    # 3. Split the data into training and testing sets with stratification
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=77,
        shuffle=True,
        stratify=y
    )
    
    # 4. Train SVM models with a linear kernel and different C values
    c_values = [0.01, 0.1, 0.5]
    accuracies = []

    for c in c_values:
        svc_model = LinearSVC(
            C=c, 
            random_state=77, 
            dual=False, 
            loss='squared_hinge',
            max_iter=50000,
            tol=2e-4 # Explicitly setting tolerance
        )
        
        try:
            svc_model.fit(X_train, y_train)
            y_pred = svc_model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            accuracies.append(accuracy)
            print(f"Model for C={c} trained. Accuracy: {accuracy:.4f}")
        except Exception as e:
            print(f"Warning: Model for C={c} failed to converge. Reason: {e}")
            accuracies.append(None) 

    # 5. Draw a line plot to visualize the change in performance
    plt.figure(figsize=(10, 6))
    
    valid_c_values = [c_values[i] for i, acc in enumerate(accuracies) if acc is not None]
    valid_accuracies = [acc for acc in accuracies if acc is not None]
    
    plt.plot(valid_c_values, valid_accuracies, marker='o', linestyle='-')
    plt.title('SVM Classifier Performance vs. Regularization Parameter C (Unscaled Data)')
    plt.xlabel('Regularization Parameter C')
    plt.ylabel('Accuracy')
    plt.xticks(c_values)
    plt.grid(True)
    
    # 6. Save the plot to a PNG file
    plot_file_name = "task7_plot.png"
    plt.savefig(plot_file_name, dpi=300, bbox_inches='tight')
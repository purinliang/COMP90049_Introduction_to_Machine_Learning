import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, classification_report

def task8():
    """
    Performs Task 8: Model Evaluation and Interpretation.
    1. Trains an SVM model with a pre-determined "best" C value.
    2. Generates and visualizes the confusion matrix.
    3. Computes and reports per-class precision, recall, and F1-score.
    4. Saves the confusion matrix plot and the metrics to files.
    """
    file_path = "urbansound8k_features_small.csv"

    # Load the dataset
    df = pd.read_csv(file_path)

    # Separate features (X) and target (y)
    X = df.drop(columns=['class', 'classID'])
    y = df['classID']
    class_names = sorted(df['class'].unique().tolist())

    # Split the data into training and testing sets with stratification
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=77,
        shuffle=True,
        stratify=y
    )

    # Train an SVM model with the "best" C value (I got C=0.5 is "best" from Task 7)
    best_c = 0.5
    svc_model = LinearSVC(
        C=best_c,
        random_state=77,
        dual=False,
        loss='squared_hinge',
        max_iter=50000,
        tol=2e-4 # Explicitly setting tolerance
    )
    svc_model.fit(X_train, y_train)
    y_pred = svc_model.predict(X_test)

    # 1. Generate and visualize the confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        cm,
        annot=True,
        fmt='d',
        cmap='Blues',
        xticklabels=class_names,
        yticklabels=class_names
    )
    plt.title('Confusion Matrix for SVM Model (C={best_c})')
    plt.ylabel('True Class')
    plt.xlabel('Predicted Class')
    plot_file_name = "task8_plot.png"
    plt.savefig(plot_file_name, dpi=300, bbox_inches='tight')
    print(f"Confusion matrix plot saved to {plot_file_name}")

    # 3. Compute and report precision, recall, and F1-score for each class
    report_dict = classification_report(y_test, y_pred, target_names=class_names, output_dict=True)

    # Prepare the output dictionary in the specified format
    metrics_summary = {}
    for class_name, metrics in report_dict.items():
        if class_name in class_names:
            metrics_summary[class_name] = {
                "precision": round(metrics['precision'], 2),
                "recall": round(metrics['recall'], 2),
                "f1-score": round(metrics['f1-score'], 2)
            }
    
    # Write the output to a JSON file
    output_file_name = "task8_summary.json"
    with open(output_file_name, 'w', encoding='utf-8') as f:
        json.dump(metrics_summary, f, indent=4)
        
    print(f"Per-class metrics saved to {output_file_name}")

    print("Task 8 completed.")
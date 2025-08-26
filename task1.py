import pandas as pd
import json

def task1():
    """
    Performs Task 1: Summary Statistics.
    1. Reads the urbansound8k_features_small.csv dataset.
    2. Calculates total rows and columns.
    3. Calculates the exact number of samples for each of the 10 sound classes.
    4. Writes the results to a JSON file named task1_summary.json.
    """
    # Assuming the file is in the same directory as the script
    file_path = "urbansound8k_features_small.csv"
    
    # 1. Read the dataset into a DataFrame
    df = pd.read_csv(file_path)
    
    # 2. Calculate the total number of rows and columns
    num_rows, num_cols = df.shape
    
    # 3. Calculate the exact number of samples for each sound class
    # Convert the Series to a dictionary with sorted keys
    class_counts = df['class'].value_counts().sort_index().to_dict()
    
    # 4. Prepare the output dictionary in the specified format
    summary_data = {
        "Total number of rows:": num_rows,
        "Total number of columns:": num_cols,
        "Class counts": class_counts
    }
    
    # Write the dictionary to a JSON file
    output_file_name = "task1_summary.json"
    with open(output_file_name, 'w', encoding='utf-8') as f:
        json.dump(summary_data, f, indent=4)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task2():
    """
    Performs Task 2: Feature Visualization.
    1. Reads the urbansound8k_features_small.csv dataset.
    2. Filters for 'dog_bark' and 'air_conditioner' classes.
    3. Creates a violin plot of the 'contrast0' feature for these two classes.
    4. Saves the plot to a file named task2_violin.png.
    """
    # Assuming the file is in the same directory as the script
    file_path = "urbansound8k_features_small.csv"
    
    try:
        # 1. Read the dataset into a DataFrame
        df = pd.read_csv(file_path)

        # 2. Filter the DataFrame for the two classes of interest
        classes_to_plot = ['dog_bark', 'air_conditioner']
        df_filtered = df[df['class'].isin(classes_to_plot)]

        # Set up the plot style
        sns.set_theme(style="whitegrid")
        
        # Create a figure and axes for the plot
        plt.figure(figsize=(8, 6))

        # 3. Create the violin plot
        # Use a more descriptive label for the y-axis
        sns.violinplot(
            x='class', 
            y='contrast0', 
            data=df_filtered, 
            palette="muted", 
            inner="quartile"
        )
        
        # Add labels and a title for better readability
        plt.title('Distribution of "contrast0" for Dog Bark and Air Conditioner Sounds')
        plt.xlabel('Sound Class')
        plt.ylabel('Spectral Contrast ("contrast0")')

        # 4. Save the plot to a PNG file
        output_file_name = "task2_violin.png"
        plt.savefig(output_file_name, dpi=300)
        
        print(f"Violin plot successfully saved to {output_file_name}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print("Please ensure the CSV file is in the same directory as this script.")
    except KeyError:
        print("Error: The required columns ('class' or 'contrast0') were not found in the dataset.")
        print("Please check the column names in your CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# This part ensures the function can be run directly as specified
if __name__ == '__main__':
    task2()
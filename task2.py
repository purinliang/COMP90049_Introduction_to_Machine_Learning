import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task2():
    """
    Task 2: Feature Visualization.
    """
    file_path = "urbansound8k_features_small.csv"
    
    # 1. Read the dataset into a DataFrame
    df = pd.read_csv(file_path)

    # 2. Filter the DataFrame for the two classes of interest
    classes_to_plot = ['dog_bark', 'air_conditioner']
    df_filtered = df[df['class'].isin(classes_to_plot)]
    
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 6))

    # 3. Create the violin plot
    sns.violinplot(
        x='class',
        y='contrast0',
        data=df_filtered,
        palette="muted",
        hue='class',  # Assign 'class' to hue to resolve the FutureWarning
        legend=False, # Hide the legend, since it's redundant
        inner="quartile"
    )
    
    # 4. Add labels and a title for better readability
    plt.title('Distribution of Spectral Contrast for Dog Bark and Air Conditioner Sounds')
    plt.xlabel('Sound Class')
    plt.ylabel('Spectral Contrast ("contrast0")')

    # 5. Save the plot to a PNG file
    output_file_name = "task2_violin.png"
    plt.savefig(output_file_name, dpi=300)
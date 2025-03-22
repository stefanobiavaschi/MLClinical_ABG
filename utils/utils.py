import numpy as np

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from scipy.stats import gaussian_kde

def calculate_coefficient_of_variation(y):
    """
    Calculates the Coefficient of Variation (CV) of class frequencies in a label array.
    
    Parameters:
        y (array-like): Array containing class labels.
        
    Returns:
        float: Coefficient of Variation of class frequencies.
    """
    # Count occurrences of each class
    class_counts = np.bincount(y)
    
    # Calculate the mean frequency
    mean_frequency = np.mean(class_counts)
    
    # Calculate the standard deviation
    std_deviation = np.std(class_counts)
    
    # Calculate the Coefficient of Variation (CV)
    coefficient_of_variation = std_deviation / mean_frequency if mean_frequency != 0 else 0
    
    return coefficient_of_variation


def calculate_skewness(y):
    """
    Calculates the Skewness (asymmetry) of class frequencies in a label array.
    
    Parameters:
        y (array-like): Array containing class labels.
        
    Returns:
        float: Skewness of class frequencies.
    """
    # Count occurrences of each class
    class_counts = np.bincount(y)
    
    # Calculate the mean frequency
    mean_frequency = np.mean(class_counts)
    
    # Calculate the standard deviation
    std_deviation = np.std(class_counts)
    
    # Calculate the skewness
    skewness = (np.sum((class_counts - mean_frequency) ** 3) / len(class_counts)) / (std_deviation ** 3) if std_deviation != 0 else 0
    
    return skewness

def plot_feature_distribution(df, feature):
    """
    Plots boxplot and KDE plot for a selected feature, split by target variable 'y' using Plotly.
    
    Parameters:
    df (DataFrame): The dataset.
    feature (str): The name of the feature to plot.
    """
    # Ensure 'y' is categorical
    df['y_desc'] = df['y_desc'].astype(str)
    
    # Create subplots
    fig = make_subplots(rows=1, cols=2, subplot_titles=(f'Boxplot of {feature} by Target', f'Distribution of {feature} by Target'))
    
    # Box plot
    box_plot = px.box(df, x='y_desc', y=feature)
    fig.add_trace(box_plot.data[0], row=1, col=1)
    
    # KDE plots
    for cls in df['y_desc'].unique():
        class_data = df[df['y_desc'] == cls][feature]
        class_data = class_data.dropna()
        # Compute KDE
        try:
            density = gaussian_kde(class_data)
            xs = np.linspace(class_data.min(), class_data.max(), 200)
            ys = density(xs)
            fig.add_trace(go.Scatter(x=xs, y=ys, mode='lines', name=f'y = {cls}'), row=1, col=2)
        except:
            print(f"It's not possible to calculate density for class {cls}")
    
    # Update layout
    fig.update_xaxes(title_text=feature, row=1, col=2)
    fig.update_yaxes(title_text='Density', row=1, col=2)
    fig.update_layout(title=f'Feature Distribution: {feature}', showlegend=True)
    
    fig.show()


def map_diagn_out(n):
    D_diag = {
        0: "TRM",
        1: "INF",
        2: "ALTRO",
        3: "CARD",
        4: "RESP",
        5: "EMO"
    }
    return D_diag[n]
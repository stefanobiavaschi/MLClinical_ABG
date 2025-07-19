import numpy as np

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
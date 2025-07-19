import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
from scipy.stats import gaussian_kde
import plotly.express as px
import plotly.graph_objects as go


def plot_correlation_matrix(df, columns=None):
    if columns is None:
        columns = df.columns
    df_corr = df[columns].copy()

    df_corr['DATA'] = pd.to_datetime(df_corr['DATA'])

    # Estrae il giorno dell'anno
    df_corr['day_of_year'] = df_corr['DATA'].apply(lambda x: x.timetuple().tm_yday)
    df_corr['sin_day'] = np.sin(2 * np.pi * df_corr['day_of_year'] / 365)
    df_corr['cos_day'] = np.cos(2 * np.pi * df_corr['day_of_year'] / 365)

    df_corr = df_corr.drop(columns=[ "DATA", "day_of_year"])

    for col in list(df_corr.columns):
        df_corr = df_corr.loc[df_corr[col] != '.....']
        df_corr[col] = df_corr[col].astype(float)

    corr_matrix = df_corr.corr()

    # Creazione della heatmap colorata
    plt.figure(figsize=(16, 12))
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap='coolwarm',
        vmin=-1,
        vmax=1,
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.8}
    )
    plt.title('Matrice di Correlazione')
    plt.show()


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
import pandas as pd
from pycaret.classification import (
    setup,
    compare_models,
    finalize_model,
    predict_model,
    tune_model,
    get_config,
    pull
)


def train_pycaret(X_train: pd.DataFrame, y_train: pd.Series, params: dict, n_class: int):
    """
    Train a classification model using PyCaret, returning the best model and feature importances.

    Args:
        X_train (pd.DataFrame): The training feature dataset.
        y_train (pd.Series): The target variable for training.
        params (dict): Additional parameters (currently unused).
        n_class (int): Number of folds for cross-validation.

    Returns:
        tuple: A tuple containing the trained model and a DataFrame of feature importances.
    """
    # Combine features and target into a single DataFrame
    train_data = X_train.copy()
    train_data["y"] = y_train

    # Initialize PyCaret setup
    exp_clf = setup(data=train_data, target='y', session_id=42, fold=n_class)

    setup_config = pull() 

    # Identify the best model based on accuracy
    best_model = compare_models(sort='Accuracy')

    # Finalize the model by training it on the entire dataset
    model = finalize_model(best_model)

    # Get the names of preprocessed features
    feature_names = get_config('X_train_transformed').columns

    try:
        feat_importance_value = model.feature_importances_
    except:
        # Some models don't have .feature_importances_
        feat_importance_value = [None]*len(feature_names)
    
    # Create a DataFrame for feature importances
    feature_importances_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': feat_importance_value
    })

    # Sort features by importance
    feature_importances_df = feature_importances_df.sort_values(by='Importance', ascending=False).reset_index(drop=True)

    # Extract model name
    base_model = model.steps[-1][1]  # Access the last step of the pipeline
    model_name = base_model.__class__.__name__

    # Retrieve metrics from the compare_models output
    metrics_df = pull()

    return model, feature_importances_df, model_name, setup_config, metrics_df


def train_pycaret_v2(X_train: pd.DataFrame, y_train: pd.Series, params: dict, n_class: int):
    """
    Train a classification model using PyCaret with hyperparameter tuning, returning the final model, its name, and parameters.

    Args:
        X_train (pd.DataFrame): The training feature dataset.
        y_train (pd.Series): The target variable for training.
        params (dict): Additional parameters (currently unused).
        n_class (int): Number of folds for cross-validation.

    Returns:
        tuple: A tuple containing the finalized model, model name, and model parameters.
    """
    # Combine features and target into a single DataFrame
    train_data = X_train.copy()
    train_data["y"] = y_train

    # Initialize PyCaret setup
    exp_clf = setup(data=train_data, target='y', session_id=42, fold=n_class)

    # Identify the best model based on accuracy
    best_model = compare_models(sort='Accuracy')

    # Fine-tune the best model to optimize accuracy
    tuned_model = tune_model(best_model, optimize='Accuracy')

    # Finalize the model by training it on the entire dataset
    final_model = finalize_model(tuned_model)

    # Extract the model name and parameters
    model_name = str(final_model)
    model_params = final_model.get_params()

    return final_model, model_name, model_params

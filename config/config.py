from datetime import datetime

DATASET_NAME = "20241209_dataset_v32"
YEARS_TRAINING = [ 2020, 2021, 2022, 2023] #  
LIST_TYPE = ["Venoso", "Arterioso"] # , "Venoso", "Arterioso"

PREPROCESSING_TRANSFORMATION = False
CLASS_UNDER_SAMPLE = True

MODEL = "Pycaret"
MODEL_NAME = f"{datetime.now().strftime('%y%m%d')}_{MODEL}"
PARAMS = {}

SAVE_PREDICT_TO_XLSX = False
SAVE_PKL_MODEL = False

TRAINING_INFO = f"{MODEL} - Dataset 20-23"
N_CLASS = 6
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np

# Calculate age difference in years
def calculate_age(start_date, end_date) -> int:
    """
    Calculates the difference in years between two dates.

    Args:
        start_date (str or pd.Timestamp): Start date.
        end_date (str or pd.Timestamp): End date.

    Returns:
        int: Difference in years.
    """
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    delta = relativedelta(end_date, start_date)
    return delta.years


# Classification by macropat categories
def classify_macropat(value: int, recursion_depth: int = 0) -> int:
    """
    Classifies a value into macropat categories based on predefined rules.

    Args:
        value (int): Value to classify.
        recursion_depth (int): Depth of recursion in case of correction. Default is 0.

    Returns:
        int: Corresponding macropat category, or None if invalid.
    """
    if 1 <= value <= 139:
        return 1
    elif 140 <= value <= 239:
        return 2
    elif 240 <= value <= 279:
        return 3
    elif 280 <= value <= 289:
        return 4
    elif 290 <= value <= 319:
        return 5
    elif 320 <= value <= 389:
        return 6
    elif 390 <= value <= 459:
        return 7
    elif 460 <= value <= 519:
        return 8
    elif 520 <= value <= 579:
        return 9
    elif 580 <= value <= 629:
        return 10
    elif 630 <= value <= 677:
        return 11
    elif 680 <= value <= 709:
        return 12
    elif 710 <= value <= 739:
        return 13
    elif 740 <= value <= 759:
        return 14
    elif 760 <= value <= 779:
        return 15
    elif 780 <= value <= 799:
        return 16
    elif 800 <= value <= 999:
        return 0
    else:
        # Handle potential errors in large numbers by taking only the first three digits
        if recursion_depth == 0:
            value = int(str(value)[:3])
            return classify_macropat(value, recursion_depth + 1)
        else:
            return None


# Simplified macropat classification
def classify_simple_macropat(value: int, recursion_depth: int = 0) -> int:
    """
    Classifies values into fewer macropat categories.

    Args:
        value (int): Value to classify.
        recursion_depth (int): Depth of recursion in case of correction. Default is 0.

    Returns:
        int: Simplified macropat category, or None if invalid.
    """
    if 1 <= value <= 139:
        return 1
    elif 140 <= value <= 239:
        return 2
    elif 240 <= value <= 279:
        return 2
    elif 280 <= value <= 999:
        return 2
    else:
        # Handle potential errors in large numbers
        if recursion_depth == 0:
            value = int(str(value)[:3])
            return classify_simple_macropat(value, recursion_depth + 1)
        else:
            return None


# Pathology classifications
def classify_cod_patology(cod: int) -> int:
    """
    Classifies pathology codes based on a predefined mapping.

    Args:
        cod (int): Pathology code to classify.

    Returns:
        int: Corresponding pathology category or 0 if invalid or unmapped.
    """
    if cod is None or np.isnan(cod):
        return 0

    mapping = {
        6: 1,
        10: 2,
        15: 3,
        53: 4,
        11: 5,
        4: 6,
        12: 7,
        5: 8,
        3: 9,
        52: 10,
        50: 11,
        1: 12,
        16: 13,
        8: 14,
        13: 15,
        7: 16
    }

    excluded_codes = {28, 20, 21, 14, 51, 9, 18, 22, 37}

    if cod in excluded_codes:
        return 0
    return mapping.get(cod, 0)


# Oxygen-related calculations
def calculate_pf(podt: float, fiod: float) -> float:
    """
    Calculate the PF ratio for oxygen levels.

    Args:
        podt (float): Blood oxygen content.
        fiod (float): Percentage of oxygen intake.

    Returns:
        float: PF ratio.
    """
    return (podt / fiod) * 100


def calculate_aadpod(part: float, fiod: float, pcod: float) -> float:
    """
    Calculate the alveolar-arterial oxygen difference.

    Args:
        part (float): Arterial oxygen pressure.
        fiod (float): Percentage of oxygen intake.
        pcod (float): Alveolar carbon dioxide pressure.

    Returns:
        float: Alveolar-arterial oxygen difference.
    """
    palv = ((fiod / 100) * 713) - (pcod / 0.83)  # Alveolar oxygen pressure
    return palv - part


def calculate_podt(po_vent: float, tc: float) -> float:
    """
    Calculate adjusted oxygen content.

    Args:
        po_vent (float): Ventilator oxygen pressure (PO21).
        tc (float): Body temperature.

    Returns:
        float: Adjusted oxygen content.
    """
    return po_vent * ((273 + 35) / (273 + tc))

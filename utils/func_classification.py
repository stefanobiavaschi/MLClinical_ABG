from typing import Optional

def class_macropat_V(value: int) -> int:
    """
    Classifies the value according to the defined rules for the "V" macro-category.
    
    Args:
        value (int): The value to classify.
    
    Returns:
        int: The corresponding category.
    """
    if 1 <= value <= 9:
        return 1
    elif value == 10:
        return 2
    elif value == 11:
        return 5
    elif value == 12:
        return 1
    elif value == 13:
        return 10
    elif value == 14:
        return 3
    elif value in {15, 17, 19}:
        return 16
    elif value == 16:
        return 2
    elif value == 18:
        return 3
    elif 20 <= value <= 29:
        return 11
    elif 30 <= value <= 39:
        return 16
    elif value == 40:
        return 5
    elif value in {41, 42, 43}:
        return 3
    elif value in {44, 45}:
        return 0
    elif value == 46:
        return 8
    elif value == 47:
        return 16
    elif 48 <= value <= 55:
        return 0
    elif value == 56:
        return 10
    elif 57 <= value <= 61:
        return 16
    elif value == 62:
        return 5
    elif value == 63:
        return 16
    elif value in {64, 66}:
        return 0
    elif value == 65:
        return 16
    elif 67 <= value <= 72:
        return 16
    elif 73 <= value <= 75:
        return 1
    elif value == 76:
        return 2
    elif value == 77:
        return 3
    elif value == 78:
        return 4
    elif value == 79:
        return 5
    elif value == 80:
        return 6
    elif value == 81:
        return 7
    elif value in {82, 83, 85, 86}:
        return {82: 16, 83: 14, 85: 13, 86: 10}[value]
    elif value == 84:
        return 3
    else:
        return 0


def class_macropat_letteremappate(letter: str, value: int, i: int = 0) -> Optional[int]:
    """
    Classifies a value based on a category letter and classification rules.

    Args:
        letter (str): The letter defining the category (e.g., "E", "V").
        value (int): The value to classify.
        i (int, optional): Counter for potential error corrections. Defaults to 0.
    
    Returns:
        Optional[int]: The corresponding category or None in case of an error.
    """
    if letter == "E":
        return 0
    elif letter == "V":
        return class_macropat_V(value)
    else:
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
            # Correct potential errors by considering only the first three digits
            if i == 0:
                value = int(str(value)[:3])
                return class_macropat_letteremappate(letter, value, i + 1)
            else:
                return None


def reduce_6class_letteremappate(class_macro: int) -> int:
    """
    Reduces macro categories into 6 main classes.

    Args:
        class_macro (int): The macro category to reduce.
    
    Returns:
        int: The reduced category into 6 classes.
    """
    mapping = {
        0: 0,  # TRM
        1: 1,  # INF
        2: 2,  # Generic
        3: 2,
        4: 5,  # EMO
        5: 2,
        6: 2,
        7: 3,  # CARD
        8: 4,  # RESP
        9: 2,
        10: 2,
        11: 2,
        12: 2,
        13: 2,
        14: 2,
        15: 2,
        16: 2,
    }
    return mapping.get(class_macro, 0)

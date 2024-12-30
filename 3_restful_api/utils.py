import numpy as np
from typing import List, Tuple


def validate_and_normalize(data: List[str]) -> Tuple[List[float], float, float]:
    if not all(isinstance(row, str) for row in data):
        raise ValueError("Each element in 'data' must be a string.")

    try:
        numbers = [float(num) for row in data for num in row.split()]
    except ValueError as e:
        raise ValueError(f"Data contains invalid elements: {e}")

    max_value = max(numbers)
    if max_value == 0:
        raise ValueError("Normalization cannot be performed because all elements are zero.")

    normalized = [num / max_value for num in numbers]
    avg_before = sum(numbers) / len(numbers)
    avg_after = sum(normalized) / len(normalized)

    return normalized, avg_before, avg_after
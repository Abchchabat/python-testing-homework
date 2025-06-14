from math import floor
from typing import List, Optional


def calculate_average(numbers: List[float]) -> Optional[float]:
    """
    Возвращает среднее арифметическое элементов списка чисел,
    округленное вниз до ближайшего целого.
    Пустой список возвращает None.
    """
    if not numbers:
        return None
    total_sum = sum(numbers)
    count = len(numbers)
    average_value = total_sum / count
    # Округляем вниз до ближайшего целого
    floored_avg = floor(average_value)
    print(f'Среднее значение ({numbers}) = {floored_avg}')
    return floored_avg

import pandas as pd
import numpy as np
from math import sqrt

from scipy.stats import chi2


chat_id = 6064443932 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    n = len(x)
    x = np.square(x).sum()
    
    return sqrt(x / 42 / chi2.ppf((p + 1) / 2, 2 * n)), sqrt(x / 42 / chi2.ppf((1 - p) / 2, 2 * n))

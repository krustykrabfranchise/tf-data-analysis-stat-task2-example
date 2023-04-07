import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    x = np.square(x).sum()
    
    return sqrt(x / 42 / chi.ppf((p + 1) / 2, 2 * len(x))), sqrt(x / 42 / chi.ppf((1 - p) / 2, 2 * len(x)))

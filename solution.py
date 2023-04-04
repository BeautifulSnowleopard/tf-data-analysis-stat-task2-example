import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 1897874711

def solution(p: float, x: np.array) -> tuple:
    # вычисляем степени свободы
    df = len(x) - 1

    # вычисляем выборочное среднее и выборочную смещенную оценку дисперсии
    mean = np.mean(x)
    var = np.var(x, ddof=1)

    # вычисляем левую и правую границы доверительного интервала
    left = np.sqrt(df * var / chi2.ppf(1 - p/2, df))
    right = np.sqrt(df * var / chi2.ppf(p/2, df))
    
    return (mean - left, mean + right)

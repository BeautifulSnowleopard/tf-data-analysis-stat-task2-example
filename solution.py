import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 1897874711

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    chi_sq = chi2.ppf(p, df=2*n)
    s = sum([d**2 for d in x])/n
    left = s*2*n/chi_sq
    right = s*2*n/chi2.ppf(1-p, df=2*n)
    return (left, right)

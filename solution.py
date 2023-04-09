import pandas as pd
import numpy as np
from scipy import stats

chat_id = 5481533510 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    otv = stats.ttest_1samp(x, 300).pvalue/2 >0.04 or x.mean() > 300
    return not otv

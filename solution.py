
import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 98268891 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    statistic, critical_values, pvalue = anderson_ksamp([x, y])
    alpha = 0.01
    if statistic > critical_values[2]:
        return True
    else:
        return False    

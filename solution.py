
import pandas as pd
import numpy as np
import scipy.stats as sps
from hyppo.ksample import MMD
from scipy import stats


chat_id = 98268891 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
      alpha = 0.01
      res = MMD(compute_kernel="rbf", gamma=1).test(x, y)[1]
      return res < alpha

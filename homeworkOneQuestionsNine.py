import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import numpy as np
import pandas as pd
import os
import json
import requests
import matplotlib.pyplot as plt
import openpyxl

data = pd.read_excel(
    r"C:\Users\MichaelTanner\OneDrive - Sandstone Group\Colorado School of Mines\Semester 3\Economics of Water\demandDataHwOne.xlsx"
)

print("yay")

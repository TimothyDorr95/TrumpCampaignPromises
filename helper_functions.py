import pandas as pd
import numpy as np
import os
import random


def read_and_show(path): 
    df = pd.read_parquet(path)
    print(df.shape)
    print(df.head())

    return df
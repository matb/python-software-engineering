import time
import typing
import re

import pandas as pd


def avg(l: list):
    return sum(l) / len(l)


def time_func(name: str, func: typing.Callable, df):
    def wrap():
        start = time.perf_counter_ns()
        _ = func(df)
        return time.perf_counter_ns() - start
    times = [wrap() for _ in range(1000)]
    print(f"{name} - avg time {(avg(times))} NS")
    print("-------")


def clean_using_pandas(data: pd.Series) -> pd.Series:
    """
    Method 2 to clean the data uses pandas native functions with which we can apply the transformation in parallel
    over the dataframe. As such it is more performant but maybe a little less intuitive
    """
    return data.str.replace("%", "", regex=False).str.replace(",", ".").astype(float)


def clean_using_apply(data: pd.Series) -> pd.Series:
    """
    Method 1 to clean the data is to use apply + a function to run over each individual record
    This method are usually easy to understand and to read
    but also consume a lot of time and computing power as they iterate row by row over the whole dataset
    """
    def convert_percent_to_numeric(s: str) -> float:
        return re.sub(r'[^\d.]', '', s)
    return data.apply(convert_percent_to_numeric)

def clean_using_loop(data: pd.Series) -> pd.Series:
    """
    Method 1 to clean the data is to use apply + a function to run over each individual record
    This method are usually easy to understand and to read
    but also consume a lot of time and computing power as they iterate row by row over the whole dataset
    """
    def convert_percent_to_numeric(s: str) -> float:
        return re.sub(r'[^\d.]', '', s)

    return [ convert_percent_to_numeric(row) for row in data]


if __name__ == '__main__':


    df = pd.read_csv("data/data.csv")

    time_func("Native", clean_using_pandas, df.score)
    time_func("Apply", clean_using_apply, df.score)
    time_func("Loop", clean_using_loop, df.score)

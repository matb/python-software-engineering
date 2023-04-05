import time
import typing

import pandas as pd


def apply_loop(df):
    score = 0

    for i in range(len(df)):
        score += df.iloc[i]['Score']

    return score / df.shape[0]


def score_iterrows(df):
    score = 0

    for index, row in df.iterrows():
        score += row['Score']

    return score / df.shape[0]


def score_itertuples(df):
    salary_sum = 0

    for row in df.itertuples():
        salary_sum += row[5]

    return salary_sum / df.shape[0]


def score_native(df):
    return df["Score"].mean()


def avg(l: list):
    return sum(l) / len(l)


def time_func(name: str, func: typing.Callable, df):
    def wrap():
        start = time.perf_counter_ns()
        _ = func(df)
        return time.perf_counter_ns() - start
    times = [wrap() for _ in range(100)]
    print(f"{name} - avg time {(avg(times))} NS")
    print("-------")


if __name__ == '__main__':

    df = pd.read_csv("data/data.csv")

    time_func("Native", score_native, df)
    time_func("Itertuples", score_itertuples, df)
    time_func("Iterrows", score_iterrows, df)
    time_func("Loop", apply_loop, df)
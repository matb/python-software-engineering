import time
import typing
import re

import pandas as pd


def avg(l: list):
    return sum(l) / len(l)


def time_func(name: str, func: typing.Callable, df):
    def wrap():
        df2 = df.copy(deep=True)
        start = time.perf_counter_ns()
        _ = func(df, df2 )
        return time.perf_counter_ns() - start
    times = [wrap() for _ in range(1000)]
    print(f"{name} - avg time {(avg(times))} NS")



def using_join(df1, df2):
    df1.join(df2, on="ID", lsuffix="df1_")


def using_merge(df1, df2 ):
    pd.merge_ordered(df, df2, on="ID")


def using_join_on_index(df1, df2):
    df.set_index("ID")
    df2.set_index("ID")
    df.join(df2, lsuffix="df1_")


def using_merge_by_order(df1,df2):
    pd.merge_ordered(df1, df2)


if __name__ == '__main__':

    df = pd.read_csv("data/data.csv")

    time_func("Simple Join", using_join, df)
    time_func("Simple Merge", using_merge, df)
    time_func("Join Index ", using_join_on_index, df)
    time_func("Merge Order ", using_merge_by_order, df)






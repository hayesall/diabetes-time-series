# Copyright 2022 Alexander L. Hayes

from pathlib import Path
import pandas as pd
import numpy as np

DIR = Path("Diabetes-Data")

KNOWN_CODES = set([
    33, 34, 35, 48, 57, 58, 59,
    60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
    70, 71, 72,
])

df = pd.read_csv(
    DIR.joinpath("data-27"),
    sep="\t",
    header=None,
)

for i in range(1, 70):

    file_number = f"{i:02}"

    df = pd.read_csv(
        DIR.joinpath(f"data-{file_number}"),
        sep="\t",
        header=None,
    )

    sym_diff = set(np.unique(df[2])) - KNOWN_CODES

    if sym_diff:
        print(file_number, sym_diff)

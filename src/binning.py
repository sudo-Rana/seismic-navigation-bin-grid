import pandas as pd


def generate_bin_grid(df, bin_size_x=25.0, bin_size_y=25.0):
    """
    Assign CMPs to bins and compute fold
    """
    x0 = df["CMP_X"].min()
    y0 = df["CMP_Y"].min()

    df["Bin_X"] = ((df["CMP_X"] - x0) / bin_size_x).astype(int)
    df["Bin_Y"] = ((df["CMP_Y"] - y0) / bin_size_y).astype(int)

    fold = (
        df.groupby(["Bin_X", "Bin_Y"])
        .size()
        .reset_index(name="Fold")
    )

    return df, fold

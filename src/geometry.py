def compute_cmp(df):
    """
    Compute CMP coordinates from source and receiver
    """
    df["CMP_X"] = (df["SX"] + df["GX"]) / 2.0
    df["CMP_Y"] = (df["SY"] + df["GY"]) / 2.0
    return df

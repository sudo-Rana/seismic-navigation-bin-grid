def validate_navigation(df):
    """
    Basic validation for seismic navigation
    """
    required = ["SX", "SY", "GX", "GY"]
    for col in required:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    if df.empty:
        raise ValueError("Navigation dataframe is empty")

    return True

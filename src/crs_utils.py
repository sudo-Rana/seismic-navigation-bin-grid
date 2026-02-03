from pyproj import Transformer


def transform_coordinates(df, x_col, y_col, src_epsg, tgt_epsg):
    """
    Transform coordinates between CRS
    """
    transformer = Transformer.from_crs(
        f"EPSG:{src_epsg}",
        f"EPSG:{tgt_epsg}",
        always_xy=True
    )

    xs, ys = transformer.transform(df[x_col].values, df[y_col].values)

    df[f"{x_col}_t"] = xs
    df[f"{y_col}_t"] = ys
    return df

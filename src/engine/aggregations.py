import pandas as pd


def get_grouped_production(
    df,
    crop,
    year,
    group_by="State_Name"
):
    """
    Common aggregation base.
    """

    result = (
        df[
            (df["Crop"] == crop) &
            (df["Crop_Year"] == year)
        ]
        .groupby(group_by)["Production"]
        .sum()
        .sort_values(ascending=False)
    )

    return result


def max_production(
    df,
    crop,
    year,
    group_by="State_Name"
):
    """
    Highest producer.
    """

    result = get_grouped_production(
        df,
        crop,
        year,
        group_by
    )

    return {
        "entity": result.index[0],
        "production": float(result.iloc[0])
    }


def min_production(
    df,
    crop,
    year,
    group_by="State_Name"
):
    """
    Lowest producer.
    """

    result = get_grouped_production(
        df,
        crop,
        year,
        group_by
    )

    result = result.sort_values()

    return {
        "entity": result.index[0],
        "production": float(result.iloc[0])
    }


def total_production(
    df,
    crop,
    year
):
    """
    Total production.
    """

    total = (
        df[
            (df["Crop"] == crop) &
            (df["Crop_Year"] == year)
        ]["Production"]
        .sum()
    )

    return {
        "total_production": float(total)
    }


def average_production(
    df,
    crop,
    year
):
    """
    Average production.
    """

    avg = (
        df[
            (df["Crop"] == crop) &
            (df["Crop_Year"] == year)
        ]["Production"]
        .mean()
    )

    return {
        "average_production": float(avg)
    }


def top_n_producers(
    df,
    crop,
    year,
    n=10,
    group_by="State_Name"
):
    """
    Top N producers.
    """

    result = get_grouped_production(
        df,
        crop,
        year,
        group_by
    )

    return result.head(n)

def distinct_values(
    df,
    column
):
    """
    Return unique values from a column.
    """

    return sorted(
        df[column]
        .dropna()
        .unique()
        .tolist()
    )
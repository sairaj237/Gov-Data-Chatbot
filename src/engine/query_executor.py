from src.engine.aggregations import (
    max_production,
    min_production,
    total_production,
    average_production,
    top_n_producers,
    distinct_values
)


def production_trend(
    df,
    crop,
    state
):
    """
    Generate production trend over years.
    """

    trend = (
        df[
            (df["Crop"] == crop) &
            (df["State_Name"] == state)
        ]
        .groupby("Crop_Year")["Production"]
        .sum()
        .reset_index()
    )

    return trend


def execute_query(
    df,
    query
):
    """
    Main query execution router.
    """

    operation = query["operation"]

    crop = query.get("crop")

    year = query.get("year")

    if operation == "max":

        return max_production(
            df=df,
            crop=crop,
            year=year
        )

    elif operation == "min":

        return min_production(
            df=df,
            crop=crop,
            year=year
        )

    elif operation == "sum":

        return total_production(
            df=df,
            crop=crop,
            year=year
        )

    elif operation == "avg":

        return average_production(
            df=df,
            crop=crop,
            year=year
        )

    elif operation == "top_n":

        return top_n_producers(
            df=df,
            crop=crop,
            year=year,
            n=query.get("n", 10)
        )

    elif operation == "trend":

        return production_trend(
            df=df,
            crop=crop,
            state=query["state"]
        )

    elif operation == "distinct":

        return distinct_values(
            df=df,
            column=query["column"]
        )

    else:

        raise ValueError(
            f"Unsupported operation: {operation}"
        )
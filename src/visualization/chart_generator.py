from pathlib import Path
from src.utils.helpers import (
    generate_timestamp,
    ensure_directory
)

from src.visualization.chart_types import (
    create_line_chart,
    create_top_n_chart,
    create_max_min_chart
)


CHART_OUTPUT_DIR = "outputs/charts"


def ensure_chart_directory():
    """
    Create chart directory if missing.
    """

    ensure_directory(CHART_OUTPUT_DIR)


def generate_chart_filename(
    operation
):
    """
    Generate unique chart filename.
    """

    timestamp = generate_timestamp()

    return (
        f"{operation}_{timestamp}.png"
    )


def save_chart(
    fig,
    filename
):
    """
    Save matplotlib figure.
    """

    ensure_chart_directory()

    chart_path = (
        Path(CHART_OUTPUT_DIR)
        / filename
    )

    fig.savefig(
        chart_path,
        bbox_inches="tight"
    )

    return str(chart_path)


def generate_chart(
    query,
    result
):
    """
    Main chart router.
    """

    operation = query["operation"]

    crop = query.get("crop", "")

    year = query.get("year", "")

    if operation == "trend":

        fig = create_line_chart(
            trend_df=result,
            crop=crop,
            state=query["state"]
        )

    elif operation == "top_n":

        fig = create_top_n_chart(
            top_n_df=result,
            crop=crop,
            year=year
        )

    elif operation == "max":

        fig = create_max_min_chart(
            entity=result["entity"],
            production=result["production"],
            crop=crop,
            year=year,
            operation="max"
        )

    elif operation == "min":

        fig = create_max_min_chart(
            entity=result["entity"],
            production=result["production"],
            crop=crop,
            year=year,
            operation="min"
        )

    else:

        return None

    filename = generate_chart_filename(
        operation
    )

    chart_path = save_chart(
        fig,
        filename
    )

    return chart_path
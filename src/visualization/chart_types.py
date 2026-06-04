import matplotlib.pyplot as plt


def create_line_chart(
    trend_df,
    crop,
    state
):
    """
    Create trend line chart.
    """

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    ax.plot(
        trend_df["Crop_Year"],
        trend_df["Production"]
    )

    ax.set_title(
        f"{crop} Production Trend - {state}"
    )

    ax.set_xlabel("Year")

    ax.set_ylabel("Production")

    ax.grid(True)

    return fig


def create_bar_chart(
    data,
    title
):
    """
    Create bar chart from Series.
    """

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    data.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(title)

    ax.set_xlabel("Category")

    ax.set_ylabel("Production")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    return fig


def create_horizontal_bar_chart(
    data,
    title
):
    """
    Create horizontal bar chart.
    """

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    data.sort_values().plot(
        kind="barh",
        ax=ax
    )

    ax.set_title(title)

    ax.set_xlabel("Production")

    ax.set_ylabel("State")

    plt.tight_layout()

    return fig


def create_top_n_chart(
    top_n_df,
    crop,
    year
):
    """
    Top N producers chart.
    """

    title = (
        f"Top Producers of "
        f"{crop} ({year})"
    )

    return create_horizontal_bar_chart(
        top_n_df,
        title
    )


def create_max_min_chart(
    entity,
    production,
    crop,
    year,
    operation
):
    """
    Single value bar chart.
    """

    fig, ax = plt.subplots(
        figsize=(6, 4)
    )

    ax.bar(
        [entity],
        [production]
    )

    ax.set_title(
        f"{operation.upper()} "
        f"{crop} Production ({year})"
    )

    ax.set_ylabel("Production")

    plt.tight_layout()

    return fig
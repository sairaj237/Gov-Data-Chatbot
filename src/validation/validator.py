SUPPORTED_OPERATIONS = [
    "max",
    "min",
    "sum",
    "avg",
    "top_n",
    "trend"
]


def validate_query(
    query,
    valid_states,
    valid_crops,
    min_year,
    max_year
):
    """
    Validate parsed query before execution.
    """

    if "operation" not in query:

        return (
            False,
            "Missing operation."
        )

    operation = query["operation"]

    if operation not in SUPPORTED_OPERATIONS:

        return (
            False,
            f"Unsupported operation: {operation}"
        )

    if "crop" in query:

        if query["crop"] not in valid_crops:

            return (
                False,
                f"Crop '{query['crop']}' not found."
            )

    if "state" in query:

        if query["state"] not in valid_states:

            return (
                False,
                f"State '{query['state']}' not found."
            )

    if "year" in query:

        year = query["year"]

        if not isinstance(year, int):

            return (
                False,
                "Year must be an integer."
            )

        if year < min_year or year > max_year:

            return (
                False,
                f"Year must be between {min_year} and {max_year}."
            )

    if operation == "top_n":

        n = query.get("n", 10)

        if not isinstance(n, int):

            return (
                False,
                "n must be an integer."
            )

        if n <= 0:

            return (
                False,
                "n must be greater than 0."
            )

    return (
        True,
        "Validation successful."
    )
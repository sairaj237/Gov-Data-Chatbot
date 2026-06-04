def generate_explanation(
    question,
    query,
    result
):

    operation = query["operation"]

    crop = query.get("crop", "")

    year = query.get("year", "")

    if operation == "max":

        return f"""
Question:
{question}

Analysis:
Production data was grouped by state and aggregated.

Answer:
{result['entity']} produced the highest amount of
{crop} in {year}.

Production:
{result['production']:,.0f}
"""

    elif operation == "min":

        return f"""
Question:
{question}

Analysis:
Production data was grouped by state and aggregated.

Answer:
{result['entity']} produced the lowest amount of
{crop} in {year}.

Production:
{result['production']:,.0f}
"""

    elif operation == "sum":

        return f"""
Question:
{question}

Answer:
Total {crop} production in {year}

Value:
{result['total_production']:,.0f}
"""

    elif operation == "avg":

        return f"""
Question:
{question}

Answer:
Average {crop} production in {year}

Value:
{result['average_production']:,.2f}
"""

    elif operation == "top_n":

        return f"""
Question:
{question}

Answer:
Top producing states generated successfully.
"""

    elif operation == "trend":

        return f"""
Question:
{question}

Answer:
Trend chart generated successfully.
"""

    return str(result)
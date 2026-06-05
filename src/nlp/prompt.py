def get_dataset_context():
    """
    Static dataset information.
    """

    return """
Dataset Columns:

State_Name
District_Name
Crop_Year
Season
Crop
Area
Production

Column Meanings:

State_Name = State
District_Name = District
Crop_Year = Year
Season = Crop Season
Crop = Crop Name
Area = Cultivated Area
Production = Crop Production

Supported Operations:

max
min
sum
avg
top_n
trend
distinct
Return ONLY valid JSON.
"""


def get_examples():
    """
    Few-shot examples for the LLM.
    """

    return """
Question:
Which state produced the most rice in 2014?

Output:
{
  "operation":"max",
  "crop":"Rice",
  "year":2014
}

Question:
Which state produced the least rice in 2014?

Output:
{
  "operation":"min",
  "crop":"Rice",
  "year":2014
}

Question:
What was the total rice production in 2014?

Output:
{
  "operation":"sum",
  "crop":"Rice",
  "year":2014
}

Question:
What was the average rice production in 2014?

Output:
{
  "operation":"avg",
  "crop":"Rice",
  "year":2014
}

Question:
Top 10 states by rice production in 2014

Output:
{
  "operation":"top_n",
  "crop":"Rice",
  "year":2014,
  "n":10
}

Question:
Show rice production trend in Punjab

Output:
{
  "operation":"trend",
  "crop":"Rice",
  "state":"Punjab"
}
Question:
What are the different crops?

Output:
{
  "operation":"distinct",
  "column":"Crop"
}

Question:
List all crop types.

Output:
{
  "operation":"distinct",
  "column":"Crop"
}

Question:
What seasons exist in the dataset?

Output:
{
  "operation":"distinct",
  "column":"Season"
}
"""


def build_prompt(
    question,
    valid_states,
    valid_crops
):
    """
    Build final prompt for query parsing.
    """

    dataset_context = get_dataset_context()

    examples = get_examples()

    prompt = f"""
{dataset_context}

Available States:
{valid_states}

Available Crops:
{valid_crops}

{examples}

Question:
{question}

Return ONLY JSON.
"""

    return prompt
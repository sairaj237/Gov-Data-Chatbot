import pandas as pd
import json
from pathlib import Path


def load_data(data_path="data/crop_production.csv"):
    """
    Load and clean crop production dataset.
    """

    df = pd.read_csv(data_path)

    # Remove missing production records
    df = df.dropna(subset=["Production"])

    # Clean string columns
    string_cols = [
        "State_Name",
        "District_Name",
        "Season",
        "Crop"
    ]

    for col in string_cols:
        df[col] = df[col].astype(str).str.strip()

    return df


def generate_metadata(df):
    """
    Generate dataset metadata.
    """

    metadata = {
        "State_Name": {
            "type": "categorical",
            "unique_values": df["State_Name"].nunique()
        },
        "District_Name": {
            "type": "categorical",
            "unique_values": df["District_Name"].nunique()
        },
        "Crop_Year": {
            "type": "numeric",
            "min": int(df["Crop_Year"].min()),
            "max": int(df["Crop_Year"].max())
        },
        "Season": {
            "type": "categorical",
            "values": sorted(
                df["Season"].unique().tolist()
            )
        },
        "Crop": {
            "type": "categorical",
            "unique_values": df["Crop"].nunique()
        },
        "Area": {
            "type": "numeric"
        },
        "Production": {
            "type": "numeric"
        }
    }

    return metadata


def save_metadata(
    metadata,
    output_path="metadata/schema.json"
):
    """
    Save metadata JSON.
    """

    Path(output_path).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(output_path, "w") as f:
        json.dump(
            metadata,
            f,
            indent=4
        )


def generate_dataset_summary(df):
    """
    Generate dataset summary text.
    """

    summary = f"""
Dataset Name: Crop Production

Rows: {len(df)}

States: {df['State_Name'].nunique()}

Districts: {df['District_Name'].nunique()}

Crops: {df['Crop'].nunique()}

Year Range:
{df['Crop_Year'].min()} - {df['Crop_Year'].max()}

Columns:
{list(df.columns)}
"""

    return summary


def save_dataset_summary(
    summary,
    output_path="metadata/dataset_summary.txt"
):
    """
    Save summary text file.
    """

    Path(output_path).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(output_path, "w") as f:
        f.write(summary)


def get_valid_states(df):
    """
    Return list of valid states.
    """

    return sorted(
        df["State_Name"]
        .dropna()
        .unique()
        .tolist()
    )


def get_valid_crops(df):
    """
    Return list of valid crops.
    """

    return sorted(
        df["Crop"]
        .dropna()
        .unique()
        .tolist()
    )
from src.data_loader.loader import (
    load_data,
    get_valid_states,
    get_valid_crops
)

from src.validation.validator import (
    validate_query
)


df = load_data()

VALID_STATES = get_valid_states(df)
VALID_CROPS = get_valid_crops(df)

MIN_YEAR = int(df["Crop_Year"].min())
MAX_YEAR = int(df["Crop_Year"].max())


query = {
    "operation": "max",
    "crop": "Rice",
    "year": 2014
}

valid, message = validate_query(
    query,
    VALID_STATES,
    VALID_CROPS,
    MIN_YEAR,
    MAX_YEAR
)

print(valid)
print(message)
from src.data_loader.loader import (
    load_data,
    get_valid_states,
    get_valid_crops
)

from src.nlp.query_parser import (
    parse_query
)

df = load_data()

VALID_STATES = get_valid_states(df)
VALID_CROPS = get_valid_crops(df)

query = parse_query(
    question="Which state produced the most wheat in 2012?",
    valid_states=VALID_STATES,
    valid_crops=VALID_CROPS
)

print(query)
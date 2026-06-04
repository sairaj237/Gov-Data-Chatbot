from src.data_loader.loader import load_data

from src.engine.aggregations import (
    max_production,
    min_production,
    total_production,
    average_production,
    top_n_producers
)
from src.engine.query_executor import (
    execute_query
)
df = load_data()

print(
    max_production(
        df,
        crop="Rice",
        year=2014
    )
)

print(
    min_production(
        df,
        crop="Rice",
        year=2014
    )
)

print(
    total_production(
        df,
        crop="Rice",
        year=2014
    )
)

print(
    average_production(
        df,
        crop="Rice",
        year=2014
    )
)

print(
    top_n_producers(
        df,
        crop="Rice",
        year=2014,
        n=5
    )
)
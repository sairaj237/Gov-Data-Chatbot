from src.data_loader.loader import load_data

from src.engine.aggregations import (
    top_n_producers
)

from src.visualization.chart_types import (
    create_top_n_chart
)

df = load_data()

top_states = top_n_producers(
    df,
    crop="Rice",
    year=2014,
    n=10
)

fig = create_top_n_chart(
    top_states,
    crop="Rice",
    year=2014
)

fig.show()
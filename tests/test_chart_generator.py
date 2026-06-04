from src.data_loader.loader import load_data

from src.engine.query_executor import (
    execute_query
)

from src.visualization.chart_generator import (
    generate_chart
)

df = load_data()


query = {
    "operation": "top_n",
    "crop": "Rice",
    "year": 2014,
    "n": 10
}

result = execute_query(
    df,
    query
)

chart_path = generate_chart(
    query,
    result
)

print(chart_path)
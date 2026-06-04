from src.explanation.explain import (
    generate_explanation
)

query = {
    "operation": "max",
    "crop": "Rice",
    "year": 2014
}

result = {
    "entity": "Punjab",
    "production": 11107000
}

print(
    generate_explanation(
        question="Which state produced the most rice in 2014?",
        query=query,
        result=result
    )
)
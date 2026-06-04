# src/engine/filters.py

import pandas as pd


class DataFilter:
    @staticmethod
    def apply(df: pd.DataFrame, conditions: list):
        """
        conditions:
        [
            {"column": "year", "op": "==", "value": 2023},
            {"column": "state", "op": "==", "value": "Maharashtra"}
        ]
        """

        result = df.copy()

        for cond in conditions:
            col = cond["column"]
            op = cond["op"]
            val = cond["value"]

            if op == "==":
                result = result[result[col] == val]

            elif op == "!=":
                result = result[result[col] != val]

            elif op == ">":
                result = result[result[col] > val]

            elif op == "<":
                result = result[result[col] < val]

            elif op == ">=":
                result = result[result[col] >= val]

            elif op == "<=":
                result = result[result[col] <= val]

        return result
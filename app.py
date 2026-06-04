import streamlit as st
import pandas as pd

from src.data_loader.loader import (
    load_data,
    get_valid_states,
    get_valid_crops
)

from src.nlp.query_parser import (
    parse_query
)

from src.validation.validator import (
    validate_query
)

from src.engine.query_executor import (
    execute_query
)

from src.explanation.explain import (
    generate_explanation
)

from src.visualization.chart_generator import (
    generate_chart
)


# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Government Data Chatbot",
    page_icon="📊",
    layout="wide"
)


# ----------------------------------
# DATA LOADING
# ----------------------------------

@st.cache_data
def initialize_data():

    df = load_data()

    valid_states = get_valid_states(df)

    valid_crops = get_valid_crops(df)

    min_year = int(
        df["Crop_Year"].min()
    )

    max_year = int(
        df["Crop_Year"].max()
    )

    return (
        df,
        valid_states,
        valid_crops,
        min_year,
        max_year
    )


(
    df,
    VALID_STATES,
    VALID_CROPS,
    MIN_YEAR,
    MAX_YEAR
) = initialize_data()


# ----------------------------------
# SIDEBAR
# ----------------------------------

st.sidebar.title(
    "Government Data Chatbot"
)

st.sidebar.markdown(
    """
### Example Questions

- Which state produced the most rice in 2014?

- Which state produced the least wheat in 2012?

- What was the total rice production in 2014?

- What was the average wheat production in 2012?

- Top 10 states by rice production in 2014

- Show rice production trend in Punjab
"""
)


# ----------------------------------
# HEADER
# ----------------------------------

st.title(
    "📊 Government Data Chatbot"
)

st.write(
    """
Ask questions about crop production data using natural language.
"""
)


# ----------------------------------
# INPUT
# ----------------------------------

question = st.text_input(
    "Ask a question"
)


# ----------------------------------
# PROCESS QUERY
# ----------------------------------

if st.button("Submit"):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        try:

            with st.spinner(
                "Analyzing..."
            ):

                query = parse_query(
                    question=question,
                    valid_states=VALID_STATES,
                    valid_crops=VALID_CROPS
                )

                st.subheader(
                    "Parsed Query"
                )

                st.json(query)

                valid, message = validate_query(
                    query=query,
                    valid_states=VALID_STATES,
                    valid_crops=VALID_CROPS,
                    min_year=MIN_YEAR,
                    max_year=MAX_YEAR
                )

                if not valid:

                    st.error(message)

                else:

                    result = execute_query(
                        df=df,
                        query=query
                    )

                    explanation = (
                        generate_explanation(
                            question=question,
                            query=query,
                            result=result
                        )
                    )

                    st.subheader(
                        "Explanation"
                    )

                    st.success(
                        explanation
                    )

                    st.subheader(
                        "Result"
                    )

                    if isinstance(
                        result,
                        pd.DataFrame
                    ):

                        st.dataframe(
                            result
                        )

                    elif isinstance(
                        result,
                        pd.Series
                    ):

                        st.dataframe(
                            result
                        )

                    else:

                        st.json(
                            result
                        )

                    chart_path = (
                        generate_chart(
                            query=query,
                            result=result
                        )
                    )

                    if chart_path:

                        st.subheader(
                            "Visualization"
                        )

                        st.image(
                            chart_path
                        )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )
# Gov Data Chatbot

An LLM-powered natural language analytics system that enables users to query Indian crop production data using plain English and receive computed answers, visualizations, and explanations.

## Overview

Government datasets often contain valuable information but are difficult for non-technical users to analyze. This project bridges that gap by allowing users to ask questions in natural language and automatically generating accurate, data-backed answers from a real agricultural dataset.

Example questions:

* Which state produced the most rice in 2014?
* Which state produced the least wheat in 2012?
* What was the total rice production in 2014?
* What was the average wheat production in 2012?
* Show rice production trend in Punjab.
* Top 10 states by rice production in 2014.

The system converts natural language into structured queries, executes computations on the dataset, generates visualizations, and provides human-readable explanations.

---

## Features

### Natural Language Querying

Users can ask questions in plain English without knowing SQL or Pandas.

### LLM-Based Query Parsing

Questions are converted into structured JSON queries using an LLM via OpenRouter.

Example:

Input:

Which state produced the most wheat in 2012?

Generated Query:

{
"operation": "max",
"crop": "Wheat",
"year": 2012
}

### Real Data Computation

All answers are computed from the dataset using Pandas.

No numbers are generated from the model's prior knowledge.

### Supported Operations

* Maximum production
* Minimum production
* Total production
* Average production
* Top N producers
* Production trends over time

### Data Validation

The system validates:

* Crop names
* State names
* Year ranges
* Supported operations

### Visualizations

Automatically generates:

* Trend line charts
* Top-N bar charts
* Comparison charts

### Explainable Results

Every answer includes:

* Parsed query
* Computation details
* Human-readable explanation

### Out-of-Scope Handling

Questions unrelated to the dataset are refused gracefully.

Example:

Who is the Prime Minister of India?

Response:

This question cannot be answered using the selected crop production dataset.

---

## Dataset

### Dataset Name

Crop Production in India

### Source

https://aikosh.indiaai.gov.in/home/datasets/details/agriculture_production_of_different_foodgrains_from_year_2003_to_2014_at_all_india_level.html

### Dataset Columns

* State_Name
* District_Name
* Crop_Year
* Season
* Crop
* Area
* Production

### Data Cleaning

* Removed records with missing production values
* Standardized categorical fields
* Trimmed whitespace
* Validated year ranges

---

## System Architecture

User Question

↓

Streamlit Interface

↓

LLM Query Parser (OpenRouter)

↓

Structured JSON Query

↓

Validation Layer

↓

Pandas Query Engine

↓

Aggregation Functions

↓

Visualization Layer

↓

Explanation Generator

↓

Final Answer

---

## Project Structure

```text
gov-data-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── crop_production.csv
│
├── metadata/
│   ├── schema.json
│   └── dataset_summary.txt
│
├── src/
│   ├── data_loader/
│   ├── nlp/
│   ├── engine/
│   ├── visualization/
│   ├── explanation/
│   ├── validation/
│   └── utils/
│
├── outputs/
│   ├── charts/
│   └── logs/
│
├── notebooks/
│   └── exploration.ipynb
│
└── tests/
```

## Technology Stack

### Frontend

* Streamlit

### LLM Layer

* OpenRouter
* Google Gemma 4

### Data Processing

* Pandas

### Visualization

* Matplotlib

### Environment Management

* Python Dotenv



---

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd gov-data-chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file:

```env
OPENROUTER_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

## Example Queries

### Maximum Production

Which state produced the most rice in 2014?

### Minimum Production

Which state produced the least wheat in 2012?

### Total Production

What was the total rice production in 2014?

### Average Production

What was the average wheat production in 2012?

### Top Producers

Top 10 states by rice production in 2014.

### Trend Analysis

Show rice production trend in Punjab.

---

## Evaluation Set

| Question                                     | Expected Result      |
| -------------------------------------------- | -------------------- |
| Which state produced the most rice in 2014?  | Highest producer     |
| Which state produced the most wheat in 2012? | Uttar Pradesh        |
| What was total rice production in 2014?      | Numeric output       |
| What was average wheat production in 2012?   | Numeric output       |
| Top 10 states by rice production in 2014     | Ranked table + chart |
| Show rice production trend in Punjab         | Trend chart          |
| Which state produced least wheat in 2012?    | Lowest producer      |
| Who is Prime Minister of India?              | Out-of-scope refusal |

---

## Correctness and Trust

The system does not generate answers directly from the language model.

Instead:

1. User question is converted into structured JSON.
2. JSON is validated.
3. Real computations are executed using Pandas.
4. Results are returned from dataset values.
5. Charts and explanations are generated from computed outputs.

This approach significantly reduces hallucination risk.

---

## Security Considerations

The system does not execute arbitrary model-generated Python code.

Instead, the model is constrained to generate structured query objects which are validated before execution.

Benefits:

* Prevents arbitrary code execution
* Improves reliability
* Easier auditing
* Safer deployment for government use cases

---

## Current Limitations

* Single dataset support
* Limited query operations
* No cross-dataset joins
* No user authentication
* Depends on external LLM API
* Limited support for ambiguous questions

---

## Future Improvements

* Multi-dataset support
* SQL backend
* Agent-based query planning
* Retrieval-Augmented Generation (RAG)
* User authentication and audit logging
* Advanced visual analytics
* Government-scale deployment architecture

---

## Screenshots

Add screenshots here:

* Main application
* Query execution
* Trend visualization
* Out-of-scope handling

---

## Author

Sairaj Magdum


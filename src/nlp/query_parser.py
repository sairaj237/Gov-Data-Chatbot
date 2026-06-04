import os
import json
import re

from dotenv import load_dotenv
from openai import OpenAI

from src.nlp.prompt import build_prompt


load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def clean_llm_response(content):
    """
    Remove markdown code fences.
    """

    content = content.strip()

    content = re.sub(
        r"^```json\s*",
        "",
        content
    )

    content = re.sub(
        r"^```\s*",
        "",
        content
    )

    content = re.sub(
        r"\s*```$",
        "",
        content
    )

    return content.strip()


def extract_json(content):
    """
    Extract JSON object from LLM response.
    """

    match = re.search(
        r"\{.*\}",
        content,
        re.DOTALL
    )

    if not match:
        raise ValueError(
            f"No JSON found in response:\n{content}"
        )

    return match.group(0)


def parse_query(
    question,
    valid_states,
    valid_crops,
    model="google/gemma-4-31b-it:free"
):
    """
    Convert natural language question
    into structured query JSON.
    """

    prompt = build_prompt(
        question=question,
        valid_states=valid_states,
        valid_crops=valid_crops
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    print("\nRAW RESPONSE:")
    print(content)

    if not content:
        raise ValueError(
            "Model returned empty response."
        )

    content = clean_llm_response(content)

    json_text = extract_json(content)

    try:

        query = json.loads(json_text)

        return query

    except json.JSONDecodeError:

        print("\nFAILED JSON:")
        print(json_text)

        raise
from src.nlp.prompt import build_prompt

prompt = build_prompt(
    question="Which state produced the most wheat in 2012?",
    valid_states=["Punjab", "Bihar"],
    valid_crops=["Rice", "Wheat"]
)

print(prompt)
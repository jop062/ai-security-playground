# AI Security Playground

AI Security Playground is a hands-on demo project that shows how LLM applications can be attacked with prompt injection and how simple guardrails can reduce risk.

## What it demonstrates

- Prompt injection attacks
- Prompt leak attempts
- Credential and secret extraction attempts
- Role override attacks
- Guardrail-based blocking and grounded-answer mode
- Risk scoring and rule-based detection

## Why this project matters

Enterprise AI systems are increasingly connected to:
- HR systems
- IT service management tools
- internal knowledge bases
- automation workflows

That means prompt injection and unsafe tool use become real security problems. This project demonstrates how to build a safer AI workflow by comparing insecure and secured responses side by side.

## Features

- Streamlit web interface
- Sample attack prompts
- Risk scoring engine
- Triggered rule reporting
- Vulnerable vs secure response comparison
- Grounded-answer mode for safe topics

## Tech stack

- Python
- Streamlit
- Rule-based detection
- Basic secure response filtering

## Project structure

```text
ai-security-playground/
├── app/
│   └── streamlit_app.py
├── src/
│   ├── config.py
│   ├── detector.py
│   ├── filters.py
│   ├── prompts.py
│   ├── simulator.py
│   └── utils.py
├── data/
│   └── sample_attacks.json
├── requirements.txt
└── README.md

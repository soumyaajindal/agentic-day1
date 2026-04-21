# LLM Context Failure vs Context Fix Demo

This project demonstrates the difference between **stateless LLM calls** and **context-aware message-based interactions** using a Google Generative AI model.

It shows how missing conversation history leads to context failure and how message-based invocation resolves it.
---

## 📁 Project Structure
.
├── app.py
└── README.md

## 🔐 Environment Setup
This project uses Google Generative AI. Set your API key (GOOGLE_API_KEY) as an environment variable:

## 🔒 Security Note

- Do **NOT** commit your `.env` file to the repository.
- The `.env` file contains sensitive information such as API keys.

### ✅ Best Practices
- Add `.env` to your `.gitignore` file

### Install Dependencies

pip install -r requirements.txt

### How To Run

python app.py

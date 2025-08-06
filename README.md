# Langchain With Langsmith

This project demonstrates how to use LangChain with LangSmith and Google Gemini to extract structured user profile information from free-form text.

## Features

- Uses [LangChain](https://github.com/langchain-ai/langchain) for prompt management and LLM orchestration.
- Integrates [LangSmith](https://smith.langchain.com/) for tracing and experiment tracking.
- Utilizes [Google Gemini](https://ai.google.dev/) via `langchain_google_genai`.
- Extracts structured data (name, favorite programming language, years of experience) from user input using Pydantic models.

## Project Structure

```
Langchain With Langsmith/
├── config.py
├── main.py
├── models.py
├── prompt_builder.py
├── README.md
```

- `config.py`: API keys and LangSmith environment setup.
- `main.py`: Main script to run the extraction workflow.
- `models.py`: Pydantic model for structured output.
- `prompt_builder.py`: Builds the prompt for the LLM.

## Getting Started

1. **Install dependencies**  
   Make sure you have Python 3.10+ and install required packages:
   ```sh
   pip install langchain langsmith langchain_google_genai pydantic
   ```

2. **Set your API keys**  
   Update `config.py` with your own Google Gemini and LangSmith API keys.

3. **Run the script**
   ```sh
   python main.py
   ```

## Example Usage

```
Tell me about yourself: John Doe, loves Python, 5 years experience

Extracted Profile:
{
  "name": "John Doe",
  "favorite_language": "Python",
  "years_experience": 5.0
}
```

## License

MIT

## References

- [LangChain Documentation](https://python.langchain.com/)
- [LangSmith Documentation](https://docs.smith.langchain.com/)
-

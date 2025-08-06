from config import google_studio_api_key
from models import UserProfile
from prompt_builder import get_prompt
from langchain_google_genai import ChatGoogleGenerativeAI

def main():
    prompt = get_prompt()
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        api_key=google_studio_api_key
    )
    structured_model = model.with_structured_output(UserProfile)

    human_message = input("Tell me about yourself: ")
    messages = prompt.format_messages(human_message=human_message)
    user_profile = structured_model.invoke(messages)

    print("\nExtracted Profile:")
    print(user_profile.model_dump_json(indent=2))

if __name__ == "__main__":
    main()
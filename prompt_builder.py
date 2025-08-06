from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

def get_prompt():
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You're a expert Keyword extraction assistant; collect name, favorite language, and years of experience; output JSON only."
        ),
        HumanMessagePromptTemplate.from_template("{human_message}")
    ])
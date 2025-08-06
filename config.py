import os

google_studio_api_key = "AIzaSyC-l8OhjmN8Ce8YOLsyR-i_bX2FY33jE2M"
langsmith_api_key = "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"

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = langsmith_api_key
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGSMITH_PROJECT"] = "test"
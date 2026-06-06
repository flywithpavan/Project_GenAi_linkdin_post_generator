from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from groq import AuthenticationError

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY is missing. Add it to the .env file in this project.")

llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.3-70b-versatile")


if __name__ == "__main__":
    try:
        response = llm.invoke("Two most important ingredients in samosa are ")
        print(response.content)
    except AuthenticationError as exc:
        raise SystemExit(
            "Groq rejected the API key in your .env file. "
            "Create a new key at https://console.groq.com/keys and replace GROQ_API_KEY."
        ) from exc




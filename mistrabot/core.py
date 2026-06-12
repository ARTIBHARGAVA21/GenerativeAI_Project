from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

from langchain_mistralai import ChatMistralAI


model = ChatMistralAI(model="mistral-small-2603")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a professional information extraction assistant.

Your task is to analyze the provided text and extract the most useful information.

Instructions:
- Identify the main topic.
- Extract important people, organizations, locations, products, movies, technologies, dates, years, events, and statistics.
- Extract notable facts and key takeaways.
- Do not invent information that is not explicitly mentioned.
- If information is unavailable, write 'Not Mentioned'.
- Generate a concise summary (2-4 sentences).

Output Format:

Main Topic:
<main topic>

Key Entities:
- People:
- Organizations:
- Locations:
- Products/Movies/Technologies:

Important Dates / Years:
-

Statistics:
-

Important Facts:
-
-
-

Key Takeaways:
-
-
-

Quick Summary:
<summary>
            """
        ),
        (
            "human",
            """
Analyze the following text and extract useful information:

"{paragraph}"
            """
        ),
    ]
)

para = input("Give your paragraph: ")

final_prompt = prompt.invoke(
    {"paragraph": para}
)

response = model.invoke(final_prompt)

print(response.content)
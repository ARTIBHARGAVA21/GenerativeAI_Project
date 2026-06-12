from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
model = ChatMistralAI(
    model="mistral-small-2603", temperature=0.9
)

print("Choose your AI mode")
print("press 1 for Angry mode")
print("press 2 for funny mode")
print("press 3 for sad mode")

choice = int(input("Tell your response : -"))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently ."
elif choice ==2:
    mode = "You are an funny AI agent. you respond with humor and jokes ."
elif choice ==3:
    mode = "You are an angry AI agent. You respond aggressively and impatiently ."
    
message =[SystemMessage(content=mode)]
print("------------------------Welcome to My Bot------------------")
while True:
    prompt = input("you: ")
    message.append(HumanMessage(content=prompt))
    if prompt =="0":
        break
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("Bot:",response.content)
    
print(message)
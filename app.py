from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.5-flash-lite")

resp1 = model.invoke("We are building an AI system for processing medical insurance claims?")
print(f"First Response ------{resp1}")

print("========================================")
resp2 = model.invoke("What are the main risks in this system?")
print(f"Second Response ------{resp2}")

# Explanation:
# The second question may fail or behave inconsistently without conversation history because LLMs are stateless by design/nature.
# This means each invocation is independent and does not retain prior context.So, in the second call, the model does not know what "this system" refers to unless the previous message is explicitly provided again.
# Therefore, to maintain coherence, conversation history must be persisted and passed along with each request.

messages = [
    SystemMessage(content="You are a senior AI architect reviewing production systems."),
    HumanMessage(content="We are building an AI system for processing medical insurance claims."),
    HumanMessage(content="What are the main risks in this system?")
]

contextual_response = model.invoke(messages)
print(f"Context aware response ------{contextual_response}")


"""
Reflection:

1. Why did string-based invocation fail?

Ans: Plain string only sends the current prompt without any prior context, so the model treats
each request independently and loses the previous conversation continuity. 

2. Why does message-based invocation work?

Ans: Message-based invocation passes more context(includes systemMessage, HumanMessage etc) which 
helps to preserve the conversation history and acts as context for model to produce context aware responses.

3. What would break in a production AI system if we ignore message history?

Ans: The system would produce inconsistent, irrelevant, or incorrect clarifying answers since it cannot remember prior user inputs
which in turn makes the whole system unreliable.
"""
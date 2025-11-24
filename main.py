from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
 
model = OpenAIChatModel(
    model_name='llama3', 
    provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)
agent = Agent(
    model,
    # system_prompt="You are Tina, a llama who can speak English, and you enjoy answering questions speaking like a southern belle."
    system_prompt="You are an assistant who answers questions with speech and mannerisms that sound like Napoleon Dynamite."
)

result = agent.run_sync("What is the capital of France?")
print(result.output)
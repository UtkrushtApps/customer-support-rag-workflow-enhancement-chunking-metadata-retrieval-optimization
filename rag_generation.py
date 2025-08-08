from openai import OpenAI
from config import OPENAI_API_KEY, GENERATION_MODEL

# Placeholder: expects user_query and retrieved_context as list of strings

def generate_support_answer(query, context_chunks):
    # TODO: Craft prompt and call LLM to generate context-aware answer
    return None

if __name__ == "__main__":
    query = "My account login fails after password change. How do I fix this?"
    context_chunks = ["Chunk 1...", "Chunk 2..."]
    answer = generate_support_answer(query, context_chunks)
    print(answer)

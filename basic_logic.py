# moengage-doc-analysis/basic_logic.py

import os
from dotenv import load_dotenv

# This script can be used for:
# 1. Quick testing of a specific LLM prompt without full integration.
# 2. Developing a function for a specific readability score (e.g., Flesch-Kincaid) before LLM integration.
# 3. Testing HTML parsing selectors before adding them to scraper.py.

if __name__ == "__main__":
    print("--- Basic Logic & Testing Script ---")

    # Example: Simple string manipulation test
    text = "This is a sentence. Another sentence follows. This is very long and complex for no reason."
    print(f"Original text: {text}")
    simplified_text = text.replace("very long and complex for no reason", "complicated")
    print(f"Simplified text: {simplified_text}")

    # Example: Basic LLM interaction test (ensure LLM_API_KEY is loaded in .env)
    # To run this part, uncomment the following lines and ensure you have 'openai' installed
    # load_dotenv()
    # from openai import OpenAI
    # client = OpenAI(api_key=os.getenv("LLM_API_KEY"))
    #
    # if client and os.getenv("LLM_API_KEY"):
    #     test_prompt = "Suggest a simple improvement for the sentence: 'The user is able to create a new profile.'"
    #     try:
    #         response = client.chat.completions.create(
    #             model="gpt-3.5-turbo",
    #             messages=[{"role": "user", "content": test_prompt}]
    #         )
    #         print(f"\nLLM Test Output: {response.choices[0].message.content}")
    #     except Exception as e:
    #         print(f"Error during LLM test: {e}")
    # else:
    #     print("\nLLM client not initialized or API key missing for test.")
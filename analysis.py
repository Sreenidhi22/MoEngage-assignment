# moengage-doc-analysis/analysis.py

import json
import os
from dotenv import load_dotenv
from openai import OpenAI # Or from google.generativeai import configure, GenerativeModel etc.

# Import the scraping function from scraper.py
from scraper import fetch_article_content

# --- Configuration and Initialization ---
print("--- Analysis Script: Documentation Analyzer Agent (Task 1) ---")

# Load environment variables from .env file
load_dotenv()
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o") # Default to a capable model, adjust if using others

if not LLM_API_KEY:
    raise ValueError("LLM_API_KEY environment variable not set. Please create a .env file.")

# Initialize LLM client
# Adjust client initialization based on your chosen LLM provider
try:
    llm_client = OpenAI(api_key=LLM_API_KEY)
    print(f"LLM Client initialized with model: {LLM_MODEL}")
except Exception as e:
    print(f"Error initializing LLM client: {e}")
    llm_client = None


# --- Helper Function: Analyze Content with LLM ---
def analyze_content_with_llm(content: str, llm_client: OpenAI, llm_model_name: str) -> dict:
    """
    Analyzes the content using an LLM based on provided criteria.
    The LLM prompt is carefully crafted to elicit structured, actionable suggestions.
    """
    if not llm_client:
        return {
            "readability_for_marketer": {"assessment": "LLM client not initialized.", "suggestions": []},
            "structure_and_flow": {"assessment": "LLM client not initialized.", "suggestions": []},
            "completeness_and_examples": {"assessment": "LLM client not initialized.", "suggestions": []},
            "style_guidelines": {"assessment": "LLM client not initialized.", "suggestions": []}
        }

    # This prompt is designed to align with the desired output format in your report.
    # It asks for assessment and specific, actionable suggestions for each criterion.
    prompt = f"""
    You are an AI assistant specialized in improving technical documentation for marketers.
    Analyze the following documentation article content and provide actionable suggestions for improvement based on the criteria below.
    The output must be a JSON object with a 'assessment' string and a 'suggestions' list of strings for each criterion.
    Suggestions should be specific and actionable, e.g., "Sentence X is too long; consider breaking it into two shorter sentences."

    Article Content:
    ---
    {content}
    ---

    Analysis Criteria:
    1. Readability for a Marketer:
       - Assess the content's readability from the perspective of a non-technical marketer.
       - Explain why it's readable or not for this persona.

    2. Structure and Flow:
       - Analyze the article's structure (headings, subheadings, paragraph length, use of lists, etc.).
       - Does the information flow logically? Is it easy to navigate and find specific information?

    3. Completeness of Information & Examples:
       - Does the article provide enough detail for a user to understand and implement the feature or concept?
       - Are there sufficient, clear, and relevant examples? If not, suggest where examples could be added or improved.

    4. Adherence to Style Guidelines (Simplified - based on Microsoft Style Guide principles):
       - Voice and Tone: Is it customer-focused, clear, and concise?
       - Clarity and Conciseness: Are there overly complex sentences or jargon that could be simplified?
       - Action-oriented language: Does it guide the user effectively?
       - Identify areas that deviate from these principles and suggest specific changes.

    Output Format (JSON):
    {{
        "readability_for_marketer": {{
            "assessment": "Brief assessment here.",
            "suggestions": ["Specific suggestion 1", "Specific suggestion 2"]
        }},
        "structure_and_flow": {{
            "assessment": "Brief assessment here.",
            "suggestions": ["Specific suggestion 1", "Specific suggestion 2"]
        }},
        "completeness_and_examples": {{
            "assessment": "Brief assessment here.",
            "suggestions": ["Specific suggestion 1", "Specific suggestion 2"]
        }},
        "style_guidelines": {{
            "assessment": "Brief assessment here.",
            "suggestions": ["Specific suggestion 1", "Specific suggestion 2"]
        }}
    }}
    """

    try:
        # Adjust the API call based on your chosen LLM (OpenAI, Gemini, Anthropic, etc.)
        # This example uses OpenAI's chat completions API
        response = llm_client.chat.completions.create(
            model=llm_model_name,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant for documentation analysis."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}, # Crucial for getting JSON output
            temperature=0.7 # Adjust for creativity vs. consistency
        )
        llm_output = response.choices[0].message.content
        return json.loads(llm_output)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from LLM: {e}")
        print(f"LLM Raw Output: {llm_output}")
        return {
            "readability_for_marketer": {"assessment": "JSON decode error.", "suggestions": []},
            "structure_and_flow": {"assessment": "JSON decode error.", "suggestions": []},
            "completeness_and_examples": {"assessment": "JSON decode error.", "suggestions": []},
            "style_guidelines": {"assessment": "JSON decode error.", "suggestions": []}
        }
    except Exception as e:
        print(f"Error during LLM analysis: {e}")
        return {
            "readability_for_marketer": {"assessment": "Error during analysis.", "suggestions": []},
            "structure_and_flow": {"assessment": "Error during analysis.", "suggestions": []},
            "completeness_and_examples": {"assessment": "Error during analysis.", "suggestions": []},
            "style_guidelines": {"assessment": "Error during analysis.", "suggestions": []}
        }

if __name__ == "__main__":
    # Option 1: Load pre-extracted content from scraper.py (recommended for iterative testing)
    extracted_data_file = "extracted_articles_complete.json"
    articles_to_analyze = []

    if os.path.exists(extracted_data_file):
        with open(extracted_data_file, 'r', encoding='utf-8') as f:
            articles_to_analyze = json.load(f)
        print(f"Loaded {len(articles_to_analyze)} articles from {extracted_data_file}.")
    else:
        print(f"'{extracted_data_file}' not found. Please run 'scraper.py' first or define URLs directly.")
        # Fallback: Define URLs directly if scraper output is not available
        articles_to_analyze = [
            {"url": "https://partners.moengage.com/hc/en-us/articles/9643917325460-Create-creatives", "content": None},
            {"url": "https://help.moengage.com/hc/en-us/articles/28194279371668-How-to-Analyze-OTT-Content-Performance", "content": None},
        ]
        # In a real scenario, you'd ensure scraper.py is run first or implement live fetching here.

    all_analysis_reports = []

    for article_data in articles_to_analyze:
        url = article_data["url"]
        content = article_data.get("content")

        if not content:
            print(f"Content not available for {url}. Attempting live fetch using scraper.py...")
            content = fetch_article_content(url) # Using the imported function from scraper.py
            if not content:
                print(f"Skipping analysis for {url} due to missing content.")
                all_analysis_reports.append({"url": url, "error": "Content not available for analysis."})
                continue

        print(f"\n--- Starting analysis for: {url} ---")
        report_data = analyze_content_with_llm(content, llm_client, LLM_MODEL)
        final_report = {"url": url}
        final_report.update(report_data) # Merge the LLM's output directly

        all_analysis_reports.append(final_report)
        print(f"\n--- Analysis Report for {url} ---")
        print(json.dumps(final_report, indent=4))
        print("-" * (len(url) + 25))

    # Optional: Save all reports to a single JSON file
    output_filename = "moengage_documentation_analysis_reports_output.json" # Distinct filename from input
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(all_analysis_reports, f, indent=4, ensure_ascii=False)
    print(f"\nAll analysis reports saved to {output_filename}")
# MoEngage AI-Powered Documentation Improvement Agent - Task 1

This repository contains the solution for Task 1: The Documentation Analyzer Agent, as part of the MoEngage Tech Intern Coding Assignment. This project utilizes Jupyter Notebooks for an iterative development and analysis workflow.

## Table of Contents

- [Project Overview](#project-overview)
- [Core Tasks Implemented](#core-tasks-implemented)
- [Technical Guidelines Adhered To](#technical-guidelines-adhered-to)
- [Project Structure](#project-structure)
- [Setup and Running the Project](#setup-and-running-the-project)
- [Notebook Explanations](#notebook-explanations)
- [Design Choices and Approach](#design-choices-and-approach)
- [Assumptions Made](#assumptions-made)
- [Challenges Faced and How They Were Addressed](#challenges-faced-and-how-they-were-addressed)
- [Example Output](#example-output)

## Project Overview

The goal of this assignment is to develop an AI-powered agent that can analyze public documentation articles from help.moengage.com and suggest improvements. Task 1 focuses on building the "Documentation Analyzer Agent" which takes a URL as input and outputs a structured list of actionable suggestions for improvement.

## Core Tasks Implemented

The agent analyzes articles based on the following criteria:

1.  **Readability for a Marketer**: Assesses content's readability for a non-technical marketer, explaining the assessment beyond just a score.
2.  **Structure and Flow**: Analyzes headings, subheadings, paragraph length, use of lists, and logical information flow.
3.  **Completeness of Information & Examples**: Checks if enough detail is provided for understanding and implementation, and suggests where examples could be added or improved.
4.  **Adherence to Style Guidelines (Simplified)**: Focuses on Voice and Tone (customer-focused, clear, concise), Clarity and Conciseness (simplifying complex sentences/jargon), and Action-oriented language. It identifies deviations and suggests specific changes.

The output is a structured report (JSON) containing the analyzed URL, a brief assessment for each criterion, and specific, actionable suggestions.

## Technical Guidelines Adhered To

* **Programming Language**: Python, primarily within Jupyter Notebooks.
* **LLMs**: Utilizes an LLM (e.g., OpenAI GPT models) via API for content analysis. The choice is configurable via environment variables within the notebooks.
* **Web Content Fetching**: Employs `requests` and `BeautifulSoup4` to fetch and parse HTML content from given URLs.
* **No UI Focus**: The assignment is backend/agent-focused, so no time was spent on frontend or UI development.
* **Code Quality**: Emphasis on clear, well-commented, and organized code within the notebook cells.

{
    "url": "[https://help.moengage.com/hc/en-us/articles/28194279371668-How-to-Analyze-OTT-Content-Performance](https://help.moengage.com/hc/en-us/articles/28194279371668-How-to-Analyze-OTT-Content-Performance)",
    "readability_for_marketer": {
        "assessment": "Above average readability with some complex phrases.",
        "suggestions": [
            "Define technical terms like 'streaming funnels' briefly on first use.",
            "Simplify the sentence in the 'Overview' section starting with 'OTT analytics enables...'"
        ]
    },
    "structure_and_flow": {
        "assessment": "Well-structured with logical flow.",
        "suggestions": [
            "Use numbered steps under the 'How to analyze section.",
            "Shorten the introduction by summarizing key takeaways."
        ]
    },
    "completeness_and_examples": {
        "assessment": "Detailed steps provided with helpful visuals.",
        "suggestions": [
            "Label screenshots with numbers for easy cross-reference.",
            "Add a sample case study or scenario."
        ]
    },
    "style_guidelines": {
        "assessment": "Adheres to most style principles.",
        "suggestions": [
            "Avoid repetitive use of 'you can'.",
            "Use consistent tone; some sections shift from instructional to descriptive."
        ]
    }
}


Article 1 Analysis

**URL:** `https://partners.moengage.com/hc/en-us/articles/9643917325460-Create-creatives`

```json
{
    "url": "[https://partners.moengage.com/hc/en-us/articles/9643917325460-Create-creatives](https://partners.moengage.com/hc/en-us/articles/9643917325460-Create-creatives)",
    "readability_for_marketer": {
        "assessment": "Moderate readability for non-technical marketers.",
        "suggestions": [
            "Simplify marketing jargon like 'creative optimization strategies' in paragraph 2.",
            "Break long paragraph under 'Content Types' into two for easier consumption."
        ]
    },
    "structure_and_flow": {
        "assessment": "Good overall structure but some sections could use subheadings.",
        "suggestions": [
            "Add a subheading before 'Image specifications' to improve skimmability.",
            "Consider using bullet points for steps in 'Create creatives'."
        ]
    },
    "completeness_and_examples": {
        "assessment": "Sufficient details provided but lacks usage examples.",
        "suggestions": [
            "Include an example of a completed creative.",
            "Add visual annotation for the creative form fields."
        ]
    },
    "style_guidelines": {
        "assessment": "Mostly consistent with simplified guidelines.",
        "suggestions": [
            "Reword passive sentences under 'Best Practices'.",
            "Use more direct, action-based language like 'Upload your file' instead of 'Files can be uploaded'."
        ]
    }
}
import json
from xmlrpc import client
from helpers import add_user_message, add_assistant_message, chat

def grade_by_model(test_case, output, client):
    eval_prompt = f"""
      You are an expert AWS code reviewer. Your task is to evaluate the following AI-generated solution.

      Original Task:
      <task>
      {test_case["task"]}
      </task>

      Solution to Evaluate:
      <solution>
      {output}
      </solution>

      Criteria you should use to evaluate the solution:
      <criteria>
      {test_case["solution_criteria"]}
      </criteria>

      Output Format
      Provide your evaluation as a structured JSON object with the following fields, in this specific order:
      - "strengths": An array of 1-3 key strengths, keep in short (up to 10 words)
      - "weaknesses": An array of 1-3 key areas for improvement, keep in short (up to 10 words)
      - "reasoning": A concise explanation of your overall assessment, keep in short (up to 10 words)
      - "score": A number between 1-10

      Respond with JSON. Keep your response concise and direct.
      Example response shape:
      {{
          "strengths": string[],
          "weaknesses": string[],
          "reasoning": string,
          "score": number
      }}
          """
    messages = []
    add_user_message(messages, eval_prompt)
    add_assistant_message(messages, "```json")
    text = chat(messages, stop_sequences=["```"], client=client)
    return json.loads(text)

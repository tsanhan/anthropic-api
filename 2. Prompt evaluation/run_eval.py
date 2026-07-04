from statistics import mean
from helpers import add_user_message, add_assistant_message, chat
from graders import grade_by_model, grade_by_code


def run_prompt(test_case, client):
    """Merges the prompt and test case input, then returns the result"""
    prompt = f"""
    Please solve the following task:

    {test_case["task"]}

    * respond only with Python, JSON, or a plain Regex
    * Do not add any comments or commentary or explanation
    * DO NOT add any escape characters or new line (like slash the the letter n) in the solution
    * these are the solution criteria, follow these instructions to create a better solution:
    {test_case["solution_criteria"]}
    """
    messages = []
    add_user_message(messages, prompt)
    add_assistant_message(messages, f"```{test_case["format"]}")
    text = chat(messages, stop_sequences=["```"], client=client)
    return text

def run_test_case(test_case, client):
    """Calls run_prompt, then grades the result"""
    result = run_prompt(test_case, client)
    model_grade = grade_by_model(test_case, result)
    code_grade = grade_by_code(result, test_case)
    score = model_grade["score"]
    reasoning = model_grade["reasoning"]

    return {
        "output": result,
        "score": mean([score, code_grade]),
        "reasoning": reasoning,
        "test_case": test_case,
        "code_grade": code_grade
    }

def run_eval(dataset, client):
    """Loads the dataset and calls run_test_case with each case"""
    results = []
    for test_case in dataset:
        result = run_test_case(test_case, client)
        results.append(result)

    average_score = mean([result["score"] for result in results])
    average_code_grade = mean([result["code_grade"] for result in results])
    print(f"Average score: {average_score}")
    print(f"Average code grade: {average_code_grade}")
    return results

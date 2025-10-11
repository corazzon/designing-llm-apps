import openai
# note: don't forget to pip install the correct version, bec sometimes older/newer versions of openai don't work or get deprecated

# Set up your OpenAI API key
openai.api_key = ""


def solve_crossword(clue, num_letters):
    """
    Queries OpenAI to solve a crossword clue.

    Parameters:
        clue (str): The crossword clue given.
        num_letters (int): The expected number of letters in the answer.

    Returns:
        tuple: (predicted answer (str), finish reason (str))
    """
    
    # Construct the prompt for the chatbot
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Solve this crossword in one word. "
                                    f"The clue is '{clue}', and it is a {num_letters}-letter word. "
                                    f"The answer is:"}
    ]

    try:
        # Call OpenAI's API to get a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Note: Using GPT-3.5 Turbo for efficiency, also da vinci is deprecated accdng to documentation
            messages=messages,
            max_tokens=3  # Limit response to a few words to avoid unnecessary text
        )

        # Extract the answer from the response
        answer = response.choices[0].message["content"].strip()
        
        # Finish reason indicates whether the response was completed successfully
        finish_reason = response.choices[0].finish_reason  # 'stop' means normal completion

        return answer, finish_reason

    except openai.error.OpenAIError as e:
        # Handle API errors and display an appropriate message
        print(f"❌ API Error: {e}")
        return None, None  # Return None values to indicate failure

def main():
    """
    Main function to test solving crossword clues.
    """
    
    # Define a list of crossword clues with expected answers, sample 
    clues = [
        {"clue": "A fruit that keeps the doctor away", "num_letters": 5, "expected": "apple"},
        {"clue": "The capital of France", "num_letters": 5, "expected": "paris"},
        # Add more clues as needed for testing
    ]

    # Counter to keep track of correct answers
    correct_answers = 0

    # Iterate through each crossword clue
    for clue in clues:
        answer, finish_reason = solve_crossword(clue["clue"], clue["num_letters"])
        
        if answer:  # Ensure that an answer was received
            print(f"Clue: {clue['clue']}, Answer: {answer}, Finish Reason: {finish_reason}")

            # Validate the predicted answer against the expected correct answer
            if answer.lower().strip(".") == clue["expected"]:  # Stripping period for better match
                correct_answers += 1  # Increment correct answers count

    # Display final results
    print(f"\n Total correct answers: {correct_answers}/{len(clues)}")

if __name__ == "__main__":
    # Run the program
    main()


#### SAMPLE OUTPUT AT
"""
Clue: A fruit that keeps the doctor away, Answer: Apple., Finish Reason: stop
Clue: The capital of France, Answer: Paris, Finish Reason: stop

Total correct answers: 1/2
(llm-playbooks) (.venv) Boosts-MacBook-Pro:Chapter4 amber$ python crossword_solver.py 
Clue: A fruit that keeps the doctor away, Answer: Apple., Finish Reason: stop
Clue: The capital of France, Answer: Paris, Finish Reason: stop

Total correct answers: 2/2
"""
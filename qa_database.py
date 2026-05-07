"""
QA Database for Voice Bot
This module contains predefined question-answer pairs for the voice bot.
"""

# Dictionary of predefined questions and answers
QA_DATABASE = {
    "what is your name": "I am a simple voice bot created to help you.",
    "hello": "Hello! How can I help you today?",
    "how are you": "I am doing great, thank you for asking!",
    "what time is it": "I don't have access to real-time data, but you can check your system clock.",
    "who are you": "I am a voice-activated assistant designed to answer your questions.",
    "tell me a joke": "Why did the programmer quit his job? Because he didn't get arrays!",
    "what is your purpose": "My purpose is to respond to your voice commands and provide helpful answers.",
    "goodbye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! Happy to help.",
    "how does this work": "I use speech recognition to understand your questions and text-to-speech to respond.",
    "what can you do": "I can listen to your voice, understand questions, and respond with speech.",
    "bye": "See you later! Take care.",
}


def get_answer(question):
    """
    Get answer for a given question from the database.
    
    Args:
        question (str): The question asked by the user
        
    Returns:
        str: The answer if found, otherwise a default message
    """
    question = question.lower().strip()
    
    # Check for exact match
    if question in QA_DATABASE:
        return QA_DATABASE[question]
    
    # Check for partial match
    for q, a in QA_DATABASE.items():
        if q in question or question in q:
            return a
    
    # Return default response if no match found
    return "I'm sorry, I didn't understand that. Could you please repeat or rephrase your question?"


def add_qa_pair(question, answer):
    """
    Add a new question-answer pair to the database.
    
    Args:
        question (str): The question
        answer (str): The answer
    """
    question = question.lower().strip()
    QA_DATABASE[question] = answer
    print(f"✓ Added: '{question}' -> '{answer}'")


def view_all_qa():
    """
    Display all question-answer pairs in the database.
    """
    print("\n" + "="*60)
    print("VOICE BOT - PREDEFINED Q&A DATABASE")
    print("="*60)
    for i, (question, answer) in enumerate(QA_DATABASE.items(), 1):
        print(f"{i}. Q: {question}")
        print(f"   A: {answer}\n")
    print("="*60 + "\n")


if __name__ == "__main__":
    # Display all Q&A pairs
    view_all_qa()
    
    # Test get_answer function
    test_question = "what is your name"
    print(f"Test Question: '{test_question}'")
    print(f"Answer: {get_answer(test_question)}\n")

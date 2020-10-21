"""
Chatbot for lonely people in lockdown
"""
import random


def respond(message):
    """
    This is a chatbot that resonds to a message from the user
    :param message: what the user is saying to the chatbot
    :return: a response from the chatbot
    """
    message = message.lower()
    response = "Sorry, I don't understand"
    categories = []

    classifications = {
        "greeting": ["hello", "hi", "whats up", "howdy", "hey"],
        "exit": ["bye"]
    }

    for cat, arr_messages in classifications.items():
        for possible_message in arr_messages:
            if possible_message in message:
                categories.append(cat)

    responses = {
        "greeting": ["Hello to you to", "Hey, nice to meet you", "Hi, how are you?"],
        "exit": ["Bye bye [wave]"]
    }

    for category in categories:
        response = random.choice(responses[category])
        print(category)

    return response


if __name__ == "__main__":
    print("Helloooooooo")
    print(respond("Hellooooo bye bye"))

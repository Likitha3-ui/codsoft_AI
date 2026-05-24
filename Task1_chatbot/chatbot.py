from datetime import datetime
import random

print("=" * 60)
print("        SMART ASSISTANT CHATBOT")
print("=" * 60)

user_name = input("Enter your name: ").title()

chat_history = []

jokes = [
    "Why do programmers love Python? Because it makes coding easier.",
    "Why did the computer get cold? It forgot to close its Windows.",
    "Why was the keyboard always calm? Because it had good control."
]

while True:

    print("\n")
    print("1. Start Chat")
    print("2. Calculator")
    print("3. Chat History")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":

        message = input(f"\n{user_name}: ").lower()

        chat_history.append(f"{user_name}: {message}")

        if "hello" in message or "hi" in message:
            reply = f"Hello {user_name}! Nice to meet you."

        elif "how are you" in message:
            reply = "I am doing great. Thank you for asking."

        elif "your name" in message:
            reply = "I am Smart Assistant, a rule-based chatbot."

        elif "time" in message:
            current_time = datetime.now().strftime("%H:%M:%S")
            reply = f"The current time is {current_time}"

        elif "date" in message:
            current_date = datetime.now().strftime("%d-%m-%Y")
            reply = f"Today's date is {current_date}"

        elif "joke" in message:
            reply = random.choice(jokes)

        elif "python" in message:
            reply = "Python is a popular programming language used in AI and software development."

        elif "artificial intelligence" in message:
            reply = "Artificial Intelligence helps machines perform tasks that normally require human intelligence."

        elif "machine learning" in message:
            reply = "Machine Learning is a branch of AI that enables systems to learn from data."

        elif "thank you" in message:
            reply = "You're welcome. Happy to help."

        elif "bye" in message:
            reply = f"Goodbye {user_name}. Have a great day."
            print("\nBot:", reply)
            break

        else:
            reply = "Sorry, I do not have an answer for that."

        chat_history.append("Bot: " + reply)

        print("\nBot:", reply)

    elif option == "2":

        try:

            first_number = float(input("Enter first number: "))
            operator = input("Choose operator (+ - * /): ")
            second_number = float(input("Enter second number: "))

            if operator == "+":
                result = first_number + second_number

            elif operator == "-":
                result = first_number - second_number

            elif operator == "*":
                result = first_number * second_number

            elif operator == "/":
                result = first_number / second_number

            else:
                result = "Invalid operator"

            print("Result:", result)

        except:
            print("Please enter valid numbers.")

    elif option == "3":

        print("\n------ CHAT HISTORY ------")

        if len(chat_history) == 0:
            print("No conversation yet.")

        else:
            for conversation in chat_history:
                print(conversation)

    elif option == "4":

        print("Thank you for using Smart Assistant.")
        break
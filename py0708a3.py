'''
Chatbot: Build a simple rule-based chatbot using conditions,if else statements and loops(doctor, health checkup, general conversation, fever along with symptoms like if bone problemn then refer to a specialist, etc.)
'''
def health_checkup():
    print('How do you feel today?')
    temperature = float(input("Enter your body temperature in Celsius: "))
    if temperature > 37.5:
        print("You have a fever. Please consult a doctor.")
    else:
        print("You seem to be fine. Keep maintaining a healthy lifestyle.")
    symptoms = input("Do you have any other symptoms? (yes/no): ").strip().lower()
    if symptoms == 'yes':
        symptom_list = input("Please list your symptoms separated by commas: ").strip().lower().split(',')
        if 'bone pain' in symptom_list:
            print("You may have a bone problem. Please consult a orthopedic specialist.")
        elif 'cough' in symptom_list or 'cold' in symptom_list:
            print("You may have a common cold. Rest and stay hydrated.")
        elif 'headache' in symptom_list:
            print("You may have a headache. Consider taking rest and staying hydrated.")
        elif 'stomach ache' in symptom_list:
            print("You may have a stomach issue. Consider consulting a gastroenterologist.")
        elif 'skin rash' in symptom_list:
            print("You may have a skin issue. Consider consulting a dermatologist.")
        elif 'fatigue' in symptom_list:
            print("You may be experiencing fatigue. Ensure you get enough rest and maintain a balanced diet.")
        elif 'dizziness' in symptom_list:
            print("You may be experiencing dizziness. Please consult a doctor for further evaluation.")
        else:
            print("Please consult a doctor for further evaluation.")
def chatbot():
    print("Hello! I am your health assistant chatbot.")
    while True:
        print("\nHow can I assist you today?")
        print("1. Health Checkup")
        print("2. General Conversation")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            health_checkup()
        elif choice == '2':
            print("Let's have a general conversation. How are you feeling today?")
            feeling = input("You: ").strip().lower()
            if 'good' in feeling or 'fine' in feeling:
                print("That's great to hear! Keep up the positive vibes.")
            elif 'bad' in feeling or 'not well' in feeling:
                print("I'm sorry to hear that. Remember to take care of yourself and seek help if needed.")
            else:
                print("Thank you for sharing. Remember, it's important to take care of your health.")
        elif choice == '3':
            print("Thank you for using the health assistant chatbot. Stay healthy!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    chatbot()
    
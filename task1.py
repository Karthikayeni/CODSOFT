#function
def chat_bot(input_user): 

    input_user = input_user.lower() 

    if 'hi' in input_user or 'hello' in input_user:
        return "Hello, how can I help you?"
    
    elif "doubt" in input_user or "help" in input_user:
        return "I am very much happy to assist you with basic queries,so feel free to ask!"
    
    elif "how are you?" in input_user or "How is it going?" in input_user:
        return '''I am doing great.
               How can I help you?'''
    
    elif "age" in input_user or 'old' in input_user:
        return "I am a basically a chatbot, so I don't have a age."
    
    elif 'name' in input_user:
        return 'I don\'t have a name.I am a chatbot and I am here to assist you with basic queries.'
    
    elif 'founder' in input_user or 'made' in input_user or 'discovered' in input_user or 'identified' in input_user:
        return 'I was created by a college student named Karthikayeni.'
    
    elif 'Karthikayeni' in input_user or 'karthika' in input_user:
        return 'I\'m sorry, I can\'t answer this question.Is there any other queries? Hopw can I help you?'
    
    elif 'ok' in input_user or 'okay' in input_user or 'Thanks' in input_user or 'Thank you' in input_user:
        return 'How can I help you?'
    
    elif 'weather' in input_user:
        return 'I apologize that we don\'t have access to real-time information.'
    
    elif 'bye' in input_user or 'good bye' in input_user or 'see you' in input_user or 'tata' in input_user:
        return '''Thank you for having this conversation.
                Good bye. Have a great day!'''
    
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase or ask something else?"

# main function
print("Chatbot: Welcome to our sample chatbot,enter \"bye\" to exit!")

while True:
    input_user = input('You: ')
    if input_user.lower() == 'bye':
        print('Chatbot: Nice to meet you, good bye!')
        break
    reply = chat_bot(input_user)
    print('Chatbot: ',reply)

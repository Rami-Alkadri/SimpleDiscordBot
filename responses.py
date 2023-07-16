def handle_response(message):
    p_message = message.lower().strip()
    
    print(f"Processed message: {p_message}")
    
    if p_message == 'hello':
        return 'Sup.'
    
    return 'What does that even mean'

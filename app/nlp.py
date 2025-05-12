


# import google.generativeai as genai
# import re

# genai.configure(api_key="AIzaSyCT2Y6tfhBBi9Yh3O-qrAQre4kec7ER_0U")
# model = genai.GenerativeModel('gemini-2.0-flash')

# def get_intent_and_response(text, user_id=None, chat_history=None):
#     # Format chat history if available
#     formatted_history = ""
#     if chat_history:
#         for turn in chat_history:
#             formatted_history += f"User: {turn['user']}\nAssistant: {turn['bot']}\n"
    
#     # Add the latest user input to the prompt
#     prompt = f"""
# You are a helpful assistant chatbot for a queue management system having a conversation with a user.

# Context:
# {formatted_history}
# User: {text}

# Your task:
# 1. Understand the user's intent: creating a support ticket or checking ticket status.
# 2. If intent is clear and all required info is present (e.g. service name or ticket ID), respond accordingly and summarize the info.
# 3. If info is missing, ask the user to provide it in a natural and conversational way.
# 4. Use polite and helpful language.
# 5. Provide the following in your response:
#    - Response: <your reply>
#    - Intent: <create_ticket / check_status / unknown>
#    - Service: <service name or None>
#    - TicketID: <ticket id or None>
# make sure to give the answer in the language of the user messaged 
# """

#     response = model.generate_content(prompt)
#     raw = response.text

#     # Extract structured info from Gemini response
#     reply = re.search(r"Response:\s*(.+?)\nIntent:", raw, re.DOTALL)
#     intent = re.search(r"Intent:\s*(\w+)", raw)
#     service = re.search(r"Service:\s*(\w+)", raw)
#     ticket_id = re.search(r"TicketID:\s*(\d+)", raw)

#     return {
#         "response": reply.group(1).strip() if reply else "Sorry, I didn't get that.",
#         "intent": intent.group(1).lower() if intent else 'unknown',
#         "service": service.group(1).lower() if service else None,
#         "ticket_id": int(ticket_id.group(1)) if ticket_id else None
#     }




#v2

# import google.generativeai as genai
# import re

# genai.configure(api_key="AIzaSyCT2Y6tfhBBi9Yh3O-qrAQre4kec7ER_0U")
# model = genai.GenerativeModel('gemini-2.0-flash')

# def get_intent_and_response(text, user_id=None, chat_history=None):
#     # Format chat history if available
#     formatted_history = ""
#     if chat_history:
#         for turn in chat_history:
#             formatted_history += f"User: {turn['user']}\nAssistant: {turn['bot']}\n"
    
#     # Add the latest user input to the prompt
#     prompt = f"""
# You are a helpful assistant chatbot for a queue management system having a conversation with a user.

# Context:
# {formatted_history}
# User: {text}

# Your task:
# 1. Understand the user's intent: creating a support ticket or checking ticket status.
# 2. If intent is clear and all required info is present ( service name, phone number, email, or ticket ID), respond accordingly and summarize the info.
# just ask only for these info .you don't need to ask about the problem .
# 3. If info is missing, ask the user to provide it in a natural and conversational way.
# 4. Use polite and helpful language.
# 5. Provide the following in your response:
#    - Response: <your reply>
#    - Intent: <create_ticket / check_status / unknown>
#    - Service: <service name or None>
#    - TicketID: <ticket id or None>
#    - Email: <user email or None>
#    - Phone: <user phone number or None>
#    - Date: <requested date or None> 
# """


#     response = model.generate_content(prompt)
#     raw = response.text

#     # Extract structured info from Gemini response
#     reply = re.search(r"Response:\s*(.+?)\nIntent:", raw, re.DOTALL)
#     intent = re.search(r"Intent:\s*(\w+)", raw)
#     service = re.search(r"Service:\s*(\w+)", raw)
#     ticket_id = re.search(r"TicketID:\s*(\d+)", raw)
#     email = re.search(r"Email:\s*([\w\.-]+@[\w\.-]+)", raw)
#     phone = re.search(r"Phone:\s*(\d{10,15})", raw)
#     date = re.search(r"Date:\s*([^\n]+)", raw)


#     return {
#         "response": reply.group(1).strip() if reply else "Sorry, I didn't get that.",
#         "intent": intent.group(1).lower() if intent else 'unknown',
#         "service": service.group(1).lower() if service else None,
#         "ticket_id": int(ticket_id.group(1)) if ticket_id else None,
#         "email": email.group(1) if email else None,
#         "phone": phone.group(1) if phone else None,
#         "date": date.group(1).strip() if date else None
#     }


#v3 

import google.generativeai as genai
import re

genai.configure(api_key="AIzaSyCT2Y6tfhBBi9Yh3O-qrAQre4kec7ER_0U")
model = genai.GenerativeModel('gemini-2.0-flash')

def clean_field(value):
    """Convert placeholder strings like 'none', 'null', etc. to actual None."""
    if not value:
        return None
    value = value.strip().lower()
    if value in ['none', 'null', 'n/a', '']:
        return None
    return value

def get_intent_and_response(text, user_id=None, chat_history=None):
    # Format chat history if available
    formatted_history = ""
    if chat_history:
        for turn in chat_history:
            formatted_history += f"User: {turn['user']}\nAssistant: {turn['bot']}\n"
    
    # Add the latest user input to the prompt
    prompt = f"""
You are a helpful assistant chatbot for a queue management system having a conversation with a user.

Context:
{formatted_history}
User: {text}

Your task:
1. Understand the user's intent: creating a ticket or checking ticket status.
2. If intent is clear and all required info is present (service name, phone number, email, or ticket ID), respond accordingly and summarize the info.
Just ask only for these info. You don't need to ask about the problem.
these are the services available :['internet', 'hardware', 'software', 'printer', 'it']
3. If info is missing,first check the history and try to collect if they are available in previous messages. if they are in the previous messages don't ask them again just include them in the reponse,
if they are not in previous messages, ask the user to provide it in a natural and conversational way.if user gives the missing info 
4. Use polite and helpful language.
5. Provide the following in your response:
   - Response: <your reply>
   - Intent: <create_ticket / check_status / unknown>
   - Service: <service name or None>
   - TicketID: <ticket id or None>
   - Email: <user email or None>
   - Phone: <user phone number or None>
   - Date: <requested date or None> 
always check the previous chat from the history and understand the intent .
make sure to reply in the language which is user messaged.
"""

    response = model.generate_content(prompt)
    raw = response.text

    # Extract structured info from Gemini response
    reply = re.search(r"Response:\s*(.+?)\nIntent:", raw, re.DOTALL)
    intent = re.search(r"Intent:\s*(\w+)", raw)
    service = re.search(r"Service:\s*(.+)", raw)
    ticket_id = re.search(r"TicketID:\s*(\d+)", raw)
    email = re.search(r"Email:\s*([\w\.-]+@[\w\.-]+)", raw)
    phone = re.search(r"Phone:\s*([+\d][\d\s\-]{8,20})", raw)
    date = re.search(r"Date:\s*(.+)", raw)

    return {
        "response": reply.group(1).strip() if reply else "Sorry, I didn't get that.",
        "intent": intent.group(1).lower() if intent else 'unknown',
        "service": clean_field(service.group(1)) if service else None,
        "ticket_id": int(ticket_id.group(1)) if ticket_id else None,
        "email": clean_field(email.group(1)) if email else None,
        "phone": clean_field(phone.group(1)) if phone else None,
        "date": clean_field(date.group(1)) if date else None
    }

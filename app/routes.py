# from flask import request, jsonify
# from app import app, db, socketio
# from app.models import Service, Ticket
# from app.nlp import get_intent
# from app.utils import extract_service_name, extract_ticket_id
# from flask_socketio import emit

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json.get('message')
#     user_id = request.json.get('user_id')
#     intent = get_intent(user_input)
    
#     if intent == 'create_ticket':
#         service_name = extract_service_name(user_input)
#         service = Service.query.filter_by(name=service_name).first()
#         if service:
#             ticket = Ticket(service_id=service.id, user_id=user_id)
#             db.session.add(ticket)
#             db.session.commit()
#             return jsonify({'message': f'Ticket created with ID {ticket.id}'})
#         else:
#             return jsonify({'message': 'Service not found'}), 404
#     elif intent == 'check_status':
#         ticket_id = extract_ticket_id(user_input)
#         ticket = Ticket.query.get(ticket_id)
#         if ticket:
#             return jsonify({'message': f'Ticket status: {ticket.status}'})
#         else:
#             return jsonify({'message': 'Ticket not found'}), 404
#     else:
#         return jsonify({'message': 'Sorry, I did not understand that.'})

# @socketio.on('message')
# def handle_message(data):
#     user_input = data['message']
#     user_id = data['user_id']
#     intent = get_intent(user_input)
    
#     if intent == 'create_ticket':
#         service_name = extract_service_name(user_input)
#         service = Service.query.filter_by(name=service_name).first()
#         if service:
#             ticket = Ticket(service_id=service.id, user_id=user_id)
#             db.session.add(ticket)
#             db.session.commit()
#             emit('response', {'message': f'Ticket created with ID {ticket.id}'})
#         else:
#             emit('response', {'message': 'Service not found'})
#     elif intent == 'check_status':
#         ticket_id = extract_ticket_id(user_input)
#         ticket = Ticket.query.get(ticket_id)
#         if ticket:
#             emit('response', {'message': f'Ticket status: {ticket.status}'})
#         else:
#             emit('response', {'message': 'Ticket not found'})
#     else:
#         emit('response', {'message': 'Sorry, I did not understand that.'})


#v3

from flask import request, jsonify,session
from app import app, db
from app.models import Service, Ticket
from app.nlp import get_intent_and_response
from app.utils import extract_service_name, extract_ticket_id

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json.get('message')
#     user_id = request.json.get('user_id')

#       # Initialize chat history in session if not already present
#     if 'chat_history' not in session:
#         session['chat_history'] = []

#     chat_history = session['chat_history']
#     print(chat_history)

#     # Get Gemini response and intent classification
#     result = get_intent_and_response(user_input, user_id=user_id, chat_history=chat_history)
#     intent = result.get("intent")
#     gemini_reply = result.get("response")
#     extracted_service = result.get("service")
#     extracted_ticket_id = result.get("ticket_id")
#     email = result.get("email")
#     phone = result.get("phone")
#     date = result.get("date")

#     print(intent)
#     print(extracted_ticket_id)
#     print(gemini_reply)
#     print(extracted_service)
#     print(f"Condition result: {not extracted_service }")

#     # if intent == 'create_ticket':
#     #     if not extracted_service:
#     #         # Let Gemini handle the missing info in a human way
#     #         return jsonify({'message': gemini_reply})
        
#     #     service = Service.query.filter_by(name=extracted_service).first()
#     #     if service:
#     #         ticket = Ticket(service_id=service.id, user_id=user_id)
#     #         db.session.add(ticket)
#     #         db.session.commit()
#     #         return jsonify({'message': f'Ticket created with ID {ticket.id}'})
#     #     else:
#     #         return jsonify({'message': gemini_reply})  # Gemini may have said "Sorry, we don't support X"

#     if intent == 'create_ticket':
#         print("kkkkkkkkkkkkkkkkkkkkkkkk")
#         if not extracted_service or not email or not phone or not date:
#             # Let Gemini prompt the user naturally for missing info
#             print("shhhhhhhhhhhhhhhhhhhhhhh")
            
#             return jsonify({'message': gemini_reply})
        
#         service = Service.query.filter_by(name=extracted_service).first()
#         if service:
#             ticket = Ticket(
#                 service_id=service.id,
#                 user_id=user_id,
#                 email=email,
#                 phone=phone,
#                 date=date
#             )
#             db.session.add(ticket)
#             db.session.commit()
#             return jsonify({'message': f'Ticket created with ID {ticket.id}'})


#     elif intent == 'check_status' and extracted_ticket_id:
#         ticket = Ticket.query.get(extracted_ticket_id)
#         if ticket:
#             return jsonify({'message': f'Ticket status: {ticket.status}'})
#         else:
#             return jsonify({'message': f"Couldn't find a ticket with ID {extracted_ticket_id}"})

#     else:
#         reply = gemini_reply

#     # Update chat history
#     session['chat_history'].append({"user": user_input, "bot": reply})
#     session.modified = True  # Ensure Flask saves the session

#     return jsonify({'message': reply})



# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json.get('message')
#     user_id = request.json.get('user_id')

#     # Initialize chat history in session if not already present
#     if 'chat_history' not in session:
#         session['chat_history'] = []

#     # Extract prior chat history (only full turns are passed)
#     chat_history = session['chat_history']

#     # Get Gemini response and intent classification
#     result = get_intent_and_response(user_input, user_id=user_id, chat_history=chat_history)
#     intent = result.get("intent")
#     gemini_reply = result.get("response")
#     extracted_service = result.get("service")
#     extracted_ticket_id = result.get("ticket_id")
#     email = result.get("email")
#     phone = result.get("phone")
#     date = result.get("date")

#     # Decide the final response
#     reply = gemini_reply

#     if intent == 'create_ticket':
#         if not extracted_service or not email or not phone or not date:
#             session['chat_history'].append({"user": user_input, "bot": reply})
#             session.modified = True
#             print(chat_history)
#             return jsonify({'message': reply})  # Gemini will ask for what's missing

#         service = Service.query.filter_by(name=extracted_service).first()
#         if service:
#             ticket = Ticket(
#                 service_id=service.id,
#                 user_id=user_id,
#                 email=email,
#                 phone=phone,
#                 date=date
#             )
#             db.session.add(ticket)
#             db.session.commit()
#             reply = f'Ticket created with ID {ticket.id}'
#         else:
#             reply = "Sorry, we don't support the specified service."

#     elif intent == 'check_status' and extracted_ticket_id:
#         ticket = Ticket.query.get(extracted_ticket_id)
#         if ticket:
#             reply = f'Ticket status: {ticket.status}'
#         else:
#             reply = f"Couldn't find a ticket with ID {extracted_ticket_id}"

#     # ✅ Append current interaction only once Gemini has responded
#     session['chat_history'].append({"user": user_input, "bot": reply})
#     session.modified = True
#     print("dsddvssvsvsvdvvvsvds")

#     print(chat_history)
#     return jsonify({'message': reply})

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    user_id = request.json.get('user_id')

    if 'chat_history' not in session:
        session['chat_history'] = []

    chat_history = session['chat_history']

    result = get_intent_and_response(user_input, user_id=user_id, chat_history=chat_history)
    intent = result.get("intent")
    reply = result.get("response")
    extracted_service = result.get("service")
    extracted_ticket_id = result.get("ticket_id")
    email = result.get("email")
    phone = result.get("phone")
    #date = result.get("date")

    print(result)

    if intent == 'create_ticket':
        print(f"Extracted: service={extracted_service}, email={email}, phone={phone}")
        if extracted_service and email and phone :
            service = Service.query.filter_by(name=extracted_service).first()
            if service:
                ticket = Ticket(
                    service_id=service.id,
                    user_id=user_id,
                    email=email,
                    phone=phone,
                    #date=date
                )
                db.session.add(ticket)
                db.session.commit()
                reply = f'Ticket created with ID {ticket.id}'
            else:
                reply = "Sorry, we don't support the specified service."
        else:
            # Gemini will naturally ask for missing info
            session['chat_history'].append({"user": user_input, "bot": reply})
            session.modified = True
            return jsonify({'message': reply})

    elif intent == 'check_status' and extracted_ticket_id:
        ticket = Ticket.query.get(extracted_ticket_id)
        if ticket:
            reply = f'Ticket status: {ticket.status}'
        else:
            reply = f"Couldn't find a ticket with ID {extracted_ticket_id}"

    # Append final interaction
    session['chat_history'].append({"user": user_input, "bot": reply})
    session.modified = True
    return jsonify({'message': reply})



@app.route('/reset', methods=['POST'])
def reset_chat():
    session.pop('chat_history', None)
    return jsonify({'message': 'Chat history cleared.'})




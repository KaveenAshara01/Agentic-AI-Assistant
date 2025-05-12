import re

# def extract_service_name(text):
  
#     services = ['internet', 'hardware', 'software', 'printer','it']
#     words = re.findall(r'\b\w+\b', text.lower())
#     print(words)

#     for word in words:
#         if word in services:
#             print(word)
#             return word
#     return None

# def extract_ticket_id(text):
#     match = re.search(r'\b\d{4,6}\b', text)
#     return int(match.group()) if match else None



def extract_service_name(text):
    services = ['internet', 'hardware', 'software', 'printer', 'it']
    words = text.lower().split()
    for word in words:
        if word in services:
            return word
    return None

def extract_ticket_id(text):
    
    match = re.search(r'\d+', text)
    return int(match.group()) if match else None

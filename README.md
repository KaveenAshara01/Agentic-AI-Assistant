Agentic Chat
Agentic Chat is a web-based application that streamlines customer support interactions using an AI-driven chat interface. It allows users to create support tickets and check their statuses through natural language conversations. The project leverages the Gemini 2.0 Flash model for intent detection and response generation, with a Flask backend and a React frontend.
Features

Conversational Interface: Users can interact with the system using natural language (e.g., "Create a ticket for billing" or "Check ticket 123").
Ticket Management: Automates ticket creation and status checking via a chat interface.
Agentic AI: Powered by the Gemini 2.0 Flash model for natural language understanding (NLU) and response generation.
Modern UI: A sleek, responsive chat interface built with React and custom CSS.
Session Management: Stores chat history in a client-side session cookie for a seamless experience.

Project Structure
agentic/
├── app/
│   ├── __init__.py       # Flask app initialization
│   ├── models.py         # Database models (Service, Ticket)
│   ├── nlp.py            # NLP functions using Gemini 2.0 Flash
│   ├── queue_management.db  # SQLite database
│   ├── routes.py         # API endpoints for chat and reset
│   └── utils.py          # Utility functions for entity extraction
├── frontend/
│   ├── node_modules/     # Node.js dependencies
│   ├── src/
│   │   ├── components/   # React components (if any)
│   │   ├── App.css       # Default CSS (not used in this project)
│   │   ├── App.js        # Main React component
│   │   ├── App.test.js   # Test file for App.js
│   │   ├── index.css     # Custom CSS for styling
│   │   ├── index.js      # React entry point
│   │   ├── logo.svg      # Default React logo (not used)
│   │   ├── reportWebVitals.js  # Performance monitoring (not used)
│   │   └── setupTests.js  # Test setup file
│   ├── .gitignore        # Git ignore file
│   ├── package-lock.json # NPM lock file
│   ├── package.json      # Frontend dependencies
│   └── README.md         # Default React README (can be removed)
├── migrations/           # Database migration folder (if applicable)
├── config.py             # Configuration settings
├── requirements.txt      # Backend dependencies
├── run.py                # Flask app entry point
└── seed.py               # Database seeding script

Prerequisites

Python 3.8+
Node.js 14+
npm 6+
SQLite (included with Python)

Installation
Backend Setup

Clone the Repository:
git clone https://github.com/KaveenAshara01/Agentic-AI-Assistant.git
cd agentic-chat


Set Up a Virtual Environment:
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux


Install Backend Dependencies:
pip install -r requirements.txt


Initialize the Database:
python seed.py


Run the Flask Server:
python run.py

The backend will run on http://localhost:5000.


Frontend Setup

Navigate to the Frontend Directory:
cd frontend


Install Frontend Dependencies:
npm install


Run the React Development Server:
npm start

The frontend will run on http://localhost:3000.


Usage

Access the Application:

Open your browser and navigate to http://localhost:3000.


Interact with the Chat:

Send messages like "I need help with my account" to create a ticket or "Check ticket 123" to check a ticket's status.
The Gemini 2.0 Flash model will interpret your intent and respond accordingly.


Manage Tickets:

Use the "Check Status" button to query a ticket's status by entering its ID.
Use the "Reset Chat" button to clear the chat history.



Technical Details

Backend: Flask with SQLite for ticket storage. Chat history is stored in a signed session cookie on the client side.
Frontend: React with custom CSS for a modern chat interface.
AI Integration: Uses the Gemini 2.0 Flash model for natural language understanding (NLU) and response generation.
API Endpoints:
POST /chat: Processes user messages and returns AI-generated responses.
POST /reset: Clears the chat history from the session.



Built with Flask and React for a robust and modern web application.


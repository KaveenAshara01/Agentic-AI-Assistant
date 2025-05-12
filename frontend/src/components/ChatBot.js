import { useState, useEffect, useRef } from 'react';
import { Send, RotateCcw, Bot, User } from 'lucide-react';
import './ChatBot.css';

// API base URL - change this to match your Flask server
const API_BASE_URL = 'http://localhost:5000';

export default function ChatBot() {
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [userId] = useState('user_' + Math.random().toString(36).substring(2, 9));
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [chatHistory]);

  const handleSubmit = async (e) => {
    if (e) e.preventDefault();
    if (!message.trim()) return;
    
    // Add user message to chat history
    const userMessage = { type: 'user', content: message };
    setChatHistory(prev => [...prev, userMessage]);
    setIsLoading(true);
    const sentMessage = message;
    setMessage('');
    
    try {
      const response = await fetch(`${API_BASE_URL}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include', // Important for cookies/sessions
        body: JSON.stringify({
          message: sentMessage,
          user_id: userId
        }),
      });
      
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      
      const data = await response.json();
      
      // Add bot response to chat history
      setChatHistory(prev => [...prev, { type: 'bot', content: data.message }]);
    } catch (error) {
      console.error('Error:', error);
      setChatHistory(prev => [...prev, { 
        type: 'bot', 
        content: 'Sorry, something went wrong. Please try again.' 
      }]);
    } finally {
      setIsLoading(false);
      inputRef.current?.focus();
    }
  };

  const resetChat = async () => {
    setIsLoading(true);
    try {
      await fetch(`${API_BASE_URL}/reset`, {
        method: 'POST',
        credentials: 'include', // Important for cookies/sessions
      });
      setChatHistory([]);
    } catch (error) {
      console.error('Error resetting chat:', error);
    } finally {
      setIsLoading(false);
      inputRef.current?.focus();
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div className="chat-container">
      {/* Header */}
      <header className="chat-header">
        <div className="header-content">
          <div className="header-title">
            <Bot size={28} />
            <h1>AI Support Assistant</h1>
          </div>
          <button 
            onClick={resetChat}
            className="reset-button"
            disabled={isLoading}
            title="Reset Chat"
          >
            <RotateCcw size={16} />
            {/* Text removed to make button shorter */}
          </button>
        </div>
      </header>

      {/* Chat Container */}
      <div className="messages-container">
        {chatHistory.length === 0 ? (
          <div className="welcome-screen">
            <Bot size={64} />
            <p className="welcome-title">Welcome! How can I assist you today?</p>
            <p className="welcome-subtitle">Ask about services or check the status of your ticket.</p>
          </div>
        ) : (
          <div className="chat-messages">
            {chatHistory.map((msg, index) => (
              <div 
                key={index} 
                className={`message-row ${msg.type === 'user' ? 'user-message' : 'bot-message'}`}
              >
                <div className="message-bubble">
                  <div className="message-icon">
                    {msg.type === 'user' ? (
                      <User size={20} />
                    ) : (
                      <Bot size={20} />
                    )}
                  </div>
                  <div className="message-content">
                    {msg.content}
                  </div>
                </div>
              </div>
            ))}
            <div ref={messagesEndRef} />
          </div>
        )}
      </div>

      {/* Loading indicator */}
      {isLoading && (
        <div className="loading-indicator">
          <div className="loading-dots">
            <div className="loading-dot"></div>
            <div className="loading-dot"></div>
            <div className="loading-dot"></div>
          </div>
        </div>
      )}

      {/* Input Area */}
      <div className="input-container">
        <div className="input-wrapper">
          <div className="input-form">
            <textarea
              ref={inputRef}
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              onKeyDown={handleKeyDown}
              className="message-input"
              placeholder="Type your message here..."
              disabled={isLoading}
              rows="1"
            />
            <button
              onClick={handleSubmit}
              className="send-button"
              disabled={isLoading || !message.trim()}
            >
              <Send size={20} />
            </button>
          </div>
          <div className="input-hint">
            Ask about creating a ticket, checking status, or any other help you need.
          </div>
        </div>
      </div>
    </div>
  );
}
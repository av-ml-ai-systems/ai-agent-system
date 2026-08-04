import { useState } from "react";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([]);

  const [input, setInput] = useState("");

  async function sendMessage() {
  if (!input.trim()) {
    return;
  }

  const userMessage = {
    role: "User",
    content: input,
  };

  setMessages((previous) => [
    ...previous,
    userMessage,
  ]);

  const currentInput = input;

  setInput("");

  try {
    const response = await fetch(
      "http://127.0.0.1:8000/chat",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: currentInput,
        }),
      },
    );

    const data = await response.json();

    const assistantMessage = {
      role: "Assistant",
      content: data.response,
    };

    setMessages((previous) => [
      ...previous,
      assistantMessage,
    ]);
  } catch (error) {
    console.error(error);

    setMessages((previous) => [
      ...previous,
      {
        role: "Assistant",
        content: "Unable to reach FastAPI.",
      },
    ]);
  }
}

  return (
    <div className="app">
      <h1>🤖 AI Agent System</h1>

      <div className="chat-window">
        {messages.length === 0 ? (
          <p className="empty">
            No conversation yet.
          </p>
        ) : (
          messages.map((message, index) => (
            <div
              key={index}
              className={`message ${message.role}`}
            >
              <strong>{message.role}</strong>

              <p>{message.content}</p>
            </div>
          ))
        )}
      </div>

      <div className="chat-input">
        <input
          type="text"
          placeholder="Type your message..."
          value={input}
          onChange={(event) => setInput(event.target.value)}
        />

        <button onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}

export default App;
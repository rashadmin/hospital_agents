# hospital_agents

> An asynchronous AI agent built with Flask and LangGraph for orchestrating hospital-related tasks and interactions.

## 🧠 Overview

The `hospital_agents` project is a modular Flask application designed to power an AI agent. It leverages LangGraph for complex agentic workflows and uses Redis Streams for asynchronous communication, allowing for efficient processing of requests in the background. The application provides a web API for interaction and a structured approach to managing agent state and configuration.

## 🔨 What I Built

This project implements a robust AI agent system with the following core features:

-   **Modular Flask Application**: Organized using Flask's Blueprint pattern and an application factory for better maintainability and testability.
-   **LangGraph Agent Orchestration**: Defines a state machine for the AI agent, managing its state and execution flow based on incoming requests.
-   **Asynchronous Request Processing**: Utilizes Redis Streams to handle incoming requests asynchronously via a dedicated background listener thread.
-   **API Endpoints**: Exposes a `/agent` POST endpoint for external clients to interact with the AI agent.
-   **Centralized Configuration Management**: Securely handles application settings and sensitive API keys using environment variables and `python-dotenv`.
-   **Custom Error Handling**: Provides user-friendly custom error pages (404 and 500) and ensures proper database session management during errors.

## 💭 Thought Process

I designed this project with modularity and scalability in mind, adopting the Flask Application Factory Pattern and Blueprints to keep the codebase organized as it grows. The choice of LangGraph was driven by its capability to define and manage complex agentic workflows and states effectively.

To handle potential bottlenecks and ensure responsiveness, I integrated Redis Streams for asynchronous message processing. This allows the application to consume requests in a non-blocking manner through a dedicated background thread, decoupling the request reception from the agent's processing. While the `/agent` endpoint's core invocation logic is currently commented out, the foundation for seamless API interaction and background processing is firmly established.

A key decision was to externalize configuration using `.env` files and `python-dotenv`, promoting security and flexibility across different environments. Robust error handling, including database session rollback on 500 errors, was also a priority to ensure application stability.

## 🛠️ Tools & Tech Stack

| Layer           | Technology                     |
| :-------------- | :----------------------------- |
| Language        | Python 3.x                     |
| Web Framework   | Flask                          |
| AI Agent        | LangGraph                      |
| Message Queue   | Redis                          |
| Env Management  | python-dotenv                  |
| Database (Impl.)| SQLAlchemy                     |
| Concurrency     | Python `threading`             |
| Core AI Libs    | `langchain_core`               |

## 🚀 Getting Started

### Prerequisites

-   Python 3.x
-   Redis Server (running on `localhost:6379` by default)
-   A Google API Key (for the AI model, e.g., Gemini)

### Installation

```bash
git clone https://github.rashadmin/hospital_agents.git
cd hospital_agents
pip install -r requirements.txt # (assuming a requirements.txt exists with: Flask, LangGraph, redis, python-dotenv, langchain_core, typing_extensions, SQLAlchemy)
```
**Note**: A `requirements.txt` file is assumed for the `pip install` command. You might need to create it with the following content:
```
Flask
langgraph
redis
python-dotenv
langchain-core
typing_extensions
SQLAlchemy
```

### Environment Variables

Create a `.env` file in the root directory of the project:

```env
SECRET_KEY=your_flask_secret_key_here
GOOGLE_API_KEY=your_gemini_api_key_here
# DATABASE_URL=your_database_url_here # Uncomment and set if using a database
```

### Run

To start the Flask application:

```bash
python hospital_agent.py
```

### Interactive Shell

For interactive development and debugging, you can access the LangGraph `graph` object in the Flask shell:

```bash
flask shell
>>> graph.invoke({"messages": "your initial message"})
```

## 📖 Usage

### API Interaction (Future Usage)

The application exposes an endpoint for interacting with the agent. The core logic for invoking the graph is currently commented out but illustrates the intended usage:

```python
# Example of intended API interaction (conceptual)
# import requests
#
# url = "http://127.0.0.1:5000/agent"
# payload = {"input": "What is the patient's status?"}
# headers = {"Content-Type": "application/json"}
#
# response = requests.post(url, json=payload, headers=headers)
# print(response.json())
```

### Asynchronous Request Flow

Requests are expected to be pushed to a Redis stream named 'requests'. The background listener will then pick these up and update the LangGraph agent's state.

```python
# Example of pushing a request to Redis (conceptual)
# import redis
# import json
#
# r = redis.Redis(host='localhost', port=6379, db=0)
# request_data = {"thread_id": "unique_thread_id_123", "message": "Schedule an appointment."}
# r.xadd('requests', {'data': json.dumps(request_data)})
```

## 📚 Resources

-   [Flask Documentation](https://flask.palletsprojects.com/en/latest/) — Web framework
-   [LangGraph Documentation](https://langgraph.readthedocs.io/en/latest/) — Agent framework
-   [Redis Documentation](https://redis.io/docs/) — Message queue/stream
-   [python-dotenv GitHub](https://github.com/theskumar/python-dotenv) — Environment variable management
-   [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/latest/) — ORM for database interaction (implied)
-   [Python Threading Documentation](https://docs.python.org/3/library/threading.html) — Concurrency
-   [LangChain Core Documentation](https://api.python.langchain.com/en/latest/core/langchain_core.html) — Core components for LangChain

## 📄 License

MIT © rashadmin

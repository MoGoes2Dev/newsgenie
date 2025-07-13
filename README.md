# newsgenie

Agentic Framework Project 



\# 🧞‍♂️ NewsGenie – An AI-Powered Information and News Assistant



NewsGenie is an intelligent, AI-powered assistant designed to help users stay informed in today’s fast-paced digital world. It offers a unified platform for real-time news curation, general query responses, and misinformation filtering—all accessible through a clean, user-friendly interface.



---



\## 🚀 Features



\- \*\*Conversational AI Chatbot\*\*  

&nbsp; Distinguishes between general questions and news-related queries using natural language understanding.



\- \*\*Real-Time News Integration\*\*  

&nbsp; Retrieves live updates in categories such as technology, finance, and sports using a news API.



\- \*\*Web Search Augmentation\*\*  

&nbsp; Dynamically pulls external data to enrich chatbot responses when needed.



\- \*\*LangGraph-Based Workflow\*\*  

&nbsp; Efficient query management and contextual handling using a LangGraph-powered architecture.



\- \*\*Streamlit UI\*\*  

&nbsp; Responsive frontend for selecting news categories, typing queries, and viewing results with session continuity.



\- \*\*Robust Error Handling\*\*  

&nbsp; Includes fallback mechanisms for API failures, missing keys, and empty results.



---



\## 🧩 Tech Stack



| Component            | Tool / Framework     |

|---------------------|----------------------|

| Frontend Interface  | Streamlit            |

| AI Chatbot          | OpenAI / LangChain   |

| Workflow Management | LangGraph            |

| News API            | (e.g., NewsAPI, GNews) |

| Web Search          | DuckDuckGo / SerpAPI |

| Language            | Python               |



---



\## 📌 Project Structure

newsgenie/

│

├── app.py # Streamlit app entry point

├── workflow.py # LangGraph workflow for query handling

├── utils/ # API integrations and support modules

├── assets/ # Images, icons, and visual assets

├── requirements.txt # Python dependencies

└── .gitignore # Ignores venv, pycache, etc.




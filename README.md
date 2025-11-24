Text To Math Solver & Wikipedia Searcher ✍️

A smart conversational agent built with Streamlit, LangChain, and Groq (using the gemma2-9b-it model). This application is designed to solve text-based mathematical problems, perform logical reasoning, and look up information on Wikipedia when necessary.

🚀 Features

Text-to-Math Resolution: Solves complex word problems by converting text into mathematical operations using LLMMathChain.

Logical Reasoning: Handles logic-based questions that require reasoning beyond simple calculation.

Wikipedia Integration: Fetches real-time information for general knowledge queries using the WikipediaAPIWrapper.

ReAct Agent: Utilizes a "Reasoning and Acting" agent approach to determine the best tool for the job (Math vs. Search vs. Logic).

Interactive UI: Clean chat interface built with Streamlit.

Transparent Execution: Displays the agent's thought process (observations and actions) using StreamlitCallbackHandler.

🛠️ Tech Stack

Python 3.8+

Streamlit: For the web interface.

LangChain: For agent orchestration and tool management.

LangChain Groq: To interface with Groq's high-speed inference engine.

Wikipedia API: For external knowledge retrieval.

⚙️ Prerequisites

Before running the application, ensure you have:

Python installed on your machine.

A Groq API Key. You can get one for free at console.groq.com.

📥 Installation

Clone the repository:

git clone [https://github.com/chakri0176/text_math_solver_bot.git] | (https://github.com/your-username/text-to-math-solver.git)
cd text-to-math-solver


Create a virtual environment (Optional but recommended):

python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


▶️ Usage

Run the Streamlit app:

streamlit run app.py


Authenticate:

The app will open in your browser.

Enter your Groq API Key in the sidebar to activate the bot.

Ask Questions:

Enter your math word problem or general question in the text area.

Click "Give me the answer".

Example Queries

"I have 5 apples, I ate 2 and bought 10 more. How many do I have?"

"What is the square root of the average distance from Earth to the Sun?" (Combines Wikipedia + Math)

"If a train travels 60 mph for 2.5 hours, how far did it go?"

🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
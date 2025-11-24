import streamlit as st
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks import StreamlitCallbackHandler
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_groq import ChatGroq


st.set_page_config(page_title="Text To Math Solver",page_icon="✍️")

st.title("Text To Math Solver and Wikipedia Searcher ✍️")

#api_key 
groq_api_key = st.sidebar.text_input(label="Enter your groq api key",type="password")

if not groq_api_key:
    st.warning("Enter the groq api key to use the bot")
    st.stop()

llm = ChatGroq(groq_api_key = groq_api_key,model="gemma2-9b-it")


#initialize the search tools

wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(name="Wikipedia",func=wikipedia_wrapper.run,description="A Tool for searching various topics available on wikipedia.")

#initialize the math tools

math_chain = LLMMathChain.from_llm(llm=llm)
math_tool = Tool(name="Calculator",func=math_chain.run,description="A Tool for answering math realted queries..")

prompt="""
Your a agent tasked for asking user Mathematical question.Logically answer the solution and display it point wise for the question.
Question:{question}
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt
)

#combine all the tools into chain
chain = LLMChain(llm=llm,prompt=prompt_template)


reasoning_tool = Tool(name="Reasoning tool",func=chain.run,description="A tool for answering logic based questions")

create_agent = initialize_agent(
    tools=[wikipedia_tool,math_tool,reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_error=True
)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role":"assistant","content":"Hi, I am a help ful agent who solves math equations which given in a text format!"}]
    
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
    
question=st.text_area("Enter The Question You Want To Ask...?",placeholder="I have two apples and 5 bananas and i gave 3 bananas and ate 1 apples, how many fruits do i left with.?")

if st.button("Give me the answer"):
    if question:
        with st.spinner("Generating..."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)
            
            st_callback = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response = create_agent.run(st.session_state.messages,callbacks=[st_callback])
            
            st.session_state.messages.append({"role":"assitant","content":response})
            st.write("# Response:")
            st.success(response)
            
    else:
        st.warning("Please enter the question...?")
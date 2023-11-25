import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from build_customized_multi_agents import main as run_agents
from startup import main as startup_main

# Sidebar for selecting functionality
functionality = st.sidebar.selectbox(
    "Select functionality:",
    ("Startup", "Multi-Agent System")
)

st.title(f'MetaGPT {functionality} Interface')

if functionality == "Startup":
    # Input for startup parameters
    idea = st.text_input("Enter your startup idea:")
    investment = st.number_input("Enter your investment amount:", min_value=0.0)
    n_round = st.number_input("Enter number of rounds:", min_value=1, format="%i")
    code_review = st.checkbox("Use code review?")
    run_tests = st.checkbox("Run tests?")
    implement = st.checkbox("Implement?")

    if st.button('Run Startup'):
        # Schedule the startup function to run concurrently
        asyncio.create_task(startup_main(idea=idea, investment=investment, n_round=n_round, code_review=code_review, run_tests=run_tests, implement=implement))

elif functionality == "Multi-Agent System":
    # Input for multi-agent system parameters
    idea_input = st.text_input("Enter your idea for the agents to work on:")
    investment_input = st.number_input("Enter the investment amount for the agents:", min_value=0.0)
    n_round_input = st.number_input("Enter the number of rounds for the agents:", min_value=1, format="%i")
    add_human_input = st.checkbox("Add human to the team?")

    if st.button('Run Agents'):
        # Schedule the multi-agent system function to run concurrently
        asyncio.create_task(run_agents(idea=idea_input, investment=investment_input, n_round=n_round_input, add_human=add_human_input))



# ...

# Button to run the multi-agent system asynchronously
if st.button('Run Agents'):
    # Run the main function from build_customized_multi_agents.py asynchronously
    st.experimental_rerun(run_agents(idea=idea_input, investment=investment_input, n_round=n_round_input, add_human=add_human_input))
# Input for user search query
search_query = st.text_input("Enter your search query:")

# Button to perform search
if st.button('Search'):
    # Call search function with user query
    results = search(search_query)
    # Display results
    for result in results:
        st.write(result)

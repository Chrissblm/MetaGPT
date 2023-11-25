import streamlit as st
from examples.build_customized_multi_agents import main as run_agents

st.title('MetaGPT Startup Interface')

# Input for user parameters
idea = st.text_input("Enter your startup idea:")
investment = st.number_input("Enter your investment amount:", min_value=0.0)
n_round = st.number_input("Enter number of rounds:", min_value=1, format="%i")
code_review = st.checkbox("Use code review?")
run_tests = st.checkbox("Run tests?")
implement = st.checkbox("Implement?")

# Input for multi-agent system parameters
idea_input = st.text_input("Enter your idea for the agents to work on:")
investment_input = st.number_input("Enter the investment amount for the agents:", min_value=0.0)
n_round_input = st.number_input("Enter the number of rounds for the agents:", min_value=1, format="%i")
add_human_input = st.checkbox("Add human to the team?")

# Button to run the multi-agent system
if st.button('Run Agents'):
    # Run the main function from build_customized_multi_agents.py
    run_agents(idea=idea_input, investment=investment_input, n_round=n_round_input, add_human=add_human_input)

import asyncio

# ...

if st.button('Run Agents'):
    # Run the main function from build_customized_multi_agents.py
    asyncio.run(run_agents(idea=idea_input, investment=investment_input, n_round=n_round_input, add_human=add_human_input))
elif st.button('Search'):
    # Call search function with user query
    results = search(search_query)
    # Display results
    for result in results:
        st.write(result)

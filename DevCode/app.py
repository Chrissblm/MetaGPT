import streamlit as st
from startup import main

st.title('MetaGPT Startup Interface')

# Input for user parameters
idea = st.text_input("Enter your startup idea:")
investment = st.number_input("Enter your investment amount:", min_value=0.0)
n_round = st.number_input("Enter number of rounds:", min_value=1, format="%i")
code_review = st.checkbox("Use code review?")
run_tests = st.checkbox("Run tests?")
implement = st.checkbox("Implement?")

# Input for search query
search_query = st.text_input("Enter your search query:")

if st.button('Start Startup'):
    # Call main function with user parameters
    main(idea, investment, n_round, code_review, run_tests, implement)
elif st.button('Search'):
    # Call search function with user query
    results = search(search_query)
    # Display results
    for result in results:
        st.write(result)

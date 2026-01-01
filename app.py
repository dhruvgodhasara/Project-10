import streamlit as st
from langchain_config import llm_chain 

st.title('Equity Research News Tool')
st.write('Enter your query to get the latest news articles summarized.')
query = st.text_input('Query') 
if st.button('Get News'): 
    if query:
         response = llm_chain.run({'query': query})
         st.write('### Summary:') 
         st.write(response)
    else:
        st.write('Please enter a query')


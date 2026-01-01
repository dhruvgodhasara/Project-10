import streamlit as st
from langchain_config import llm_chain
import time
from datetime import datetime, timedelta
import yfinance
# Correct import statement for NewsApiClient
from newsapi.newsapi_client import NewsApiClient
from config import api_key

# Initialize NewsAPI client (replace with your API key)
newsapi_key = api_key
newsapi_client = NewsApiClient(api_key=newsapi_key)

# Function to fetch the latest news
@st.cache(ttl=300)  # Cache results for 5 minutes
def fetch_latest_news(query):
    try:
        # Fetch latest news using top-headlines endpoint
        top_headlines = newsapi_client.get_top_headlines(q=query, language='en')
        if top_headlines['articles']:
            return top_headlines['articles'][0]
        else:
            return None
    except Exception as e:
        st.error(f"Error fetching news: {e}")
        return None

# Function to summarize news using LangChain
@st.cache(ttl=300)  # Cache results for 5 minutes
def summarize_news(query):
    return llm_chain.run({'query': query})

# Initialize session state
if 'latest_news' not in st.session_state:
    st.session_state.latest_news = None
if 'last_updated' not in st.session_state:
    st.session_state.last_updated = datetime.now() - timedelta(minutes=5)  # Force initial update

st.title('Equity Research News Tool')
st.write('Enter your query to get the latest news articles summarized.')

query = st.text_input('Query')

if st.button('Get News'):
    if query:
        # Fetch and summarize news if not updated recently
        if datetime.now() - st.session_state.last_updated >= timedelta(minutes=5):
            st.session_state.latest_news = summarize_news(query)
            st.session_state.last_updated = datetime.now()
        # Display latest news
        st.write('### Summary:')
        st.write(st.session_state.latest_news)
    else:
        st.write('Please enter a query')

# Auto-refresh every 5 minutes (Streamlit handles this automatically)
# No need for the while loop and st.rerun()
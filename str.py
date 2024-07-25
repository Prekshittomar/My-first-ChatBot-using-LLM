import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Set your API key environment variable
os.environ['GOOGLE_API_KEY'] = 'AIzaSyC2SogygWzqa4F5N2Dxtiw8bopsXDTxlPU'

# Title of the Streamlit app
st.title('Ask Your Question')

# Text input for user question
user_input = st.text_input('Ask your question')

# Initialize the ChatGoogleGenerativeAI model
try:
    llm = ChatGoogleGenerativeAI(model='gemini-pro')
except Exception as e:
    st.error(f"Failed to initialize the model: {e}")
    st.stop()

# Check if the user has entered any input
if user_input:
    try:
        # Debug: Print the user input
        st.write(f"User input: {user_input}")

        # Invoke the model with user input
        result = llm.invoke(user_input)

        # Extract and display only the content
        
        st.write('Your result is:', result.content)
    except Exception as e:
        # Handle any exceptions that occur
        st.error(f"An error occurred: {e}")
else:
    st.write("Please enter a question to get a response.")

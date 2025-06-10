import streamlit as st
import openai
import os

# Set your API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🤖 GenAI Product Ideator")
st.write("Enter an idea or domain. Get a detailed GenAI-based product concept!")

# Input from user
topic = st.text_input("Enter a topic or domain", placeholder="e.g., Generative AI for travel planning")

if st.button("Generate Idea"):
    if topic:
        prompt = f"""
You are an expert product consultant. Given the topic: "{topic}", provide a detailed GenAI-based product idea including:

1. Overview of the concept
2. Innovative angle or differentiation. 
3. Suggested features and try to relate to real time custoner needs
4. Recommended technology stack
5. Target users and their benefits.
6. Potential business impact
7. Challenges and considerations for implementation.
8. Future enhancements or iterations.
9. Market trends and how this idea aligns with them.


Respond in 10+ lines with bullet points where helpful.
"""
        try:
            with st.spinner("Generating your GenAI product idea...Please wait my friend!"):
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=700
                )            

                result = response['choices'][0]['message']['content']
            
            st.subheader("🔍 GenAI Idea Summary")
            st.markdown(result)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a topic.")

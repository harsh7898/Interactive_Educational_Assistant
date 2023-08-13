#pip install openai

#pip install streamlit

import openai
import streamlit as st

# Configure OpenAI API key
openai.api_key = " "



def generate_explanation(question):
    prompt = f"Question: {question}\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,  # Increase max_tokens for longer responses
        temperature=0.7
    )
    return response.choices[0].text.strip()

def main():
    st.markdown('<link rel="stylesheet" href="styles.css">', unsafe_allow_html=True)


    st.title("Interactive Educational Assistant")
    st.sidebar.title("User Options")
    question = st.text_area("Enter your question or topic:", key="user_input")
    st.markdown('<style>textarea{margin-bottom:20px;}</style>', unsafe_allow_html=True)


    if st.button("Generate Explanation"):
        if question:
            explanation = generate_explanation(question)
            st.subheader("Explanation:")
            st.write(explanation)

if __name__ == "__main__":
    main()




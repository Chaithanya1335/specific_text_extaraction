import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

# Page configuration settings
st.set_page_config("Experience Extraction from Text ",layout='wide')

st.title("Experience Extraction from Job Description")

st.divider()


# Getting api key from streamlit app
api_key = st.sidebar.text_input("enter your api key here",type='password')

jd = st.text_area("### Enter your job description")

if api_key and jd:
    compound_model = ChatGroq(model_name = 'compound-beta-mini',api_key=api_key)

    # creating prompt templete
    prompt_template = """
    You are an expert assistant helping with job description analysis.

    Your task is to analyze the job description and extract experience information based on the following rules:

    Rules:
    1. If the job description mentions the **total overall professional experience required for the job**, extract only that value.
    2. If no total experience is mentioned, extract the years of experience required for each individual skill, tool, or technology mentioned.
    3. When extracting per-skill experience, list them in the format: 
    - [Skill/Tool]: [X years, X+ years, X-Y years]

    Response Format:
    - If total experience is mentioned:
    experience: [X years, X-Y years, etc.]

    - If no total experience is mentioned:
    experience_by_skill:
    - [Skill/Tool]: [X years]
    - [Skill/Tool]: [X years]
    (and so on)

    If no experience requirements at all are mentioned, respond exactly as:
    experience: None

    Job Description:
    {context}
    """

    prompt = ChatPromptTemplate.from_template(
        template=prompt_template,
        input_variable=['context']
    )


    # LCEL (Langchain Expression Language)
    chain =  prompt|compound_model


    # Getting Response from The chain
    response =  chain.invoke(jd).content

    # writing the extracted experience in streamlit

    st.markdown(" ### **Response :**")

    st.code(response)

else:
    st.warning("Please Enter your Groq API Key")
    
    # Button Link to get api key
    st.link_button("To Get api key click here",url="https://console.groq.com/keys")


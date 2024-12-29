import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os
import random

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
print(MISTRAL_API_KEY)
if not MISTRAL_API_KEY:
    st.error("Mistral API key is missing! Please set it in your environment variables.")
    st.stop()

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

try:
    faiss_db = FAISS.load_local(
        "faiss_index",
        embedding_model,
        allow_dangerous_deserialization=True
    )
except Exception as e:
    st.error(f"Error loading FAISS database: {e}")
    st.stop()

try:
    chat_model = ChatMistralAI(
        model="ministral-8b-latest",
        temperature=0.7,
        api_key=MISTRAL_API_KEY
    )
except Exception as e:
    st.error(f"Failed to initialize Mistral AI: {e}")
    st.stop()

prompt = ChatPromptTemplate.from_template(
    "Rewrite the following recipe using {ingredient} as the main focus and a different cooking method."
    "Make it simpler or more unique. Recipe: {recipe}"
)

st.title("AI Recipe Recommendation App 🍳")
st.write("Enter the ingredients you have, and I'll suggest a recipe for you!")

query = st.text_input("Enter ingredients (comma-separated):")

if query:
    try:
        if "previous_query" not in st.session_state or st.session_state.previous_query != query:
            results = faiss_db.similarity_search(query, k=50)
            random_results = random.sample(results, 10)

            recipe_names = [result.page_content.split("\n\n")[0] for result in random_results]

            st.session_state.random_results = random_results
            st.session_state.recipe_names = recipe_names
            st.session_state.previous_query = query

        selected_recipe_name = st.selectbox("Pick a recipe to modify:", st.session_state.recipe_names)

        if st.button("Regenerate Random Recipes"):
            results = faiss_db.similarity_search(query, k=50)
            random_results = random.sample(results, 10)
            recipe_names = [result.page_content.split("\n\n")[0] for result in random_results]

            st.session_state.random_results = random_results
            st.session_state.recipe_names = recipe_names

            st.experimental_rerun()

        selected_recipe_content = next(result.page_content for result in st.session_state.random_results if result.page_content.split("\n\n")[0] == selected_recipe_name)

        if selected_recipe_content:
            input_data = prompt.format_messages(
                ingredient=query,
                recipe=selected_recipe_content
            )

            response = chat_model.invoke(input_data)

            st.subheader("Reformulated Recipe Suggestion:")
            st.write(response.content)

    except Exception as e:
        st.error(f"Error generating recipe: {e}")

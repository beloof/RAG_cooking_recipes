import pandas as pd
import ast
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

file_path = "recipes.csv"
df = pd.read_csv(file_path)

df = df[["Title", "Cleaned_Ingredients", "Instructions"]]
df['Cleaned_Ingredients'] = df['Cleaned_Ingredients'].apply(lambda x: ast.literal_eval(x))
df['content'] = (
    df['Title'] + "\n\nIngredients:\n" +
    df['Cleaned_Ingredients'].apply(lambda x: ", ".join(x)) + 
    "\n\nInstructions:\n" + df['Instructions']
)
new_df = df['content'].dropna()
new_df.to_csv("recipes_cleaned.csv")

cleaned_df = pd.read_csv("recipes_cleaned.csv")
documents = cleaned_df["content"].tolist()
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
faiss_db = FAISS.from_texts(documents, embedding_model)
faiss_db.save_local("faiss_index")

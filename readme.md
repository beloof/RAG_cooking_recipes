# AI Recipe Recommendation App 🍳

This project is a web app built using **Streamlit**, **LangChain**, **Mistral AI**, and **FAISS**. It implements **Retrieval-Augmented Generation (RAG)** and **Large Language Models (LLMs)** to generate creative and unique recipes based on user-provided ingredients. 

The app fetches relevant recipes from a pre-built **FAISS** index of recipes, utilizes **LLMs** for natural language understanding and processing, and reformulates the selected recipe using **AI-driven creativity** to suggest a new dish.

---

## Features
- **RAG Pipeline**: Combines information retrieval with language generation to provide relevant and customized recipe suggestions.
- **Retrieve Recipes**: Find recipes based on ingredients using FAISS for efficient vector similarity search.
- **AI Reformulation with LLMs**: Generate new and creative recipes by leveraging the power of Mistral AI.
- **Regenerate Recipes**: Regenerate random recipes at the click of a button for variety and inspiration.

---



## Requirements

To run this project locally, you need the following Python libraries:

- `pandas`
- `langchain`
- `langchain_community`
- `streamlit`
- `faiss-cpu`
- `langchain_mistralai`
- `huggingface-hub`
- `python-dotenv`
- `sentence-transformers`

---

## Setup

### **1. Clone the repository**

```
git clone https://github.com/yourusername/ai-recipe-recommendation-app.git
```

### **2. Install dependencies**

```
cd ai-recipe-recommendation-app
pip install .
```

### **3. Set up your environment variables**

- Update the `.env` file and add your Mistral API key:

```
MISTRAL_API_KEY=your_mistral_api_key
```


### **4. Prepare the FAISS Index** *(Optional)*  

The repository already includes preprocessed data (`recipes_cleaned.csv`) and a pre-built FAISS index stored in the **`faiss_index/`** directory.  

However, if you wish to modify the dataset or rebuild the FAISS index from scratch, you can run the **data preparation script**:  

```
python data_prep.py  
```  

### **5. Launch the Streamlit app**
```
streamlit run file_location\rag_app.py  
```
---

## Repository Structure

```
ai-recipe-recommendation-app/
├── faiss_index/               # Directory to store FAISS index files  
├── data_prep.py               # Script to prepare the dataset and build FAISS index  
├── rag_app.py                 # Main Streamlit app for recipe generation  
├── recipes.csv                # Original dataset of recipes  
├── recipes_cleaned.csv        # Preprocessed dataset with clean recipes  
├── setup.py                   # Setup file for dependency installation  
├── .env                       # Environment variables 
└── README.md                  # Project documentation  
```

---
## Data Source
The recipe data used in this project is sourced from the [recipe-dataset repository by josephrmartinez](https://github.com/josephrmartinez/recipe-dataset)..

## Licenses

- The **code** in this repository is licensed under the [MIT License](LICENSE.txt).
- The **data** (including `recipes.csv` and `recipes_cleaned.csv`) is licensed under the **[Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)](https://creativecommons.org/licenses/by-sa/3.0/)** license.

---

## Usage Example
- Enter ingredients like:
```
chicken, rosemary, garlic  
```
- Pick a recipe from the dropdown menu based on its title.
- Click Regenerate Random Recipes to fetch new suggestions.
- View the AI-generated, reformulated recipe in the output section.

---

## acknowledgement
Special thanks to [codebasics](https://www.youtube.com/@codebasics) for sharing informative videos




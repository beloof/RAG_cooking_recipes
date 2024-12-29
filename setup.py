from setuptools import setup, find_packages

setup(
    name="AI Recipe Recommendation App",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "langchain",
        "streamlit",
        "faiss-cpu",
        "sentence-transformers",
        "langchain_community",
        "langchain_mistralai",
        "huggingface-hub",
        "python-dotenv",
    ],
    author="LASSIOUED Badis",
    description="A web app to generate AI-powered recipe suggestions.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/beloof/RAG_cooking_recipes",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

from setuptools import setup, find_packages

setup(
    name="AI Recipe Recommendation App",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "ast",
        "langchain",
        "langchain_mistralai",
        "streamlit",
        "huggingface-hub",
        "faiss-cpu",
        "python-dotenv",
        "sentence-transformers",
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8",
        ]
    },
    entry_points={
        'console_scripts': [
            'ai_recipe_app = app:main',  # Change 'app:main' to the correct entry point
        ]
    },
    author="Your Name",
    author_email="your_email@example.com",
    description="A web app to generate AI-powered recipe suggestions.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ai-recipe-recommendation-app",  # Change to your GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

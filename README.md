<h1 align="center">🧠🔍📖 DocuSense AI Assistant</h1>

<h3 align="center">Your Intelligent Assistant for Documents and Coding.</h3>


<img align="right" alt="AI Assistant" width="400" src="https://miro.medium.com/v2/resize:fit:1400/1*6z7Q8ZJXwWlU9ZvZz5Zz9g.gif">

<br>
<h2 align="left">About This Project:</h2>

<p align="left">
This is a <b>Streamlit-based application</b> that combines multiple AI-powered services into one cohesive platform. The app currently supports the following services:
</p>

- **Document Assistant**: Analyze and query research documents using advanced Retrieval-Augmented Generation (RAG) techniques. (rag_deep.py)

<be>

![image alt](https://github.com/saquib5005/DocuSense---Your-Intelligent-Document-Assistant/blob/ad9a66b53e09658d00de68244732a1dde9d13d3b/Streamlit%20Interface%20Images/Screenshot%202025-03-02%20143400.png)
![image alt](https://github.com/saquib5005/DocuSense---Your-Intelligent-Document-Assistant/blob/bad85c24067564f15a153ff4143bff7e280bf1e7/Streamlit%20Interface%20Images/Screenshot%202025-03-02%20143601.png)
<br>


- **Coding Assistant**: Get help with coding-related tasks like generating code snippets, debugging, or explaining concepts. (app.py)


![image alt](https://github.com/saquib5005/DocuSense---Your-Intelligent-Document-Assistant/blob/bad85c24067564f15a153ff4143bff7e280bf1e7/Streamlit%20Interface%20Images/Screenshot%202025-03-02%20142954.png)
![image alt](https://github.com/saquib5005/DocuSense---Your-Intelligent-Document-Assistant/blob/bad85c24067564f15a153ff4143bff7e280bf1e7/Streamlit%20Interface%20Images/Screenshot%202025-03-02%20142819.png)




<h2 align="left">Features:</h2>

<p align="left">
</p>

- Modular design for easy addition of new services.
- User-friendly interface powered by Streamlit.
- Advanced AI models utilizing LangChain, Ollama, and other state-of-the-art tools.
- Scalable architecture designed to handle multiple services without compromising performance.
</p>

<br>
<h2 align="left">📦💻Installation:</h2>

<p align="left">
1. Clone the repository:
</p>

```bash
git clone https://github.com/your-username/DocuSense---Your-Intelligent-Document-Assistant.git
cd DocuSense---Your-Intelligent-Document-Assistant
```

<p align="left">


2. Install the required dependencies:
</p>

```bash
pip install -r requirements.txt
```
<p align="left">


3. Run the application:
</p>

```bash
streamlit run app.py
```
<p align="left">


4. Access the app in your browser at the URL provided by Streamlit (usually <code>http://localhost:8501</code>).
</p>

<br>
<h2 align="left">Project Structure:</h2>

<p align="left">


```bash
project_root/
│
├── main.py                       # Main application file (entry point)
├── rag_deep.py                   # Document Assistant logic (PDF processing and RAG)
├── app.py                        # Coding Assistant logic (code generation and debugging)
├── document_store/               # Directory for storing uploaded PDFs
│ └── pdfs/                          # Uploaded PDFs are stored here
├── requirements.txt              # List of Python dependencies
├── .gitignore                    # Files and directories to ignore when pushing to GitHub
└── README.md                     # This file (project documentation)
``` 


</p>

<br>
<h2 align="left">Usage:</h2>

<p align="left">
<h3 align="left">📄 Document Assistant</h3>
- Upload a PDF document using the "Document Assistant" service.
- Ask questions about the content of the document.
- The app will analyze the document and provide concise answers based on the context.
</p>

<p align="left">
<h3 align="left">💻 Coding Assistant</h3>
- Run app.py using Streamlit
- Enter your coding-related question (e.g., "How to sort a list in Python?").
- The app will generate a relevant response or code snippet.
</p>



<br>
<h2 align="left">Connect with Me:</h2>

<p align="left">
<a href="https://linkedin.com/in/your-username" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" /></a>
<a href="https://kaggle.com/your-username" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="Kaggle" height="30" width="40" /></a>
<a href="https://instagram.com/your-username" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="30" width="40" /></a>
<a href="https://medium.com/@your-username" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/medium.svg" alt="Medium" height="30" width="40" /></a>
</p>

<br>
<h2 align="left">License:</h2>

<p align="left">

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
</p>



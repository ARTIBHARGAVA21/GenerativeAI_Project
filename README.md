# GenerativeAI_Project
# 🤖 Generative AI Projects Collection

A collection of Generative AI applications built using Python, LangChain, Mistral AI, Hugging Face Embeddings, Pydantic Output Parsers, and Streamlit.

## 🚀 Features

* AI Chatbot using Mistral AI
* Structured Output Generation using Pydantic Parser
* Hugging Face Embeddings
* Local LLM Integration
* Streamlit-based User Interfaces
* Prompt Engineering with LangChain
* Environment Variable Management using dotenv

---

## 📁 Project Structure

```text
GenerativeAI/
│
├── chatmodels/
│   ├── chat.py
│   ├── chatbot.py
│   ├── hugging.py
│   ├── localmodel.py
│   ├── Uichatbot.py
│   └── Uichatchoicesbot.py
│
├── embeddingmodels/
│   ├── embeddings.py
│   └── huggingface_embedding.py
│
├── mistrabot/
│   ├── chatUi.py
│   ├── core.py
│   ├── PydanticParser.py
│   └── PydanticParserUI.py
│
├── .env
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

---

# 🛠 Technologies Used

* Python
* LangChain
* Mistral AI
* Hugging Face
* Pydantic
* Streamlit
* dotenv

---

# 💬 Chatbot Project

This chatbot uses LangChain and Mistral AI to generate intelligent conversational responses.

### Features

* Interactive Chat Interface
* Conversation History
* Prompt Templates
* Mistral AI Integration
* Streamlit UI

### Run

```bash
streamlit run chatmodels/Uichatbot.py
```

---

# 📊 Pydantic Parser Project

The Pydantic Parser project extracts structured information from unstructured text using LangChain Output Parsers.

### Features

* Structured JSON Output
* Type Validation
* Data Extraction
* Error Handling
* Streamlit User Interface

### Example

Input:

```text
Inception is a 2010 science fiction film directed by Christopher Nolan. It stars Leonardo DiCaprio and has a rating of 8.8.
```

Output:

```json
{
  "name": "Inception",
  "release_year": 2010,
  "genre": ["Science Fiction"],
  "director": "Christopher Nolan",
  "cast": ["Leonardo DiCaprio"],
  "rating": 8.8
}
```

### Run

```bash
streamlit run mistrabot/PydanticParserUI.py
```

---

# 🔍 Embedding Models

The embedding module demonstrates text embedding generation using Hugging Face models.

### Features

* Text Vectorization
* Semantic Search
* Embedding Generation
* Local Embedding Models

### Run

```bash
python embeddingmodels/huggingface_embedding.py
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <repository-url>
cd GenerativeAI
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root directory.

```env
MISTRAL_API_KEY=your_mistral_api_key
```

---

# ▶️ Running Streamlit Applications

### Chatbot UI

```bash
streamlit run chatmodels/Uichatbot.py
```

### Chatbot Choice UI

```bash
streamlit run chatmodels/Uichatchoicesbot.py
```

### Pydantic Parser UI

```bash
streamlit run mistrabot/PydanticParserUI.py
```

---

# 📚 Learning Outcomes

Through these projects, I gained practical experience in:

* Prompt Engineering
* LangChain Framework
* LLM Integration
* Streamlit Application Development
* Output Parsing
* Vector Embeddings
* Environment Management
* AI Application Development

---



---

# 📄 License

This project is licensed under the MIT License.

# 🔥 TextForge - Advanced NLP Analytics & Visualization

<div align="center">

![TextForge Logo](https://img.shields.io/badge/TextForge-NLP%20Analytics-blue?style=for-the-badge&logo=python&logoColor=white)

**A comprehensive Natural Language Processing platform for interactive text analysis and visualization**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![NLTK](https://img.shields.io/badge/NLTK-3.8.1-orange.svg)](https://nltk.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Demo](#demo) • [Features](#features) • [Installation](#installation) • [Usage](#usage) • [Contributing](#contributing)

</div>

---

## 🌟 Features

### 📝 **Text Processing**
- **Tokenization**: Word, sentence, whitespace, and blankline tokenization
- **Stemming**: Porter, Lancaster, and Snowball stemmers
- **Lemmatization**: WordNet-based lemmatization for root word extraction
- **Stopwords Removal**: Filter out common English stopwords
- **N-Grams**: Configurable n-gram generation (bigrams, trigrams, etc.)

### 🔍 **Linguistic Analysis**
- **POS Tagging**: Part-of-speech tagging for grammatical analysis
- **Named Entity Recognition (NER)**: Identify people, organizations, locations
- **Chunking**: Extract noun phrases and syntactic structures
- **Word Frequency Analysis**: Statistical analysis of word occurrences

### 📊 **Visualizations**
- **Custom Word Clouds**: Beautiful spiral-pattern word clouds with Canvas
- **Interactive Charts**: Frequency analysis with Chart.js
- **Real-time Updates**: Dynamic visualization updates
- **Responsive Design**: Works on desktop and mobile devices

### 🎯 **Advanced Features**
- **Text Summarization**: Automatic text summarization using Gensim
- **Professional UI**: Modern tabbed interface with smooth animations
- **Error Handling**: Robust error handling and fallback mechanisms
- **Performance Optimized**: Efficient processing for large texts

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/textforge-nlp-analytics.git
cd textforge-nlp-analytics
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python app.py
```

4. **Open your browser:**
Navigate to `http://localhost:5000`

---

## 💻 Usage

### Basic Analysis
1. **Enter Text**: Paste or type your text in the input area
2. **Configure Options**: Select tokenization method, stemming algorithm, etc.
3. **Analyze**: Click "🚀 Analyze Text" to process
4. **Explore Results**: Navigate through different tabs to view results

### Advanced Configuration
- **Tokenization**: Choose from word, sentence, whitespace, or blankline
- **Stemming**: Select Porter, Lancaster, or Snowball stemmer
- **Processing Options**: Enable lemmatization, stopword removal, summarization
- **N-Grams**: Configure n-gram size (1-5)

### Output Tabs
- **🔤 Tokens**: View tokenization results
- **⚙️ Processing**: Stemming, lemmatization, and filtering results
- **🔍 Linguistics**: POS tags, NER entities, and noun phrase chunks
- **📈 Visualization**: Interactive word clouds and frequency charts
- **📋 Summary**: Automatic text summarization

---

## 🛠️ Tech Stack

### Backend
- **Flask**: Lightweight web framework
- **NLTK**: Natural language processing toolkit
- **Gensim**: Topic modeling and text summarization
- **NumPy**: Numerical computing
- **SciPy**: Scientific computing

### Frontend
- **HTML5**: Modern markup
- **CSS3**: Responsive styling with gradients and animations
- **JavaScript**: Interactive functionality
- **Chart.js**: Data visualization library
- **Custom Canvas**: Word cloud rendering

---

## 📁 Project Structure

```
TextForge/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── style.css         # CSS styling
│   └── script.js         # JavaScript functionality
└── .vscode/
    └── launch.json       # VS Code configuration
```

---

## 🔧 Development

### Running in Development Mode
```bash
# Set environment variables
export FLASK_ENV=development
export FLASK_DEBUG=1

# Run the application
python app.py
```

### VS Code Setup
1. Open the project folder in VS Code
2. Install Python extension
3. Use `F5` to run with debugging
4. Or use integrated terminal: `python app.py`

---

## 📋 Requirements

```
Flask==2.3.3
nltk==3.8.1
gensim==4.3.2
numpy==1.24.3
scipy==1.10.1
```

---

## 🎯 Use Cases

- **Academic Research**: Analyze research papers and documents
- **Content Analysis**: Study blog posts, articles, and social media
- **Text Mining**: Extract insights from large text datasets
- **Educational**: Learn NLP concepts interactively
- **Business Intelligence**: Analyze customer feedback and reviews

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

<div align="center">

**Made with ❤️ for the NLP community**

⭐ **Star this repository if you found it helpful!** ⭐

</div>

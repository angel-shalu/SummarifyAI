from flask import Flask, request, jsonify, render_template, send_from_directory
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, WhitespaceTokenizer, BlanklineTokenizer
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk import pos_tag, ne_chunk, RegexpParser
from collections import Counter
try:
    from gensim.summarization import summarize
except ImportError:
    # Fallback for newer versions of gensim where summarization is removed
    def summarize(text, word_count=50):
        sentences = text.split('.')
        return '. '.join(sentences[:3]) + '.' if len(sentences) > 3 else text
import os

# Download NLTK resources (with error handling)
import nltk.data
try:
    # Check if data already exists before downloading
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    
    try:
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('wordnet', quiet=True)
    
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)
    
    try:
        nltk.data.find('taggers/averaged_perceptron_tagger')
    except LookupError:
        nltk.download('averaged_perceptron_tagger', quiet=True)
    
    try:
        nltk.data.find('chunkers/maxent_ne_chunker')
    except LookupError:
        nltk.download('maxent_ne_chunker', quiet=True)
    
    try:
        nltk.data.find('corpora/words')
    except LookupError:
        nltk.download('words', quiet=True)
        
except Exception as e:
    print(f"Warning: Could not download some NLTK data: {e}")
    print("The application will still work with existing NLTK data.")

app = Flask(__name__)

# ----------------- HOMEPAGE ROUTE -----------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

@app.route("/process", methods=["POST"])
def process_text():
    try:
        data = request.json
        text = data.get("text", "")
        token_type = data.get("token_type", "word")
        stemmer_choice = data.get("stemmer", "None")
        lemmatize = data.get("lemmatize", False)
        ngram_n = data.get("ngram_n", 2)
        remove_stopwords = data.get("remove_stopwords", False)
        summarize_text = data.get("summarize", False)
        
        if not text or text.strip() == "":
            return jsonify({"error": "Please provide text to analyze"}), 400

        # ----------------- TOKENIZATION -----------------
        try:
            if token_type == "word":
                tokens = word_tokenize(text)
            elif token_type == "sentence":
                tokens = sent_tokenize(text)
            elif token_type == "whitespace":
                tokens = WhitespaceTokenizer().tokenize(text)
            else:
                tokens = BlanklineTokenizer().tokenize(text)
        except Exception as e:
            print(f"Tokenization error: {e}")
            tokens = text.split()  # Fallback to simple split

        # ----------------- STEMMING -----------------
        try:
            stemmed = []
            if stemmer_choice != "None":
                if stemmer_choice == "Porter":
                    ps = PorterStemmer()
                    stemmed = [ps.stem(w) for w in word_tokenize(text)]
                elif stemmer_choice == "Lancaster":
                    ls = LancasterStemmer()
                    stemmed = [ls.stem(w) for w in word_tokenize(text)]
                elif stemmer_choice == "Snowball":
                    ss = SnowballStemmer("english")
                    stemmed = [ss.stem(w) for w in word_tokenize(text)]
        except Exception as e:
            print(f"Stemming error: {e}")
            stemmed = []

        # ----------------- LEMMATIZATION -----------------
        try:
            if lemmatize:
                lemmatizer = WordNetLemmatizer()
                lemmatized = [lemmatizer.lemmatize(w) for w in word_tokenize(text)]
            else:
                lemmatized = []
        except Exception as e:
            print(f"Lemmatization error: {e}")
            lemmatized = []

        # ----------------- STOPWORD REMOVAL -----------------
        try:
            if remove_stopwords:
                stop_words = set(stopwords.words('english'))
                filtered = [w for w in word_tokenize(text) if w.lower() not in stop_words]
            else:
                filtered = []
        except Exception as e:
            print(f"Stopword removal error: {e}")
            filtered = []

        # ----------------- N-GRAMS -----------------
        try:
            if ngram_n > 1:
                ngrams_list = [" ".join(gram) for gram in ngrams(word_tokenize(text), ngram_n)]
            else:
                ngrams_list = []
        except Exception as e:
            print(f"N-grams error: {e}")
            ngrams_list = []

        # ----------------- POS & NER -----------------
        try:
            pos_tags = pos_tag(word_tokenize(text))
            ner_tree = ne_chunk(pos_tags)
            ner = []
            for subtree in ner_tree:
                if hasattr(subtree, 'label'):
                    ner.append((subtree.label(), ' '.join(c[0] for c in subtree)))
        except Exception as e:
            print(f"POS/NER error: {e}")
            pos_tags = []
            ner = []

        # ----------------- CHUNKING -----------------
        try:
            grammar = "NP: {<DT>?<JJ>*<NN.*>+}"  # Noun phrase chunking
            cp = RegexpParser(grammar)
            tree = cp.parse(pos_tags)
            chunks = []
            for subtree in tree.subtrees():
                if subtree.label() == 'NP':
                    chunks.append(" ".join([token for token, pos in subtree.leaves()]))
        except Exception as e:
            print(f"Chunking error: {e}")
            chunks = []

        # ----------------- WORD FREQUENCY -----------------
        try:
            freq = dict(Counter(word_tokenize(text)))
        except Exception as e:
            print(f"Frequency analysis error: {e}")
            freq = {}

        # ----------------- SUMMARIZATION -----------------
        try:
            if summarize_text:
                summary = summarize(text, word_count=50)
            else:
                summary = ""
        except Exception as e:
            print(f"Summarization error: {e}")
            summary = "Text too short for summarization or summarization failed."

        return jsonify({
            "tokens": tokens,
            "stemmed": stemmed,
            "lemmatized": lemmatized,
            "filtered": filtered,
            "ngrams": ngrams_list,
            "pos_tags": pos_tags,
            "ner": ner,
            "chunks": chunks,
            "frequency": freq,
            "summary": summary
        })
        
    except Exception as e:
        print(f"General processing error: {e}")
        return jsonify({"error": f"An error occurred while processing the text: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)

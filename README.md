# 🌍 Emoji-Driven Sentiment Analysis

An intelligent **NLP-based web application** that analyzes sentiment from text while taking **emojis into account**. The system detects emojis, converts them into meaningful textual descriptions, translates the input into a selected language, and performs sentiment analysis using **TextBlob**.

🔗 **Live Demo:** https://emoji-driven-sentiment-analysis.vercel.app/  
🔗 **GitHub Repository:** https://github.com/challa-swetha/emoji-driven-sentiment-analysis

---

## 📌 Overview

Traditional sentiment analysis systems often focus only on textual content and may ignore emojis. However, emojis can significantly change the emotional meaning of a sentence.

For example:

> `I got selected for the internship 🎉❤️`

The emojis **🎉** and **❤️** carry additional emotional information that should be considered when determining the sentiment.

This project addresses that limitation by:

- Detecting emojis in user input
- Extracting the semantic meaning of emojis
- Replacing emojis with meaningful textual descriptions
- Translating the input into a selected target language
- Performing sentiment analysis on the emoji-expanded text
- Displaying polarity and subjectivity scores
- Providing a simple web-based interface

The Flask application processes the input and returns the original text, emoji-expanded text, translation, emoji meanings, and sentiment results.

---

## ✨ Features

### 😊 Emoji-Aware Sentiment Analysis

The system identifies emojis and converts them into textual meanings before sentiment analysis.

Example:

```text
Input:
I am very happy today 😊❤️

Expanded:
I am very happy today [smiling face with smiling eyes] [red heart]
```

The expanded representation allows the sentiment analyzer to consider the emotional information conveyed by emojis.

---

### 🌐 Multilingual Translation

Users can specify a target language using a language code.

Examples:

```text
en → English
fr → French
es → Spanish
hi → Hindi
te → Telugu
```

The application uses `googletrans` to translate both the input text and emoji meanings.

---

### 📊 Sentiment Classification

The project uses **TextBlob** to calculate:

- Sentiment
- Polarity
- Subjectivity

The sentiment is classified as:

| Polarity | Sentiment |
|---|---|
| > 0 | Positive |
| < 0 | Negative |
| = 0 | Neutral |

The application returns the polarity and subjectivity values along with the sentiment label.

---

### 🔤 Emoji Meaning Extraction

The `emoji` Python library is used to convert emojis into textual descriptions.

For example:

```text
❤️ → red heart
😊 → smiling face
😂 → face with tears of joy
😢 → crying face
🔥 → fire
```

These meanings are then incorporated into the text before sentiment analysis.

---

## 🏗️ System Architecture

```text
                ┌───────────────────────┐
                │      User Input       │
                │  Text + Emojis        │
                └───────────┬───────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │   Emoji Detection     │
                └───────────┬───────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │ Emoji Meaning         │
                │ Extraction            │
                └───────────┬───────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │ Emoji Expansion       │
                │ 😊 → [smiling face]   │
                └───────────┬───────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │ Language Translation  │
                │     Googletrans       │
                └───────────┬───────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │ TextBlob Sentiment    │
                │ Analysis              │
                └───────────┬───────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │       Results         │
                │ Positive / Negative   │
                │ Neutral + Scores      │
                └───────────────────────┘
```

---

## 🔄 Processing Pipeline

The application follows the following workflow:

### Step 1 — User Input

The user enters a sentence containing text and optionally emojis.

```text
"I love this product 😍🔥"
```

### Step 2 — Emoji Detection

The application checks individual characters and identifies emoji characters.

### Step 3 — Emoji Interpretation

Detected emojis are converted into meaningful descriptions.

```text
😍 → smiling face with heart-eyes
🔥 → fire
```

### Step 4 — Text Expansion

The original emojis are replaced with textual representations.

```text
I love this product [smiling face with heart-eyes] [fire]
```

### Step 5 — Translation

The original input and emoji meanings can be translated into the target language.

### Step 6 — Sentiment Analysis

TextBlob calculates:

```text
Polarity
Subjectivity
Sentiment
```

### Step 7 — Result Display

The web interface displays:

- Original text
- Expanded text
- Translated text
- Emoji meanings
- Sentiment
- Polarity
- Subjectivity

These output fields correspond directly to the application's Flask processing pipeline.

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Natural Language Processing

- TextBlob
- Emoji

### Translation

- Google Translate
- `googletrans==4.0.0-rc1`

### Backend

- Flask

### Web Server

- Gunicorn

### Frontend

- HTML
- CSS
- Jinja2 templates

The repository's dependency file currently specifies Flask, Gunicorn, emoji, TextBlob, and `googletrans==4.0.0-rc1`.

---

## 📂 Project Structure

```text
emoji-driven-sentiment-analysis/
│
├── app.py
├── translator.py
├── index.html
├── requirements.txt
├── procfile.txt
├── translator.cpython-312.pyc
└── README.md
```

### `app.py`

The Flask application that:

- Creates the web server
- Accepts user input
- Receives the target language
- Calls the emoji translator
- Performs sentiment analysis
- Sends results to the HTML interface


### `translator.py`

Contains the main NLP functionality:

- Emoji detection
- Emoji meaning extraction
- Emoji expansion
- Text translation
- Sentiment analysis


### `index.html`

Provides the web interface where users enter text and a target language and view the generated analysis.

### `requirements.txt`

Contains the Python dependencies required to run the application.

### `procfile.txt`

Contains the Gunicorn command used to run the Flask application in a deployment environment.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/challa-swetha/emoji-driven-sentiment-analysis.git
```

### 2. Navigate to the Project

```bash
cd emoji-driven-sentiment-analysis
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

The Flask application uses port `10000` when the `PORT` environment variable is not provided.

Open:

```text
http://localhost:10000
```

---

## 💻 Usage

1. Open the web application.
2. Enter text containing emojis.
3. Enter the target language code.
4. Click **Translate & Analyze**.
5. View the generated results.

### Example

**Input**

```text
I am having a wonderful day 😊❤️
```

**Target Language**

```text
en
```

**Output**

```text
Original:
I am having a wonderful day 😊❤️

Expanded:
I am having a wonderful day [smiling face] [red heart]

Translated:
I am having a wonderful day 😊❤️

Emoji Meanings:
smiling face, red heart

Sentiment:
Positive
```

---

## 📊 Sentiment Metrics

### Polarity

Polarity represents the emotional orientation of the text.

```text
-1.0 ───────── 0 ───────── +1.0
Negative      Neutral      Positive
```

### Subjectivity

Subjectivity indicates how subjective or opinion-based the text is.

```text
0.0 → Highly objective
1.0 → Highly subjective
```

TextBlob provides both metrics through its sentiment analysis functionality.

---

## 🎯 Applications

This project can be used in several real-world NLP applications:

- 📱 Social media sentiment analysis
- 💬 Chat and messaging analytics
- 🛍️ Customer review analysis
- 📊 Customer feedback monitoring
- 😊 Emotion-aware conversational systems
- 🌐 Multilingual sentiment analysis
- 📢 Brand monitoring
- 📰 Social media analytics

---

## 🔬 Key Learning Outcomes

Through this project, the following concepts are demonstrated:

- Natural Language Processing
- Sentiment Analysis
- Emoji Semantics
- Text Preprocessing
- Multilingual Translation
- Polarity and Subjectivity Analysis
- Python Web Development
- Flask Application Development
- API-based Translation
- Web Application Deployment

---

## ⚠️ Limitations

The current implementation has some limitations:

- TextBlob provides relatively simple lexicon-based sentiment analysis.
- Sarcasm and irony can be difficult to detect.
- Context-dependent emoji meanings may not always be captured correctly.
- Translation quality depends on the external translation service.
- Some emojis may have different meanings depending on context.
- `googletrans` relies on an unofficial Google Translate interface and may be affected by service/API changes.

---

## 🔮 Future Enhancements

Possible improvements include:

### 🤖 Transformer-Based Sentiment Analysis

Replace or supplement TextBlob with modern transformer models such as:

- BERT
- RoBERTa
- DistilBERT
- XLM-RoBERTa

### 😊 Emotion Classification

Instead of only:

```text
Positive
Negative
Neutral
```

the system could detect:

```text
Joy
Sadness
Anger
Fear
Love
Surprise
Disgust
```

### 🌍 Better Multilingual NLP

Use multilingual transformer models to perform sentiment analysis directly across multiple languages.

### 🧠 Context-Aware Emoji Analysis

Develop a model that considers the relationship between emojis and surrounding words instead of treating each emoji independently.

### 📈 Analytics Dashboard

Add visualizations showing:

- Sentiment distribution
- Emoji frequency
- Emotion trends
- Language distribution
- Polarity trends

---

## 🧪 Example Test Cases

| Input | Expected Sentiment |
|---|---|
| `I love this! ❤️😊` | Positive |
| `This is amazing! 🎉🔥` | Positive |
| `I am feeling sad 😢` | Negative |
| `I hate this 😡` | Negative |
| `The meeting is at 5 PM.` | Neutral |

*Actual results depend on the TextBlob sentiment model and the exact input context.*

---

## 📌 Project Highlights

- **Domain:** Natural Language Processing
- **Project Type:** AI/ML + Web Application
- **Core Concept:** Emoji-Aware Sentiment Analysis
- **Languages:** Python, HTML, CSS
- **Framework:** Flask
- **NLP:** TextBlob
- **Translation:** Googletrans
- **Emoji Processing:** Emoji Python Library
- **Deployment:** Web application with Gunicorn

---

## 👩‍💻 Author

### Swetha Challa

B.Tech — Artificial Intelligence & Machine Learning

GitHub:  
https://github.com/challa-swetha

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is intended for educational and research purposes.

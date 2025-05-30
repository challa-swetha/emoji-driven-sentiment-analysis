from flask import Flask, render_template, request
from translator import EmojiTranslator

app = Flask(__name__)
translator = EmojiTranslator()

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        input_text = request.form["text"]
        lang = request.form["lang"].strip().lower()

        expanded_text, emoji_meanings = translator.translate_emojis(input_text, dest_lang=lang)
        translated_sentence = translator.translate_text(input_text, dest_lang=lang)
        sentiment = translator.analyze_sentiment(expanded_text)

        result = {
            "original": input_text,
            "expanded": expanded_text,
            "translated": translated_sentence,
            "sentiment": sentiment,
            "emoji_meanings": emoji_meanings,
            "lang": lang
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

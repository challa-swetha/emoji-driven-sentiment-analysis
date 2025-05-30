import unicodedata
from googletrans import Translator
import emoji
from textblob import TextBlob

class EmojiTranslator:
    def __init__(self):
        self.translator = Translator()

    def is_emoji(self, char):
        try:
            return unicodedata.category(char) == 'So' or char in emoji.EMOJI_DATA
        except TypeError:
            return False

    def get_emoji_meaning(self, char):
        demojized = emoji.demojize(char)
        meaning = demojized.strip(":").replace("_", " ")
        if meaning == char:
            return f"emoji {char}"
        return meaning

    def translate_emojis(self, text, dest_lang='en'):
        processed_parts = []
        emoji_meanings = []

        for char in text:
            if self.is_emoji(char):
                meaning = self.get_emoji_meaning(char)
                if not meaning.startswith("emoji "):
                    translated_meaning = self.translator.translate(meaning, dest=dest_lang).text
                    processed_parts.append(f"[{translated_meaning}]")
                    emoji_meanings.append(translated_meaning)
                else:
                    processed_parts.append(char)
            else:
                processed_parts.append(char)

        expanded_text = "".join(processed_parts)
        return expanded_text, emoji_meanings

    def translate_text(self, text, dest_lang='en'):
        try:
            translation = self.translator.translate(text, dest=dest_lang)
            return translation.text
        except Exception as e:
            print(f"Translation error: {e}")
            return text

    def analyze_sentiment(self, english_text):
        if not english_text or not english_text.strip():
            return {
                "sentiment": "neutral",
                "polarity": 0.0,
                "subjectivity": 0.0
            }

        blob = TextBlob(english_text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        sentiment = (
            "positive" if polarity > 0 else
            "negative" if polarity < 0 else
            "neutral"
        )

        return {
            "sentiment": sentiment,
            "polarity": polarity,
            "subjectivity": subjectivity
        }

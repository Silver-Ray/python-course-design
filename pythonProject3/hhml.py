import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob


import jieba
from snownlp import SnowNLP


nltk.download('stopwords')
nltk.download('punkt')
nltk.download('vader_lexicon')


def preprocess(text):
    stop_words=stopwords.words('english')
    word_tokens=word_tokenize(text)
    filtered_text=[word for word in word_tokens if word.lower() not in stop_words and word.isalpha()]
    return''.join(filtered_text)

text="I am very sad because the weather is bad."
preprocessed_text=preprocess(text)
print(preprocessed_text)
print()

blob=TextBlob(preprocessed_text)
score=blob.sentiment.polarity

print('score:',score)

print()


def analyze_sentiment_vader(text):
    analyze=SentimentIntensityAnalyzer()
    sentiment=analyzer.polarity_scores(text)['compound']
    return sentiment

chinese_text="今天天气真好，我很高兴"

sentiment=SnowNLP(chinese_text)
socre=sentiment.sentiments
print()

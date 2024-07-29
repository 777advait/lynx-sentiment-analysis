from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiment_analyzer(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = analyzer.polarity_scores(text)

    if sentiment_dict['compound'] >= 0.05:
        return {**sentiment_dict, "overall": "positive"}

    elif sentiment_dict['compound'] <= - 0.05:
        return {**sentiment_dict, "overall": "negative"}

    else:
        return {**sentiment_dict, "overall": "neutral"}

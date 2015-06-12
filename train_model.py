from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import recurrent as r

pipeline = Pipeline([
    ('vectorizer',  CountVectorizer()),
    ('classifier',  MultinomialNB())])

df = pd.read_csv('data/intents.csv')

features = df['text']

labels = df['intent']

features_vectorizer = CountVectorizer()
features_transformed = features_vectorizer.fit_transform(features)


def understand(text, clf):
    intent = clf.predict([text])[0]
    e = r.RecurringEvent()
    e.parse(text)
    params = e.get_params()
    return dict(intent=intent, frequency=params['freq'], interval=params['interval'])


examples = ["Hey", "Add new task create report every Friday at 11am"]

pipeline.fit(features, labels)

res = understand(examples[1], pipeline)

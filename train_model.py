from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

df = pd.read_csv('data/intents.csv')

features = df[['text']]

labels = df[['intent']]

features_vectorizer = TfidfVectorizer(stop_words='english')
features_transformed = features_vectorizer.fit_transform(features)


labels_vetorizer = TfidfVectorizer(stop_words='english')
labels_transformed = labels_vetorizer.fit_transform(labels)

clf = DecisionTreeClassifier()
clf.fit(features_transformed, labels_transformed)

pred = clf.predict(features_vectorizer.transform("Remind me to write my report"))

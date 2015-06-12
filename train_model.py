from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import recurrent as r
from recurrent.event_parser import Tokenizer

pipeline = Pipeline([
    ('vectorizer',  CountVectorizer()),
    ('classifier',  MultinomialNB())])

df = pd.read_csv('data/intents.csv')

features = df['text']

labels = df['intent']


def understand_task(text):
    commands = ['Create task', 'Add task', 'Add ToDo', 'New task',
                'Make task', 'Add new task']
    t = text
    for c in commands:
        i = text.rfind(c)
        if i != -1:
            with_command = t[:i + len(c)]
            t = t.replace(with_command, "").strip()

    e = r.RecurringEvent()
    e.parse(t)
    params = e.get_params()

    tokenizer = Tokenizer(t)
    tokens = filter(lambda t: t.type_ != None, tokenizer.all_)
    first_token = tokens[0].text
    last_token = tokens[-1].text
    event_text = t[t.find(first_token):t.find(last_token) + len(last_token)]
    task_name = t.replace(event_text, "").strip()

    return dict(intent='new_task',task_name=task_name,
                frequency=params['freq'], interval=params['interval'],
                text=text)


def understand(text, clf):
    intent = clf.predict([text])[0]
    if intent == 'new_task':
        return understand_task(text)
    else:
        return dict(text=text)

examples = ["Hey there", "Add new task create report every Friday at 11am"]

pipeline.fit(features, labels)

res = understand(examples[1], pipeline)

import csv


def tasks():
    new_task_commands = ['Create task', 'Add task', 'Add ToDo', 'New task', 'Make task']
    tasks = [['smile every morning minimum once per day', 'smile', 'morning', 'daily', '1', '1'],
             ['drink a cup of water 6 times a day', 'drink a cup of water', 'anytime', 'daily', '6', '1'],
             ['study flashcards 2 times a day', 'study flashcards', 'anytime', 'daily', '2', '1'],
             ['read science paper once per day', 'read science paper', 'anytime', 'daily', '1', '1'],
             ['workout every next morning', 'workout', 'morning', 'next day', '1', '1']]
    result = []
    for command in new_task_commands:
        for task in tasks:
            task = list(task)
            task[0] = command + ' ' + task[0]
            task.insert(1, 'new_task')
            result.append(task)

    return result


def chat_messages():
    e = ['', '', '', '', '']
    messages = [
        'Hello',
        'Hi there!',
        'How are you doing?',
        "I'm doing great",
        "Thank you",
        "You are welcome",
        "Good morning",
        "How can I create a puddle?"
    ]
    result = []
    for message in messages:
        row = []
        row.append(message)
        row.append('chat')
        row = row + e
        result.append(row)
    return result


with open('data/intents.csv', 'wb') as c:
    w = csv.writer(c)
    w.writerow(['text', 'intent', 'task', 'daytime', 'frequency', 'times', 'interval'])
    for row in tasks():
        w.writerow(row)
    for row in chat_messages():
        w.writerow(row)

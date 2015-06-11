import csv

with open('data/intents.csv', 'wb') as c:
    w = csv.writer(c)
    w.writerow(['text', 'intent'])
    w.writerow(['Remind me to turn on the heater tonight', 'remind'])
    w.writerow(['Remind me to turn off the heater tonight', 'remind'])
    w.writerow(['Remind me to restart the pc tomorrow', 'remind'])
    w.writerow(['Turn on the flashlight', 'flashlight'])

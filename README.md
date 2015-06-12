# understand-me
Turn natural language text to structured data

# Example

```python

understand('Add new task create report every Friday at 11am')

```

Gives you the following output

```json

{
  "frequency": "weekly",
  "intent": "new_task",
  "interval": 1,
  "task_name": "create report",
  "text": "Add new task create report every Friday at 11am"
}

```

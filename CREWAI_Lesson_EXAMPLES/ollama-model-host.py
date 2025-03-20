from ollama import chat
user_input = input("Your query?")
stream = chat(
    model='llama3.1',
    messages=[{'role': 'user', 'content': user_input}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)

from groq import Groq

client = Groq()
prompt = input()
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "system",
            "content": "You are a coding assitant, given some code, you will provide an explanation of what it does."
        },
        {
            "role": "user",
            "content":prompt
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")


import openai
openai.api_key = 'YOUR_API_KEY'

response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=
    temperature=0.7,
    max_tokens=100
)

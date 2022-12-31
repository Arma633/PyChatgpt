import openai

# Set the OpenAI API key
openai.api_key = "<API_KEY_GOES_HERE>"

model_engine = "text-davinci-002"

prompt = ""

while True:
    prompt = input(">");
    if prompt == "exit":
        break;
    completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, temperature=1)
    print(completion["choices"][0]["text"]);
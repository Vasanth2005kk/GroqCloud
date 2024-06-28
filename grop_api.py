from groq import Groq


client = Groq(api_key='<apikey_from_groq_acc>')
completion = client.chat.completions.create(
    model="< Models_id >",
    messages=[
        {
            "role": "system",
            "content":"Frontend Developer" # any content 
        },
	{
	 "role": "user",
	 "content": "%s"%(input('Enter your interview question: '))
	}
    ],
    temperature=0,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)


for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
print('\n')


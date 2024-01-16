from openai import OpenAI
import settings
from GptPrompt import get_prompt


client = OpenAI(api_key=settings.OPENAI_API_KEY)

def gpt(content, model="gpt-3.5-turbo-1106"):
    messages = get_prompt(content=content)
    response = client.chat.completions.create(
        model=model, 
        response_format={"type":"json_object"}, 
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content
if __name__ == "__main__":
    prompt = gpt("アプリ開発に使用されるフレームワークは何ですか？")

    print(prompt)
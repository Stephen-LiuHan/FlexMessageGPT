def get_prompt(content):
    prompt=[
            {"role": "system", "content": "あなたは返答をすべてJSON形式で出力します。"}, 
            #システムメッセージにJSONという文字列を含めます。
            {"role": "user", "content": content},
        ]
    return prompt
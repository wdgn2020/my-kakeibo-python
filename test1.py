from openai import OpenAI

# 1. AIを準備する（'your-api-key'の部分に本物のキーを入れます）
client = OpenAI(api_key='your-api-key-here')

# 2. AIに質問を投げかける
response = client.chat.completions.create(
    model="gpt-4o", # 使うAIの種類
    messages=[{"role": "user", "content": "Python初心者に、今日の学習を褒める一言をください！"}]
)

# 3. 返事を受け取って表示する
print(response.choices[0].message.content)

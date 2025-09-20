from openai import OpenAI

client = OpenAI(api_key=<여기에 본인의 API 키를 입력하세요>)

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "당신은 뛰어난 이야기 작가입니다."},
        {"role": "user", "content": "강아지와 코끼리가 친구 관계를 끝내는 짧은 어린이 이야기를 써주세요."}
    ]
)

print(response.output[0].content[0].text)
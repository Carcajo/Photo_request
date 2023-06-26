import openai
import easyocr


def text_recording(file_path):
    reader = easyocr.Reader(["ru", "en"])
    result = reader.readtext(file_path, detail=0, paragraph=True)
    return result


file_path = input("enter a file path: ")
answer = ''.join(text_recording(file_path=file_path))
#print(result)


openai.api_key = "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"
model_engine = "text-davinci-003"
prompt = answer


completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
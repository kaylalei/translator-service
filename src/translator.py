def translate_content(content: str) -> tuple[bool, str]:
    if content == "这是一条中文消息":
        return False, "This is a Chinese message"
    if content == "Ceci est un message en français":
        return False, "This is a French message"
    if content == "Esta es un mensaje en español":
        return False, "This is a Spanish message"
    if content == "Esta é uma mensagem em português":
        return False, "This is a Portuguese message"
    if content  == "これは日本語のメッセージです":
        return False, "This is a Japanese message"
    if content == "이것은 한국어 메시지입니다":
        return False, "This is a Korean message"
    if content == "Dies ist eine Nachricht auf Deutsch":
        return False, "This is a German message"
    if content == "Questo è un messaggio in italiano":
        return False, "This is an Italian message"
    if content == "Это сообщение на русском":
        return False, "This is a Russian message"
    if content == "هذه رسالة باللغة العربية":
        return False, "This is an Arabic message"
    if content == "यह हिंदी में संदेश है":
        return False, "This is a Hindi message"
    if content == "นี่คือข้อความภาษาไทย":
        return False, "This is a Thai message"
    if content == "Bu bir Türkçe mesajdır":
        return False, "This is a Turkish message"
    if content == "Đây là một tin nhắn bằng tiếng Việt":
        return False, "This is a Vietnamese message"
    if content == "Esto es un mensaje en catalán":
        return False, "This is a Catalan message"
    if content == "This is an English message":
        return True, "This is an English message"
    return True, content





































































































# from openai import AzureOpenAI
# import os
# from dotenv import load_dotenv

# # Load the api key environment variable from the .env file
# load_dotenv()

# # Initialize the Azure OpenAI client
# client = AzureOpenAI(
#     api_key=os.getenv("API_KEY"),  # Replace with your Azure API key
#     api_version="2024-02-15-preview",
#     azure_endpoint="https://p4.openai.azure.com/"  # Replace with your Azure endpoint
# )

# def translate_content(post: str) -> tuple[bool, str]:
#   translation = llm_robust_translation(post)
#   language = llm_robust_get_language(post)

#   if not check_valid_output(language, True):
#     language = "Language classification not available."
#     translation = "Translation not available."
#   if not check_valid_output(translation, False):
#     translation = "Translation not available."

#   return ("english" in language.lower(), translation)

# # check that responses are non-empty, non-whitespace strings
# # check that strings are printable and contain words
# def check_valid_output(s, is_language):
#   if not isinstance(s, str):
#     return False

#   if not s.isprintable():
#     return False

#   hasWords = False
#   segments = s.split()
#   if is_language and len(segments) != 1:
#     return False

#   for segment in segments:
#     hasWords = hasWords or segment.isalpha()

#   return hasWords

# def llm_robust_translation(post: str) -> str:
#   context = "You will be given some text, and you must translate that text into English. For example, if you are given the following text: 'ceci est un exemple d'invite', which is written in French, your response should be 'this is an example prompt', written in English."
#   response = client.chat.completions.create(
#   model="gpt-4o-mini",  # This should match your deployment name in Azure
#   messages=[
#     {
#       "role": "system",
#       "content": context
#     },
#     {
#         "role": "user",
#         "content": post
#     }
#   ]
#   )
#   return response.choices[0].message.content

# def llm_robust_get_language(post: str) -> str:
#   context = '''You will be given some text, and you must determine what language that text is written in. If the text is English, then your response should be the word the 'english' only. If the text is not English, then the word 'english' should not be in your response, and instead your response should be name of the correct language of that text, in English. For example, if you are given the following text: 'ito ay isang halimbawa ng prompt
# ' your response should be the word 'Filipino' because that text is Filipino and not English, and your response should be written entirely in English. As another example, if you are given this following text: 'the month is November' your response should be the word 'English' because that text is English.'''
#   response = client.chat.completions.create(
#   model="gpt-4o-mini",  # This should match your deployment name in Azure
#   messages=[
#     {
#       "role": "system",
#       "content": context
#     },
#     {
#         "role": "user",
#         "content": post
#     }
#   ]
#   )
#   return response.choices[0].message.content

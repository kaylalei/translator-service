from openai import AzureOpenAI
import os
from dotenv import load_dotenv

# Load the api key environment variable from the .env file
load_dotenv()

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("API_KEY"),  # Replace with your Azure API key
    api_version="2024-02-15-preview",
    azure_endpoint="https://p4.openai.azure.com/"  # Replace with your Azure endpoint
)

def translate_content(post: str) -> tuple[bool, str]:
  translation = llm_robust_translation(post)
  language = llm_robust_get_language(post)

  if not check_valid_output(language, True):
    language = "Language classification not available."
    translation = "Translation not available."
  if not check_valid_output(translation, False):
    translation = "Translation not available."

  return ("english" in language.lower(), translation)

# check that responses are non-empty, non-whitespace strings
# check that strings are printable and contain words
def check_valid_output(s, is_language):
  if not isinstance(s, str):
    return False

  if not s.isprintable():
    return False

  hasWords = False
  segments = s.split()
  if is_language and len(segments) != 1:
    return False

  for segment in segments:
    hasWords = hasWords or segment.isalpha()

  return hasWords

def llm_robust_translation(post: str) -> str:
  context = "You will be given some text, and you must translate that text into English. For example, if you are given the following text: 'ceci est un exemple d'invite', which is written in French, your response should be 'this is an example prompt', written in English."
  response = client.chat.completions.create(
  model="gpt-4o-mini",  # This should match your deployment name in Azure
  messages=[
    {
      "role": "system",
      "content": context
    },
    {
        "role": "user",
        "content": post
    }
  ]
  )
  return response.choices[0].message.content

def llm_robust_get_language(post: str) -> str:
  context = '''You will be given some text, and you must determine what language that text is written in. If the text is English, then your response should be the word the 'english' only. If the text is not English, then the word 'english' should not be in your response, and instead your response should be name of the correct language of that text, in English. For example, if you are given the following text: 'ito ay isang halimbawa ng prompt
' your response should be the word 'Filipino' because that text is Filipino and not English, and your response should be written entirely in English. As another example, if you are given this following text: 'the month is November' your response should be the word 'English' because that text is English.'''
  response = client.chat.completions.create(
  model="gpt-4o-mini",  # This should match your deployment name in Azure
  messages=[
    {
      "role": "system",
      "content": context
    },
    {
        "role": "user",
        "content": post
    }
  ]
  )
  return response.choices[0].message.content

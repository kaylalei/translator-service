from src.translator import client, translate_content
from mock import patch

@patch.object(client.chat.completions, 'create')
def test_unexpected_language(mocker):
  # we mock the model's response to return a random message
  mocker.return_value.choices[0].message.content = "I don't understand your request"
  response = translate_content("Hier ist dein erstes Beispiel.")
  assert response == (False, "Translation not available.")

@patch.object(client.chat.completions, 'create')
def test_nonetype_response(mocker):
  mocker.return_value.choices[0].message.content = None
  response = translate_content("Hier ist dein erstes Beispiel.")
  assert response == (False, "Translation not available.")

@patch.object(client.chat.completions, 'create')
def test_empty_string_response(mocker):
  mocker.return_value.choices[0].message.content = ""
  response = translate_content("Hier ist dein erstes Beispiel.")
  assert response == (False, "Translation not available.")

@patch.object(client.chat.completions, 'create')
def test_gibberish_response(mocker):
  mocker.return_value.choices[0].message.content = "2244fdqwr4 239fud- !!=vnot4 \t\n5givt"
  response = translate_content("Hier ist dein erstes Beispiel.")
  assert response == (False, "Translation not available.")

@patch.object(client.chat.completions, 'create')
def test_whitespace_response(mocker):
  mocker.return_value.choices[0].message.content = "\t\t\t        \n  \t \n"
  response = translate_content("Hier ist dein erstes Beispiel.")
  assert response == (False, "Translation not available.")

@patch.object(client.chat.completions, 'create')
def test_one_invalid_word_response(mocker):
  mocker.return_value.choices[0].message.content = "wordwithanumber00"
  response = translate_content("Hier ist dein erstes Beispiel.")
  assert response == (False, "Translation not available.")

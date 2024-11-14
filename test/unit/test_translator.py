# from src.translator import translate_content
# from mock import patch

# def test_chinese():
#     is_english, translated_content = translate_content("这是一条中文消息")
#     assert is_english == False
#     assert translated_content == "This is a Chinese message"

# def test_llm_normal_response():
#   is_english, translated_content = translate_content("Hier ist dein erstes Beispiel.")
#   assert is_english == True
#   assert translated_content == "Hier ist dein erstes Beispiel."

# def test_llm_gibberish_response():
#   is_english, translated_content = translate_content("2244fdqwr4 239fud- !!=vnot4 \t\n5givt")
#   assert is_english == True
#   assert translated_content == "2244fdqwr4 239fud- !!=vnot4 \t\n5givt"




























































































def fake_test():
    pass

def fake_test_2():
    pass





# from src.translator import client, translate_content
# from mock import patch

# def test_normal_response():
#   response = translate_content("Hier ist dein erstes Beispiel.")
#   assert response == (False, "Here is your first example.")

# def test_english_response():
#   response = translate_content("The content of test topic")
#   assert response == (True, "The content of test topic")

# @patch.object(client.chat.completions, 'create')
# def test_unexpected_language(mocker):
#   # we mock the model's response to return a random message
#   mocker.return_value.choices[0].message.content = "I don't understand your request"
#   response = translate_content("Hier ist dein erstes Beispiel.")
#   assert response == (False, "Translation not available.")

# @patch.object(client.chat.completions, 'create')
# def test_nonetype_response(mocker):
#   mocker.return_value.choices[0].message.content = None
#   response = translate_content("Hier ist dein erstes Beispiel.")
#   assert response == (False, "Translation not available.")

# @patch.object(client.chat.completions, 'create')
# def test_empty_string_response(mocker):
#   mocker.return_value.choices[0].message.content = ""
#   response = translate_content("Hier ist dein erstes Beispiel.")
#   assert response == (False, "Translation not available.")

# @patch.object(client.chat.completions, 'create')
# def test_gibberish_response(mocker):
#   mocker.return_value.choices[0].message.content = "2244fdqwr4 239fud- !!=vnot4 \t\n5givt"
#   response = translate_content("Hier ist dein erstes Beispiel.")
#   assert response == (False, "Translation not available.")

# @patch.object(client.chat.completions, 'create')
# def test_whitespace_response(mocker):
#   mocker.return_value.choices[0].message.content = "\t\t\t        \n  \t \n"
#   response = translate_content("Hier ist dein erstes Beispiel.")
#   assert response == (False, "Translation not available.")

# @patch.object(client.chat.completions, 'create')
# def test_one_invalid_word_response(mocker):
#   mocker.return_value.choices[0].message.content = "wordwithanumber00"
#   response = translate_content("Hier ist dein erstes Beispiel.")
#   assert response == (False, "Translation not available.")

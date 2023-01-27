import base64
  
def encodeBase64(str):
  sample_string_bytes = str.encode("ascii")
  base64_bytes = base64.b64encode(sample_string_bytes)
  encodedString  = base64_bytes.decode("ascii")
  print(f"Encoded string: {encodedString}")
  return encodedString

def decodeBase64(fstring):
  base64_string = str(fstring)
  base64_bytes = base64_string.encode("ascii")
  sample_string_bytes = base64.b64decode(base64_bytes)
  sample_string = sample_string_bytes.decode("ascii")
  print(f"Decoded string: {sample_string}")
  return sample_string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_stopwords_py(text):
    # Tokenize the text
    words = word_tokenize(text)
    # Get a set of stop words
    stop_words = set(stopwords.words("english"))
    # Remove stop words from the tokenized words
    filtered_words = [word for word in words if word.lower() not in stop_words]
    # Join the filtered words back into a single string
    filtered_text = " ".join(filtered_words)
    return filtered_text

  
# a = encodeBase64("hello world")
# b = decodeBase64(a)




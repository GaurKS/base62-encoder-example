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

  
# a = encodeBase64("hello world")
# b = decodeBase64(a)




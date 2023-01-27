// const {encodeBase64, decodeBase64} = require('./main.go');
const { encodeBase64, decodeBase64, remove_stopwords_py } = require('./encoder.py');

// const str = encodeBase64('Hey there! Welcome to MetaCall');
const encode = (str) => {
  console.log("Encoded from Javascript runtime...");
  return encodeBase64(str)
}

const decode = (str) => {
  console.log("Decoded from Javascript runtime...");
  return decodeBase64(str);
}

const removeStopWords = (str) => {
  const output = remove_stopwords_py(str);
  // console.log("Processed text is: ", output)
  return output
}

module.exports = {
  encode,
  decode,
  removeStopWords
}

// const s = encode("Hello World! MetaCall is amazing...")
// encode("Hello World! MetaCall is amazing...")
// decode(s)
// removeStopWords("This is just a dummy text to test the remove stop words function")

// console.log({encodeString: str});
// console.log({decodeString: decodeBase64(str)});
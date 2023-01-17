// const {encodeBase64, decodeBase64} = require('./main.go');
const { encodeBase64, decodeBase64 } = require('./encoder.py');

// const str = encodeBase64('Hey there! Welcome to MetaCall');
const encode = (str) => {
  console.log("Encoded from Javascript runtime...");
  return encodeBase64(str)
}

const decode = (str) => {
  console.log("Decoded from Javascript runtime...");
  return decodeBase64(str);
}

// console.log({encodeString: str});
// console.log({decodeString: decodeBase64(str)});

module.exports = {
  encode, 
  decode
}

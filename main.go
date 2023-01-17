package base62Encoder

import (
	b64 "encoding/base64"
	"fmt"
)

func encodeBase64(input string) string {
	encodedStr := b64.StdEncoding.EncodeToString([]byte(input))
	fmt.Println("Encoded string: ", encodedStr)
	return encodedStr
}

func decodeBase64(input string) (string, error) {
	decodedStr, err := b64.StdEncoding.DecodeString(input)
	fmt.Println("decoded string: ", string(decodedStr))
	return string(decodedStr), err
}

func main() {

	data := "www.github.com/gaurks"
	wee := encodeBase64(data)
	decodeBase64(wee)

}

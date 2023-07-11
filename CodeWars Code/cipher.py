class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        encoded = ''
        for i in range(len(text)):
            text_char = text[i]
            if text_char not in self.alphabet:
                encoded += text_char
            else:
                key_char = self.key[i % len(self.key)]
                shift = self.alphabet.index(key_char)
                text_index = self.alphabet.index(text_char)
                encoded_index = (text_index + shift) % len(self.alphabet)
                encoded += self.alphabet[encoded_index]

        return encoded

    def decode(self, encoded):
        text = ''
        for i in range(len(encoded)):
            encoded_char = encoded[i]
            if encoded_char not in self.alphabet:
                text += encoded_char
            else:
                key_char = self.key[i % len(self.key)]
                shift = self.alphabet.index(key_char)
                encoded_index = self.alphabet.index(encoded_char)
                text_index = (encoded_index - shift) % len(self.alphabet)
                text += self.alphabet[text_index]
        return text

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "password"
cipher = VigenereCipher(key, alphabet)

message = "my secret code i want to secure"
encoded = cipher.encode(message)
decoded = cipher.decode(encoded)

print("Original message:", message)
print("Encoded message:", encoded)
print("Decoded message:", decoded)

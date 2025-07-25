class CaesarCipher:
    @staticmethod
    def encode(text: str, shift: int) -> str:
        output = []
        for ch in text:
            if ch.isupper():
                shifted = (ord(ch) - ord('A') + shift) % 26 + ord('A')
                output.append(chr(shifted))
            elif ch.islower():
                shifted = (ord(ch) - ord('a') + shift) % 26 + ord('a')
                output.append(chr(shifted))
            else:
                output.append(ch)
        return ''.join(output)

    @staticmethod
    def decode(text: str, shift: int) -> str:
        return CaesarCipher.encode(text, -shift)

if __name__ == "__main__":
    msg = input("Enter message: ")
    shift_val = int(input("Enter shift: "))
    encoded_msg = CaesarCipher.encode(msg, shift_val)
    print(f"Encoded: {encoded_msg}")
    decoded_msg = CaesarCipher.decode(encoded_msg, shift_val)
    print(f"Decoded: {decoded_msg}")

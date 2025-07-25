from decimal import Decimal

def format_indian_currency(amount: Decimal) -> str:
    amt_str = str(amount)
    if '.' in amt_str:
        amt_str = amt_str.rstrip('0').rstrip('.')
    if '.' in amt_str:
        int_part, dec_part = amt_str.split('.')
    else:
        int_part, dec_part = amt_str, ''

    rev_int = int_part[::-1]
    chunks = [rev_int[:3]]
    rev_int = rev_int[3:]

    while rev_int:
        chunks.append(rev_int[:2])
        rev_int = rev_int[2:]

    formatted = ','.join(chunks)[::-1]

    if dec_part:
        return f"{formatted}.{dec_part}"
    return formatted

if __name__ == "__main__":
    try:
        num = Decimal(input("Enter amount: "))
        print("Formatted:", format_indian_currency(num))
    except:
        print("Invalid input.")

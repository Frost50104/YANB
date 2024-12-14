# функция, которая проверяет, является ли данная строка палиндромом или нет, и возвращается результат проверки

text = "Кит на море не романтик"

def palindrome(text):
    text_red = text.lower()
    text_red = text_red.replace(" ", "")
    if text_red == text_red[::-1]:
        print(f'Текст "{text}" является палиндромом')
    else:
        print(f'Текст "{text}" не является палиндромом')

palindrome(text)
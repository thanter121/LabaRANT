import requests


# Функция для получения курса валют
def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/RUB"  # API для получения курсов
    response = requests.get(url)

    # Проверка ответа API
    if response.status_code != 200:
        print("Ошибка при получении данных о курсах валют.")
        return None, None

    data = response.json()
    return data['rates']['USD'], data['rates']['RUB']  # Возвращаем курс доллара и рубля


# Функция для конвертации рублей в доллары
def convert_rub_to_usd(amount_rub):
    exchange_rate, _ = get_exchange_rate()
    if exchange_rate is None:
        return None  # Если курс не удалось получить
    amount_usd = amount_rub / exchange_rate
    return amount_usd, exchange_rate


def main():
    print("Добро пожаловать в конвертер валют!")
    while True:
        print("Введите сумму в рублях (или 'exit' для выхода):")
        user_input = input()

        if user_input.lower() == 'exit':
            print("Выход из программы.")
            break

        try:
            amount_rub = float(user_input)
            amount_usd, exchange_rate = convert_rub_to_usd(amount_rub)
            if amount_usd is not None:
                print(f"Курс: 1 RUB = {exchange_rate:.4f} USD")
                print(f"{amount_rub} RUB = {amount_usd:.4f} USD")
        except ValueError:
            print("Пожалуйста, введите корректное числовое значение.")


# Запуск программы
name == "main"
main()



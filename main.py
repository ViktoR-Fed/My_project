from src.data_processing import unpacking_csv, unpacking_xlsx
from src.date import convert_date
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.utils import receiving_financial_transactions
from src.widget import mask_account_card


def main():
    while True:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        user_choice = input().strip()

        if user_choice == "1":
            transactions = receiving_financial_transactions()
            print("Был выбран JSON-файл.")
            break
        elif user_choice == "2":
            transactions = unpacking_csv()
            print("Был выбран CSV-файл.")
            break
        elif user_choice == "3":
            transactions = unpacking_xlsx()
            print("Был выбран XLSX-файл.")
            break
        else:
            print(f"Данный выбор {user_choice} не доступен")
            continue

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = ["EXECUTED", "CANCELED", "PENDING"]
        user_status_choice = input().upper().strip()
        if user_status_choice in status:
            status_filter = user_status_choice
            print(f"Был выбран статус: {status_filter}")
            ft = filter_by_state(transactions, status_filter)
            break
        else:
            print(f"Статус операции {user_status_choice} недоступен")
            continue

    while True:
        sort_by_date_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
        if sort_by_date_choice == "да":
            order_choice = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
            if order_choice == "по возрастанию":
                order_filter = False
                ft = sort_by_date(ft, order_filter)
                break
            else:
                break
        else:
            break

    while True:
        currency_choice = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
        if currency_choice in ("да", "нет"):
            if currency_choice.lower() == "да" and user_choice in ["1", "2", "3"]:
                ft = [t for t in ft if t.get("currency_code") == "RUB"]
                break
            elif currency_choice.lower() == "да" and user_choice == "1":
                ft = list(filter_by_currency(ft, "RUB"))
                break
            if currency_choice.lower() == "нет":
                break

    while True:
        word_for_filter = (
            input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
        )
        if word_for_filter in ["да", "нет"]:
            if word_for_filter == "да":
                filter_word = input("Введите слово:\n")
                ft = process_bank_search(ft, filter_word)
                break
            else:
                break
        else:
            continue

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(ft)}")

    for transaction in ft:
        formatted_date = convert_date(str(transaction["date"]))
        from_account_raw = str(transaction.get("from", "неизвестно"))
        to_account_raw = str(transaction.get("to", "неизвестно"))
        amount = transaction.get("amount", "не указана сумма")
        currency = transaction.get("currency_name", "не указана валюта")
        if from_account_raw:
            from_account = mask_account_card(from_account_raw)
        else:
            from_account = ""  # или другое значение

        if to_account_raw:
            to_account = mask_account_card(to_account_raw)
        else:
            to_account = ""  # или другое значение

        formatted_output = (
            f"{formatted_date} {transaction['description']}\n"
            f"{from_account} -> {to_account}\n"
            f"Сумма: {amount} {currency}\n"
        )
        print(formatted_output)
    if len(ft) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()

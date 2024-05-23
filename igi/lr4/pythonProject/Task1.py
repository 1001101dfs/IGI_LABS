from Persone import Persone
from CheckInput import check_date_input


def task_1():
    info = [
        {"Name": "Ромашевский Г.Д.", "Date": "07.11.2004"},
        {"Name": "Байтасов Р.М.", "Date": "29.06.2004"},
        {"Name": "Ланец В.И.", "Date": "25.11.2005"}
    ]

    myClass_pkl = Persone("data.pkl")
    myClass_csv = Persone("data.csv")

    myClass_pkl.write_data_pickle(info)
    myClass_csv.write_data_csv(info)

    myClass_csv.read_data_csv()
    myClass_pkl.read_data_pkl()

    print('Введите дату формата \"дд.мм.гггг\"')
    date = check_date_input()
    myClass_csv.do_task(date)

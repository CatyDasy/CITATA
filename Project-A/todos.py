import json
from useful_functions import indent4, print_banner,  print_line, print_color
import datetimes as dts




def load_todos(name):
    with open(f"static/json/todos-{name}.json", 'r') as f:
        isi = json.load(f)
    return indent4(isi["TODOS"][dts.Day("Asia/Jakarta")])


def main():
    todos = load_todos("samil")

    day = dts.Day("Asia/Jakarta")

    todonow = todos[day]
    # Cetak banner hari
    print_banner(f"TO DO HARI {day.upper()}")

    # Loop setiap sesi
    for sesi, kegiatan in todonow.items():
        print_line(f"{sesi.upper()}", 50, color="#71debd")
        for item in kegiatan:
            print_color(f"• {item}", "#a4bfbb")


if __name__ == "__main__":
    main()













































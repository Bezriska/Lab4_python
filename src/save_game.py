from src.classes.PlayerClass import Player
from src.classes.GooseClasess import Goose, WarGoose, HonkGoose, GooseFlock
from src.classes.CasinoClass import Casino

import json


def save_game(seed_name: str, players: list[Player], gooses: list[Goose | WarGoose | HonkGoose], seed: int):
    """Сохраняет текущее состояние игры в JSON файл.
    
    Args:
        seed_name: Название сохранения
        players: Список игроков для сохранения
        gooses: Список гусей для сохранения
        seed: Сид генератора случайных чисел
    """
    try:
        with open("src/saved_seeds.json", "r") as data:
            saves = json.load(data)
    except (FileNotFoundError, json.JSONDecodeError):
        saves = {"seeds": {}}

    if not (players and gooses and seed_name):
        return

    new_save = {
        "players": {},
        "gooses": {},
        "seed": str(seed)
    }

    for i, player in enumerate(players, 1):

        new_save["players"][f"player{i}"] = {
            "balance": player.balance,
            "name": player.name
        }

    for i, goose in enumerate(gooses, 1):

        new_save["gooses"][f"goose{i}"] = {
            "name": goose.name,
            "type": type(goose).__name__
        }

    saves["seeds"][seed_name] = new_save

    with open("src/saved_seeds.json", "w") as file:
        json.dump(saves, file, indent=4, ensure_ascii=False)


def register_players_from_save(filepath: str, save_name: str, casic: Casino):
    """Регистрирует игроков из сохраненной игры в казино.
    
    Args:
        filepath: Путь к файлу с сохранениями
        save_name: Название сохранения для загрузки
        casic: Экземпляр казино для регистрации игроков
    """
    with open(filepath, "r") as data:
        save = json.load(data)

    for player_data in save["seeds"][save_name]["players"].values():

        name = player_data["name"]
        balance = int(player_data["balance"])

        casic.player_registry(name, balance)
    return


def register_gooses_from_save(filepath: str, save_name: str, casic: Casino):
    """Регистрирует гусей из сохраненной игры в казино.
    
    Args:
        filepath: Путь к файлу с сохранениями
        save_name: Название сохранения для загрузки
        casic: Экземпляр казино для регистрации гусей
    """
    with open(filepath, "r") as data:
        save = json.load(data)

    for goose_data in save["seeds"][save_name]["gooses"].values():

        name = goose_data["name"]
        goose_type = goose_data["type"]

        casic.goose_registry(goose_type, name)
    return


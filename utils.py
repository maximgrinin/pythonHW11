from os import path as os_path
from json import load as json_load


# Функция загружает данные кандидатов из файла в список
def load_candidates_from_json(path):
    """
    Загружает данные кандидатов из файла в список
    """
    json = []
    if os_path.exists(path):
        with open(path, 'r', encoding="utf-8") as file:
            json = json_load(file)
    return json


# Функция возвращает одного кандидата по его id
def get_candidate(candidates_list, candidate_id):
    """
    Возвращает кандидата по его id
    """
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate


# Функция возвращает кандидатов по имени
def get_candidates_by_name(candidates_list, candidate_name):
    """
    Возвращает кандидатов по имени
    """
    candidates = []
    for candidate in candidates_list:
        if candidate_name.strip().lower() in candidate['name'].strip().lower():
            candidates.append(candidate)

    return candidates


# Функция возвращает кандидатов по навыку
def get_candidates_by_skill(candidates_list, skill_name):
    """
    Возвращает кандидатов по навыку
    """
    candidates = []
    for candidate in candidates_list:
        if skill_name.strip().lower() in candidate['skills'].strip().lower().split(", "):
            candidates.append(candidate)

    return candidates

#!/usr/bin/python3
# Generowanie pliku struktury kursu
# SKEProjekt
import os
import sys
import json
import os.path as path


def get_exercise_structure(exercise_path, depth):
    exercise_structure = {}

    if not path.isdir(exercise_path):
        print(f"Podany folder nie istnieje - {exercise_path}")
        sys.exit(-1)
    print(depth * "\t" + f"- Generowanie struktury ćwiczenia {exercise_path}")
    try:
        exercise_id = int(path.basename(path.normpath(exercise_path)).split("_")[0])
    except:
        print(depth * "\t" + f"- [ERROR] kurs nie posiada id")
        sys.exit(-1)
    print(depth * "\t" + f"- ID ćwiczenia : {exercise_id}")

    tresc_path = path.join(course_path, 'tresc.md')
    if not path.isfile(tresc_path):
        print(depth * "\t" + f"- [ERROR] ćwiczenie nie posiada tresci")
        sys.exit(-1)
    with open(tresc_path, 'r+', encoding='utf-8') as f:
        course_tresc = f.read()
    course_title = course_tresc.split('\n')[0]
    print(depth * "\t" + f"- Tytuł: {course_title}")

    przyklad_path = path.join(course_path, 'przyklad.ed')
    if not path.isfile(tresc_path):
        print(depth * "\t" + f"- [ERROR] ćwiczenie nie posiada przykładowego rozwiązania")
        sys.exit(-1)
    with open(przyklad_path, 'r+', encoding='utf-8') as f:
        exercise_przyklad = f.read()

    wynik_path = path.join(course_path, 'wynik.out')
    if not path.isfile(wynik_path):
        print(depth * "\t" + f"- [ERROR] ćwiczenie nie posiada oczekiwanego wyniku")
        sys.exit(-1)
    with open(wynik_path, 'r+', encoding='utf-8') as f:
        exercise_wynik = f.read()

    start_path = path.join(course_path, 'start.ed')
    if not path.isfile(tresc_path):
        print(depth * "\t" + f"- [ERROR] ćwiczenie nie posiada kodu początkowego")
        sys.exit(-1)
    with open(start_path, 'r+', encoding='utf-8') as f:
        exercise_start = f.read()

    exercise_structure['path'] = exercise_path
    exercise_structure['id'] = exercise_id

    print(depth * "\t" + f"- Ćwiczenie jest poprawny strukturalnie")
    return exercise_structure

def get_course_structure(course_path, depth = 0):
    course_structure = {}

    if not path.isdir(course_path):
        print(f"Podany folder nie istnieje - {course_path}")
        sys.exit(-1)

    print(depth * "\t" + f"- Generowanie struktury kursu {course_path}")

    try:
        course_id = int(path.basename(path.normpath(course_path)).split("_")[0])
    except:
        print(depth * "\t" + f"- [ERROR] kurs nie posiada id")
        sys.exit(-1)
    print(depth * "\t" + f"- ID kursu : {course_id}")

    tresc_path = path.join(course_path, 'tresc.md')
    if not path.isfile(tresc_path):
        print(depth * "\t" + f"- [ERROR] kurs nie posiada tresci")
        sys.exit(-1)
    with open(tresc_path, 'r+', encoding='utf-8') as f:
        course_tresc = f.read()
    course_title = course_tresc.split('\n')[0]
    print(depth * "\t" + f"- Tytuł: {course_title}")

    all_files_in_dir = os.listdir(course_path)
    subcourse_dirs = [subdir for subdir in all_files_in_dir if (path.isdir(path.join(course_path, subdir)) and subdir != "exer") ]
    if subcourse_dirs:
        print(depth * "\t" + f"- Sprawdzanie pod-kursów")
        course_structure['subcourses'] = []
        for subdir in subcourse_dirs:
            course_structure['subcourses'].append(get_course_structure(path.join(course_path, subdir), depth + 1))

    if path.isdir(path.join(course_path, 'exer')):
        print(depth * "\t" + f"- Sprawdzanie ćwiczeń")
        course_structure['exercises'] = []
        for exer_dir in [subdir for subdir in os.listdir(path.join(course_path, 'exer')) if path.isdir(path.join(path.join(course_path, 'exer'), subdir))]:
            course_structure['exercises'].append(get_course_structure(path.join(path.join(course_path, 'exer'), exer_dir), depth+1))

    course_structure['path'] = course_path
    course_structure['id'] = course_id
    course_structure['title'] = course_title

    print(depth * "\t" + f"- Kurs jest poprawny strukturalnie")
    return course_structure



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Nie podano folderu kursu")
        sys.exit(-1)

    root_course_folder = sys.argv[1]
    course_structure = get_course_structure(root_course_folder)
    json_path = path.basename(path.normpath(root_course_folder)) + '.json'

    with open(json_path, 'w+', encoding='utf-8') as f:
        f.write(json.dumps(course_structure, indent=4))
    print("Plik strukturalny został wygenerowany")

import os
from time import sleep
from random import uniform
from sys import stdin


def typewriter(words):
    for char in words:
        sleep(uniform(0.05, 0.1))
        print(char, end='', flush=True)


def dots(words: str):
    splitted = words.split("\n")
    new_words = []
    count = 0
    first = True
    for i in range(splitted.count('') + 1):
        new_words.append([])
        while 1:
            if count <= len(splitted) - 1:
                if splitted[count]:
                    if first:
                        new_words[i].append(">>> " + splitted[count])
                        first = False
                    else:
                        new_words[i].append("... " + splitted[count])
                    count += 1
                else:
                    new_words[i].append(">>>")
                    first = True
                    count += 1
                    break
            else:
                break
    new_words_str = ""
    for el in new_words:
        for le in el:
            new_words_str += (le + "\n")
    new_words_str += ">>>\n"
    return new_words_str


def main():
    try:
        with open("config", "r") as config:
            hostname = config.readlines()[0].rstrip("\n")
    except FileNotFoundError:
        hostname = input("Hey there! Seems like it's your first time here! Let's config me.\nType in your desired "
                         "hostname:\n")
        print(hostname, file=open("config", "w+"))
    print("Hello to ultimate typewriter script!\nPaste me the text you want me to imitate writing into python console, "
          "then hit ^D")
    data = stdin.read()

    os.system("clear")

    print(f"{hostname} ", end="")
    typewriter("python3")
    print("\nPython 3.10.9 (main, Dec 15 2022, 17:11:09) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin \nType "
          "\"help\", \"copyright\", \"credits\" or \"license\" for more information.")
    typewriter(dots(data))
    sleep(10)


if __name__ == "__main__":
    main()

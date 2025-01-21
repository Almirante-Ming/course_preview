greetings = {
    "HELLO": "ENGLISH",
    "HOLA": "SPANISH",
    "HALLO": "GERMAN",
    "BONJOUR": "FRENCH",
    "CIAO": "ITALIAN",
    "ZDRAVSTVUJTE": "RUSSIAN"
}

case_number = 1
while True:
    line = input().strip()
    if line == "#":
        break
    language = greetings.get(line, "UNKNOWN")
    print(f"Case {case_number}: {language}")
    case_number += 1
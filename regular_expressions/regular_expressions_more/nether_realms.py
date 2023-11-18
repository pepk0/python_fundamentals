import re


def get_demon_health(text: str) -> int:
    health = 0
    match_pattern = re.findall(r"[^0-9\*\+\-\/\.]", text)
    for letter in match_pattern:
        health += ord(letter)
    return health


def calculate_damage(text: str) -> float:
    base_damage = 0
    multiply_divide = re.findall(r"[\/\*]", text)
    number_matches = re.findall(r"(\-?[0-9]+[\.0-9]*)", text)
    for number in number_matches:
        if "-" in number:
            number = float(number.replace("-", "")) * -1
        base_damage += float(number)
    for operation in multiply_divide:
        if operation == "*":
            base_damage *= 2
        else:
            base_damage /= 2
    return base_damage


demons = re.sub(" ", "", input()).split(",")
demon_stats = {}
for demon in demons:
    demon_health = get_demon_health(demon)
    demon_attack = calculate_damage(demon)
    demon_stats[demon] = (demon_health, demon_attack)

for demon_name, (health, damage) in sorted(demon_stats.items(),
                                           key=lambda x: x[0]):
    print(f"{demon_name} - {health} health, {damage:.2f} damage")

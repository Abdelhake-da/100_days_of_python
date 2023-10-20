names = []
with open('input/names/invited_names.txt') as file:
    names = file.read().split()
letter = ''
with open('input/letters/starting_letter.txt')as file:
    letter = file.read()
for name in names:
    letter_f = letter.replace('[name]', name)
    with open(f'output/letter_for_{name}', 'w')as file:
        file.write(letter_f)

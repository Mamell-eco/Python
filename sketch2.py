name = input('Qual é seu nome? ')
pronome = 'a' if (name[-1] == 'a') or ((name[-2] == 'a') and (name[-1] != 's')) else 'o' 
print(f'eu sou {pronome} {name}')
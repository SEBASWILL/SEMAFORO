import os

# Ejecutar el comando "ls" en una carpeta específica

a = input('nombre de rama:')
os.system('git add .')
b = input('mensaje de commit:')
os.system('git commit -m "'+b+'"')
os.system('git push origin '+a)
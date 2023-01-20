# Tem alguns jeitos de fazer isso em python, vou deixar dois deles, um mais "pythonico" (sem utilizar funções que ja fazem isso) 
# e outro mais usando lógica de programação mesmo.
 
txt = 'Target Sistemas' 

def inverter_string_python(string: str):
    return string[::-1]

def inverter_string_logica(string: str):
    size = len(string) - 1
    reversed_string = ''
    while size >= 0:
        reversed_string += string[size]
        size -= 1
    return reversed_string
        
print(inverter_string_logica(txt)) # sametsiS tegraT
print(inverter_string_python(txt)) # sametsiS tegraT
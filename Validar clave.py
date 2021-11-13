def passwd_check(passwd):
    """Verifica si la clave cumple con los requisitos.

   Los siguientes son los criterios para verificar la contraseña:
    1. Al menos 1 letra entre [a-z]
    2. Al menos 1 número entre [0-9]
    1. Al menos 1 letra entre [A-Z]
    3. Al menos 1 carácter de [$ # @]
    4. Longitud mínima de la contraseña de la transacción: 6
    5. Longitud máxima de la contraseña de la transacción: 12

    """
    SpecialSym=['$','@','#']
    return_val=True
    if len(passwd) < 6:
        print('la longitud de la contraseña debe ser de al menos 6 caracteres')
        return_val=False
    if len(passwd) > 12:
        print('la longitud de la contraseña no debe ser superior a 12')
        return_val=False
    if not any(char.isdigit() for char in passwd):
        print('la contraseña debe tener al menos un número')
        return_val=False
    if not any(char.isupper() for char in passwd):
        print('la contraseña debe tener al menos una letra mayúscula')
        return_val=False
    if not any(char.islower() for char in passwd):
        print('la contraseña debe tener al menos una letra minúscula')
        return_val=False
    if not any(char in SpecialSym for char in passwd):
        print('la contraseña debe tener al menos uno de los símbolos $@#')
        return_val=False
    if return_val:
        print('Cumple con los criterios')
    return return_val

print(passwd_check.__doc__)

passwd = input('Ingrese las claves: ')


print(passwd_check(passwd))
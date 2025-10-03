import string
import random


def generate_password(n_lower: int = 2,
                      n_upper: int = 2,
                      n_digits: int = 2,
                      n_special: int = 2,
                      minimum_length: int = 0) -> str:
    """
    Generate a random password based on specified character requirements.

    The password will contain at least:
        - `n_lower` lowercase letters
        - `n_upper` uppercase letters
        - `n_digits` numeric digits
        - `n_special` special characters (punctuation)
    If the sum of these is less than `minimal_length`, additional random
    letters or digits are added to meet the minimum length.

    Args:
        n_lower (int, optional): Minimum number of lowercase letters. Defaults to 3.
        n_upper (int, optional): Minimum number of uppercase letters. Defaults to 3.
        n_digits (int, optional): Minimum number of digits. Defaults to 1.
        n_special (int, optional): Minimum number of special characters. Defaults to 1.
        minimum_length (int, optional): Minimal total length of the password. Defaults to 12.

    Returns:
        str: A randomly generated password meeting the specified criteria.

    Example:
        >>> generate_password(n_lower=2, n_upper=2, n_digits=2, n_special=2, minimum_length=10)
        'aB3#dE2&fG'
    """

    lower = random.choices(string.ascii_lowercase, k = n_lower)
    upper = random.choices(string.ascii_uppercase, k = n_upper)
    digits = random.choices(string.digits, k = n_digits)
    special = random.choices(string.punctuation, k = n_special)

    n_extra = max(0, minimum_length - n_lower - n_upper - n_digits - n_special)
    extra = random.choices(string.ascii_letters + string.digits, k = n_extra)

    all = lower + upper + digits + special + extra

    random.shuffle(all)

    password = ''.join(all)

    return password


def check_password_requirements(password: str,
                   n_lower: int = 3,
                   n_upper: int = 3,
                   n_digits: int = 1,
                   n_special: int = 1,
                   minimum_length: int = 12) -> bool:
    """
    Check if a password meets the specified security requirements.

    The password must contain at least:
        - `n_lower` lowercase letters
        - `n_upper` uppercase letters
        - `n_digits` numeric digits
        - `n_special` special characters (punctuation)
    and have a total length of at least `minimum_length`.

    Args:
        password (str): The password string to validate.
        n_lower (int, optional): Minimum number of lowercase letters. Defaults to 3.
        n_upper (int, optional): Minimum number of uppercase letters. Defaults to 3.
        n_digits (int, optional): Minimum number of digits. Defaults to 1.
        n_special (int, optional): Minimum number of special characters. Defaults to 1.
        minimum_length (int, optional): Minimum required total length of the password. Defaults to 12.

    Returns:
        bool: True if the password meets all requirements, False otherwise.

    Example:
        >>> check_password("Abc123!@#", n_lower=2, n_upper=1, n_digits=2, n_special=2, minimum_length=8)
        True

        >>> check_password("abc123", n_lower=2, n_upper=1, n_digits=2, n_special=1, minimum_length=8)
        False
    """

    if len([c for c in password if c in string.ascii_lowercase]) < n_lower:
        return False
    
    if len([c for c in password if c in string.ascii_uppercase]) < n_upper:
        return False

    if len([c for c in password if c in string.digits]) < n_digits:
        return False

    if len([c for c in password if c in string.punctuation]) < n_special:
        return False

    if len(password) < minimum_length:
        return False

    return True


def is_common_password(password):
    filename = 'Cursus/Dag 3/10-million-password-list-top-1000000.txtX'

    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line.lower() == password.lower():
                    return True
                
        return False

    except FileNotFoundError:
        raise Exception(f'Cannot open file {filename}!')

    except:
        raise Exception('OOOOOPS')



# ------------------------------------------------------

if __name__ == '__main__':

    new_password = generate_password(0, 0, 8, 0, 0)
    print(f'Your new password is: {new_password}')

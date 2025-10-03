def banner(s):
    n = len(s)
    print((n + 6) * '*')
    print(f'*  {s}  *')
    print((n + 6) * '*')


def create_banner(s: str, c: str='*') -> str:
    """Create a string containing the tekst s surrounded by characters like a banner."""
    n = len(s)
    lines = [(n + 6) * c, 
             f'{c}  {s}  {c}',
             (n + 6) * c]
    return '\n'.join(lines)


def print_banner(s: str, c: str='*'):
    """Print a banner"""
    print(create_banner(s, c))


def koffie_tijd():
    print("      ( (")
    print("       ) )")
    print("    ........")
    print("    |      |]")
    print("    \\      /")
    print("     `----'")


          
# --------------------------------------------------------

# tekst = input('Geef tekst: ')

# banner(tekst)
# print_banner(tekst, '$')
# print_banner(tekst, '\u2620')

# # koffie_tijd()

import passwords

# new_password = passwords.generate_password()
# print(f'Your new password is: {new_password}')

# print(f'Or: {passwords.generate_password(8, 0, 0, 0, 8)}')
# print(f'Or: {passwords.generate_password(0, 8, 0, 0, 8)}')
# print(f'Or: {passwords.generate_password(0, 0, 8, 0, 8)}')

password = input('Enter your password: ')

# if passwords.check_password_requirements(password, 1, 1, 1, 1, 10):
#     print('Your password is OK')

# else:
#     print('Your password does not satisfy the requirements! Choose a different password.')

try:
    if passwords.is_common_password(password):
        print('Your password is too common! Choose a different password.')
    else:
        print('Your password is OK')

except Exception as ex:
    print(ex)
username_list = ['chris', 'frank', 'jack', 'welshy', 'jim']

print('\n'
      ':: Welcome to the Shipping Accounts Program App ::'
      '\n')

username = input('Please input your username:'
                 '\n').lower()

if username in username_list:
    print('Hello {}. Welcome back to your account.'.format(username.title()))

    print('\n'
          'Current shipping prices are as follows:'
          '\n\n')

    print('Shipping orders from 0 to 100:\t\t£5.10 each')
    print('Shipping orders from 100 to 500:\t£5.00 each')
    print('Shipping orders from 500 to 1000:\t£4.95 each')
    print('Shipping orders over 1000:\t\t\t£4.80 each')

    amount = int(input('\n'
                       'How many orders would you like to make?'
                       '\n'))

    if 0 <= amount < 100:
        print('To ship {0} items it will cost you £{1} at £5.10 per item.'.format(amount, float(amount) * 5.10))
    elif 100 <= amount < 500:
        print('To ship {0} items it will cost you £{1} at £5.00 per item.'.format(amount, float(amount) * 5.00))
    elif 500 <= amount < 1000:
        print('To ship {0} items it will cost you £{1} at £4.95 per item.'.format(amount, float(amount) * 4.95))
    elif 1000 <= amount:
        print('To ship {0} items it will cost you £{1} at £4.80 per item.'.format(amount, float(amount) * 4.80))

    ordered = input('\n'
                    'Would you like to place the order? (Y/N)').lower()

    if ordered == 'y':
        print('Okay. Shipping your {} item(s)'.format(amount))
    else:
        print('Okay. No order will be placed at this time.')

else:
    print('Sorry, you do not have an account with us. Goodbye.')

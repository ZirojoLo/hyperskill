def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have, {name}!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is {str(age)}; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    while True:
        choice = input("""
        What is the best programming language?
        1. Java
        2. Python
        3. C++
        4. JavaScript
        """)
        if choice == '2':
            break
        else:
            print('Please, try again.')
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')

    
def start_the_bot():
  greet('Aid', '2020')
  remind_name()
  guess_age()
  count()
  test()
  end()


if __name__ = "__main__":
  start_the_bot()

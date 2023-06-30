import random

def game(guess, answer):
    if  0 < int(guess) < 11:
        if guess == answer:
            print('You are a genius! You won the game!')
            return True
        else:
            print('Wrong guess! Try again')
    else:
        print('Hey silly, I said 1 to 10. Try again within the range!')
        return False

if __name__ == '__main__':
    
    answer = random.randint(1, 10)
    
    while True:
        try:
            guess = int(input('Guess the lucky number of the day within 1~10:  '))
            
            if (game(guess,answer)):
                break
        
        except ValueError: 
            print('please enter a number')
            continue
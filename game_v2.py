"""Guess the number
The computer makes a guess and guesses the number itself"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guess the number

    Args:
        number (int, optional): The hidden number. Defaults to 1.

    Returns:
        int: The number of attempts.
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break # exit the loop if you guessed right
    return(count)
print(f"The number of attempts is {random_predict()}")


def score_game(random_predict) -> int:
    """For how many attempts on average out of 1000 approaches does our algorithm guess correctly

    Args:
        random_predict (_type_): _guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = [] #list to save the number of attempts
    np.random.seed(1) #fixing seed for reproducibility 
    random_array = np.random.randint(1,101, size=(1000)) # made a list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # count the average number of attempts
       
    print(f"Your algorithm guesses the number in avarage for: {score} attempts")
    return score

#RUN
if __name__== "__main__":
    score_game(random_predict)
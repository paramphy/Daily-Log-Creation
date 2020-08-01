import random

def q1():

    quote = "Your limitation—it’s only your imagination."
    return(quote)

def q2():

    quote = "Push yourself, because no one else is going to do it for you."
    return(quote)   

def q3():

    quote = "Sometimes later becomes never. Do it now."
    return(quote)   

def q4():

    quote = "Great things never come from comfort zones."
    return(quote)   

def q5():

    quote = "Dream it. Wish it. Do it."
    return(quote) 

def q6():

    quote = "Success doesn’t just find you. You have to go out and get it."
    return(quote) 

def q7():

    quote = "The harder you work for something, the greater you’ll feel when you achieve it."
    return(quote) 

def q8():

    quote = "Dream bigger. Do bigger."
    return(quote) 

def q9():

    quote = "Don’t stop when you’re tired. Stop when you’re done."
    return(quote) 

def q10():

    quote = "Wake up with determination. Go to bed with satisfaction."
    return(quote) 

def q11():

    quote = "Do something today that your future self will thank you for."
    return(quote) 

def q12():

    quote = "Little things make big days."
    return(quote)  

def q13():

    quote = "It’s going to be hard, but hard does not mean impossible."
    return(quote)  

def q14():

    quote = "Don’t wait for opportunity. Create it."
    return(quote)  

def q15():

    quote = "Sometimes we’re tested not to show our weaknesses, but to discover our strengths."
    return(quote)  

def q16():

    quote = "The key to success is to focus on goals, not obstacles."
    return(quote) 
def q17():

    quote = "Dream it. Believe it. Build it."
    return(quote) 

def random_quote():
    rand = random.randint(1,17)
    if rand == 1:
        q = q1()
    elif rand == 2:
        q = q2()
    elif rand == 3:
        q = q3()
    elif rand == 4:
        q = q4()
    elif rand == 5:
        q = q5()
    elif rand == 6:
        q = q6()
    elif rand == 7:
        q = q7()
    elif rand == 8:
        q = q8()
    elif rand == 9:
        q = q9()
    elif rand == 10:
        q = q10()
    elif rand == 11:
        q = q11()
    elif rand == 12:
        q = q12()
    elif rand == 13:
        q = q13()
    elif rand == 14:
        q = q14()
    elif rand == 15:
        q = q15()
    elif rand == 16:
        q = q16()
    elif rand == 17:
        q = q17()
    
    return(q)

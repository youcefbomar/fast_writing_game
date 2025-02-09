import os
from termcolor import colored

keys_to_skip = ['caps lock','ctrl','shift','alt','alt gr','right ctrl','right shift','num lock','tab','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','enter','menu','home']

def main(text , goal_text , event):
    key_check(event.name,text)
    similarity = similarity_check(goal_text,text)
    os.system('cls' if os.name == 'nt' else 'clear')    # Clear the console output
    show = ''.join(text)
    print(goal_text,'\n\n')
    printer(similarity,show) 


def printer(similarity , printable):
    if similarity == True :
        print(colored(printable,'white','on_green'))
    else :
        print(colored(printable,'white','on_red'))


def similarity_check(main_text,written_text):
    try :
        size_of_written = int(len(written_text))
        for i in range(size_of_written) :
            if written_text[i]==main_text[i] :
                similarity = True
            else :
                similarity = False
                return similarity
        return similarity
    except :
        pass



def key_check(key,text):

    if key in keys_to_skip:
        pass

    elif key == 'backspace' :
        try :
           text.pop()
        except :
            pass

    elif key == 'space':
        text.append(' ')
        
    elif key == 'decimal':
        text.append('.')

    else :
        text.append(key)

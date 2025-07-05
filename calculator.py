print("CALCULATOR")
HISTORY_FILE = 'history.txt'

def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No data found")
    else:
        print("---------HISTORY----------")
        for line in lines:
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print("History cleared")

def save_detils(b, Result):
    file = open(HISTORY_FILE, 'a')
    file.write(b + '=' + str(Result) + '\n')

while True:
    print("What you want to do:-  1)Calculate  2) History  3) Clear Histroy  4) Exit  ")
    a = input("Tell your Response:- ").lower()
    
    try:
        if a == '1' or a == 'calculate':
            b = input("Tell your Expression :- ")
            Result = eval(b)
            print(f'Result:- {Result}')
            save_detils(b , Result)
        elif a == '2' or a == 'history':
            show_history()
        elif a == '3' or a == "clear history":
            clear_history()
        elif a == '4' or a == 'exit':
            print("Exiting Calculator")
            break
        
        else:
            print("Choose correctly")
            break
    except Exception as err:
        print(f"Zero division error :- can't divide by zero as {err}")    
            
    
def main():
    print("\033[H\033[J", end="")
    rulesDir = input("Location of rules >> ")
    text: str = ""
    
    with open(rulesDir, 'r') as f:
        text = f.read()
    

if __name__ == '__main__':
    main()

class Lexer:
    def __init__(self):
        pass
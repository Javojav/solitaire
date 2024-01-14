import games.spider.spider 

def displayMenu():
    print("Welcome to Solitaire!")
    print("1. Spider Solitaire")
    print("q. Quit")
    print("")


def quit():
    exit()


def menuInput():
    choice = input("Enter your choice: ")

    if choice == "1":
        return games.spider.spider.spiderMain, ["games/spider/config.json"]
    elif choice == "q":
        return quit, None
    else:
        print("Invalid choice")
        return main, None


def main():
    displayMenu()
    
    execute, args = menuInput()

    if args is not None:
        execute(*args)
    else:
        execute()
    

if __name__ == '__main__':
    main()
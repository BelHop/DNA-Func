from functions.replication import init
from functions.transcription import Tinit
from functions.translation import tinit
from read import Helicase


def start():
    try:
        process = input("""
1) DNA replication
2) DNA transcription
3) DNA translation
4) Split helix

Any other key to quit
What would you like to do: """)

        if process == "1":
            init()
        elif process == "2":
            Tinit()
        elif process == "3":
            tinit()
        elif process == "4":
            Helicase()
        else:
            print("quitting...")
    except (KeyboardInterrupt, SystemExit):
        print("\nquitting...")
        pass


if __name__ == "__main__":
    start()

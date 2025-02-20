import sys
def get_integer() -> int:
    while True:
        try:
            return(int(input('type a number:  ')))
        except ValueError:
            print('not an integer number: try again')
        except KeyboardInterrupt: #CTRL-C
            print('\n If you want to exit type CTRL-D')
        except EOFError: # CTRL-D
            sys.exit('\n exit as requested')

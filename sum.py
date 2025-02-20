def main():
    import sys
    try:
        x,y = float(sys.argv[1]), float(sys.argv[2])
        print('the sum is',x+y)
    except IndexError:
        print('missing argument')
    except ValueError:
        print('The arguments are not numbers')

main()

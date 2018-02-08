
def get_input():
    while True:
        try:
            yield ''.join(input())
        except EOFError:
            break    

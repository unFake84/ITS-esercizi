'''
Large Shirts:
Modify the make_shirt() function so that shirts are large by default with a message that reads
I love Python.
Make a large shirt and a medium shirt with the default message,
and a shirt of any size with a different message.
'''

def make_shirt(size: str = 'L', text: str = 'I love Python.') -> None:

    print(f"The T-shirt of size {size} contains this sentence ‘{text}’..")

if __name__ == "__main__":

    make_shirt()
    make_shirt("M")
    make_shirt("XS", "I REALLY LOVE PYTHON!")
def save_to_file(content, filename): 
    with open(filename, 'w') as file: 
        file.write(content)

def read_file(filename): 
    with open(filename, 'r') as file: 
        return file.read()

def find_in(interable, finder, expected): 
    for i in iterable: 
        if finder(i) == expected: 
            return i 

    raise NotFoundError(f'{expected} not found in provided iterable.')
    
class NotFoundError(Exception): 
    pass

print(__name__)
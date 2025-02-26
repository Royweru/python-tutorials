file_path = 'textfiles/newme.txt'

with open(file_path) as file_object :
    new_file_lines = file_object.readlines()
    
count = 0

for line in new_file_lines :
    count += 1
    modified_line = line.replace("Python", "C")
    print(f"line {count} . {modified_line.rstrip()} ")
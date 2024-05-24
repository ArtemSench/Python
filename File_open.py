from pprint import pprint

file_name = 'byron.txt'
file = open(file_name, mode = 'r', encoding = 'utf-8')
file_content = file.read()
file.close()
pprint(file_content)
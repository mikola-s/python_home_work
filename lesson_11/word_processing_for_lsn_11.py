from os import getcwd, listdir, linesep


txt_file_list = []
print("choice file and enter it number")

for counter in listdir(getcwd()):
    if counter[-4::] == '.txt':
        txt_file_list.append(counter)
        print(str(len(txt_file_list)) + '. ' + str(txt_file_list[-1]))

choice_num = int(input())

with open(txt_file_list[choice_num - 1], 'r') as txt_file:
    txt_file_content_set = set(txt_file.read().split(linesep))

print(txt_file_content_set)

with open('rec_' + txt_file_list[choice_num - 1], 'w') as txt_file:
    for string_of_file in txt_file_content_set:
        txt_file.writelines(string_of_file)

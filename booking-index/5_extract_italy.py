import os
from bs4 import BeautifulSoup

# Define the folder containing the XML files
folder_path = '4@_decompressed_sitemaps'
output_file = '5@_italian_hotels_list.txt'

# Define the range of files and line numbers

counter_start = 37
start_line_number = 17603

counter_end = 43
end_line_number = 47147

file_name_base = 'sitembk-hotel-it.00'
file_extension = '.xml'

counter_iterations = counter_end - counter_start

is_within_range = False
output_lines:list[str] = []

# Loop through all files
for i in range(counter_start, counter_end+1):
    file_name = file_name_base + str(i) + file_extension
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        if i == counter_start:
            output_lines.extend(lines[start_line_number-1:])
        elif i == counter_end:
            output_lines.extend(lines[:end_line_number])
            break
        else:
            output_lines.extend(lines)


loc_tag="<loc>"
loc_tag_end="</loc>"

urls = [line.split(loc_tag)[-1].split(loc_tag_end)[0] + "\n" for line in output_lines if loc_tag in line]

# Write the collected lines to an output file
with open(output_file, 'w', encoding='utf-8') as out_file:
    out_file.writelines(urls)

# print(f'Lines from {start_file}:{start_line_number} to {end_file}:{end_line_number} have been written to {output_file_path}')

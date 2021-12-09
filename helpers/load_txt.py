from pathlib import Path

def load_txt_to_list(day: int, line_type: str):
    
    day_str = 'day' + str(day)
    
    path_parts = [f"aoc-2021-{day_str}-input.txt"]
    file_path = Path.cwd().joinpath(*path_parts)
    
    with open(file_path, 'r') as input_file:
        
        lines = input_file.readlines()
        
        if line_type == "int":
            input_list = [int(i) for i in lines]
        elif line_type == "str":
            input_list = lines

            
    return input_list
    


def welcome():
    print("""
*********************************
Welcome to MadLibs! 
To play, please {enter} the 
{correct} word type when prompted.
Have {farts}!
*********************************
""")

example = '../assets/dark_and_stormy_night_template.txt'
example2 = '../assets/make_me_a_video_game.txt'

def read_template(txt_file):
    try:
        with open(txt_file, 'r') as f:
            contents = f.read()
        return contents
    except FileNotFoundError as not_found:
        raise not_found


# print(read_template('../assets/dark_and_stormy_night_template.txt'))

def parse_template(start_string):
    stripped_string = start_string.replace("Adjective", "").replace("Noun", "")

    pieces_string = start_string
    pieces = []

    while pieces_string.find("{") != -1:
        slice_open = pieces_string.find("{")
        slice_close = pieces_string.find("}")
        pieces.append(pieces_string[slice_open+1:slice_close])
        pieces_string = pieces_string[:slice_open] + pieces_string[slice_close+1:]
    # print(pieces)
    pieces = tuple(pieces)

    # print(stripped_string)
    # print(pieces)
    return (stripped_string, pieces)


# parse_template(read_template(example))

def merge(empty_string, new_inputs):
    new_lib = empty_string.format(*new_inputs)
    return new_lib


if __name__ == "__main__":
    welcome()
    collected_answers = []
    (stripped_string, pieces) = parse_template(read_template(example))

    for x in pieces:
        print(f"supply \"{x}\" ")
        answer = input("> ")
        collected_answers.append(answer)

    collected_answers = tuple(collected_answers)
    new_lib = merge(stripped_string, collected_answers)
    print(f"""
    your new madlib:
    {new_lib}
    
    Thanks for playing!
    """)

    with open('../assets/new_lib.txt', 'w') as new_file:
        new_file.write(new_lib)
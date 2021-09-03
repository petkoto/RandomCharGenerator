import random
import string
import json

def main():
    options = ['English alphabet', 'Macedonian alphabet', 'Your list of characters', 'Exit']
    data = dict()
    replacement = bool()
    print_start_screen()
    choice = get_choice(options)
    if choice != len(options):
        data = generate_data(choice)
        replacement = get_replacement_choice()

    fn_dict = {len(options): break_function}
    fn_dict.setdefault(choice, perform_picks)

    fn_dict[choice](data, choice, replacement)


def print_start_screen():
    """
    Prints the first welcome screen
    :return:
    """

    print('This is a random letter generator. Useful for games such as: Brza Geografija :)\n'
          'Options for generating letters are:')
    # print_options(opts)


def print_options(opts: list):
    """
    Printns available options to choose from to randomly generate chars from.
    :param opts: list() List of options
    :return:
    """
    for i in range(0, len(opts)):
        print('{num}. \t{opt}'.format(num=i+1, opt=opts[i]))


def add_separator():
    print(32*"-")


def get_choice(opts: list):
    """
    Gets the option choice for type of Alphabet to pick random chars from
    :param opts: list() List of Alphabets available
    :return: Integer of the chosen option in seq number
    """

    opts_len = len(opts)
    no_selection = True
    choice = opts_len           # Set default value of choice to the Exit function
    while no_selection:
        print_options(opts)
        choice = input("Choose one of the options in range: [1,{0}]"
                       " through typing the correct ordered number and pressing Enter\n".format(opts_len))
        try:
            choice = int(choice)
        except IOError:
            print("Wrong input, try again...")
            add_separator()
        else:
            if (choice <= opts_len) and (choice > 0):
                no_selection = False
            else:
                add_separator()
                print("The number \"{2}\" you've entered is out of the range. Choose an option between  {0} and {1}."
                      .format(1, opts_len, choice))
                add_separator()
    return choice


def get_replacement_choice():
    no_selection = True

    while no_selection:
        replacement = input("Should be there a replacement back of the chosen letters? (Y,N)\n")
        try:
            replacement = str(replacement)
        except IOError:
            add_separator()
            print('Wrong input, try again. For "YES" type in \"Y\", for "NO" type in \"N\"')
            add_separator()
        else:
            if replacement.upper() == "Y":
                # no_selection = False
                replacement_decision = True
                print("You've selected replacement of the chars, "
                      "once picked the characters will be returned to the selection pool.\n")
                return replacement_decision
            elif replacement.upper() == "N":
                # no_selection = False
                replacement_decision = False
                print("You've selected no replacement of the chars, "
                      "once picked the characters will be removed from the selection pool.\n")
                return replacement_decision
            else:
                add_separator()
                print('Wrong input, try again. For "YES" type in \"Y\", for "NO" type in \"N\"')
                add_separator()


# Choose random item with or without replacement
def get_random_item(list_to_choose: list, replacement: bool):
    try:
        rn = random.randint(0, len(list_to_choose) - 1)
    except IOError:
        print('You entered an empty list of characters')
    else:
        if replacement:
            random_item = list_to_choose[rn]
        else:
            random_item = list_to_choose.pop(rn)
        return [list_to_choose,
                random_item,
                ]


def get_your_input():
    s = input("Type in the list of characters:\n")
    return list(s.upper())


def generate_data(choice: int):
    data = dict()
    data_list = list()
    # Get English alphabet:
    data_list.append(list(string.ascii_uppercase))
    # Get Macedonian alphabet:
    data_list.append(list('АБВГДЃЕЖЗЅИЈКЛЉМНЊОПРСТЌУФХЦЧЏШ'))
    # Your input:
    if choice == 3:
        data_list.append(get_your_input())
    for i in range(0, len(data_list)):
        data[i+1] = data_list[i]
    return data            # {"en_alphabet": en_alphabet, "mk_alphabet": mk_alphabet}


def perform_picks(data: dict, choice: int, replacement: bool):
    s = data[choice]
    choose_char = True
    while choose_char:
        [s, random_char] = get_random_item(s, replacement)
        add_separator()
        print("The chosen character is: {}".format(random_char))
        add_separator()
        print("{0} more characters left to choose".format(len(s)))
        try:
            play_again = input("To choose another character just press Enter, to Quit type in \"Q\"\n")
            str(play_again)
        except IOError:
            print()
        else:
            if play_again.upper() == "Q":
                choose_char = False

        if len(s) == 0:
            print("All characters from the list have been popped out. The random selection stops here.")
            choose_char = False


def break_function(*args):
    return 0


if __name__ == "__main__":
    main()

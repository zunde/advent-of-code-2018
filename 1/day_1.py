"""Advent of code - day 1."""

def change_frequency(orig, new):
    orig += new
    return orig


def main():
    current_frequency = 0
    path = 'day_1_input.txt'
    frequency_found = False
    freq_list = []
    freq_list.append(current_frequency)

    original_freq = []
    # Create copy of a file in the array to make it faster
    with open(path, 'r') as file:
        for line in file:
            original_freq.append(int(line.rstrip().strip().lstrip()))

    while(not frequency_found):
        # Iterate over the original input list as long as needed
        for num in original_freq:
            current_frequency = change_frequency(current_frequency, num)
            if(current_frequency in freq_list):
                print("frequency {} has been twice.".format(current_frequency))
                frequency_found = True
                break
            freq_list.append(current_frequency)


main()

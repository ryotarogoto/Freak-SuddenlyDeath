#!/usr/bin/env python
# -*- coding: utf-8 -*-

def generator(characters):
    decoded_lines = characters.split("\n")
    char_length = len(characters)
    max_length = 0
    max_length = char_length if(char_length > max_length) else max_length
    ascii_art = list()
    frame_length = round((max_length + 6) / 2)
    ascii_art.append('＿' + '人' * frame_length + '＿')
    for line in decoded_lines:
        str_length = max_length - len(line)
        space_length = '  ' * round(str_length / 2)
        (left, right) = (space_length, space_length)
        left = (left + ' ') if(str_length % 2 != 0) else left
        ascii_art.append('＞ ' + left + line + right + ' ＜')
    ascii_art.append('￣' + '^Y' * (frame_length - 1) + '^￣')
    return ascii_art

def sudden_death(characters):
    ascii_art = generator(characters)
    return '\n'.join(ascii_art)

def sudden_death_single(characters):
    ascii_art = generator(characters)
    return ''.join(ascii_art)

if __name__ == "__main__":
    print(sudden_death('突然の死') + '\n')
    print(sudden_death('突然の\n死') + '\n')
    print(sudden_death_single('突然の死') + '\n')

    print(sudden_death('suddenly_death') + '\n')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2016-11-25
# copyright © Philip R. Huffman 2016 all rights reserved.
"""
helpers.py A collection of simple cryptographic routines.
"""

from string import ascii_lowercase
from string import ascii_letters
from string import digits
from string import punctuation

__author__ = "Philip R. Huffman"


def create_my_printable():
    """creates a big string
    :returns: TODO

    """
    return ascii_letters + digits + punctuation + ' '

my_printable = create_my_printable()


def alphabet_position(char):
    """
    returns index of character in string.ascii_lowercase
    :param char: string of length 1
    :return: integer
    """
    return ascii_lowercase.index(char.lower())


def alt_position(char):
    """
    returns index of character in string.my_printable
    :param char: string of length 1
    :return: integer
    """
    return my_printable.index(char)


def block(text_string, block_size=5):
    """
    inserts a blank every block size characters
    :param text_string: string
    :param block_size: integer
    :return: string
    """
    o_string = ''
    for i in range(0, len(text_string), block_size):
        o_string += text_string[i:i + block_size] + ' '
    return o_string


def rotate_character(char, rot):
    """
    translates character by rot characters in string.ascii_lowercase
    :param char: string of length one
    :param rot: integer
    :return: string of length one
    """
    if char in ascii_letters:
        o_char = alphabet_position(char) + rot
        if o_char >= 26:
            o_char -= 26
        adj = ord('A')
        if char in ascii_lowercase:
            adj = ord('a')
        return chr(o_char + adj)

    return char


def rot_character(char, rot):
    """
    translates character by rot characters in string.my_printable
    :param char: string of length one
    :param rot: integer
    :return: string of length one
    """
    if char in my_printable:
        o_char = alt_position(char) + rot
        if o_char >= len(my_printable):
            o_char -= len(my_printable)
        return my_printable[o_char]

    return char


def pad(text_string, block_size=5):
    """
    adds blanks to end of string while length ins not a multiple of block size
    :param text_string: string
    :param block_size: integer
    :return: string
    """
    while len(text_string) % block_size:
        text_string += ' '
    return text_string


def unblock(n_string, block_size=5):
    """
    inverse of block function
    :param n_string: string
    :param block_size: integer
    :return: string
    """
    tmp = n_string.split()
    return ''.join(tmp)

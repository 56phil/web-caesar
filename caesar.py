#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2016-11-25
# copyright © Philip R. Huffman 2016 all rights reserved.
"""
uses the caesar method to encrypt a string.
"""
from sys import argv
from helpers import rotate_character

__author__ = 'Philip R. Huffman'


def decrypt(cypher_text, shift_amount):
    """
    convert cypher text to plain text
    :param cypher_text: string
    :param shift_amount: int
    :return: string
    """
    plain_text = ''
    for char in cypher_text:
        plain_text += rotate_character(char, 26 - shift_amount)
    return plain_text


def encrypt(plain_text, shift_amount=13):
    """
    convert plain text to cypher text
    :param plain_text: string
    :param shift_amount: integer
    :return: string
    """
    cypher_text = ''
    for char in plain_text:
        cypher_text += rotate_character(char, shift_amount)
    return cypher_text


def main():
    """
    for use from terminal
    :return: none
    """
    if user_input_is_valid(argv):
        rotation_number = int(argv[1])
        plain = input('Type a message: ')
        print('{}'.format(encrypt(plain, rotation_number)))
    else:
        print('usage: python3 caesar.py n')


def user_input_is_valid(args):
    """
    validates terminal input
    :param args: list
    :return: bool
    """
    return len(args) == 2 and args[1].isdigit()


if __name__ == '__main__':
    main()

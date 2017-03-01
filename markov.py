from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = open(file_path).read()
    # text += open(file_path2).read()

    return text


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    words = text_string.split()

    start_index = 0
    end_index = 1
    value_index = 2

    while value_index < len(words):
        word_pair = (words[start_index], words[end_index])
        value = words[value_index]
        chains[word_pair] = chains.get(word_pair, []) + [value]
        start_index += 1
        end_index += 1
        value_index += 1

    chains[(words[start_index], words[end_index])] = [""]

    return chains


def make_n_chains(text_string, n):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2.., wordn)
    and the value would be a list of the word(s) that follow those words
    in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    words = text_string.split()

    start_index = 0
    end_index = n - 1
    value_index = n

    while value_index < len(words):
        word_tuple = tuple(words[start_index:end_index + 1])
        value = words[value_index]
        chains[word_tuple] = chains.get(word_tuple, []) + [value]
        start_index += 1
        end_index += 1
        value_index += 1

    chains[tuple(words[start_index:end_index + 1])] = [""]
    print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    while True:
        word_pair = choice(chains.keys())
        if word_pair[0][0].isupper() is True:
            break

    end_punctuation = [".", "!", "?"]
    while True:
        end_word_pair = choice(chains.keys())
        if end_word_pair[1][-1] in end_punctuation:
            break

    while word_pair != end_word_pair:
        if word_pair[1] == "":
            break

        text += word_pair[0] + " "
        next_word = choice(chains[word_pair])
        word_pair = (word_pair[1], next_word)

    text += word_pair[0] + " " + word_pair[1]
    return text


def make_n_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    while True:
        word_tuple = choice(chains.keys())
        if word_tuple[0][0].isupper() is True:
            break

    end_punctuation = [".", "!", "?"]
    while True:
        end_word_tuple = choice(chains.keys())
        if end_word_tuple[-1][-1] in end_punctuation:
            break

    while word_tuple != end_word_tuple:
        if word_tuple[-1] == "":
            break

        text += str(word_tuple[0]) + " "
        next_word = choice(chains[word_tuple])
        word_tuple = word_tuple[1:] + (next_word,)

    text += word_tuple[0] + " " + word_tuple[1]
    return text



input_path = sys.argv[1]
# input_path_2 = sys.argv[2]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# set n to a number
n = 3

# # Get a Markov chain
chains = make_n_chains(input_text, n)


# Produce random text
random_text = make_n_text(chains)

print random_text

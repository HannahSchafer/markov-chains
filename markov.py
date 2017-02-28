from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = open(file_path).read()

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
    words = text.split()

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

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    word_pair = choice(chains)
    print word_pair


#     while word_pair in chains:
#         text += word_pair
#         next_word = choice(chains[word_pair])
#         text += next_word
#         word_pair = (word_pair[1], next_word)

#     return text


text = open_and_read_file("green-eggs.txt")
chains = make_chains(text)
print make_text(chains)


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text

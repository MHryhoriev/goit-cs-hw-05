from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict

def map_function(word):
    """
    Maps a word to a key-value pair (word, 1).

    Args:
        word (str): The input word.

    Returns:
        tuple: A key-value pair (word, 1).
    """
    return word, 1

def shuffle_function(mapped_values):
    """
    Groups mapped key-value pairs by keys.

    Args:
        mapped_values (list): List of key-value pairs.

    Returns:
        dict_items: Grouped key-value pairs.
    """
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()

def reduce_function(key_values):
    """
    Reduces grouped key-value pairs to a single key-value pair.

    Args:
        key_values (tuple): A tuple containing a key and a list of values.

    Returns:
        tuple: A reduced key-value pair (key, sum(values)).
    """
    key, values = key_values
    return key, sum(values)

def map_reduce(text, search_words=None):
    """
    Performs a MapReduce operation to count word frequencies.

    Args:
        text (str): The input text.
        search_words (list, optional): List of words to filter by.

    Returns:
        dict: A dictionary with word frequencies.
    """
    # Remove punctuation
    words = text.split()

    # Filter words if a search list is provided
    if search_words:
        words = [word for word in words if word in search_words]

    # Parallel mapping
    with ThreadPoolExecutor() as executor:
        mapped_values = list(executor.map(map_function, words))

    # Shuffle step
    shuffled_values = shuffle_function(mapped_values)

    # Parallel reduction
    with ThreadPoolExecutor() as executor:
        reduced_values = list(executor.map(reduce_function, shuffled_values))

    return dict(reduced_values)

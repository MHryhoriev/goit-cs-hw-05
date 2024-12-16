import requests
import string

def get_text(url):
    """
    Fetches text from a given URL.

    Args:
        url (str): The URL to fetch the text from.

    Returns:
        str: The fetched text, or None if there was an error.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return None

def remove_punctuation(text):
    """
    Removes punctuation from a given text.

    Args:
        text (str): The input text.

    Returns:
        str: The text without punctuation.
    """
    return text.translate(str.maketrans("", "", string.punctuation))

from utils import get_text, remove_punctuation
from task_2.map_reduce import map_reduce
from visualization import visualize_top_words

def main():
    """
    Main entry point for the script. Fetches text from a URL, processes it using MapReduce,
    and visualizes the most frequent words.

    Returns:
        None
    """
    # URL of the text to process
    url = "https://gutenberg.net.au/ebooks01/0100021.txt"

    # Fetch text from URL
    text = get_text(url)
    if text:
        text = remove_punctuation(text)

        # Define the search words
        search_words = ["the", "of", "a", "was", "to", "and", "in", "that", "it", "had"]

        # Perform MapReduce
        result = map_reduce(text, search_words)

        # Print and visualize the results
        print("Word Frequency Results:", result)
        visualize_top_words(result)
    else:
        print("Error: Failed to fetch text from the URL.")

if __name__ == "__main__":
    main()

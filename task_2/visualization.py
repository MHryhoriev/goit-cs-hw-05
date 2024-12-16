import matplotlib.pyplot as plt

def visualize_top_words(word_counts, top_n=10):
    """
    Visualizes the top N most frequent words using a horizontal bar chart.

    Args:
        word_counts (dict): A dictionary of word frequencies.
        top_n (int): Number of top words to visualize.

    Returns:
        None
    """
    # Sort and select the top N words
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]

    # Unpack words and counts
    words, counts = zip(*sorted_word_counts)

    # Plot the horizontal bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(words, counts, color="skyblue")
    plt.title("Top {} Most Frequent Words".format(top_n), fontsize=16)
    plt.xlabel("Frequency", fontsize=14)
    plt.ylabel("Words", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

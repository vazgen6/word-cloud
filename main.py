import wordcloud
from matplotlib import pyplot as plt


def calculate_frequencies(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    ignore_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "in", "for"
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", "read"]

    freq = {}

    for word in file_contents.split():
        lower_word_stripped = word.lower().strip(punctuations)
        if lower_word_stripped not in ignore_words:
            if lower_word_stripped in freq:
                freq[lower_word_stripped] = freq[lower_word_stripped] + 1
            else:
                freq[lower_word_stripped] = 1

    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(freq)
    return cloud.to_array()


with open('sample.txt') as file:
    myimage = calculate_frequencies(file.read())
    plt.imshow(myimage, interpolation='nearest')
    plt.axis('off')
    plt.show()

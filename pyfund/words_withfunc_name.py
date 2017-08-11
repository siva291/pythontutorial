from urllib.request import urlopen
def words_func():
        with urlopen('http://sixty-north.com/c/t.txt') as story:
            story_words=[]
            for line in story:
                line_words=line.decode('utf-8').split()
                for word in line_words:
                    story_words.append(word)

        for words in story_words:
            print(words)

print(__name__)
if __name__ == '__main__':
    words_func()
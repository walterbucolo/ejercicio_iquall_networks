

ARTICLE = "This is the article from the one we want to write a letter." # This can be a file

class LetterWriter:
    def __init__(self, article) -> None:
        self.article = article.lower().split(' ')
        self.missed_words = []

    def show_article(self):
        print("Pick the words from the following article to write your letter: \n {}".format(ARTICLE))

    def get_words(self):
        return input("Please, insert any words or phrases you want to validate agains the article, : ")
    
    def words_verifier(self, words):
        is_letter_valid = True
        for word in words.lower().split(' '):
            if not self.is_word_valid(word):
                is_letter_valid = False    
        return is_letter_valid

    def is_word_valid(self, word):
        if word in self.article:
            self.article.remove(word)
            return True
        else:
            self.missed_words.append(word)
            return False



def main():
    letter_writer = LetterWriter(article=ARTICLE)
    letter_writer.show_article()
    words = letter_writer.get_words()
    if letter_writer.words_verifier(words=words):
        print("Success")
        if user_wants_to_repeat():
            return main()
        else:
            print("Finished")
    else:
        print("The following words are not part of the article: \n {}".format(''.join(letter_writer.missed_words)))
        if user_wants_to_repeat():
            return main()
        else:
            print("Finished")
        
def user_wants_to_repeat():
    response = input("Press 'Y' if you want to check other words: ")
    if response == 'Y':
        return True
    else:
        return False

main()

"""
He partido de una intencion del usuario de escribir una carta y encontrar las palabras adecuadas en el articulo.

El siguiente codigo muestra al usuario final un articulo/revista y da la posibilidad de insertar palabras, frases o incluso la carta completa. 

Una vez enviada, se le informa al usuario si la misma es correcta o se detallan las palabras que no pertenecen al articulo
dandose la posibilidad de volver a comenzar. 

Si bien el codigo funciona y puede ser probado, hay algunas validaciones que he obviado por cuestiones de practicidad pero que pueden
ser agregadas si se requiere. Por ejemplo, si hay un punto o una coma al final de una palabra, se toma el punto o la coma como parte 
de la palabra (carta.)

El proceso queda explicados dentro del metodo main, los pasos son:
1- Mostrar el articulo
2- Pedir al usuario que escriba una palabra o frase
3- Validar
    - Si es valida 
        3.a.1- Finalizar el proceso
    - Si es invalida
        3.b.1- Mostrar palabras incorrectas
        3.b.2- Preguntar al usuario si quiere volver a comenzar

"""

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
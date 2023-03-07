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

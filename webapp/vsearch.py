def search4letters(phrase:str, letters:str='aeiou')->set:
    return(set(phrase).intersection(set(letters)))
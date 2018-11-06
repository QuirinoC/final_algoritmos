def replace_string(text):
    texto=text.replace('\\xc3\\xa1', 'a')
    texto=texto.replace('\\xc3\\xa9', 'e')
    texto=texto.replace('\\xc3\\xad', 'i')
    texto=texto.replace('\\xc3\\xb3', 'o')
    texto=texto.replace('\\xc3\\xba', 'u')
    texto=texto.replace('\\xc3\\x81', 'a')
    texto=texto.replace('\\xc3\\x89', 'e')
    texto=texto.replace('\\xc3\\x8d', 'i')
    texto=texto.replace('\\xc3\\x93', 'o')
    texto=texto.replace('\\xc3\\x9a', 'u')
    texto=texto.replace('\\xc3\\xba', 'u')
    texto=texto.replace('\\xc3\\x91', 'nn')
    texto=texto.replace('\\xc3\\xb1', 'nn')
    texto=texto.replace('\\xc2\\xa1', '')
    texto=texto.replace('\\xc2\\xbf', '') 
    texto=texto.replace('\\xc2\\xab', '') 
    

    
    texto=texto.replace('\\xe2\\x80\\xa6', '') 
    texto=texto.replace("b'", '')
    texto=texto.replace('"','')
    texto=texto.replace("'",'')


    return texto.replace('"','')



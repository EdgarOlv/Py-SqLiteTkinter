import webbrowser

# Mostrar url usando o navegador padrão. Se o novo for 0, a url é aberto na mesma janela do navegador,
# se possível. Se é novo 1, uma nova janela do navegador é aberto, se possível.

webbrowser.open('www.google.com', new=1, autoraise=True)

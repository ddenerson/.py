import re
import urllib.request as request


html = request.urlopen("http://www.pythonparatodos.com.br/contato")
texto = html.read()

busca_email = r'[\w]+@[\w.-]+'
match = re.findall(busca_email,str(texto))
print(match)

busca_telefone = r'\(\d{2}\) \d{5}\-\d{4}'
match = re.findall(busca_telefone,str(texto))
print(match)

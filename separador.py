import re #import regex

#leitura do documento de texto
with open('Arquivo_texto.txt', 'r') as archive:
    texto = archive.read()
    text_split = texto.split(' ') #separa o texto em uma lista

text_aux = [] #lista final

for values in text_split:
    val = values
    if(val == ','): val = ';' #substitiu as , por ; sozinhas na lista
    
    #encontra as posicoes das virgulas
    virg1 = re.findall('.+[,]$|.+\s.+[,]$', val)  
    virg2 = re.findall('.+[,]\s[,]?$', val) 
    virg3 = re.findall('[,].+\s[,]$', val)
    
    #faz a substituicao das , por ; nos locais encontrados
    if(virg1 != []):
        for i in virg1: text_aux.extend(re.sub(r'[,]$', r';', i) + ' ') #adiciona a string substituida na lista final
    elif(virg2 != []):
        for i in virg2: text_aux.extend(re.sub(r'[,]', r';', i) + ' ')
    elif(virg3 != []):
        for i in virg3: text_aux.extend(re.sub(r'[,]', r';', i) + ' ')
            
    #caso nao encontre virgula somente adiciona a lista de texto final
    elif(virg1 == [] and virg2 == [] and virg3 == []): text_aux.extend(val + ' ') 
        
final_text = ''.join(text_aux) #junta a lista final em uma string

archive.close() #fecha o arquivo

print(final_text)

#faz a escrita no arquivo de texto
with open('New_file_text.txt', 'w') as archive:
    archive.write(final_text)

archive.close() #fecha o arquivo
    

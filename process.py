from pathlib import Path


#read data file list
def datalist(datapath: str = 'data/'):
    links: list = []
    for file in Path(datapath).iterdir():
        filetype = file.name.split('.')
        if len(filetype) > 1:
            if filetype[-1] == 'card':
                links.append(filetype[0])
    
    return links


#read file content
def readfile(name: str):
    with open(f'data/{name}.card', 'r', encoding="utf-8") as f_link:
        content = f_link.read()
    
    return content


#read the file header
def readheader(name: str):
    header: str = ''
    buffer = b''
    with open(f'data/{name}.card', 'rb') as f_link:
        byte = f_link.read(1)
        while byte:
            buffer += byte
            try:
                char = buffer.decode('utf-8')
                buffer = b''
            except UnicodeDecodeError:
                continue
            byte = f_link.read(1)
            header = f'{header}{char}'
            if header[len(header)-2:] == '&&':
                return header[0:len(header)-2]
        return "The header is not found"


#removing a header from the file content
def delheader(content):
    return content.split('&&')[1]


#gets a list of cases (pairs of words)
#to divide cases we use the | character
def getcases(content):
    return content.split('|')


#get a word pair from a words list item taking by getcases()
#to divide a pair of words we use the == characters
def getpair(case):
    return case.split('==')
    

#removing breaks
def cutbreaks(content):
    return content.replace('\n', '')


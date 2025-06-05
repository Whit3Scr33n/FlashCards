import process


#gets a dictionary with headers as keys and corresponding links as values
def links_headers():
    links = process.datalist()
    headers: list = []
    links_and_headers: dict = {}
    for link in links:
        header: str = process.readheader(link)
        if header != "The header is not found":
            links_and_headers[header] = link
            headers.append(header)
    
    return headers, links_and_headers


#gets a 2-dimentional list with pairs of words
def get_word_pairs(link):
    pairs: list = []
    content: str = process.readfile(link)
    content = process.cutbreaks(content)
    content = process.delheader(content)
    cases: list = process.getcases(content)
    for case in cases:
        pairs.append(process.getpair(case))
    
    return pairs


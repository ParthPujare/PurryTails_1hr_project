import re 

def analyzeText(text:str):
    sentences = re.split(r'[.!?]', text)
    words = re.findall(r'\b\w+\b', text)

    return{
        "word_count" : len(words),
        "unique_words" : len(set(words))
    }
import re 
import json 

def jsonify_corpus(raw_texts):
    """extract data into json dictionaries 

        Args: 
            Wikipedia raw text corpus from https://corpus.byu.edu/wikitext-samples/text.zip
        Returns: 
            list of dictionaries [{'text_ID':@@4533, 'text':'rawtext'}]
            
    """
    def text_ID(text, regex="@@\d\d\d\d"):
        ID = re.findall(regex, text)[0]
        return ID
    def raw_text(text,regex="@@\d\d\d\d"):
        raw_text = re.split(regex, txt[0])[1]
        return raw_text
    corpus = [{'text ID': text_ID(t), 'text':raw_text(t)} for t in txt]
    return corpus

def export_corpus(corpus):
    with open('data/02_intermediate/wikitext.json','w') as f:
    for c in corpus:
        json.dump(c, f)
        f.write("\n")
        print('json file exported')

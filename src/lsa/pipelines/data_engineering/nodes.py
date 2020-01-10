import re 
import json  

def jsonify_raw_corpus(filepath):
    """extract data into json dictionaries 

        Args: 
            Wikipedia raw text corpus from https://corpus.byu.edu/wikitext-samples/text.zip
        Returns: 
            list of dictionaries [{'text_ID':@@4533, 'text':'rawtext'}]
            
    """
    # define helper functions 
    def text_ID(text, regex="@@\d\d\d\d"):
        ID = re.findall(regex, text)[0]
        return ID

    def raw_text(text,regex="@@\d\d\d\d"):
        raw_text = re.split(regex, text)[1]
        return raw_text

    # read in raw data 
    print('preprocessing corpus...')
    with open(filepath, 'r') as f:
        file = f.readlines()
        raw_texts = file[3:] # leave out headers and only keep text

    # preprocess raw data
    wikitext_json = [{'text ID': text_ID(t), 'text':raw_text(t)} for t in raw_texts]
    return wikitext_json
    # with open('/Users/nus/Desktop/aas-kedro-mlflow/lsa/data/02_intermediate/wikitext.json','w') as f:
    #     for w in wikitext_json:
    #         json.dump(w, f)
    #         f.write("\n")
    #         print('json file exported')

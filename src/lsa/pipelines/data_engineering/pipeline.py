from typing import Dict
from kedro.pipeline import Pipeline, node
from lsa.pipelines.data_engineering.nodes import jsonify_raw_corpus

def create_pipeline(**kwargs):
    """create the project's pipeline

    Args:
        kwargs: ignore any additional arguments added in the future 

    Returns:
        Pipeline object.
    """
    node1 = node(func=jsonify_raw_corpus,inputs="wikitext",outputs="wikitext_json",name="jsonify_raw_corpus")
    de_pipeline = Pipeline([node1])
    return de_pipeline


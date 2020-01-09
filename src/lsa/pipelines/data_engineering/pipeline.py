from typing import Dict
from kedro.pipeline import Pipeline, node
from .nodes import jsonify_corpus, export_corpus

def create_pipeline(**kwargs):
    """create the project's pipeline

    Args:
        kwargs: ignore any additional arguments added in the future 

    Returns:
        Pipeline object.
    """
    def pipeline = Pipeline(
        [
            node(
                func=jsonify_corpus
                inputs="wikitext",
                outputs="jsonified_corpus"
                name="jsonify_corpus"
            ),
            node(
                func=export_corpus
                inputs="jsonified_corpus"
                outputs="wikitext_json"
            )
        ]
    )
    return de_pipeline


"""Pipeline construction."""

from typing import Dict
import time 

from kedro.pipeline import Pipeline, node
from lsa.pipelines.data_engineering import pipeline as de

print('running pipeline')
time.sleep(5)

def create_pipelines(**kwargs):
    de_pipeline = de.create_pipeline()
    return {
        "de": de_pipeline,
        "__default__": de_pipeline
    }
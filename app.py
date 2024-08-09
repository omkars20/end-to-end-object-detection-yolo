import sys, os
from signLanguage.pipeline.training_pipeline import TrainPipeline
from signLanguage.exception import SignException


def run_pipeline() -> None:
    try: 
        obj = TrainPipeline()
        obj.run_pipeline()
    except Exception as e:
        raise SignException(e, sys)

if __name__ == "__main__":
    run_pipeline()
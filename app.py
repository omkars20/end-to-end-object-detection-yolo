import sys, os
from signLanguage.pipeline.training_pipeline import TrainPipeline
from signLanguage.exception import SignException


def run_pipeline() -> str:
    try: 
        obj = TrainPipeline()
        obj.run_pipeline()
        return "Training succesful thanks for being here"
    except Exception as e:
        raise SignException(e, sys)

if __name__ == "__main__":
    run_pipeline()
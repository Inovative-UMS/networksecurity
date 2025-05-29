from datetime import datetime
import os
from networksecurity.constant import training_pipeline

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIAFCT_DIR)

class TrainigPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIAFCT_DIR
        self.artifact_dir = os.path.join(self.artifact_name,timestamp)
        self.timestamp: str=timestamp


class DataIngestionConfig:
    def __init__(self,trainig_pipeline_confog:TrainigPipelineConfig):
        self.data_ingestion

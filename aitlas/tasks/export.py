import logging

from ..base import BaseDataset, BaseModel, BaseTask
from .schemas import SplitTaskSchema


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


class ExportSplitsTask(BaseTask):
    """Exports the internal split indices to dataset IDs. This might be useful for someone to use the splits elsewhere"""

    schema = SplitTaskSchema

    def __init__(self, model: BaseModel, dataset: BaseDataset, config):
        super().__init__(model, dataset, config)

    def run(self):
        self.dataset.prepare()

        logging.info("And that's it!")
import logging

import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from ..base import BaseDataset, BaseModel
from ..utils import current_ms
from .schemas import BaseClassifierSchema


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


# Available losses. Add keys with new losses here.
losses = {"cross_entropy": nn.CrossEntropyLoss()}


# Available metrics. Add keys with new metrics here.
classification_metrics = {
    # 'accuracy': tf.keras.metrics.CategoricalAccuracy(name='accuracy'),
    # 'precision': tf.keras.metrics.Precision,
    # 'recall': tf.keras.metrics.Recall
}


class BaseClassifier(BaseModel):
    schema = BaseClassifierSchema

    def __init__(self, config):
        super().__init__(config)

        # initialize loss and optmizer
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = None  # this has to be None, here so, we'll actually initialize it in the `fit` method.

    def fit(
        self,
        dataset: BaseDataset = None,
        epochs: int = 100,
        model_directory: str = None,
        save_epochs: int = 10,
        iterations_log: int = 100,
        resume_model: str = None,
        **kwargs,
    ):

        start_epoch = 0
        start = current_ms()

        # load optimizer
        if not self.optimizer:
            self.optimizer = optim.SGD(
                self.parameters(), lr=self.config.learning_rate, momentum=0.9
            )

        # load the model if needs to resume training
        if resume_model:
            start_epoch, loss, start = self.load_model(resume_model, self.optimizer)
            start_epoch += 1

        self.train()
        for epoch in range(start_epoch, epochs):  # loop over the dataset multiple times
            loss = self.train_epoch(
                epoch, dataset, self.optimizer, self.criterion, iterations_log
            )
            if epoch % save_epochs == 0:
                self.save_model(model_directory, self.optimizer, epoch, loss, start)

        logging.info(f"finished training. training time: {current_ms()-start}")

    def train_epoch(self, epoch, dataset, optimizer, criterion, iterations_log):
        start = current_ms()
        running_loss = 0.0
        total_loss = 0.0
        total = 0

        for i, data in enumerate(dataset):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = self(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # log statistics
            running_loss += loss.item()
            total_loss += running_loss

            if (
                i % iterations_log == iterations_log - 1
            ):  # print every iterations_log mini-batches
                logging.info(
                    f"[{epoch}, {i}], loss: {running_loss / iterations_log : %.5f}"
                )
                running_loss = 0.0

            total += 1

        total_loss = total_loss / total
        logging.info(
            f"epoch: {epoch}, time: {current_ms() - start}, loss: {total_loss: %.5f}"
        )
        return total_loss

    def log_epoch(self):
        logging.info("")


class CifarModel(BaseClassifier):
    def __init__(self, config):
        BaseClassifier.__init__(self, config)

        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

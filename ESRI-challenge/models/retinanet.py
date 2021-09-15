import torch
import torchvision

from torchvision.models.detection.retinanet import RetinaNetClassificationHead
from torchvision.models.detection.retinanet import RetinaNetRegressionHead

from .detection import BaseDetectionClassifier

class RetinaNet(BaseDetectionClassifier):
    def __init__(self, config):
        BaseDetectionClassifier.__init__(self, config)

        self.model = torchvision.models.detection.retinanet_resnet50_fpn(pretrained = self.config.pretrained)


        self.model.head.classification_head = RetinaNetClassificationHead(self.model.backbone.out_channels, 
                                                                          self.model.anchor_generator.num_anchors_per_location()[0], 
                                                                          config['num_classes'])
        self.model.head.regression_head = RetinaNetRegressionHead(self.model.backbone.out_channels, self.model.anchor_generator.num_anchors_per_location()[0])
        
        # select either GPU or CPU as the active device
        # GPU is always preferred
        device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

        # move model to the right devicee
        self.model.to(device)

    def forward_train(self, x, y):
        return self.model.forward(x, targets = y)

    def forward_eval(self, x):
        return self.model.forward(x)

    

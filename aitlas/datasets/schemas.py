from marshmallow import fields, validate

from ..base.schemas import BaseDatasetSchema, SplitableDatasetSchema


class EurosatDatasetSchema(SplitableDatasetSchema):
    download = fields.Bool(
        missing=True, description="Whether to download the dataset", example=True
    )
    root = fields.String(
        required=True, description="Dataset path on disk", example="./data/EuroSAT/"
    )
    mode = fields.String(
        missing="rgb",
        default="Work with rgb or all bands mode",
        example="rgb",
        validate=validate.OneOf(["rgb", "all"]),
    )


class CrackForestSchema(SplitableDatasetSchema):
    root = fields.String(
        required=True,
        description="Dataset path on disk",
        example="./data/CrackForest-dataset-master/",
    )


class UcMercedDatasetSchema(SplitableDatasetSchema):
    download = fields.Bool(
        missing=True, description="Whether to download the dataset", example=True
    )
    root = fields.String(
        required=True, description="Dataset path on disk", example="./data/UcMerced/"
    )


class UcMercedMultiLabelsDatasetSchema(SplitableDatasetSchema):
    download = fields.Bool(
        missing=True, description="Whether to download the dataset", example=True
    )
    root = fields.String(
        required=True,
        description="Is it train dataset",
        example="./data/UcMercedMultiLabels/",
    )


class Resisc45DatasetSchema(SplitableDatasetSchema):
    download = fields.Bool(
        missing=True, description="Whether to download the dataset", example=True
    )
    root = fields.String(
        required=True, description="Dataset path on disk", example="./data/Resisc45/"
    )


class PatternNetDatasetSchema(SplitableDatasetSchema):
    download = fields.Bool(
        missing=True, description="Whether to download the dataset", example=True
    )
    root = fields.String(
        required=True, description="Dataset path on disk", example="./data/PatternNet/"
    )


class BigEarthNetSchema(SplitableDatasetSchema):
    lmdb_path = fields.String(required=True, description="Path to the lmdb storage")
    root = fields.String(
        required=True, description="Dataset path on disk", example="./data/BigEarthNet/"
    )
    prepare = fields.Bool(
        missing=False, description="Should the data be processed to LMDB"
    )

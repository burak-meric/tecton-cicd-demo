from tecton import (
    StreamProcessingMode,
    Aggregate,
    stream_feature_view,
    Entity,
    StreamSource,
    spark_stream_config,
    HiveConfig,
    BatchSource,
    FeatureService
)

from tecton.types import Field, Float64, String


user = Entity(
    name='usery',
    join_keys=[Field('user_id', String)],
)

account_entity = Entity(
    name="account",
    description="Enterprise Account id",
    join_keys=[Field("account_id", String)],
    prevent_destroy=False,
)
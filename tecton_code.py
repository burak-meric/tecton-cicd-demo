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
    name='useryzx',
    join_keys=[Field('user_id', String)],
)

account_new = Entity(
    name="account_new",
    description="Enterprise Account id",
    join_keys=[Field("account_id", String)],
    # prevent_destroy=True,
)
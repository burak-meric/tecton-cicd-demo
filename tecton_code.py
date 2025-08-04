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


user = Entity(
    name='user_id',
    join_keys=[Field('user_id', String)],
)
AIFABRIC_STAGING = "aifabric-staging"
ML_MODEL_FILES = "ml-model-files"
TRAIN_DATA = "train-data"
DEFAULT_EXTERNAL_ACCESS_SCHEME = "https"
DEFAULT_INTERNAL_ACCESS_SCHEME = "http"
DEFAULT_EXTERNAL_PORT = 443
MANDATORY_BUCKETS = [TRAIN_DATA, ML_MODEL_FILES, AIFABRIC_STAGING]
TMP = "tmp"
BUCKET_ROOT_PATH = "preflights/"
BUCKET_SUB_PATH = "preflights/sub/"
BINARY_UPLOAD_OBJECT = "binary_upload_object"
BINARY_DOWNLOAD_OBJECT = "binary_download_object"
BINARY_OBJ_SIZE = 25 * 1024 * 1024  # TODO 25MB
PRESIGNED_UPLOAD_TXT = "presigned_upload.txt"
PRESIGNED_DOWNLOAD_TXT = "presigned_download.txt"
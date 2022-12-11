# This is a Django Rest Framework app with custom user model, image/video upload and hls video encoding.

# What's included?
    - Dockerised
    - Postgres db
    - Custom User model with SimpleJWT authentication
    - APIs with read only permission if not authenticated
    - Video/Image file validation
    - HLS videos
    - Use celery to handle the conversion
    - Forced conversion to HLS when not created automatically


# Imrovements coming soon
    - Upload to AWS
    - Upload to IPFS

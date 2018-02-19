#!/usr/bin/env bash

mc mb minio/static
mc mb minio/media
mc policy minio/static
mc policy minio/media
mc policy download minio/static/
mc policy download minio/media/ 

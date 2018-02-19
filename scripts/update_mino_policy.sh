#!/usr/bin/env bash

mc policy minio/static
mc policy minio/media
mc policy download minio/static/
mc policy download minio/media/ 

# -*- coding: UTF-8 -*-
import docker

dockerEnv = docker.from_env()
print('listing all images')
for I in dockerEnv.images.list():
    imgId = I.attrs["Id"]
    print("image tag: ", I.attrs["RepoTags"], " id: ", imgId)
    try:
        print("Trying to remove image", imgId)
        dockerEnv.images.remove(imgId)
        print("Removed image", imgId)
    except docker.errors.APIError:
        print("Skipping image ", imgId, "as it cannot be removed")

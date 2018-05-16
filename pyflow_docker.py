# -*- coding: UTF-8 -*-
import docker

dockerEnv = docker.from_env()
print('listing all images')
for I in dockerEnv.images.list():
    print("image ", I.attrs["RepoTags"])

print('listing all containers')
pyflowContainers = []
for I in dockerEnv.containers.list(all):
    print("Container ", I.attrs)
    print("Container ", I.attrs["Config"]["Image"])
    # if I.attrs["Config"]["Image"] == "pyflow-httpd":
    pyflowContainers.append(I.attrs["Id"])

for imgId in pyflowContainers:
    try:
        print("Trying to kill container", imgId)
        container = dockerEnv.containers.get(imgId)
        container.kill()
        print("Killed container", imgId)
        container.remove()
        print("Removed container", imgId)
    except docker.errors.APIError:
        print("Skipping image ", imgId, "as it failed to stop")
        print("Trying to remove instead ", imgId, "as it failed to stop")
        try:
            container.remove()
        except docker.errors.APIError:
            print("Failed to remove")

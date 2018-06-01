# -*- coding: UTF-8 -*-
import subprocess

print('starting docker build')
# kill all containers
# docker ps -a -q | % { docker kill $_ }
# remove all containers
# docker ps -a -q | % { docker rm $_ }
# docker build -f docker/apache/apache.Dockerfile -t pyflow-httpd .
# docker images -q | % { docker rmi $_ }
subprocess.run(["docker", "build", "-f", "apache.Dockerfile", "-t", "pyflow-httpd", "."], stdout=subprocess.PIPE,
               cwd="docker/apache/")
print('running docker images')
# docker run -p 8080:80 -dit --name pyflow-app pyflow-httpd
port = 8080
appNamePrefix = "artemis-app-"
for i in range(5):
    port = port + 1
    print("running docker httpd on port ", port)
    appName = appNamePrefix + str(port)
    pOption = str(port) + ":80"
    subprocess.run(["docker", "run", "-p", pOption, "-dit", "--name", appName, "pyflow-httpd"],
                   stdout=subprocess.PIPE)

@echo off

echo BUILD CONTAINER: udp-send
podman build -t udp-send:1.0 -f Dockerfile-udp-send

echo BUILD CONTAINER: udp-receive
podman build -t udp-receive:1.0 -f Dockerfile-udp-receive

exit /b
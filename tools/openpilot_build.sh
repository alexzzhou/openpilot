docker run --rm -v $(pwd):/tmp/openpilot -it openpilot-sim:alex bash -c 'cd /tmp/openpilot && scons -j$(nproc)'

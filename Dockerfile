FROM ubuntu:latest


# see pygame dependencies
# https://pypi.org/project/pygame/
# https://wiki.libsdl.org/SDL2/Installation


RUN apt-get update && apt-get install -y \
    python3 \
	python3-pip \
    nano \
    libsdl2-2.0-0  # Dependency of pygame

# Dependency of pygame
RUN pip install Cython --install-option="--no-cython-compile"

RUN python3 -m pip install -U pygame --user
# can be tested with `python3 -m pygame.examples.aliens`

# Set the environment variable for XQuartz display
ENV DISPLAY=:0

#

# Run the following:
# docker built -t game .
# xhost +
# docker run -it --rm -e DISPLAY=host.docker.internal:0 -v /tmp/.X11-unix:/tmp/.X11-unix game
# xhost =
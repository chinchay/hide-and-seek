# Overview

The purpose of the *hide-and-seek* program is to bring entertainment through a simple game. It integrates graphical and sound interface, event processing (keyboard and mouse), game logic, and network communication. This 2-dimensional game is inspired on the [OpenAI research work](https://openai.com/research/emergent-tool-use) where hiders and seekers compete to find new strategies and adapt to new sitations. The game begins with *sleeping* seekers, giving hiders the opportunity to rearrange digital objects in their favor. As soon as seekers wake up, they begin to look for the hiders and can create new strategies to find them. During the game, agents cannot see through objects, like blocks or walls, so each player will see black areas rendered on the screen depending on the agent's position. This software also serves as a renderer for [my next project]() on reinforcement learning.


# How it works

The *hide-and-seek* program relies on [PyGame](https://www.pygame.org/).

A demonstration of the software running and a walkthrough of the code can be found [here]().



# How to use it

Assuming Python and pip are installed on your machine, clone this repository

```console
$ git clone https://github.com/chinchay/hide-and-seek.git
```

install the requirements:

```console
$ cd hide-and-seek
$ pip install requirements.txt
```

and run the game

```console
$ python game.py
```


# Development Environment

* __Editor__: Visual Studio Code
* __Language__: Python 3.10.5
* __Version control system__: Git
* __Cloud repository__: GitHub
* __Python packages__: [PyGame](https://www.pygame.org/)


# Solving problems

After installing XQuartz, type

```console
$ xhost +local:$(whoami)
```

and do this after finishing your program

```console
$ xhost -local:$(whoami)
```

[Testing Xquartz](https://gist.github.com/sorny/969fe55d85c9b0035b0109a31cbcb088)

[More](https://gist.github.com/cschiewek/246a244ba23da8b9f0e7b11a68bf3285)


Run the container:

```console
$ docker build -t mygame .

$ docker run -it --rm -e DISPLAY=host.docker.internal:0 -v /tmp/.X11-unix:/tmp/.X11-unix mygame
```


After identifying the `*.so.1` file with:

```console
$ ldconfig -p | grep -i gl.so
```

and removed it

```console
$ rm /lib/x86_64-linux-gnu/libGL.so.1
```

Pygame worked (although now Arcade says `ImportError: Library "GL" not found.` when typing `import arcade` `arcade.open_window(600, 600, '')`)

and we can check is working by:

```console
$ python -m pygame.examples.aliens
```

solutions found at:

[1](https://askubuntu.com/questions/834254/steam-libgl-error-no-matching-fbconfigs-or-visuals-found-libgl-error-failed-t), [2](https://github.com/kivy/kivy/issues/7879), [3](https://superuser.com/questions/1470439/cant-run-glxgears-using-xquartx)






# Readings

* [Running Pygame in a Docker container (MacOS)](https://opeonikute.dev/posts/running-pygame-in-a-docker-container-macos)
* [xquartz](https://www.xquartz.org/)
* [How to show X11 windows with Docker on Mac](https://medium.com/@mreichelt/how-to-show-x11-windows-within-docker-on-mac-50759f4b65cb)
* [Running GUI applications using Docker for Mac](https://sourabhbajaj.com/blog/2017/02/07/gui-applications-docker-mac/)

For future project:
* [Machine learning is fun](https://medium.com/@ageitgey/machine-learning-is-fun-part-2-a26a10b68df3)



# Future work
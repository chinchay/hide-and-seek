# hide-and-seek
Play the hide-and-seek game!




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
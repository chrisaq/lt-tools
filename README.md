# lt-tools


## lt-range

Set range on all G25/27 wheels to 200 (for Dirt Showdown):

```
sudo lt-range.py 200
```

It is also possible to change the steam launch options for games so that you don't need to run the above command every time. Right-click the game in the steam library view and choose properties, then click 'set launch options...' and enter the following:

```
sudo python2 /usr/local/bin/lt-range .py 200; %command%
```

If you keep lt-range.py in another location, change the path above.

Using udev you can change the permissions to the logitch wheel device and drop the sudo. I will not document how to do that here, there are several good tutorials on the web.

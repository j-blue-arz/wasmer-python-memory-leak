# MWE for memory leak in wasmer-python

Uses poetry for dependency management.

Example run:
``` sh
$ python script.py
(Cmd) rss
rss: 16.01 MiB
(Cmd) run
(Cmd) rss
rss: 105.91 MiB
(Cmd) run
(Cmd) gc
(Cmd) rss
rss: 140.70 MiB
(Cmd)
```
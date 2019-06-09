# README

[Repo](https://github.com/hobnobpirate/CSC842/tree/master/Module2)

This script examines files in a given directory to determine their type (according to *libmagic*, similar to the Unix `file` command) and compares it to the file's extension. Using a whitelist, the program will determine if there is a mismatch between the file type and the extension.

The core functionality for this script relies on [python-magic](https://github.com/ahupp/python-magic) by Adam Hupp. For installation questions outside of Linux (or the provided docker container), please see the [python-magic page on GitHub](https://github.com/ahupp/python-magic).

## Requirements

This script requires Python3.6+ as well as the [python-magic](https://github.com/ahupp/python-magic) and [prettytable](https://code.google.com/archive/p/prettytable/) libraries. These can be installed using the included requirements.txt file or manually:

```bash
pip3 install -r requirements.txt
```

**OR**

```bash
pip3 install python-magic prettytable
```

## Usage

```
python file-examine.py --help
usage: file-examine.py [-h] [-ng] [-nb] [-nu] [-w WHITELIST] directory

Module 2 thing

positional arguments:
  directory             The directory where analysis will start

optional arguments:
  -h, --help            show this help message and exit
  -ng, --no-good        Do not show matches
  -nb, --no-bad         Do not show mismatches
  -nu, --no-unknown     Do not show unknown
  -w WHITELIST, --whitelist WHITELIST
                        Path to custom whitelist
```

For example:

```
$ python3 file-examine.py Samples/
Analyzed 10 files
Matched: 5
Mismatched: 2
Unknown: 3
+------------------------------------+------------------------+--------------------------+----------+
| FILE NAME                          | FILE TYPE              | MIME TYPE                | STATUS   |
+------------------------------------+------------------------+--------------------------+----------+
| Samples/file.png                   | PNG image data         | image/png                | Match    |
| Samples/file.py                    | ASCII text             | text/plain               | Match    |
| Samples/file.tar.gz                | gzip compressed data   | application/gzip         | Match    |
| Samples/file.txt                   | ASCII text             | text/plain               | Match    |
| Samples/test/secondlevel.txt       | ASCII text             | text/plain               | Match    |
| Samples/fake.tar.gz                | ASCII text             | text/plain               | Mismatch |
| Samples/this_was_a_private_key.txt | OpenSSH private key    | text/plain               | Mismatch |
| Samples/file.dat                   | data                   | application/octet-stream | Unknown  |
| Samples/not_my_real_key            | OpenSSH private key    | text/plain               | Unknown  |
| Samples/not_my_real_key.pub        | OpenSSH RSA public key | text/plain               | Unknown  |
+------------------------------------+------------------------+--------------------------+----------+
```

## Docker

Due to some [complicated installation steps](https://github.com/ahupp/python-magic#Installation) for python-magic on Windows operating systems, I have included a Docker environment as well. If you have cloned the repo and have [docker-compose installed](https://docs.docker.com/compose/install/), simply run:

```bash
docker-compose -f "docker-compose.yml" up -d --build
```

Once the container is built, you can run the container with:

```bash
docker run -it --rm file-examine python file-examine.py [-ng] [-ng] [-nb] [-w whitelist] directory
```

## Whitelist

A default whitelist is built into the script in case one is not defined on the command line. It provides a minimal number of entries in order to demonstrate usage. A sample whitelist is also included in the repository to allow the user to add their own entries. The following formatting must be followed to ensure compatibility with file-examine:

```
[
    {"t": "beginning of output from file command, cut off at first comma", "ext": ".extension"},
    {"t": "gzip compressed data", "ext": ".gz"},
    {"t": "PNG image data", "ext": ".png"},
    {"t": "Python script", "ext": ".py"},
    {"t": "ASCII text", "ext": [".txt", ".py"]},
    {"t": "JSON data", "ext": ".json"}
]
```

## Author

This is a project I completed for CSC842 at Dakota State University during the Summer 2019 semester. It is inspired by CTF-type challenges. Please feel free to contact me on GitHub.

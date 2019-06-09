=====
Usage
=====

To use Examine Files in a project::

    import examine_files

=====
Stand alone
=====

This script examines files in a given directory to determine their type 
(according to *libmagic*, similar to the Unix `file` command) and compares 
it to the file's extension. Using a whitelist, the program will determine 
if there is a mismatch between the file type and the extension. After installation::

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
    
For example::

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

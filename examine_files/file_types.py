# FORMAT
# list = [{"t": "output from file (file foo | cut -d "," -f1)", "ext": "extension (.bar)"}]

archives = [
    {"t": "gzip compressed data", "ext": ".gz"},
    {"t": "Zip archive data", "ext": [".zip", ".whl", ".egg"]},
]
executables = [
    {"t": "PE32 executable (console) Intel 80386", "ext": ".exe"}
]
images = [
    {"t": "PNG image data", "ext": ".png"},
    {"t": "GIF image data", "ext": ".gif"},
    {"t": "SVG Scalable Vector Graphics image", "ext": ".svg"},
]
misc = [
    {"t": "C++ source", "ext": ".cpp"}, 
    {"t": "data", "ext": ".dat"},
    {"t": "python", "ext": "pyc"},
    {"t": "Bourne-Again shell script", "ext": ".sh"},
    {"t": "LaTeX document", "ext": ".tex"},
    {"t": "DOS batch file", "ext": ".bat"},
]
productivity = [
    {"t": "Microsoft Excel 2007+", "ext": ".xlsx"},
    {"t": "PDF document", "ext": ".pdf"},
    {"t": "HTML document", "ext": ".html"},
    {"t": "JSON data", "ext": ".json"},
    {"t": "OpenDocument Text", "ext": ".odt"},
    {"t": "XML 1.0 document", "ext": ".xml"},
]
security = [
    {"t": "OpenSSH RSA public key", "ext": ".pub"}
]
text = [
    {"t": "Python script", "ext": [".py", ".pyi"]},
    {"t": "ASCII text", "ext": [".txt", ".py", ".md"]},
]

WHITELIST = archives + executables + images + misc + productivity + security + text

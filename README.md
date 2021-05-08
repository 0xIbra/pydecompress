[PyDecompress](https://github.com/polkovnik-z/pydecompress)
==============
Lightweight package that allows you to decompress archive files.

##### Supported formats
 - `.zip`
 - `.tar`
 - `.tar.gz`
 - `.tar.xz`
 - `.tar.bz2`
 - `.tar.xz`
 - `.tar.Z` - Requires the Linux **uncompress** package.

Installation
------------
via **pip**:
```bash
pip install pydecompress
```

Usage example
-----
```python
from pydecompress.extractor import Extractor

res = Extractor.extract('path/to/archive.tar.gz', '/destination/folder')
print(res) # Output: PosixPath('/destination/folder')
```
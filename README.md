# PyDecompress
> A Python package that allows you to extract contents from different types of archives easily.

## Usage
```python
from pydecompress.extractor import Extractor

res = Extractor.extract('path/to/archive.tar.gz', '/destination/folder')
print(res) # Output: PosixPath('/destination/folder')
```
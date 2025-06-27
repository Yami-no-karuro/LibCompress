from libcompress.bindings import compress
from libcompress.bindings import decompress

file: str = "input/source.txt"
compressed: str = "output/compressed"
decompressed: str = "output/decompressed"

compress(file, compressed)
decompress(compressed, decompressed)

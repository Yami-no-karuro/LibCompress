from libcompress.bindings import huf_compress
from libcompress.bindings import huf_decompress

file: str = "input/source.txt"
compressed: str = "output/compressed"
decompressed: str = "output/decompressed"

huf_compress(file, compressed)
huf_decompress(compressed, decompressed)

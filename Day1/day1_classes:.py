import struct

# ── Constants ────────────────────────────────────────
# Define these at the top so they're easy to change

IPP_VERSION_MAJOR = 0x01
IPP_VERSION_MINOR = 0x01
OPERATION_GET_PRINTER_ATTRIBUTES = 0x000B   # 0x000B
REQUEST_ID = 0x00000001

TAG_OPERATION_ATTRIBUTES = 0x01           # 0x01
TAG_END_OF_ATTRIBUTES = 0x03             # 0x03

TAG_CHARSET = 0x47                        # 0x47
TAG_NATURAL_LANGUAGE = 0x48              # 0x48
TAG_URI = 0x45                           # 0x45

PRINTER_URI = "ipp://localhost:631/printers/VirtualPrinter"


# ── Helper function ───────────────────────────────────
# This encodes one IPP attribute into bytes
# Every attribute follows the same pattern:
#   tag (1 byte) + name_length (2 bytes) + name + value_length (2 bytes) + value

def encode_attribute(tag, name, value):
    # 1. pack the tag as 1 byte
    packed_tag = struct.pack('!B', tag)
    # 2. pack len(name) as 2 bytes big-endian
    name_bytes = name.encode("utf-8")
    # 3. encode name as bytes
    packed_name = struct.pack('!H',len(name_bytes))
    # 4. pack len(value) as 2 bytes big-endian
    value_bytes = value.encode("utf-8")
    # 5. encode value as bytes
    packed_value = struct.pack('!H', len(value_bytes))
    # 6. return all of it joined together
    return (packed_tag + packed_name + name_bytes + packed_value + value_bytes)


# ── Build function ────────────────────────────────────
# Assembles the complete IPP message as one bytes object

def build_request():
    # 1. pack version (major, minor) → 2 bytes
    version_major = struct.pack('!B', IPP_VERSION_MAJOR)
    version_minor = struct.pack('!B', IPP_VERSION_MINOR)
    # 2. pack operation code → 2 bytes
    opcode = struct.pack('!H', OPERATION_GET_PRINTER_ATTRIBUTES)
    # 3. pack request ID → 4 bytes
    request_id = struct.pack('!I', REQUEST_ID)
    # 4. pack begin-operation-attributes tag → 1 byte
    begin_operations_attributes = struct.pack('!B', TAG_OPERATION_ATTRIBUTES)
    # 5. call encode_attribute for attributes-charset
    attr1 = encode_attribute(TAG_CHARSET, "attributes-charset", "utf-8")
    # 6. call encode_attribute for attributes-natural-language
    attr2 = encode_attribute(TAG_NATURAL_LANGUAGE, "attributes-natural-language", "en-us")
    # 7. call encode_attribute for printer-uri
    attr3 = encode_attribute(TAG_URI, "printer-uri", "https://localhost:631/ipp/print")
    # 8. pack end-of-attributes tag → 1 byte
    end_attr = struct.pack('!B', TAG_END_OF_ATTRIBUTES)
    # 9. return everything joined together
    return (version_major + version_minor + opcode + request_id + begin_operations_attributes + attr1 + attr2 + attr3 + end_attr)


# ── Main ─────────────────────────────────────────────
# Runs when you execute the file directly

if __name__ == "__main__":
    # 1. call build_request()
    result = build_request()
    # 2. write the result to "ipp_request.bin" in binary mode
    with open("ipp_request.bin", "wb") as f:
        f.write(result)
    # 3. print how many bytes were written so you can sanity check
    print(len(result))
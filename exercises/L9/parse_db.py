with open("./Students", "rb") as f:
    def get_u4() -> bytes:
        return f.read(4)
    
    def get_u2() -> bytes: 
        return f.read(2)
    
    def get_u16() -> bytes:
        return f.read(16)

    def get_u1() -> bytes:
        return f.read(1)

    def to_int(bytes: bytes) -> int:
        return int.from_bytes(bytes)


    data = {}
    data["magic"] = get_u16()
    data["page_size"] = to_int(get_u2())
    data["write_version"] = to_int(get_u1())
    data["read_version"] = to_int(get_u1())

    print(data)
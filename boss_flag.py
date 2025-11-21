from pymem import Pymem
debug = 1

boss_flags = {
    "Asylum Demon": {"base_offset": 0x01C7C5F0,"offsets": [0x20, 0x0, 0x1],"bit": 7},
    "Gargoyles": {"base_offset": 0x01C7C5F0,"offsets": [0x20, 0x0, 0x3],"bit": 4},
    "Sif": {"base_offset": 0x01C7C5F0,"offsets": [0x20, 0x0, 0x3],"bit": 2},
    "Quelaag": {"base_offset": 0x01C7C5F0,"offsets": [0x20, 0x0, 0x2],"bit": 6},
    "Iron Golem": {"base_offset": 0x01C7C5F0,"offsets": [0x20, 0x0, 0x2],"bit": 4},
    "Ornstein & Smough": {"base_offset": 0x01C7C5F0,"offsets": [0x20, 0x0, 0x2],"bit": 3},
    "Four Kings": {"base_offset": 0x01C7C5F0,"offsets": [0x20, 0x0, 0x2],"bit": 2},
    "Ceaseless Discharge": {"base_offset": 0x01C7C5F0,"offsets": [0x20, 0x0, 0x1],"bit": 3},
    "Bed of Chaos": {"base_offset": 0x01C7C5F0,"offsets": [0x20, 0x0, 0x2],"bit": 5},
    "Gravelord Nito": {"base_offset": 0x01C7C5F0,"offsets": [0x20, 0x0, 0x3],"bit": 0},
     "Seath": {"base_offset": 0x01C7C5F0,"offsets": [0x20, 0x0, 0x2],"bit": 1}
}

def get_all_boss_statuses():
    results = {}
    for boss, info in boss_flags.items():
        dead_status = is_boss_dead(info["base_offset"], info["offsets"], info["bit"])
        results[boss] = dead_status
    return results

def is_boss_dead(base_offset, offsets, bit_index):
    pm = Pymem('DarkSoulsRemastered.exe')
    module_base = pm.base_address
    base_addr = module_base + base_offset
    if debug:
        print(f"PM {pm}")
        print(f"MB {module_base}")
        print(f"BO {base_offset}")
        print(f"BA {base_addr}")
    final_address = resolve_pointer(pm, base_addr, offsets)
    byte_value = pm.read_bytes(final_address, 1)[0]
    if debug:
        print(f"[DEBUG] Byte at {hex(final_address)}: {byte_value} (bit index: {bit_index})")
        print(f"[DEBUG] Binary: {bin(byte_value)}")
    return (byte_value & (1 << bit_index)) != 0
   
def resolve_pointer(pm, base_addr, offsets):
    address = base_addr
    for offset in offsets:
        address = pm.read_int(address) + offset
    return address

if debug:
    print(get_all_boss_statuses())
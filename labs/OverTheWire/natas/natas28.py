import re
from difflib import SequenceMatcher
from itertools import combinations

text = """
If - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2133dc8b2f857cc139674e5f577a0fab848799a07b1d29b5982015c9355c2e00eaded9bdbaca6a73b71b35a010d2c4c57
Be - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf21ba087a9ae0c9f42b2b663f9c4be054548799a07b1d29b5982015c9355c2e00eaded9bdbaca6a73b71b35a010d2c4c57
Bec - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf255d2bd212ce61f7fc26e5a0d258f5e709a2e2b5db6f31f19a14f75678eadaa904249b93e4dea0909479995b9c44b351a
Abe - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf26b2d42368e0dbcb4cac25fbd0e61b84b9a2e2b5db6f31f19a14f75678eadaa904249b93e4dea0909479995b9c44b351a
OBOL - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2dc64e9b3eebf5f357b632bba4a6721ce29287f3cc5479e12e66f31c863b1804756d5732dc8c770f64397158bc17a6e66
Dudu - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2ee81daea4cf3a32f30b9f9ad812f63a329287f3cc5479e12e66f31c863b1804756d5732dc8c770f64397158bc17a6e66
" or 1=1 -- - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2f0d12560b7879c12abc3c9866b3fdfae2287d631f55813124b774a2219de3f4a75fd5044fd063d26f6bb7f734b41c899
Qqqqqqqqqqq - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2070bdd4684c4270354b8f08f7cb5480e68b151738d0187c720487ee2912fdb22ca8cf4e610913abae39a067619204a5a
Qqqqqqqqqqk - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2070bdd4684c4270354b8f08f7cb5480edfc9113cd04d1d65b06c7a624629a828ca8cf4e610913abae39a067619204a5a
" or 1=2 -- - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf23a3af555d3f9f1e46f405fda038b29cc2287d631f55813124b774a2219de3f4a75fd5044fd063d26f6bb7f734b41c899
"""

HIGHLIGHT = "\033[1;31m"
RESET = "\033[0m"

# More than 4 bytes means 5+ bytes.
MIN_PATTERN_BYTES = 5


def parse_labeled_hex_lines(text):
    """
    Parses lines like:
    label - deadbeef...
    """
    items = []

    for line_no, line in enumerate(text.strip().splitlines(), start=1):
        line = line.strip()

        if not line:
            continue

        match = re.match(r"^(.*?)\s+-\s+([0-9a-fA-F]+)\s*$", line)

        if not match:
            print(f"[!] Skipping line {line_no}: could not parse")
            continue

        label = match.group(1).strip()
        hex_string = match.group(2).strip().lower()

        if len(hex_string) % 2 != 0:
            print(f"[!] Skipping line {line_no}: hex length is odd")
            continue

        try:
            raw = bytes.fromhex(hex_string)
        except ValueError:
            print(f"[!] Skipping line {line_no}: invalid hex")
            continue

        items.append({
            "label": label,
            "hex": hex_string,
            "bytes": raw,
            "ranges": []
        })

    return items


def find_matching_byte_patterns(a, b, min_len):
    """
    Finds identical byte sequences between two byte strings.
    """
    matcher = SequenceMatcher(None, a, b, autojunk=False)
    matches = []

    for match in matcher.get_matching_blocks():
        if match.size >= min_len:
            matched_bytes = a[match.a:match.a + match.size]

            matches.append({
                "bytes": matched_bytes,
                "a_start": match.a,
                "a_end": match.a + match.size,
                "b_start": match.b,
                "b_end": match.b + match.size,
                "length": match.size
            })

    return matches


def merge_overlapping_ranges(ranges):
    if not ranges:
        return []

    ranges = sorted(ranges)
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def highlight_hex_by_byte_ranges(hex_string, byte_ranges):
    """
    Converts byte ranges to hex-character ranges and highlights them.
    byte 0 -> hex chars 0:2
    byte 1 -> hex chars 2:4
    """
    byte_ranges = merge_overlapping_ranges(byte_ranges)

    result = []
    last_hex_index = 0

    for byte_start, byte_end in byte_ranges:
        hex_start = byte_start * 2
        hex_end = byte_end * 2

        result.append(hex_string[last_hex_index:hex_start])
        result.append(HIGHLIGHT + hex_string[hex_start:hex_end] + RESET)

        last_hex_index = hex_end

    result.append(hex_string[last_hex_index:])

    return "".join(result)


items = parse_labeled_hex_lines(text)

print(f"Found {len(items)} hex values\n")

print("=" * 100)
print(f"Recurring byte patterns, length >= {MIN_PATTERN_BYTES} bytes")
print("=" * 100)

for i, j in combinations(range(len(items)), 2):
    item_a = items[i]
    item_b = items[j]

    matches = find_matching_byte_patterns(
        item_a["bytes"],
        item_b["bytes"],
        MIN_PATTERN_BYTES
    )

    if not matches:
        continue

    print(f"\nComparing: {item_a['label']}  <->  {item_b['label']}")

    for m in matches:
        matched_hex = m["bytes"].hex()

        print(
            f"  {m['length']} bytes "
            f" | {item_a['label']}[{m['a_start']}:{m['a_end']}] "
            f" <-> {item_b['label']}[{m['b_start']}:{m['b_end']}]"
        )
        print(f"    {matched_hex}")

        item_a["ranges"].append((m["a_start"], m["a_end"]))
        item_b["ranges"].append((m["b_start"], m["b_end"]))


print()
print("=" * 100)
print("Highlighted hex values")
print("=" * 100)

for item in items:
    print(f"\n{item['label']}:")
    print(highlight_hex_by_byte_ranges(item["hex"], item["ranges"]))
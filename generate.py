import hashlib, pathlib, re

zips = pathlib.Path("zips")
parts = []
for p in sorted(zips.glob("*/addon.xml")):
    text = p.read_text(encoding="utf-8")
    text = re.sub(r'^\s*<\?xml[^>]*\?>\s*', '', text)
    parts.append(text.strip())

out = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<addons>\n'
out += "\n".join(parts) + "\n</addons>\n"
data = out.encode("utf-8")

with open(zips / "addons.xml", "wb") as f:
    f.write(data)
with open(zips / "addons.xml.md5", "w", encoding="utf-8", newline="\n") as f:
    f.write(hashlib.md5(data).hexdigest())
print("addons:", len(parts))
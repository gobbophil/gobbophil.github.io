from pathlib import Path

for key in Path(".").glob("*.html"):
    print(key.stem.upper(), key.read_text("utf-8").split("main")[1])

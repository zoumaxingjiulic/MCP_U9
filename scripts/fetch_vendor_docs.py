"""Download only the three public resources observed in the vendor documentation UI."""

from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1] / ".local/vendor-docs"
PUBLIC_SOURCES = {
    "swagger-config.json": "https://openapi.yyu9c.com/v3/api-docs/swagger-config",
    "U9COPENAPI.json": "https://openapi.yyu9c.com/file/U9COPENAPI.json",
    "document.pdf": "https://openapi.yyu9c.com/file/document.pdf",
}


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    for name, url in PUBLIC_SOURCES.items():
        with urlopen(url, timeout=40) as response:
            data = response.read(10_000_001)
        if len(data) > 10_000_000:
            raise ValueError("Public document exceeds download limit")
        (ROOT / name).write_bytes(data)
        print(f"Downloaded {name}: {len(data)} bytes")


if __name__ == "__main__":
    main()

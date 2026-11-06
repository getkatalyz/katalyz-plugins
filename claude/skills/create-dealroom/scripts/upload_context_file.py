import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


def upload_file(path: Path, session: dict) -> None:
    url = session["uploadUrl"]
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("Upload URL must be HTTPS")

    headers = {item["key"]: item["value"] for item in session["uploadHeaders"]}
    headers["Content-Length"] = str(path.stat().st_size)
    with path.open("rb") as source:
        request = urllib.request.Request(url, data=source, headers=headers, method="PUT")
        with urllib.request.urlopen(request, timeout=120) as response:
            if not 200 <= response.status < 300:
                raise RuntimeError(f"Upload failed (HTTP {response.status})")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Pass exactly one local file path")
        upload_file(Path(sys.argv[1]), json.load(sys.stdin))
        print("Upload succeeded")
    except urllib.error.HTTPError as error:
        print(f"Upload failed (HTTP {error.code})", file=sys.stderr)
        sys.exit(1)
    except (OSError, ValueError, KeyError, urllib.error.URLError, RuntimeError):
        print("Upload failed; do not complete this upload session", file=sys.stderr)
        sys.exit(1)

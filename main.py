import argparse
from datetime import datetime
from pathlib import Path
import webbrowser


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Open a URL in your default browser")
    parser.add_argument("--url", default="https://example.com", help="URL to open")
    parser.add_argument(
        "--history",
        default="open_history.log",
        help="Path to log file with open history",
    )
    return parser.parse_args()


def append_history(path: str, url: str) -> None:
    timestamp = datetime.now().isoformat(timespec="seconds")
    Path(path).write_text(
        Path(path).read_text() + f"{timestamp} | {url}\n" if Path(path).exists() else f"{timestamp} | {url}\n",
        encoding="utf-8",
    )


def main() -> None:
    args = parse_args()
    webbrowser.open(args.url)
    append_history(args.history, args.url)
    print(f"Opened: {args.url}")


if __name__ == "__main__":
    main()

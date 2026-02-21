import argparse
import webbrowser


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Open a URL in your default browser")
    parser.add_argument("--url", default="https://example.com", help="URL to open")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    webbrowser.open(args.url)
    print(f"Opened: {args.url}")


if __name__ == "__main__":
    main()

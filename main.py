import webbrowser


def main() -> None:
    url = "https://example.com"
    webbrowser.open(url)
    print(f"Opened: {url}")


if __name__ == "__main__":
    main()

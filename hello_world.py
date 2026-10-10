
"""Basic Hello World script for Git practice."""


def build_message(name: str = "World") -> str:
    return f"Hello, {name}!"


def build_club_welcome(name: str) -> str:
    """Build a personalized welcome message for the club."""
    return (
        f"{build_message(name)} "
        "Welcome to the UCSB Assistive Technology Club."
    )

def greet(name: str) -> str:
    return f"Hey, {name}! Can I get your WeChat?"

def main() -> None:
    print(build_message())
    print(greet("b3tron"))


if __name__ == "__main__":
    main()




"""Basic Hello World script for Git practice."""


def build_message(name: str = "World") -> str:
    return f"Hello, {name}!"

def greet(name: str) -> str:
    return f"Hello, {name}!"

def main() -> None:
    print(build_message())
    print(greet("b3tron"))


if __name__ == "__main__":
    main()



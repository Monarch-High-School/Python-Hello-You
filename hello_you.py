"""
This program asks a user for their name and says "Hello, name!"
Jon Cihlar - September 2025
"""

# This is a single line comment

def main() -> None:
    name: str = "Jon"
    print("Hello,", name, "!")
    print("Hello, " + name + "!")
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
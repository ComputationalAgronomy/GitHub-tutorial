def main():
    name = input("Enter your name: ").strip()
    if not name:
        name = "friend"
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()

"""A slightly opinionated take on the classic 'Hello World' program."""

from datetime import datetime

GREETINGS = {
    "English": "Hello, World!",
    "Spanish": "¡Hola, Mundo!",
    "French": "Bonjour, le Monde!",
    "Japanese": "こんにちは世界!",
}


def time_of_day(hour: int) -> str:
    """Return a greeting word that matches the hour on a 24-hour clock."""
    if hour < 12:
        return "Good morning"
    if hour < 18:
        return "Good afternoon"
    return "Good evening"


def banner(text: str) -> str:
    """Wrap text in a simple box so the output is easy to spot in a terminal."""
    line = "*" * (len(text) + 4)
    return f"{line}\n* {text} *\n{line}"


def main() -> None:
    now = datetime.now()

    print(banner(GREETINGS["English"]))
    print()
    print(f"{time_of_day(now.hour)}! It is {now.strftime('%A, %B %d, %Y at %I:%M %p')}.")
    print()
    print("The same greeting in a few other languages:")

    for language, greeting in GREETINGS.items():
        print(f"  {language:<10} {greeting}")

    print()
    print("Environment is working. Time to build something.")


if __name__ == "__main__":
    main()

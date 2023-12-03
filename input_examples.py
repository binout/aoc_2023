def retrieve_intput(day: int) -> str:
    with open(f"day{day}.txt", "r") as f:
        return f.read()

import os

TEXT_PART_ONE = "Apologies for the delay: I hallucinated an email from you "
TEXT_PART_TWO = "extending the deadline, and I believed me."
TEXT = TEXT_PART_ONE + TEXT_PART_TWO


def write_output(out_dir, content):
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(content)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    write_output(out_dir, TEXT)


if __name__ == "__main__":
    main()

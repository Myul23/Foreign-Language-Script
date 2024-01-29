import os


def file_read(address: str):
    if not os.path.exists(address):
        print(address, "file doesn't exist")
        raise FileNotFoundError

    with open(address, "r") as tf:
        texts = tf.readlines()
    return texts


def transform(input_texts: str):
    output_texts, text = [], []
    for line in input_texts:
        line = line.rstrip("\n")
        if len(line) < 1:
            continue

        if ":" in line[:6]:
            output_texts.append(" ".join(text))
            text = []

            line = "`" + line + "`"
        text.append(line)
    return "## " + "\n\n<br>\n\n".join(output_texts)


def file_save(texts: str, address: str):
    if os.path.exists(address):
        print(address, "file already existed")
        raise FileExistsError

    with open(address, "w") as tf:
        tf.writelines(texts)


if __name__ == "__main__":
    base_address = "1. once/Foreign Language Script"
    script_input = base_address + "/foreign_language_script_test_input.txt"
    script_output = base_address + "/foreign_language_script_test_output.txt"
    file_save(transform(file_read(script_input)), script_output)

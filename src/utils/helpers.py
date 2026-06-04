from pathlib import Path
from datetime import datetime


def ensure_directory(path):
    """
    Create directory if it does not exist.
    """

    Path(path).mkdir(
        parents=True,
        exist_ok=True
    )


def generate_timestamp():
    """
    Generate timestamp string.
    """

    return datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


def safe_float(value):
    """
    Safely convert value to float.
    """

    try:
        return float(value)

    except Exception:

        return 0.0


def format_number(value):
    """
    Format numbers with commas.
    """

    try:

        return f"{value:,.0f}"

    except Exception:

        return str(value)


def format_decimal(value):
    """
    Format decimal values.
    """

    try:

        return f"{value:,.2f}"

    except Exception:

        return str(value)


def save_text_file(
    content,
    filepath
):
    """
    Save text file.
    """

    filepath = Path(filepath)

    filepath.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)


def read_text_file(filepath):
    """
    Read text file.
    """

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()


def get_project_root():
    """
    Return project root path.
    """

    return Path(__file__).resolve().parent.parent.parent
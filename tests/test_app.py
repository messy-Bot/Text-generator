import importlib.util
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
APP_FILE = PROJECT_ROOT / "text-generator.py"

spec = importlib.util.spec_from_file_location(
    "text_generator",
    APP_FILE
)

text_generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(text_generator)


def test_generate_styled_text():
    result = text_generator.generate_styled_text(
        "Hello World",
        "Arial"
    )

    assert result["text"] == "Hello World"
    assert result["font"] == "Arial"
    assert result["size"] == 16


def test_generate_styled_text_with_different_font():
    result = text_generator.generate_styled_text(
        "Python",
        "Courier New"
    )

    assert result["text"] == "Python"
    assert result["font"] == "Courier New"
    assert result["size"] == 16


def test_empty_text():
    result = text_generator.generate_styled_text(
        "",
        "Verdana"
    )

    assert result["text"] == ""
    assert result["font"] == "Verdana"
    assert result["size"] == 16

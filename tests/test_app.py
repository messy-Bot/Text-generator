from text_generator import generate_styled_text


def test_generate_styled_text():
    result = generate_styled_text(
        "Hello World",
        "Arial"
    )

    assert result["text"] == "Hello World"
    assert result["font"] == "Arial"
    assert result["size"] == 16


def test_generate_styled_text_with_different_font():
    result = generate_styled_text(
        "Python",
        "Courier New"
    )

    assert result["text"] == "Python"
    assert result["font"] == "Courier New"
    assert result["size"] == 16


def test_empty_text():
    result = generate_styled_text(
        "",
        "Verdana"
    )

    assert result["text"] == ""
    assert result["font"] == "Verdana"
    assert result["size"] == 16

import pytest
from validator import Validator


def test_input_and_output_must_have_the_same_type():
    val = Validator("image.png", "image.png", "blur")
    assert val.input == "image.png"

    with pytest.raises(ValueError):
        Validator("image.png", "image.jpg", "blur")

def test_input_and_output_should_have_a_valid_type():
    val = Validator("image.jpg", "image.jpg", "blur")
    assert val.action == "blur"
    val = Validator("image.png", "image.png", "grayscale")
    assert val.action == "grayscale"
    val = Validator("image.jpeg", "image.jpeg", "contour")
    assert val.action == "contour"

    with pytest.raises(ValueError):
        val = Validator("image.gif", "image.gif", "blur")

def test_validator_must_accept_only_valid_actions():
    val = Validator("image.png", "image.png", "blur")
    assert val.action == "blur"

    with pytest.raises(ValueError):
        Validator("image.png", "image.png", "invalid")

def test_validator_must_accept_only_valid_sizes():
    val = Validator("image.png", "image.png", "resize", "400x200")
    assert val.size == (400, 200)

    with pytest.raises(ValueError):
        Validator("image.png", "image.png", "resize", "400, 200")

def test_size_is_mandatory_when_action_is_resize():
    with pytest.raises(ValueError):
        Validator("image.png", "image.png", "resize")

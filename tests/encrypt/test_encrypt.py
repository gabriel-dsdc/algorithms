import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("🦋🦄🐝🦆🐝🦄", 3) == "🐝🦄🦋_🦄🐝🦆"
    assert encrypt_message("🦋🦄🐝🦆🐝🦄", 4) == "🦄🐝_🦆🐝🦄🦋"
    assert encrypt_message("🦋🦄🐝🦆🐝🦄", 9) == "🦄🐝🦆🐝🦄🦋"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("🦋🦄🐝🦆🐝🦄", "🦋🦄🐝🦆🐝🦄")  # type: ignore
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 3)  # type: ignore

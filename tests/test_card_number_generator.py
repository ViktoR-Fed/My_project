from turtledemo.penrose import start

import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize(
    "start, stop, expected_cards",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (1004000000000004, 1004000000000006, ["1004 0000 0000 0004", "1004 0000 0000 0005", "1004 0000 0000 0006"]),
        (4000000000000005, 4000000000000007, ["4000 0000 0000 0005", "4000 0000 0000 0006", "4000 0000 0000 0007"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected_cards: list) -> None:
    result = list(card_number_generator(start, stop))
    assert result == expected_cards

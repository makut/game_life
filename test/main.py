import game_process
import pytest


HEIGHT, WIDTH = 200, 100


def test_size():
    field_ex = ['.' * WIDTH] * HEIGHT
    field = game_process.Field(field_ex)
    assert field.get_height() == HEIGHT
    assert field.get_width() == WIDTH


def test_null_size():
    field_ex = []
    field = game_process.Field(field_ex)
    assert field.get_height() == 0
    assert field.get_width() == 0


def test_validness():
    field_ex = ['.' * WIDTH] * HEIGHT
    field = game_process.Field(field_ex)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            assert field.is_valid(i, j)
    for j in range(WIDTH):
        assert not field.is_valid(-1, j)
        assert not field.is_valid(HEIGHT, j)
    for i in range(HEIGHT):
        assert not field.is_valid(i, -1)
        assert not field.is_valid(i, WIDTH)


def test_neighbours():
    field_ex = ['.' * WIDTH] * HEIGHT
    field = game_process.Field(field_ex)
    assert field.get_neighbours(0, 0) == [game_process.EmptyCell] * 3
    assert field.get_neighbours(HEIGHT - 1, 0) == [game_process.EmptyCell] * 3
    assert field.get_neighbours(0, WIDTH - 1) == [game_process.EmptyCell] * 3
    assert (field.get_neighbours(HEIGHT - 1, WIDTH - 1) ==
            [game_process.EmptyCell] * 3)
    for i in range(1, HEIGHT - 1):
        assert field.get_neighbours(i, 0) == [game_process.EmptyCell] * 5
        assert (field.get_neighbours(i, WIDTH - 1) ==
                [game_process.EmptyCell] * 5)
    for j in range(1, WIDTH - 1):
        assert field.get_neighbours(0, j) == [game_process.EmptyCell] * 5
        assert (field.get_neighbours(HEIGHT - 1, j) ==
                [game_process.EmptyCell] * 5)
    for i in range(1, HEIGHT - 1):
        for j in range(1, WIDTH - 1):
            assert field.get_neighbours(i, j) == [game_process.EmptyCell] * 8


def main():
    pytest.main([__file__])


if __name__ == '__main__':
    main()

import pytest

from gameplay import astar as mod

CASES = [
    ('manhattan', [(0, 0), (3, 4)], 7, False),
    ('heap_push', [[], 5, 'a'], [[5, 'a']], False),
    ('heap_push', [[[1, 'a']], 0, 'b'], [[0, 'b'], [1, 'a']], False),
    ('heap_pop', [[[1, 'a'], [3, 'b']]], (1, 'a', [[3, 'b']]), False),
    ('heap_pop', [[]], (None, None, []), False),
    ('astar_path', [['...', '.#.', '...'], (0, 0), (2, 2)], [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], False),
    ('astar_distance', [['...', '.#.', '...'], (0, 0), (2, 0)], 2, False),
    ('astar_distance', [['...', '###', '...'], (0, 0), (0, 2)], -1, False),
    ('manhattan', [(1, 1), (1, 1)], 0, False),
    ('manhattan', [(2, 3), (0, 0)], 5, False),
    ('heap_push', [[[2, 'a']], 1, 'b'], [[1, 'b'], [2, 'a']], False),
    ('heap_pop', [[[2, 'a'], [1, 'b']]], (2, 'a', [[1, 'b']]), False),
    ('astar_path', [['..', '..'], (0, 0), (1, 1)], [(0, 0), (0, 1), (1, 1)], False),
    ('astar_path', [['#.'], (1, 0), (1, 0)], [(1, 0)], False),
    ('astar_distance', [['..'], (0, 0), (0, 1)], -1, False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_astar_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected

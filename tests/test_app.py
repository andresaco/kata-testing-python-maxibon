import pytest
import sys
from hypothesis import given
from hypothesis.strategies import text, integers, lists, tuples, builds
from app import Developer, Kitchen

@given(text(), integers(-sys.maxsize -1, -1))
def test_developer_negative_maxibon(n, m):
    # GIVEN
    # WHEN
    d = Developer(n, m)
    # THEN
    assert d.maxibon_requests() == 0

@given(text(), integers(0, sys.maxsize))
def test_developer_request(n,m):
    # GIVEN
    # WHEN
    d = Developer(n,m)
    # THEN
    assert d.maxibon_requests() == m

def test_team_needs():
    """
    Check team needs do not vary when setting the team
    """

    #GIVEN
    team = [( Developer("Pedro", 3),   3),
            ( Developer("Davide" , 0), 0),
            ( Developer("Alberto", 1),  1),
            ( Developer("Jorge", 1),   1),
            ( Developer("Jorge", 2),   2),
            ( Developer("Sergio", 1),  1)]

    #WHEN
    #THEN
    for d in team:
        assert d[0].maxibon_requests() == d[1]

@given(builds(Developer, text(), integers(0, 10)))
def test_always_min_maxibons(developer):
    # Given
    k = Kitchen()

    # When
    remaining = developer.pick_maxibon(k)

    # Then
    assert remaining > 2

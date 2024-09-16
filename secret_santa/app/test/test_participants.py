#!/usr/bin/env python3

from app.domain.participants import Participant, create_draw


def test_participant_can_be_created():
    p = Participant("john")
    assert p.name == "john"


def test_create_draw_with_two_participants():
    draw = create_draw([Participant("john"), Participant("jane")])
    assert draw.items[0].name == "john"
    assert draw.items[0].offers_to == "jane"
    assert draw.items[1].name == "jane"
    assert draw.items[1].offers_to == "john"


def test_create_random_draw():
    draw = create_draw([Participant("john"), Participant("jane"), Participant("foo")])
    assert draw.items[0].name == "john"
    assert draw.items[0].offers_to in ["jane", "foo"]
    if draw.items[1].name == "jane":
        assert draw.items[1].offers_to == "foo"
    if draw.items[1].name == "foo":
        assert draw.items[1].offers_to == "jane"
    assert draw.items[2].name in ["jane", "foo"]
    assert draw.items[2].offers_to == "john"


def test_create_draw_using_blacklist():
    l = [
        Participant("john", ["jane", "foo"]),
        Participant("jane"),
        Participant("foo"),
        Participant("bar"),
    ]
    draw = create_draw(l)
    assert draw.items[0].name == "john"
    assert draw.items[0].offers_to == "bar"


def test_sort_list_to_put_participant_with_longest_list_first():
    l = [
        Participant("jane"),
        Participant("john", ["jane", "foo"]),
        Participant("foo"),
        Participant("bar"),
    ]
    draw = create_draw(l)
    assert draw.items[0].name == "john"
    assert draw.items[0].offers_to == "bar"

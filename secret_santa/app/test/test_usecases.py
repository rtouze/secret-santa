#!/usr/bin/env python3

from app.domain.participants import UpdateParticipantBlacklist, Participant


class FakeSantaRepository:
    def __init__(self):
        self.participant = None

    def save_participant(self, participant):
        self.participant = participant

    def get_participant_list(self):
        return [
            Participant("foo"),
            Participant("bar"),
            Participant("baz"),
        ]


def test_created_participant_contains_its_blacklist():
    repo = FakeSantaRepository()
    blacklist = UpdateParticipantBlacklist(repo).execute("foo", ["bar", "baz"])
    assert repo.participant.name == "foo"
    assert repo.participant.blacklist == ["bar", "baz"]
    assert blacklist == ["bar", "baz"]


def test_created_participant_blacklist_filter_empty_items():
    repo = FakeSantaRepository()
    UpdateParticipantBlacklist(repo).execute("foo", ["bar", "   ", "baz "])
    assert repo.participant.name == "foo"
    assert repo.participant.blacklist == ["bar", "baz"]


def test_created_participant_blacklist_filter_participant_name():
    repo = FakeSantaRepository()
    UpdateParticipantBlacklist(repo).execute("foo", ["bar", "foo", "baz "])
    assert repo.participant.name == "foo"
    assert repo.participant.blacklist == ["bar", "baz"]


def test_created_participant_strip_name():
    repo = FakeSantaRepository()
    UpdateParticipantBlacklist(repo).execute("  foo ", ["bar", "foo", "baz "])
    assert repo.participant.name == "foo"


def test_blacklist_contains_only_existing_participants():
    repo = FakeSantaRepository()
    UpdateParticipantBlacklist(repo).execute("  foo ", ["bar", "foo", "baz "])
    assert repo.participant.name == "foo"

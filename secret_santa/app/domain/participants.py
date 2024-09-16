#!/usr/bin/env python3

import random


class Participant:
    def __init__(self, name, blacklist=None):
        self.name = name
        self.blacklist = blacklist or []

    def __str__(self):
        return f"Participant {self.name}, {self.blacklist}"


class Draw:
    def __init__(self, items: list, date=None):
        self.items = items
        self.date = date

    def as_dict(self):
        return {"date": self.date, "items": [i.as_dict() for i in self.items]}


class DrawItem:
    def __init__(self, name, offers_to):
        self.name = name
        self.offers_to = offers_to

    def as_dict(self):
        return {"name": self.name, "offers_to": self.offers_to}

    def __repr__(self):
        return f"DrawItem: {self.name} -> {self.offers_to}"

    def __str__(self):
        return self.__repr__()


def create_draw(participants: list):
    """This function generates a random draw using a participant list.

    The participant list is sorted to put the one with the longest blacklist at first.

    The first giver is used as the last receiver.

    """
    items = []
    recipients = set()

    sorted_participants = sorted(participants, key=lambda p: len(p.blacklist), reverse=True)

    n = 0
    g = sorted_participants[0]
    recipients = []
    while True:
        if n == len(sorted_participants) - 1:
            items.append(DrawItem(g.name, sorted_participants[0].name))
            break

        r = find_recipient(g, sorted_participants, recipients)
        items.append(DrawItem(g.name, r.name))
        recipients.append(r.name)
        g = r
        n += 1
    return Draw(items)


def find_recipient(giver, participants, recipients):
    print("giver", giver)
    print("recipients", recipients)
    candidates = [
        recipient
        for recipient in participants
        if recipient.name != giver.name
        and recipient.name not in recipients
        and recipient.name != participants[0].name
        and recipient.name not in giver.blacklist
    ]
    return random.choice(candidates)


# Use cases


class GenerateAndSaveDraw:
    def __init__(self, repository):
        self.repo = repository

    def execute(self):
        participants = self.repo.get_participant_list()
        draw = create_draw(participants)
        self.repo.save_draw(draw)


class UpdateParticipantList:
    def __init__(self, repository):
        self.repo = repository

    def execute(self, participant_list):
        plist = [Participant(p.strip()) for p in participant_list if p.strip()]
        self.repo.save_participant_list(plist)


class GetParticipantList:
    def __init__(self, repository):
        self.repo = repository

    def execute(self):
        participants = self.repo.get_participant_list()  # DbParticipant.objects.all()
        return [{"name": p.name, "blacklist": p.blacklist} for p in participants]


class GetDrawList:
    def __init__(self, repository):
        self.repo = repository

    def execute(self):
        return [d.as_dict() for d in self.repo.get_draws()]


class UpdateParticipantBlacklist:
    def __init__(self, repository):
        self.repo = repository

    def execute(self, name, blacklist):
        p_names = {p.name for p in self.repo.get_participant_list()}
        participant = Participant(
            name.strip(),
            [
                b.strip()
                for b in blacklist
                if b.strip() and b.strip() != name and b.strip() in p_names
            ],
        )
        self.repo.save_participant(participant)
        return participant.blacklist

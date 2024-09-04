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
        return {
                "date": self.date,
                "items": [ i.as_dict() for i in self.items ]
                }


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
    items = []
    recipients = set()

    n = 0
    g = participants[0]
    recipients = []
    while True:
        if n == len(participants) - 1:
            items.append(DrawItem(g.name, participants[0].name))
            break

        r = find_recipient(g, participants, recipients)
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
    def __init__(self,repository):
        self.repo = repository

    def execute(self, participant_list):
        plist = [Participant(p.strip()) for p in participant_list if p.strip()]
        self.repo.save_participant_list(plist)

class GetParticipantList:
    def __init__(self,repository):
        self.repo = repository

    def execute(self):
        participants = self.repo.get_participant_list() # DbParticipant.objects.all()
        return [ {"name": p.name } for p in participants]

class GetDrawList:
    def __init__(self, repository):
        self.repo = repository

    def execute(self):
        return [ d.as_dict() for d in self.repo.get_draws() ]

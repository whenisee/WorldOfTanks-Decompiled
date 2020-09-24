# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/notification/settings.py
LIST_SCROLL_STEP_FACTOR = 10
DEF_ICON_PATH = '../maps/icons/library/{0:>s}-1.png'

class NOTIFICATION_STATE(object):
    POPUPS = 0
    LIST = 1


class NOTIFICATION_TYPE(object):
    UNDEFINED = 0
    MESSAGE = 1
    INVITE = 2
    FRIENDSHIP_RQ = 3
    WGNC_POP_UP = 4
    CLAN_INVITES = 5
    CLAN_APPS = 6
    CLAN_APP_ACTION = 7
    CLAN_INVITE_ACTION = 8
    CLAN_INVITE = 9
    CLAN_APP = 10
    PROGRESSIVE_REWARD = 11
    MISSING_EVENTS = 12
    RANGE = (MESSAGE,
     INVITE,
     FRIENDSHIP_RQ,
     WGNC_POP_UP,
     CLAN_INVITES,
     CLAN_APPS,
     CLAN_APP_ACTION,
     CLAN_INVITE_ACTION,
     CLAN_INVITE,
     CLAN_APP,
     PROGRESSIVE_REWARD,
     MISSING_EVENTS)


ITEMS_MAX_LENGTHS = {NOTIFICATION_TYPE.MESSAGE: 250,
 NOTIFICATION_TYPE.INVITE: 100,
 NOTIFICATION_TYPE.FRIENDSHIP_RQ: 100,
 NOTIFICATION_TYPE.WGNC_POP_UP: 500,
 NOTIFICATION_TYPE.CLAN_APPS: 1,
 NOTIFICATION_TYPE.CLAN_INVITES: 1,
 NOTIFICATION_TYPE.CLAN_APP_ACTION: 500,
 NOTIFICATION_TYPE.CLAN_INVITE_ACTION: 500,
 NOTIFICATION_TYPE.CLAN_INVITE: 500,
 NOTIFICATION_TYPE.CLAN_APP: 500,
 NOTIFICATION_TYPE.PROGRESSIVE_REWARD: 1,
 NOTIFICATION_TYPE.MISSING_EVENTS: 1}

class NOTIFICATION_BUTTON_STATE(object):
    HIDDEN = 0
    VISIBLE = 1
    ENABLED = 2
    DEFAULT = VISIBLE | ENABLED


def makePathToIcon(iconName):
    result = ''
    if iconName:
        result = DEF_ICON_PATH.format(iconName)
    return result

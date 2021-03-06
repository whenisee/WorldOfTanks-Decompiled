# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/missions/bonuses/extended_item_bonus_model.py
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class ExtendedItemBonusModel(ItemBonusModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(ExtendedItemBonusModel, self).__init__(properties=properties, commands=commands)

    def getUserName(self):
        return self._getString(7)

    def setUserName(self, value):
        self._setString(7, value)

    def _initialize(self):
        super(ExtendedItemBonusModel, self)._initialize()
        self._addStringProperty('userName', '')

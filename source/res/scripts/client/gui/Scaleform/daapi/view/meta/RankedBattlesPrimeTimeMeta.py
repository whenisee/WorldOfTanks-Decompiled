# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesPrimeTimeMeta.py
from gui.Scaleform.framework.entities.View import View

class RankedBattlesPrimeTimeMeta(View):

    def closeView(self):
        self._printOverrideError('closeView')

    def apply(self):
        self._printOverrideError('apply')

    def selectServer(self, id):
        self._printOverrideError('selectServer')

    def as_setDataS(self, data):
        """
        :param data: Represented by PrimeTimeVO (AS)
        """
        return self.flashObject.as_setData(data) if self._isDAAPIInited() else None

    def as_setSelectedServerIndexS(self, index):
        return self.flashObject.as_setSelectedServerIndex(index) if self._isDAAPIInited() else None

    def as_getServersDPS(self):
        return self.flashObject.as_getServersDP() if self._isDAAPIInited() else None

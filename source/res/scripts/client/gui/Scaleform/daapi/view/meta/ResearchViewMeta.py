# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ResearchViewMeta.py
from gui.Scaleform.framework.entities.View import View

class ResearchViewMeta(View):

    def request4Unlock(self, itemCD, parentID, unlockIdx, xpCost):
        self._printOverrideError('request4Unlock')

    def request4Buy(self, itemCD):
        self._printOverrideError('request4Buy')

    def request4Info(self, itemCD, rootCD):
        self._printOverrideError('request4Info')

    def request4SelectInHangar(self, itemCD):
        self._printOverrideError('request4SelectInHangar')

    def showSystemMessage(self, typeString, message):
        self._printOverrideError('showSystemMessage')

    def as_setNodesStatesS(self, primary, data):
        return self.flashObject.as_setNodesStates(primary, data) if self._isDAAPIInited() else None

    def as_setNext2UnlockS(self, data):
        return self.flashObject.as_setNext2Unlock(data) if self._isDAAPIInited() else None

    def as_setVehicleTypeXPS(self, xps):
        return self.flashObject.as_setVehicleTypeXP(xps) if self._isDAAPIInited() else None

    def as_setInventoryItemsS(self, data):
        return self.flashObject.as_setInventoryItems(data) if self._isDAAPIInited() else None

    def as_useXMLDumpingS(self):
        return self.flashObject.as_useXMLDumping() if self._isDAAPIInited() else None
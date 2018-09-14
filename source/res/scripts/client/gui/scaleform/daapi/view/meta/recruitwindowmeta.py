# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RecruitWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class RecruitWindowMeta(AbstractWindowView):

    def updateVehicleClassDropdown(self, nation):
        self._printOverrideError('updateVehicleClassDropdown')

    def updateVehicleTypeDropdown(self, nation, vclass):
        self._printOverrideError('updateVehicleTypeDropdown')

    def updateRoleDropdown(self, nation, vclass, vtype):
        self._printOverrideError('updateRoleDropdown')

    def updateNationDropdown(self):
        self._printOverrideError('updateNationDropdown')

    def buyTankman(self, nationID, typeID, role, studyType, slot):
        self._printOverrideError('buyTankman')

    def updateAllDropdowns(self, nationID, tankType, typeID, roleType):
        self._printOverrideError('updateAllDropdowns')

    def as_setVehicleClassDropdownS(self, vehicleClassData):
        """
        :param vehicleClassData: Represented by DataProvider (AS)
        """
        return self.flashObject.as_setVehicleClassDropdown(vehicleClassData) if self._isDAAPIInited() else None

    def as_setVehicleTypeDropdownS(self, vehicleTypeData):
        """
        :param vehicleTypeData: Represented by DataProvider (AS)
        """
        return self.flashObject.as_setVehicleTypeDropdown(vehicleTypeData) if self._isDAAPIInited() else None

    def as_setRoleDropdownS(self, roleData):
        """
        :param roleData: Represented by DataProvider (AS)
        """
        return self.flashObject.as_setRoleDropdown(roleData) if self._isDAAPIInited() else None

    def as_setCreditsChangedS(self, credits):
        return self.flashObject.as_setCreditsChanged(credits) if self._isDAAPIInited() else None

    def as_setGoldChangedS(self, gold):
        return self.flashObject.as_setGoldChanged(gold) if self._isDAAPIInited() else None

    def as_initDataS(self, data):
        return self.flashObject.as_initData(data) if self._isDAAPIInited() else None

    def as_setNationsS(self, nationsData):
        """
        :param nationsData: Represented by DataProvider (AS)
        """
        return self.flashObject.as_setNations(nationsData) if self._isDAAPIInited() else None

    def as_setAllDropdownsS(self, nationsData, vehicleClassData, vehicleTypeData, roleData):
        """
        :param nationsData: Represented by DataProvider (AS)
        :param vehicleClassData: Represented by DataProvider (AS)
        :param vehicleTypeData: Represented by DataProvider (AS)
        :param roleData: Represented by DataProvider (AS)
        """
        return self.flashObject.as_setAllDropdowns(nationsData, vehicleClassData, vehicleTypeData, roleData) if self._isDAAPIInited() else None

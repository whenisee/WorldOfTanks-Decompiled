# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/battle_royale/players_panel.py
import logging
from helpers import dependency, int2roman
from gui.battle_control.arena_info import vos_collections
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from gui.battle_control.controllers.battle_field_ctrl import IBattleFieldListener
from gui.clans.formatters import getClanAbbrevString
from gui.impl import backport
from gui.impl.gen import R
from gui.Scaleform.daapi.view.meta.BattleRoyalePlayersPanelMeta import BattleRoyalePlayersPanelMeta
from items.vehicles import VehicleDescr
from nations import NAMES
from skeletons.gui.battle_session import IBattleSessionProvider

class PlayersPanel(IBattleFieldListener, IArenaVehiclesController, BattleRoyalePlayersPanelMeta):
    __slots__ = ('__vehicleIDs',)
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    _HEALTH_PERCENT = 100

    def __init__(self):
        super(PlayersPanel, self).__init__()
        self.__vehicleIDs = None
        return

    def updateVehiclesStats(self, updated, arenaDP):
        for _, vStatsVO in updated:
            if vStatsVO.vehicleID in self.__vehicleIDs:
                index = self.__vehicleIDs.index(vStatsVO.vehicleID)
                self.as_setPlayerFragsS(index, self.__getFrags(vStatsVO.frags))

    def updateVehiclesInfo(self, updated, arenaDP):
        for _, vInfoVO in updated:
            if vInfoVO.vehicleID in self.__vehicleIDs:
                index = self.__vehicleIDs.index(vInfoVO.vehicleID)
                self.as_setVehicleLevelS(index, int2roman(self._getVehicleLevel(vInfoVO)))

    def invalidateVehicleStatus(self, flags, vInfoVO, arenaDP):
        if vInfoVO.vehicleID in self.__vehicleIDs:
            index = self.__vehicleIDs.index(vInfoVO.vehicleID)
            if not vInfoVO.isAlive():
                self.as_setPlayerHPS(index, 0)
            self.as_setPlayerStatusS(index, vInfoVO.isAlive(), vInfoVO.isReady())

    def updateVehicleHealth(self, vehicleID, newHealth, maxHealth):
        if vehicleID in self.__vehicleIDs:
            index = self.__vehicleIDs.index(vehicleID)
            self.as_setPlayerHPS(index, self._HEALTH_PERCENT * newHealth / maxHealth)

    def _populate(self):
        super(PlayersPanel, self)._populate()
        self.__initSquadPlayers()
        if self.__vehicleIDs:
            self.__initSquadState()
            self.sessionProvider.addArenaCtrl(self)

    def _dispose(self):
        if self.__vehicleIDs:
            self.sessionProvider.removeArenaCtrl(self)
        self.__vehicleIDs = None
        super(PlayersPanel, self)._dispose()
        return

    def _getVehicleLevel(self, vInfoVO):
        descriptor = VehicleDescr(compactDescr=vInfoVO.vehicleType.strCompactDescr)
        return max(descriptor.chassis.level, descriptor.turret.level, descriptor.gun.level, descriptor.radio.level, descriptor.engine.level)

    def __initSquadPlayers(self):
        self.__vehicleIDs = []
        arenaDP = self.sessionProvider.getArenaDP()
        collection = vos_collections.AllyItemsCollection().ids(arenaDP)
        names = []
        clans = []
        for vId in collection:
            vInfoVO = arenaDP.getVehicleInfo(vId)
            if not vInfoVO.isObserver() and arenaDP.isSquadMan(vId) and arenaDP.getPlayerVehicleID() != vId:
                self.__vehicleIDs.append(vId)
                names.append(vInfoVO.player.name)
                clanAbbrev = getClanAbbrevString(vInfoVO.player.clanAbbrev) if vInfoVO.player.clanAbbrev else None
                clans.append(clanAbbrev)

        if self.__vehicleIDs:
            self.as_setInitDataS(backport.text(R.strings.battle_royale.playersPanel.title()), names, clans)
        return

    def __initSquadState(self):
        logger = logging.getLogger(__name__)
        arenaDP = self.sessionProvider.getArenaDP()
        for index, vId in enumerate(self.__vehicleIDs):
            vInfoVO = arenaDP.getVehicleInfo(vId)
            vStatsVO = arenaDP.getVehicleStats(vId)
            level = self._getVehicleLevel(vInfoVO)
            nation = NAMES[vInfoVO.vehicleType.nationID]
            nationEmblems = R.images.gui.maps.icons.battleRoyale.emblems
            nationEmblemImage = None
            if hasattr(nationEmblems, nation):
                nationEmblem = getattr(nationEmblems, nation)
                nationEmblemImage = backport.image(nationEmblem())
            else:
                logger.warning('Could not find emblem for nation')
            self.as_setPlayerStateS(index, vInfoVO.isAlive(), vInfoVO.isReady(), self._HEALTH_PERCENT, self.__getFrags(vStatsVO.frags), int2roman(level), nationEmblemImage)
            if not vInfoVO.isAlive():
                self.as_setPlayerHPS(index, 0)

        return

    @staticmethod
    def __getFrags(frags):
        return frags if frags != 0 else ''

# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/web/web_client_api/sound/__init__.py
import SoundGroups
import WWISE
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from web.web_client_api import w2c, w2capi, W2CSchema, Field

class _SoundSchema(W2CSchema):
    sound_id = Field(required=True, type=basestring)


class _SoundStateSchema(W2CSchema):
    state_name = Field(required=True, type=basestring)
    state_value = Field(required=True, type=basestring)


class _HangarSoundSchema(W2CSchema):
    mute = Field(required=True, type=bool)


@w2capi()
class SoundWebApi(object):
    _ENTER_EXIT_SOUND_MAPPING = {'eb_ambient_progress_page_enter': 'eb_ambient_progress_page_exit'}

    def __init__(self):
        super(SoundWebApi, self).__init__()
        self.__exitSounds = set()

    @w2c(_SoundSchema, 'sound', finiHandlerName='_soundFini')
    def sound(self, cmd):
        appLoader = dependency.instance(IAppLoader)
        app = appLoader.getApp()
        if app and app.soundManager:
            app.soundManager.playEffectSound(cmd.sound_id)
            exitSound = self._ENTER_EXIT_SOUND_MAPPING.get(cmd.sound_id)
            if exitSound:
                self.__exitSounds.add(exitSound)

    def _soundFini(self):
        for exitSound in self.__exitSounds:
            WWISE.WW_eventGlobal(exitSound)

        self.__exitSounds.clear()


@w2capi()
class SoundStateWebApi(object):
    __ON_EXIT_STATES = {'STATE_overlay_hangar_general': 'STATE_overlay_hangar_general_off',
     'STATE_video_overlay': 'STATE_video_overlay_off',
     'STATE_clans_craft': 'STATE_clans_craft_progress_off',
     'STATE_gamemode_progress_page': 'STATE_gamemode_progress_page_off'}

    @w2c(_SoundStateSchema, 'sound_state', finiHandlerName='_soundStateFini')
    def setSoundState(self, cmd):
        WWISE.WW_setState(str(cmd.state_name), str(cmd.state_value))

    def _soundStateFini(self):
        for stateName, stateValue in self.__ON_EXIT_STATES.iteritems():
            WWISE.WW_setState(stateName, stateValue)


@w2capi()
class HangarSoundWebApi(object):

    @w2c(_HangarSoundSchema, 'hangar_sound', finiHandlerName='_hangarSoundFini')
    def hangarSound(self, cmd):
        if cmd.mute:
            SoundGroups.g_instance.playSound2D('ue_master_mute')
        else:
            SoundGroups.g_instance.playSound2D('ue_master_unmute')

    def _hangarSoundFini(self):
        SoundGroups.g_instance.playSound2D('ue_master_unmute')

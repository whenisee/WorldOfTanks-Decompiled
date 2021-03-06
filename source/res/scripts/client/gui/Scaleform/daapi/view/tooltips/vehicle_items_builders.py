# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/vehicle_items_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts, TOOLTIP_COMPONENT
from gui.shared.tooltips import module
from gui.shared.tooltips import shell, advanced
from gui.shared.tooltips.builders import DataBuilder, AdvancedDataBuilder, AdvancedComplexBuilder
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS
from items import vehicles
__all__ = ('getTooltipBuilders',)

def _advancedBlockCondition(context):

    def advancedTooltipExist(*args):
        item = context.buildItem(*args)
        return item.getGUIEmblemID() in advanced.MODULE_MOVIES

    return advancedTooltipExist


def _allowEventConsumableAdvancedTooltip(compactDesc, *args):
    intCD = int(compactDesc)
    descriptor = vehicles.getItemByCompactDescr(intCD)
    return VEHICLE_TAGS.EVENT not in descriptor.tags


class InventoryModuleBuilder(AdvancedDataBuilder):
    __slots__ = ()

    def __init__(self, tooltipType, linkage):
        super(InventoryModuleBuilder, self).__init__(tooltipType, linkage, module.ModuleBlockTooltipData(contexts.InventoryContext()), advanced.HangarModuleAdvanced(contexts.InventoryContext()), condition=_advancedBlockCondition(contexts.InventoryContext()))

    def _buildData(self, _advanced, intCD, *args, **kwargs):
        return super(InventoryModuleBuilder, self)._buildData(_advanced, intCD)


class ShopModuleBuilder(AdvancedDataBuilder):
    __slots__ = ()

    def __init__(self, tooltipType, linkage):
        super(ShopModuleBuilder, self).__init__(tooltipType, linkage, module.ModuleBlockTooltipData(contexts.DefaultContext()), advanced.HangarModuleAdvanced(contexts.DefaultContext()), condition=_advancedBlockCondition(contexts.DefaultContext()))

    def _buildData(self, _advanced, intCD, *args, **kwargs):
        return super(ShopModuleBuilder, self)._buildData(_advanced, intCD)


class TechTreeModuleBuilder(AdvancedDataBuilder):
    __slots__ = ()

    def __init__(self, tooltipType, linkage):
        super(TechTreeModuleBuilder, self).__init__(tooltipType, linkage, module.ModuleBlockTooltipData(contexts.ModuleContext()), advanced.HangarModuleAdvanced(contexts.ModuleContext()))

    def _buildData(self, _advanced, node, parentCD, *args, **kwargs):
        return super(TechTreeModuleBuilder, self)._buildData(_advanced, node, parentCD)


class ModuleDataBuilder(AdvancedDataBuilder):
    __slots__ = ()

    def __init__(self, tooltipType, linkage, condition=None):
        super(ModuleDataBuilder, self).__init__(tooltipType, linkage, module.ModuleBlockTooltipData(contexts.TechMainContext()), advanced.HangarModuleAdvanced(contexts.TechMainContext()), condition=_advancedBlockCondition(contexts.TechMainContext()))

    def _buildData(self, _advanced, intCD, buyPrice=None, inventoryCount=0, vehicleCount=0, slotIdx=0, eqs=None, *args):
        return super(ModuleDataBuilder, self)._buildData(_advanced, intCD, slotIdx, eqs)


class ShellBuilder(DataBuilder):
    __slots__ = ()

    def _buildData(self, _advanced, intCD, *args, **kwargs):
        return super(ShellBuilder, self)._buildData(_advanced, intCD)


class AdvancedShellBuilder(AdvancedDataBuilder):
    __slots__ = ()

    def _buildData(self, _advanced, intCD, *args, **kwargs):
        return super(AdvancedShellBuilder, self)._buildData(_advanced, intCD)


def getTooltipBuilders():
    return (InventoryModuleBuilder(TOOLTIPS_CONSTANTS.INVENTORY_MODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI),
     ShopModuleBuilder(TOOLTIPS_CONSTANTS.DEFAULT_MODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI),
     TechTreeModuleBuilder(TOOLTIPS_CONSTANTS.TECHTREE_MODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI),
     ModuleDataBuilder(TOOLTIPS_CONSTANTS.TECH_MAIN_MODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, _allowEventConsumableAdvancedTooltip),
     AdvancedDataBuilder(TOOLTIPS_CONSTANTS.HANGAR_MODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, module.ModuleBlockTooltipData(contexts.HangarContext()), advanced.HangarModuleAdvanced(contexts.HangarContext()), condition=_advancedBlockCondition(contexts.HangarContext())),
     AdvancedDataBuilder(TOOLTIPS_CONSTANTS.HANGAR_CARD_MODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, module.ModuleBlockTooltipData(contexts.HangarCardContext()), advanced.HangarModuleAdvanced(contexts.HangarCardContext()), condition=_advancedBlockCondition(contexts.HangarCardContext())),
     AdvancedDataBuilder(TOOLTIPS_CONSTANTS.HANGAR_SLOT_MODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, module.ModuleBlockTooltipData(contexts.HangarSlotContext()), advanced.HangarModuleAdvanced(contexts.HangarSlotContext()), condition=_advancedBlockCondition(contexts.HangarSlotContext())),
     AdvancedComplexBuilder(TOOLTIPS_CONSTANTS.OPT_DEVICE_EMPTY_SLOT, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, module.OptDeviceEmptyBlockTooltipData(contexts.EmptyOptDeviceSlotContext(TOOLTIP_COMPONENT.HANGAR))),
     AdvancedComplexBuilder(TOOLTIPS_CONSTANTS.AMMUNITION_EMPTY_SLOT, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, module.AmmunitionEmptyBlockTooltipData(contexts.ToolTipContext(TOOLTIP_COMPONENT.HANGAR))),
     AdvancedDataBuilder(TOOLTIPS_CONSTANTS.NATION_CHANGE_HANGAR_MODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, module.ModuleBlockTooltipData(contexts.NationChangeHangarContext()), advanced.HangarModuleAdvanced(contexts.NationChangeHangarContext()), condition=_advancedBlockCondition(contexts.NationChangeHangarContext())),
     AdvancedDataBuilder(TOOLTIPS_CONSTANTS.COMPARE_MODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, module.ModuleBlockTooltipData(contexts.VehCmpConfigurationContext()), advanced.HangarModuleAdvanced(contexts.VehCmpConfigurationContext()), condition=_advancedBlockCondition(contexts.VehCmpConfigurationContext())),
     AdvancedDataBuilder(TOOLTIPS_CONSTANTS.COMPARE_SLOT_MODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, module.ModuleBlockTooltipData(contexts.VehCmpConfigurationSlotContext()), advanced.HangarModuleAdvanced(contexts.VehCmpConfigurationSlotContext()), condition=_advancedBlockCondition(contexts.VehCmpConfigurationSlotContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.VEH_COMPARE_TECHTREE_MODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, module.ModuleBlockTooltipData(contexts.VehCmpModulesContext())),
     AdvancedDataBuilder(TOOLTIPS_CONSTANTS.PREVIEW_MODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, module.ModuleBlockTooltipData(contexts.PreviewContext()), advanced.HangarModuleAdvanced(contexts.PreviewContext()), condition=_advancedBlockCondition(contexts.PreviewContext())),
     AdvancedDataBuilder(TOOLTIPS_CONSTANTS.AWARD_MODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, module.ModuleBlockTooltipData(contexts.AwardContext()), advanced.HangarModuleAdvanced(contexts.AwardContext()), condition=_advancedBlockCondition(contexts.AwardContext())),
     AdvancedDataBuilder(TOOLTIPS_CONSTANTS.SHOP_MODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, module.ModuleBlockTooltipData(contexts.ShopContext()), advanced.HangarModuleAdvanced(contexts.ShopContext()), condition=_advancedBlockCondition(contexts.ShopContext())),
     ShellBuilder(TOOLTIPS_CONSTANTS.SHOP_SHELL, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, shell.ShellBlockToolTipData(contexts.ShopContext())),
     AdvancedShellBuilder(TOOLTIPS_CONSTANTS.DEFAULT_SHELL, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, shell.ShellBlockToolTipData(contexts.DefaultContext()), advanced.HangarShellAdvanced(contexts.DefaultContext())),
     ShellBuilder(TOOLTIPS_CONSTANTS.AWARD_SHELL, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, shell.ShellBlockToolTipData(contexts.AwardContext())),
     AdvancedDataBuilder(TOOLTIPS_CONSTANTS.HANGAR_SHELL, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, shell.ShellBlockToolTipData(contexts.HangarContext()), advanced.HangarShellAdvanced(contexts.HangarContext())),
     AdvancedDataBuilder(TOOLTIPS_CONSTANTS.NATION_CHANGE_HANGAR_SHELL, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, shell.ShellBlockToolTipData(contexts.NationChangeHangarContext()), advanced.HangarShellAdvanced(contexts.NationChangeHangarContext())),
     AdvancedShellBuilder(TOOLTIPS_CONSTANTS.COMPARE_SHELL, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, shell.ShellBlockToolTipData(contexts.VehCmpConfigurationContext()), advanced.HangarShellAdvanced(contexts.VehCmpConfigurationContext())),
     AdvancedShellBuilder(TOOLTIPS_CONSTANTS.INVENTORY_SHELL, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, shell.ShellBlockToolTipData(contexts.InventoryContext()), advanced.HangarShellAdvanced(contexts.TechMainContext())),
     AdvancedShellBuilder(TOOLTIPS_CONSTANTS.TECH_MAIN_SHELL, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, shell.ShellBlockToolTipData(contexts.TechMainContext()), advanced.HangarShellAdvanced(contexts.TechMainContext())))

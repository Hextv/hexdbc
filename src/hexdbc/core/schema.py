from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, List, Optional


class FieldType(Enum):
    UINT = auto()
    INT = auto()
    FLOAT = auto()
    STRING = auto()
    LOCSTRING = auto()
    FLAGS = auto()
    ENUM = auto()


@dataclass
class FieldDef:
    name: str
    type: FieldType = FieldType.UINT
    description: str = ""
    enum_name: Optional[str] = None


@dataclass
class SchemaDef:
    name: str
    fields: List[FieldDef] = field(default_factory=list)
    enums: Dict[str, Dict[int, str]] = field(default_factory=dict)

    def get_field(self, index: int) -> Optional[FieldDef]:
        if 0 <= index < len(self.fields):
            return self.fields[index]
        return None


# Built-in schemas for WoW 3.3.5a DBCs
BUILTIN_SCHEMAS: Dict[str, SchemaDef] = {}


# Achievement - 62 fields
BUILTIN_SCHEMAS["Achievement"] = SchemaDef(
    name="Achievement",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Faction", FieldType.INT),
        FieldDef("Instance_Id", FieldType.INT),
        FieldDef("Supercedes", FieldType.INT),
        FieldDef("Title_Lang_enUS", FieldType.STRING),
        FieldDef("Title_Lang_koKR", FieldType.STRING),
        FieldDef("Title_Lang_frFR", FieldType.STRING),
        FieldDef("Title_Lang_deDE", FieldType.STRING),
        FieldDef("Title_Lang_enCN", FieldType.STRING),
        FieldDef("Title_Lang_enTW", FieldType.STRING),
        FieldDef("Title_Lang_esES", FieldType.STRING),
        FieldDef("Title_Lang_esMX", FieldType.STRING),
        FieldDef("Title_Lang_ruRU", FieldType.STRING),
        FieldDef("Title_Lang_jaJP", FieldType.STRING),
        FieldDef("Title_Lang_ptPT", FieldType.STRING),
        FieldDef("Title_Lang_itIT", FieldType.STRING),
        FieldDef("Title_Lang_Unk12", FieldType.STRING),
        FieldDef("Title_Lang_Unk13", FieldType.STRING),
        FieldDef("Title_Lang_Unk14", FieldType.STRING),
        FieldDef("Title_Lang_Unk15", FieldType.STRING),
        FieldDef("Title_Lang_Flags", FieldType.UINT),
        FieldDef("Description_Lang_enUS", FieldType.STRING),
        FieldDef("Description_Lang_koKR", FieldType.STRING),
        FieldDef("Description_Lang_frFR", FieldType.STRING),
        FieldDef("Description_Lang_deDE", FieldType.STRING),
        FieldDef("Description_Lang_enCN", FieldType.STRING),
        FieldDef("Description_Lang_enTW", FieldType.STRING),
        FieldDef("Description_Lang_esES", FieldType.STRING),
        FieldDef("Description_Lang_esMX", FieldType.STRING),
        FieldDef("Description_Lang_ruRU", FieldType.STRING),
        FieldDef("Description_Lang_jaJP", FieldType.STRING),
        FieldDef("Description_Lang_ptPT", FieldType.STRING),
        FieldDef("Description_Lang_itIT", FieldType.STRING),
        FieldDef("Description_Lang_Unk12", FieldType.STRING),
        FieldDef("Description_Lang_Unk13", FieldType.STRING),
        FieldDef("Description_Lang_Unk14", FieldType.STRING),
        FieldDef("Description_Lang_Unk15", FieldType.STRING),
        FieldDef("Description_Lang_Flags", FieldType.UINT),
        FieldDef("Category", FieldType.INT),
        FieldDef("Points", FieldType.INT),
        FieldDef("Ui_Order", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("IconID", FieldType.INT),
        FieldDef("Reward_Lang_enUS", FieldType.STRING),
        FieldDef("Reward_Lang_koKR", FieldType.STRING),
        FieldDef("Reward_Lang_frFR", FieldType.STRING),
        FieldDef("Reward_Lang_deDE", FieldType.STRING),
        FieldDef("Reward_Lang_enCN", FieldType.STRING),
        FieldDef("Reward_Lang_enTW", FieldType.STRING),
        FieldDef("Reward_Lang_esES", FieldType.STRING),
        FieldDef("Reward_Lang_esMX", FieldType.STRING),
        FieldDef("Reward_Lang_ruRU", FieldType.STRING),
        FieldDef("Reward_Lang_jaJP", FieldType.STRING),
        FieldDef("Reward_Lang_ptPT", FieldType.STRING),
        FieldDef("Reward_Lang_itIT", FieldType.STRING),
        FieldDef("Reward_Lang_Unk12", FieldType.STRING),
        FieldDef("Reward_Lang_Unk13", FieldType.STRING),
        FieldDef("Reward_Lang_Unk14", FieldType.STRING),
        FieldDef("Reward_Lang_Unk15", FieldType.STRING),
        FieldDef("Reward_Lang_Flags", FieldType.UINT),
        FieldDef("Minimum_Criteria", FieldType.INT),
        FieldDef("Shares_Criteria", FieldType.INT),
    ]
)

# Achievement_Category - 20 fields
BUILTIN_SCHEMAS["Achievement_Category"] = SchemaDef(
    name="Achievement_Category",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Parent", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("Ui_Order", FieldType.INT),
    ]
)

# Achievement_Criteria - 31 fields
BUILTIN_SCHEMAS["Achievement_Criteria"] = SchemaDef(
    name="Achievement_Criteria",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Achievement_Id", FieldType.INT),
        FieldDef("Type", FieldType.INT),
        FieldDef("Asset_Id", FieldType.INT),
        FieldDef("Quantity", FieldType.INT),
        FieldDef("Start_Event", FieldType.INT),
        FieldDef("Start_Asset", FieldType.INT),
        FieldDef("Fail_Event", FieldType.INT),
        FieldDef("Fail_Asset", FieldType.INT),
        FieldDef("Description_Lang_enUS", FieldType.STRING),
        FieldDef("Description_Lang_koKR", FieldType.STRING),
        FieldDef("Description_Lang_frFR", FieldType.STRING),
        FieldDef("Description_Lang_deDE", FieldType.STRING),
        FieldDef("Description_Lang_enCN", FieldType.STRING),
        FieldDef("Description_Lang_enTW", FieldType.STRING),
        FieldDef("Description_Lang_esES", FieldType.STRING),
        FieldDef("Description_Lang_esMX", FieldType.STRING),
        FieldDef("Description_Lang_ruRU", FieldType.STRING),
        FieldDef("Description_Lang_jaJP", FieldType.STRING),
        FieldDef("Description_Lang_ptPT", FieldType.STRING),
        FieldDef("Description_Lang_itIT", FieldType.STRING),
        FieldDef("Description_Lang_Unk12", FieldType.STRING),
        FieldDef("Description_Lang_Unk13", FieldType.STRING),
        FieldDef("Description_Lang_Unk14", FieldType.STRING),
        FieldDef("Description_Lang_Unk15", FieldType.STRING),
        FieldDef("Description_Lang_Flags", FieldType.UINT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("Timer_Start_Event", FieldType.INT),
        FieldDef("Timer_Asset_Id", FieldType.INT),
        FieldDef("Timer_Time", FieldType.INT),
        FieldDef("Ui_Order", FieldType.INT),
    ]
)

# AnimKit - 3 fields
BUILTIN_SCHEMAS["AnimKit"] = SchemaDef(
    name="AnimKit",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("OneShotDuration", FieldType.INT),
        FieldDef("OneShotStopAnimKitID", FieldType.INT),
    ]
)

# AnimKitBoneSet - 6 fields
BUILTIN_SCHEMAS["AnimKitBoneSet"] = SchemaDef(
    name="AnimKitBoneSet",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("BoneDataID", FieldType.INT),
        FieldDef("ParentAnimKitBoneSetID", FieldType.INT),
        FieldDef("ExtraBoneCount", FieldType.INT),
        FieldDef("AltAnimKitBoneSetID", FieldType.INT),
    ]
)

# AnimKitBoneSetAlias - 3 fields
BUILTIN_SCHEMAS["AnimKitBoneSetAlias"] = SchemaDef(
    name="AnimKitBoneSetAlias",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("BoneDataID", FieldType.INT),
        FieldDef("AnimKitBoneSetID", FieldType.INT),
    ]
)

# AnimKitConfig - 2 fields
BUILTIN_SCHEMAS["AnimKitConfig"] = SchemaDef(
    name="AnimKitConfig",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ConfigFlags", FieldType.INT),
    ]
)

# AnimKitConfigBoneSet - 4 fields
BUILTIN_SCHEMAS["AnimKitConfigBoneSet"] = SchemaDef(
    name="AnimKitConfigBoneSet",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ParentAnimKitConfigID", FieldType.INT),
        FieldDef("AnimKitBoneSetID", FieldType.INT),
        FieldDef("AnimKitPriorityID", FieldType.INT),
    ]
)

# AnimKitPriority - 2 fields
BUILTIN_SCHEMAS["AnimKitPriority"] = SchemaDef(
    name="AnimKitPriority",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Priority", FieldType.INT),
    ]
)

# AnimKitSegment - 16 fields
BUILTIN_SCHEMAS["AnimKitSegment"] = SchemaDef(
    name="AnimKitSegment",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ParentAnimKitID", FieldType.INT),
        FieldDef("AnimID", FieldType.INT),
        FieldDef("AnimStartTime", FieldType.INT),
        FieldDef("AnimKitConfigID", FieldType.INT),
        FieldDef("StartCondition", FieldType.INT),
        FieldDef("StartConditionParam", FieldType.INT),
        FieldDef("StartConditionDelay", FieldType.INT),
        FieldDef("EndCondition", FieldType.INT),
        FieldDef("EndConditionParam", FieldType.INT),
        FieldDef("EndConditionDelay", FieldType.INT),
        FieldDef("Speed", FieldType.FLOAT),
        FieldDef("SegmentFlags", FieldType.INT),
        FieldDef("ForcedVariation", FieldType.INT),
        FieldDef("OverrideConfigFlags", FieldType.INT),
        FieldDef("LoopToSegmentIndex", FieldType.INT),
    ]
)

# AnimReplacement - 4 fields
BUILTIN_SCHEMAS["AnimReplacement"] = SchemaDef(
    name="AnimReplacement",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SrcAnimID", FieldType.INT),
        FieldDef("DstAnimID", FieldType.INT),
        FieldDef("ParentAnimReplacementSetID", FieldType.INT),
    ]
)

# AnimReplacementSet - 2 fields
BUILTIN_SCHEMAS["AnimReplacementSet"] = SchemaDef(
    name="AnimReplacementSet",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ExecOrder", FieldType.INT),
    ]
)

# AnimationData - 8 fields
BUILTIN_SCHEMAS["AnimationData"] = SchemaDef(
    name="AnimationData",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("Weaponflags", FieldType.INT),
        FieldDef("Bodyflags", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("Fallback", FieldType.INT),
        FieldDef("BehaviorID", FieldType.INT),
        FieldDef("BehaviorTier", FieldType.INT),
    ]
)

# AreaAssignment - 5 fields
BUILTIN_SCHEMAS["AreaAssignment"] = SchemaDef(
    name="AreaAssignment",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MapID", FieldType.INT),
        FieldDef("AreaID", FieldType.INT),
        FieldDef("ChunkX", FieldType.INT),
        FieldDef("ChunkY", FieldType.INT),
    ]
)

# AreaGroup - 8 fields
BUILTIN_SCHEMAS["AreaGroup"] = SchemaDef(
    name="AreaGroup",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("AreaID_0", FieldType.INT),
        FieldDef("AreaID_1", FieldType.INT),
        FieldDef("AreaID_2", FieldType.INT),
        FieldDef("AreaID_3", FieldType.INT),
        FieldDef("AreaID_4", FieldType.INT),
        FieldDef("AreaID_5", FieldType.INT),
        FieldDef("NextAreaID", FieldType.INT),
    ]
)

# AreaPOI - 54 fields
BUILTIN_SCHEMAS["AreaPOI"] = SchemaDef(
    name="AreaPOI",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Importance", FieldType.INT),
        FieldDef("Icon_0", FieldType.INT),
        FieldDef("Icon_1", FieldType.INT),
        FieldDef("Icon_2", FieldType.INT),
        FieldDef("Icon_3", FieldType.INT),
        FieldDef("Icon_4", FieldType.INT),
        FieldDef("Icon_5", FieldType.INT),
        FieldDef("Icon_6", FieldType.INT),
        FieldDef("Icon_7", FieldType.INT),
        FieldDef("Icon_8", FieldType.INT),
        FieldDef("FactionID", FieldType.INT),
        FieldDef("X", FieldType.FLOAT),
        FieldDef("Y", FieldType.FLOAT),
        FieldDef("Z", FieldType.FLOAT),
        FieldDef("ContinentID", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("AreaID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("Description_Lang_enUS", FieldType.STRING),
        FieldDef("Description_Lang_koKR", FieldType.STRING),
        FieldDef("Description_Lang_frFR", FieldType.STRING),
        FieldDef("Description_Lang_deDE", FieldType.STRING),
        FieldDef("Description_Lang_enCN", FieldType.STRING),
        FieldDef("Description_Lang_enTW", FieldType.STRING),
        FieldDef("Description_Lang_esES", FieldType.STRING),
        FieldDef("Description_Lang_esMX", FieldType.STRING),
        FieldDef("Description_Lang_ruRU", FieldType.STRING),
        FieldDef("Description_Lang_jaJP", FieldType.STRING),
        FieldDef("Description_Lang_ptPT", FieldType.STRING),
        FieldDef("Description_Lang_itIT", FieldType.STRING),
        FieldDef("Description_Lang_Unk12", FieldType.STRING),
        FieldDef("Description_Lang_Unk13", FieldType.STRING),
        FieldDef("Description_Lang_Unk14", FieldType.STRING),
        FieldDef("Description_Lang_Unk15", FieldType.STRING),
        FieldDef("Description_Lang_Flags", FieldType.UINT),
        FieldDef("WorldStateID", FieldType.INT),
        FieldDef("WorldMapLink", FieldType.INT),
    ]
)

# AreaTable - 36 fields
BUILTIN_SCHEMAS["AreaTable"] = SchemaDef(
    name="AreaTable",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ContinentID", FieldType.INT),
        FieldDef("ParentAreaID", FieldType.INT),
        FieldDef("AreaBit", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("SoundProviderPref", FieldType.INT),
        FieldDef("SoundProviderPrefUnderwater", FieldType.INT),
        FieldDef("AmbienceID", FieldType.INT),
        FieldDef("ZoneMusic", FieldType.INT),
        FieldDef("IntroSound", FieldType.INT),
        FieldDef("ExplorationLevel", FieldType.INT),
        FieldDef("AreaName_Lang_enUS", FieldType.STRING),
        FieldDef("AreaName_Lang_koKR", FieldType.STRING),
        FieldDef("AreaName_Lang_frFR", FieldType.STRING),
        FieldDef("AreaName_Lang_deDE", FieldType.STRING),
        FieldDef("AreaName_Lang_enCN", FieldType.STRING),
        FieldDef("AreaName_Lang_enTW", FieldType.STRING),
        FieldDef("AreaName_Lang_esES", FieldType.STRING),
        FieldDef("AreaName_Lang_esMX", FieldType.STRING),
        FieldDef("AreaName_Lang_ruRU", FieldType.STRING),
        FieldDef("AreaName_Lang_jaJP", FieldType.STRING),
        FieldDef("AreaName_Lang_ptPT", FieldType.STRING),
        FieldDef("AreaName_Lang_itIT", FieldType.STRING),
        FieldDef("AreaName_Lang_Unk12", FieldType.STRING),
        FieldDef("AreaName_Lang_Unk13", FieldType.STRING),
        FieldDef("AreaName_Lang_Unk14", FieldType.STRING),
        FieldDef("AreaName_Lang_Unk15", FieldType.STRING),
        FieldDef("AreaName_Lang_Flags", FieldType.UINT),
        FieldDef("FactionGroupMask", FieldType.INT),
        FieldDef("LiquidTypeID_0", FieldType.INT),
        FieldDef("LiquidTypeID_1", FieldType.INT),
        FieldDef("LiquidTypeID_2", FieldType.INT),
        FieldDef("LiquidTypeID_3", FieldType.INT),
        FieldDef("MinElevation", FieldType.FLOAT),
        FieldDef("Ambient_Multiplier", FieldType.FLOAT),
        FieldDef("Lightid", FieldType.INT),
    ]
)

# AreaTrigger - 10 fields
BUILTIN_SCHEMAS["AreaTrigger"] = SchemaDef(
    name="AreaTrigger",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ContinentID", FieldType.INT),
        FieldDef("X", FieldType.FLOAT),
        FieldDef("Y", FieldType.FLOAT),
        FieldDef("Z", FieldType.FLOAT),
        FieldDef("Radius", FieldType.FLOAT),
        FieldDef("Box_Length", FieldType.FLOAT),
        FieldDef("Box_Width", FieldType.FLOAT),
        FieldDef("Box_Height", FieldType.FLOAT),
        FieldDef("Box_Yaw", FieldType.FLOAT),
    ]
)

# Armorlocation - 6 fields
BUILTIN_SCHEMAS["Armorlocation"] = SchemaDef(
    name="Armorlocation",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Clothmodifier", FieldType.FLOAT),
        FieldDef("Leathermodifier", FieldType.FLOAT),
        FieldDef("Chainmodifier", FieldType.FLOAT),
        FieldDef("Platemodifier", FieldType.FLOAT),
        FieldDef("Modifier", FieldType.FLOAT),
    ]
)

# AttackAnimKits - 5 fields
BUILTIN_SCHEMAS["AttackAnimKits"] = SchemaDef(
    name="AttackAnimKits",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Animation", FieldType.INT),
        FieldDef("Type", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("Field04", FieldType.INT),
    ]
)

# AttackAnimTypes - 2 fields
BUILTIN_SCHEMAS["AttackAnimTypes"] = SchemaDef(
    name="AttackAnimTypes",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
    ]
)

# AuctionHouse - 21 fields
BUILTIN_SCHEMAS["AuctionHouse"] = SchemaDef(
    name="AuctionHouse",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("FactionID", FieldType.INT),
        FieldDef("DepositRate", FieldType.INT),
        FieldDef("ConsignmentRate", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
    ]
)

# BankBagSlotPrices - 2 fields
BUILTIN_SCHEMAS["BankBagSlotPrices"] = SchemaDef(
    name="BankBagSlotPrices",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Cost", FieldType.INT),
    ]
)

# BannedAddOns - 11 fields
BUILTIN_SCHEMAS["BannedAddOns"] = SchemaDef(
    name="BannedAddOns",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("NameMD5__0", FieldType.UINT),
        FieldDef("NameMD5__1", FieldType.UINT),
        FieldDef("NameMD5__2", FieldType.UINT),
        FieldDef("NameMD5__3", FieldType.UINT),
        FieldDef("VersionMD5__0", FieldType.UINT),
        FieldDef("VersionMD5__1", FieldType.UINT),
        FieldDef("VersionMD5__2", FieldType.UINT),
        FieldDef("VersionMD5__3", FieldType.UINT),
        FieldDef("LastModified", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
    ]
)

# BarberShopStyle - 40 fields
BUILTIN_SCHEMAS["BarberShopStyle"] = SchemaDef(
    name="BarberShopStyle",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Type", FieldType.INT),
        FieldDef("DisplayName_Lang_enUS", FieldType.STRING),
        FieldDef("DisplayName_Lang_koKR", FieldType.STRING),
        FieldDef("DisplayName_Lang_frFR", FieldType.STRING),
        FieldDef("DisplayName_Lang_deDE", FieldType.STRING),
        FieldDef("DisplayName_Lang_enCN", FieldType.STRING),
        FieldDef("DisplayName_Lang_enTW", FieldType.STRING),
        FieldDef("DisplayName_Lang_esES", FieldType.STRING),
        FieldDef("DisplayName_Lang_esMX", FieldType.STRING),
        FieldDef("DisplayName_Lang_ruRU", FieldType.STRING),
        FieldDef("DisplayName_Lang_jaJP", FieldType.STRING),
        FieldDef("DisplayName_Lang_ptPT", FieldType.STRING),
        FieldDef("DisplayName_Lang_itIT", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk12", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk13", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk14", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk15", FieldType.STRING),
        FieldDef("DisplayName_Lang_Flags", FieldType.UINT),
        FieldDef("Description_Lang_enUS", FieldType.STRING),
        FieldDef("Description_Lang_koKR", FieldType.STRING),
        FieldDef("Description_Lang_frFR", FieldType.STRING),
        FieldDef("Description_Lang_deDE", FieldType.STRING),
        FieldDef("Description_Lang_enCN", FieldType.STRING),
        FieldDef("Description_Lang_enTW", FieldType.STRING),
        FieldDef("Description_Lang_esES", FieldType.STRING),
        FieldDef("Description_Lang_esMX", FieldType.STRING),
        FieldDef("Description_Lang_ruRU", FieldType.STRING),
        FieldDef("Description_Lang_jaJP", FieldType.STRING),
        FieldDef("Description_Lang_ptPT", FieldType.STRING),
        FieldDef("Description_Lang_itIT", FieldType.STRING),
        FieldDef("Description_Lang_Unk12", FieldType.STRING),
        FieldDef("Description_Lang_Unk13", FieldType.STRING),
        FieldDef("Description_Lang_Unk14", FieldType.STRING),
        FieldDef("Description_Lang_Unk15", FieldType.STRING),
        FieldDef("Description_Lang_Flags", FieldType.UINT),
        FieldDef("Cost_Modifier", FieldType.FLOAT),
        FieldDef("Race", FieldType.INT),
        FieldDef("Sex", FieldType.INT),
        FieldDef("Data", FieldType.INT),
    ]
)

# BattlemasterList - 32 fields
BUILTIN_SCHEMAS["BattlemasterList"] = SchemaDef(
    name="BattlemasterList",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MapID_0", FieldType.INT),
        FieldDef("MapID_1", FieldType.INT),
        FieldDef("MapID_2", FieldType.INT),
        FieldDef("MapID_3", FieldType.INT),
        FieldDef("MapID_4", FieldType.INT),
        FieldDef("MapID_5", FieldType.INT),
        FieldDef("MapID_6", FieldType.INT),
        FieldDef("MapID_7", FieldType.INT),
        FieldDef("InstanceType", FieldType.INT),
        FieldDef("GroupsAllowed", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("MaxGroupSize", FieldType.INT),
        FieldDef("HolidayWorldState", FieldType.INT),
        FieldDef("Minlevel", FieldType.INT),
        FieldDef("Maxlevel", FieldType.INT),
    ]
)

# CameraShakes - 8 fields
BUILTIN_SCHEMAS["CameraShakes"] = SchemaDef(
    name="CameraShakes",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ShakeType", FieldType.INT),
        FieldDef("Direction", FieldType.INT),
        FieldDef("Amplitude", FieldType.FLOAT),
        FieldDef("Frequency", FieldType.FLOAT),
        FieldDef("Duration", FieldType.FLOAT),
        FieldDef("Phase", FieldType.FLOAT),
        FieldDef("Coefficient", FieldType.FLOAT),
    ]
)

# Cfg_Categories - 21 fields
BUILTIN_SCHEMAS["Cfg_Categories"] = SchemaDef(
    name="Cfg_Categories",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("LocaleMask", FieldType.INT),
        FieldDef("CharsetMask", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
    ]
)

# Cfg_Configs - 5 fields
BUILTIN_SCHEMAS["Cfg_Configs"] = SchemaDef(
    name="Cfg_Configs",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ID", FieldType.INT),
        FieldDef("RealmType", FieldType.INT),
        FieldDef("PlayerKillingAllowed", FieldType.INT),
        FieldDef("Roleplaying", FieldType.INT),
    ]
)

# CharBaseInfo - 3 fields
BUILTIN_SCHEMAS["CharBaseInfo"] = SchemaDef(
    name="CharBaseInfo",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("RaceID", FieldType.UINT),
        FieldDef("ClassID", FieldType.UINT),
    ]
)

# CharHairGeosets - 6 fields
BUILTIN_SCHEMAS["CharHairGeosets"] = SchemaDef(
    name="CharHairGeosets",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("RaceID", FieldType.INT),
        FieldDef("SexID", FieldType.INT),
        FieldDef("VariationID", FieldType.INT),
        FieldDef("GeosetID", FieldType.INT),
        FieldDef("Showscalp", FieldType.INT),
    ]
)

# CharHairTextures - 8 fields
BUILTIN_SCHEMAS["CharHairTextures"] = SchemaDef(
    name="CharHairTextures",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Race", FieldType.INT),
        FieldDef("Gender", FieldType.UINT),
        FieldDef("Field03", FieldType.UINT),
        FieldDef("Field04_0", FieldType.INT),
        FieldDef("Field04_1", FieldType.INT),
        FieldDef("Field04_2", FieldType.INT),
        FieldDef("Field04_3", FieldType.INT),
    ]
)

# CharSections - 10 fields
BUILTIN_SCHEMAS["CharSections"] = SchemaDef(
    name="CharSections",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("RaceID", FieldType.INT),
        FieldDef("SexID", FieldType.INT),
        FieldDef("BaseSection", FieldType.INT),
        FieldDef("TextureName_0", FieldType.STRING),
        FieldDef("TextureName_1", FieldType.STRING),
        FieldDef("TextureName_2", FieldType.STRING),
        FieldDef("Flags", FieldType.INT),
        FieldDef("VariationIndex", FieldType.INT),
        FieldDef("ColorIndex", FieldType.INT),
    ]
)

# CharStartOutfit - 77 fields
BUILTIN_SCHEMAS["CharStartOutfit"] = SchemaDef(
    name="CharStartOutfit",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("RaceID", FieldType.UINT),
        FieldDef("ClassID", FieldType.UINT),
        FieldDef("SexID", FieldType.UINT),
        FieldDef("OutfitID", FieldType.UINT),
        FieldDef("ItemID_0", FieldType.INT),
        FieldDef("ItemID_1", FieldType.INT),
        FieldDef("ItemID_2", FieldType.INT),
        FieldDef("ItemID_3", FieldType.INT),
        FieldDef("ItemID_4", FieldType.INT),
        FieldDef("ItemID_5", FieldType.INT),
        FieldDef("ItemID_6", FieldType.INT),
        FieldDef("ItemID_7", FieldType.INT),
        FieldDef("ItemID_8", FieldType.INT),
        FieldDef("ItemID_9", FieldType.INT),
        FieldDef("ItemID_10", FieldType.INT),
        FieldDef("ItemID_11", FieldType.INT),
        FieldDef("ItemID_12", FieldType.INT),
        FieldDef("ItemID_13", FieldType.INT),
        FieldDef("ItemID_14", FieldType.INT),
        FieldDef("ItemID_15", FieldType.INT),
        FieldDef("ItemID_16", FieldType.INT),
        FieldDef("ItemID_17", FieldType.INT),
        FieldDef("ItemID_18", FieldType.INT),
        FieldDef("ItemID_19", FieldType.INT),
        FieldDef("ItemID_20", FieldType.INT),
        FieldDef("ItemID_21", FieldType.INT),
        FieldDef("ItemID_22", FieldType.INT),
        FieldDef("ItemID_23", FieldType.INT),
        FieldDef("DisplayItemID_0", FieldType.INT),
        FieldDef("DisplayItemID_1", FieldType.INT),
        FieldDef("DisplayItemID_2", FieldType.INT),
        FieldDef("DisplayItemID_3", FieldType.INT),
        FieldDef("DisplayItemID_4", FieldType.INT),
        FieldDef("DisplayItemID_5", FieldType.INT),
        FieldDef("DisplayItemID_6", FieldType.INT),
        FieldDef("DisplayItemID_7", FieldType.INT),
        FieldDef("DisplayItemID_8", FieldType.INT),
        FieldDef("DisplayItemID_9", FieldType.INT),
        FieldDef("DisplayItemID_10", FieldType.INT),
        FieldDef("DisplayItemID_11", FieldType.INT),
        FieldDef("DisplayItemID_12", FieldType.INT),
        FieldDef("DisplayItemID_13", FieldType.INT),
        FieldDef("DisplayItemID_14", FieldType.INT),
        FieldDef("DisplayItemID_15", FieldType.INT),
        FieldDef("DisplayItemID_16", FieldType.INT),
        FieldDef("DisplayItemID_17", FieldType.INT),
        FieldDef("DisplayItemID_18", FieldType.INT),
        FieldDef("DisplayItemID_19", FieldType.INT),
        FieldDef("DisplayItemID_20", FieldType.INT),
        FieldDef("DisplayItemID_21", FieldType.INT),
        FieldDef("DisplayItemID_22", FieldType.INT),
        FieldDef("DisplayItemID_23", FieldType.INT),
        FieldDef("InventoryType_0", FieldType.INT),
        FieldDef("InventoryType_1", FieldType.INT),
        FieldDef("InventoryType_2", FieldType.INT),
        FieldDef("InventoryType_3", FieldType.INT),
        FieldDef("InventoryType_4", FieldType.INT),
        FieldDef("InventoryType_5", FieldType.INT),
        FieldDef("InventoryType_6", FieldType.INT),
        FieldDef("InventoryType_7", FieldType.INT),
        FieldDef("InventoryType_8", FieldType.INT),
        FieldDef("InventoryType_9", FieldType.INT),
        FieldDef("InventoryType_10", FieldType.INT),
        FieldDef("InventoryType_11", FieldType.INT),
        FieldDef("InventoryType_12", FieldType.INT),
        FieldDef("InventoryType_13", FieldType.INT),
        FieldDef("InventoryType_14", FieldType.INT),
        FieldDef("InventoryType_15", FieldType.INT),
        FieldDef("InventoryType_16", FieldType.INT),
        FieldDef("InventoryType_17", FieldType.INT),
        FieldDef("InventoryType_18", FieldType.INT),
        FieldDef("InventoryType_19", FieldType.INT),
        FieldDef("InventoryType_20", FieldType.INT),
        FieldDef("InventoryType_21", FieldType.INT),
        FieldDef("InventoryType_22", FieldType.INT),
        FieldDef("InventoryType_23", FieldType.INT),
    ]
)

# CharTitles - 37 fields
BUILTIN_SCHEMAS["CharTitles"] = SchemaDef(
    name="CharTitles",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Condition_ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("Name1_Lang_enUS", FieldType.STRING),
        FieldDef("Name1_Lang_koKR", FieldType.STRING),
        FieldDef("Name1_Lang_frFR", FieldType.STRING),
        FieldDef("Name1_Lang_deDE", FieldType.STRING),
        FieldDef("Name1_Lang_enCN", FieldType.STRING),
        FieldDef("Name1_Lang_enTW", FieldType.STRING),
        FieldDef("Name1_Lang_esES", FieldType.STRING),
        FieldDef("Name1_Lang_esMX", FieldType.STRING),
        FieldDef("Name1_Lang_ruRU", FieldType.STRING),
        FieldDef("Name1_Lang_jaJP", FieldType.STRING),
        FieldDef("Name1_Lang_ptPT", FieldType.STRING),
        FieldDef("Name1_Lang_itIT", FieldType.STRING),
        FieldDef("Name1_Lang_Unk12", FieldType.STRING),
        FieldDef("Name1_Lang_Unk13", FieldType.STRING),
        FieldDef("Name1_Lang_Unk14", FieldType.STRING),
        FieldDef("Name1_Lang_Unk15", FieldType.STRING),
        FieldDef("Name1_Lang_Flags", FieldType.UINT),
        FieldDef("Mask_ID", FieldType.INT),
    ]
)

# CharVariations - 6 fields
BUILTIN_SCHEMAS["CharVariations"] = SchemaDef(
    name="CharVariations",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("RaceID", FieldType.INT),
        FieldDef("Gender", FieldType.INT),
        FieldDef("Unknown1", FieldType.INT),
        FieldDef("Unknown2", FieldType.INT),
        FieldDef("Unknown3", FieldType.INT),
    ]
)

# CharacterFacialHairStyles - 9 fields
BUILTIN_SCHEMAS["CharacterFacialHairStyles"] = SchemaDef(
    name="CharacterFacialHairStyles",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("RaceID", FieldType.INT),
        FieldDef("SexID", FieldType.INT),
        FieldDef("VariationID", FieldType.INT),
        FieldDef("Geoset_0", FieldType.INT),
        FieldDef("Geoset_1", FieldType.INT),
        FieldDef("Geoset_2", FieldType.INT),
        FieldDef("Geoset_3", FieldType.INT),
        FieldDef("Geoset_4", FieldType.INT),
    ]
)

# ChatChannels - 37 fields
BUILTIN_SCHEMAS["ChatChannels"] = SchemaDef(
    name="ChatChannels",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("FactionGroup", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("Shortcut_Lang_enUS", FieldType.STRING),
        FieldDef("Shortcut_Lang_koKR", FieldType.STRING),
        FieldDef("Shortcut_Lang_frFR", FieldType.STRING),
        FieldDef("Shortcut_Lang_deDE", FieldType.STRING),
        FieldDef("Shortcut_Lang_enCN", FieldType.STRING),
        FieldDef("Shortcut_Lang_enTW", FieldType.STRING),
        FieldDef("Shortcut_Lang_esES", FieldType.STRING),
        FieldDef("Shortcut_Lang_esMX", FieldType.STRING),
        FieldDef("Shortcut_Lang_ruRU", FieldType.STRING),
        FieldDef("Shortcut_Lang_jaJP", FieldType.STRING),
        FieldDef("Shortcut_Lang_ptPT", FieldType.STRING),
        FieldDef("Shortcut_Lang_itIT", FieldType.STRING),
        FieldDef("Shortcut_Lang_Unk12", FieldType.STRING),
        FieldDef("Shortcut_Lang_Unk13", FieldType.STRING),
        FieldDef("Shortcut_Lang_Unk14", FieldType.STRING),
        FieldDef("Shortcut_Lang_Unk15", FieldType.STRING),
        FieldDef("Shortcut_Lang_Flags", FieldType.UINT),
    ]
)

# ChatProfanity - 3 fields
BUILTIN_SCHEMAS["ChatProfanity"] = SchemaDef(
    name="ChatProfanity",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Text", FieldType.STRING),
        FieldDef("Language", FieldType.INT),
    ]
)

# ChrClasses - 60 fields
BUILTIN_SCHEMAS["ChrClasses"] = SchemaDef(
    name="ChrClasses",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Field01", FieldType.INT),
        FieldDef("DisplayPower", FieldType.INT),
        FieldDef("PetNameToken", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("Name_Female_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Female_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Female_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Female_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Female_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Female_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Female_Lang_esES", FieldType.STRING),
        FieldDef("Name_Female_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Female_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Female_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Female_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Female_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Female_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Female_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Female_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Female_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Female_Lang_Flags", FieldType.UINT),
        FieldDef("Name_Male_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Male_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Male_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Male_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Male_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Male_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Male_Lang_esES", FieldType.STRING),
        FieldDef("Name_Male_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Male_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Male_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Male_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Male_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Male_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Male_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Male_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Male_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Male_Lang_Flags", FieldType.UINT),
        FieldDef("Filename", FieldType.STRING),
        FieldDef("SpellClassSet", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("CinematicSequenceID", FieldType.INT),
        FieldDef("Required_Expansion", FieldType.INT),
    ]
)

# ChrRaces - 69 fields
BUILTIN_SCHEMAS["ChrRaces"] = SchemaDef(
    name="ChrRaces",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("FactionID", FieldType.INT),
        FieldDef("ExplorationSoundID", FieldType.INT),
        FieldDef("MaleDisplayId", FieldType.INT),
        FieldDef("FemaleDisplayId", FieldType.INT),
        FieldDef("ClientPrefix", FieldType.STRING),
        FieldDef("BaseLanguage", FieldType.INT),
        FieldDef("CreatureType", FieldType.INT),
        FieldDef("ResSicknessSpellID", FieldType.INT),
        FieldDef("SplashSoundID", FieldType.INT),
        FieldDef("ClientFilestring", FieldType.STRING),
        FieldDef("CinematicSequenceID", FieldType.INT),
        FieldDef("Alliance", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("Name_Female_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Female_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Female_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Female_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Female_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Female_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Female_Lang_esES", FieldType.STRING),
        FieldDef("Name_Female_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Female_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Female_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Female_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Female_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Female_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Female_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Female_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Female_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Female_Lang_Flags", FieldType.UINT),
        FieldDef("Name_Male_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Male_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Male_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Male_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Male_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Male_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Male_Lang_esES", FieldType.STRING),
        FieldDef("Name_Male_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Male_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Male_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Male_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Male_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Male_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Male_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Male_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Male_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Male_Lang_Flags", FieldType.UINT),
        FieldDef("FacialHairCustomization_0", FieldType.STRING),
        FieldDef("FacialHairCustomization_1", FieldType.STRING),
        FieldDef("HairCustomization", FieldType.STRING),
        FieldDef("Required_Expansion", FieldType.INT),
    ]
)

# CinematicCamera - 7 fields
BUILTIN_SCHEMAS["CinematicCamera"] = SchemaDef(
    name="CinematicCamera",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Model", FieldType.STRING),
        FieldDef("SoundID", FieldType.INT),
        FieldDef("OriginX", FieldType.FLOAT),
        FieldDef("OriginY", FieldType.FLOAT),
        FieldDef("OriginZ", FieldType.FLOAT),
        FieldDef("OriginFacing", FieldType.FLOAT),
    ]
)

# CinematicSequences - 10 fields
BUILTIN_SCHEMAS["CinematicSequences"] = SchemaDef(
    name="CinematicSequences",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SoundID", FieldType.INT),
        FieldDef("Camera_0", FieldType.INT),
        FieldDef("Camera_1", FieldType.INT),
        FieldDef("Camera_2", FieldType.INT),
        FieldDef("Camera_3", FieldType.INT),
        FieldDef("Camera_4", FieldType.INT),
        FieldDef("Camera_5", FieldType.INT),
        FieldDef("Camera_6", FieldType.INT),
        FieldDef("Camera_7", FieldType.INT),
    ]
)

# CreatureDisplayInfo - 16 fields
BUILTIN_SCHEMAS["CreatureDisplayInfo"] = SchemaDef(
    name="CreatureDisplayInfo",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ModelID", FieldType.INT),
        FieldDef("SoundID", FieldType.INT),
        FieldDef("ExtendedDisplayInfoID", FieldType.INT),
        FieldDef("CreatureModelScale", FieldType.FLOAT),
        FieldDef("CreatureModelAlpha", FieldType.INT),
        FieldDef("TextureVariation_0", FieldType.STRING),
        FieldDef("TextureVariation_1", FieldType.STRING),
        FieldDef("TextureVariation_2", FieldType.STRING),
        FieldDef("PortraitTextureName", FieldType.STRING),
        FieldDef("BloodLevel", FieldType.INT),
        FieldDef("BloodID", FieldType.INT),
        FieldDef("NPCSoundID", FieldType.INT),
        FieldDef("ParticleColorID", FieldType.INT),
        FieldDef("CreatureGeosetData", FieldType.INT),
        FieldDef("ObjectEffectPackageID", FieldType.INT),
    ]
)

# CreatureDisplayInfoExtra - 21 fields
BUILTIN_SCHEMAS["CreatureDisplayInfoExtra"] = SchemaDef(
    name="CreatureDisplayInfoExtra",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("DisplayRaceID", FieldType.INT),
        FieldDef("DisplaySexID", FieldType.INT),
        FieldDef("SkinID", FieldType.INT),
        FieldDef("FaceID", FieldType.INT),
        FieldDef("HairStyleID", FieldType.INT),
        FieldDef("HairColorID", FieldType.INT),
        FieldDef("FacialHairID", FieldType.INT),
        FieldDef("NPCItemDisplay_0", FieldType.INT),
        FieldDef("NPCItemDisplay_1", FieldType.INT),
        FieldDef("NPCItemDisplay_2", FieldType.INT),
        FieldDef("NPCItemDisplay_3", FieldType.INT),
        FieldDef("NPCItemDisplay_4", FieldType.INT),
        FieldDef("NPCItemDisplay_5", FieldType.INT),
        FieldDef("NPCItemDisplay_6", FieldType.INT),
        FieldDef("NPCItemDisplay_7", FieldType.INT),
        FieldDef("NPCItemDisplay_8", FieldType.INT),
        FieldDef("NPCItemDisplay_9", FieldType.INT),
        FieldDef("NPCItemDisplay_10", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("BakeName", FieldType.STRING),
    ]
)

# CreatureFamily - 28 fields
BUILTIN_SCHEMAS["CreatureFamily"] = SchemaDef(
    name="CreatureFamily",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MinScale", FieldType.FLOAT),
        FieldDef("MinScaleLevel", FieldType.INT),
        FieldDef("MaxScale", FieldType.FLOAT),
        FieldDef("MaxScaleLevel", FieldType.INT),
        FieldDef("SkillLine_0", FieldType.INT),
        FieldDef("SkillLine_1", FieldType.INT),
        FieldDef("PetFoodMask", FieldType.INT),
        FieldDef("PetTalentType", FieldType.INT),
        FieldDef("CategoryEnumID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("IconFile", FieldType.STRING),
    ]
)

# CreatureModelData - 28 fields
BUILTIN_SCHEMAS["CreatureModelData"] = SchemaDef(
    name="CreatureModelData",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("ModelName", FieldType.STRING),
        FieldDef("SizeClass", FieldType.INT),
        FieldDef("ModelScale", FieldType.FLOAT),
        FieldDef("BloodID", FieldType.INT),
        FieldDef("FootprintTextureID", FieldType.INT),
        FieldDef("FootprintTextureLength", FieldType.FLOAT),
        FieldDef("FootprintTextureWidth", FieldType.FLOAT),
        FieldDef("FootprintParticleScale", FieldType.FLOAT),
        FieldDef("FoleyMaterialID", FieldType.INT),
        FieldDef("FootstepShakeSize", FieldType.INT),
        FieldDef("DeathThudShakeSize", FieldType.INT),
        FieldDef("SoundID", FieldType.INT),
        FieldDef("CollisionWidth", FieldType.FLOAT),
        FieldDef("CollisionHeight", FieldType.FLOAT),
        FieldDef("MountHeight", FieldType.FLOAT),
        FieldDef("GeoBoxMinX", FieldType.FLOAT),
        FieldDef("GeoBoxMinY", FieldType.FLOAT),
        FieldDef("GeoBoxMinZ", FieldType.FLOAT),
        FieldDef("GeoBoxMaxX", FieldType.FLOAT),
        FieldDef("GeoBoxMaxY", FieldType.FLOAT),
        FieldDef("GeoBoxMaxZ", FieldType.FLOAT),
        FieldDef("WorldEffectScale", FieldType.FLOAT),
        FieldDef("AttachedEffectScale", FieldType.FLOAT),
        FieldDef("MissileCollisionRadius", FieldType.FLOAT),
        FieldDef("MissileCollisionPush", FieldType.FLOAT),
        FieldDef("MissileCollisionRaise", FieldType.FLOAT),
    ]
)

# CreatureMovementInfo - 2 fields
BUILTIN_SCHEMAS["CreatureMovementInfo"] = SchemaDef(
    name="CreatureMovementInfo",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SmoothFacingChaseRate", FieldType.FLOAT),
    ]
)

# CreatureSoundData - 38 fields
BUILTIN_SCHEMAS["CreatureSoundData"] = SchemaDef(
    name="CreatureSoundData",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SoundExertionID", FieldType.INT),
        FieldDef("SoundExertionCriticalID", FieldType.INT),
        FieldDef("SoundInjuryID", FieldType.INT),
        FieldDef("SoundInjuryCriticalID", FieldType.INT),
        FieldDef("SoundInjuryCrushingBlowID", FieldType.INT),
        FieldDef("SoundDeathID", FieldType.INT),
        FieldDef("SoundStunID", FieldType.INT),
        FieldDef("SoundStandID", FieldType.INT),
        FieldDef("SoundFootstepID", FieldType.INT),
        FieldDef("SoundAggroID", FieldType.INT),
        FieldDef("SoundWingFlapID", FieldType.INT),
        FieldDef("SoundWingGlideID", FieldType.INT),
        FieldDef("SoundAlertID", FieldType.INT),
        FieldDef("SoundFidget_0", FieldType.INT),
        FieldDef("SoundFidget_1", FieldType.INT),
        FieldDef("SoundFidget_2", FieldType.INT),
        FieldDef("SoundFidget_3", FieldType.INT),
        FieldDef("SoundFidget_4", FieldType.INT),
        FieldDef("CustomAttack_0", FieldType.INT),
        FieldDef("CustomAttack_1", FieldType.INT),
        FieldDef("CustomAttack_2", FieldType.INT),
        FieldDef("CustomAttack_3", FieldType.INT),
        FieldDef("NPCSoundID", FieldType.INT),
        FieldDef("LoopSoundID", FieldType.INT),
        FieldDef("CreatureImpactType", FieldType.INT),
        FieldDef("SoundJumpStartID", FieldType.INT),
        FieldDef("SoundJumpEndID", FieldType.INT),
        FieldDef("SoundPetAttackID", FieldType.INT),
        FieldDef("SoundPetOrderID", FieldType.INT),
        FieldDef("SoundPetDismissID", FieldType.INT),
        FieldDef("FidgetDelaySecondsMin", FieldType.FLOAT),
        FieldDef("FidgetDelaySecondsMax", FieldType.FLOAT),
        FieldDef("BirthSoundID", FieldType.INT),
        FieldDef("SpellCastDirectedSoundID", FieldType.INT),
        FieldDef("SubmergeSoundID", FieldType.INT),
        FieldDef("SubmergedSoundID", FieldType.INT),
        FieldDef("CreatureSoundDataIDPet", FieldType.INT),
    ]
)

# CreatureSpellData - 9 fields
BUILTIN_SCHEMAS["CreatureSpellData"] = SchemaDef(
    name="CreatureSpellData",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Spells_0", FieldType.INT),
        FieldDef("Spells_1", FieldType.INT),
        FieldDef("Spells_2", FieldType.INT),
        FieldDef("Spells_3", FieldType.INT),
        FieldDef("Availability_0", FieldType.INT),
        FieldDef("Availability_1", FieldType.INT),
        FieldDef("Availability_2", FieldType.INT),
        FieldDef("Availability_3", FieldType.INT),
    ]
)

# CreatureType - 19 fields
BUILTIN_SCHEMAS["CreatureType"] = SchemaDef(
    name="CreatureType",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("Flags", FieldType.INT),
    ]
)

# CurrencyCategory - 19 fields
BUILTIN_SCHEMAS["CurrencyCategory"] = SchemaDef(
    name="CurrencyCategory",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
    ]
)

# CurrencyTypes - 4 fields
BUILTIN_SCHEMAS["CurrencyTypes"] = SchemaDef(
    name="CurrencyTypes",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ItemID", FieldType.INT),
        FieldDef("CategoryID", FieldType.INT),
        FieldDef("BitIndex", FieldType.INT),
    ]
)

# DanceMoves - 24 fields
BUILTIN_SCHEMAS["DanceMoves"] = SchemaDef(
    name="DanceMoves",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Type", FieldType.INT),
        FieldDef("Param", FieldType.INT),
        FieldDef("Fallback", FieldType.INT),
        FieldDef("Racemask", FieldType.INT),
        FieldDef("Internal_Name", FieldType.STRING),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("LockID", FieldType.INT),
    ]
)

# DeathThudLookups - 5 fields
BUILTIN_SCHEMAS["DeathThudLookups"] = SchemaDef(
    name="DeathThudLookups",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SizeClass", FieldType.INT),
        FieldDef("TerraintypeSoundID", FieldType.INT),
        FieldDef("SoundEntryID", FieldType.INT),
        FieldDef("SoundEntryIDWater", FieldType.INT),
    ]
)

# DeclinedWord - 2 fields
BUILTIN_SCHEMAS["DeclinedWord"] = SchemaDef(
    name="DeclinedWord",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Word", FieldType.STRING),
    ]
)

# DeclinedWordCases - 4 fields
BUILTIN_SCHEMAS["DeclinedWordCases"] = SchemaDef(
    name="DeclinedWordCases",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("DeclinedWordID", FieldType.INT),
        FieldDef("CaseIndex", FieldType.INT),
        FieldDef("DeclinedWord", FieldType.STRING),
    ]
)

# DestructibleModelData - 19 fields
BUILTIN_SCHEMAS["DestructibleModelData"] = SchemaDef(
    name="DestructibleModelData",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("State0Wmo", FieldType.INT),
        FieldDef("State0DestructionDoodadSet", FieldType.INT),
        FieldDef("State0ImpactEffectDoodadSet", FieldType.INT),
        FieldDef("State0AmbientDoodadSet", FieldType.INT),
        FieldDef("State1Wmo", FieldType.INT),
        FieldDef("State1DestructionDoodadSet", FieldType.INT),
        FieldDef("State1ImpactEffectDoodadSet", FieldType.INT),
        FieldDef("State1AmbientDoodadSet", FieldType.INT),
        FieldDef("State2Wmo", FieldType.INT),
        FieldDef("State2DestructionDoodadSet", FieldType.INT),
        FieldDef("State2ImpactEffectDoodadSet", FieldType.INT),
        FieldDef("State2AmbientDoodadSet", FieldType.INT),
        FieldDef("State3Wmo", FieldType.INT),
        FieldDef("State3DestructionDoodadSet", FieldType.INT),
        FieldDef("State3ImpactEffectDoodadSet", FieldType.INT),
        FieldDef("State3AmbientDoodadSet", FieldType.INT),
        FieldDef("Field17", FieldType.INT),
        FieldDef("Field18", FieldType.INT),
    ]
)

# DungeonEncounter - 23 fields
BUILTIN_SCHEMAS["DungeonEncounter"] = SchemaDef(
    name="DungeonEncounter",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MapID", FieldType.INT),
        FieldDef("Difficulty", FieldType.INT),
        FieldDef("OrderIndex", FieldType.INT),
        FieldDef("Bit", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("SpellIconID", FieldType.INT),
    ]
)

# DungeonMap - 8 fields
BUILTIN_SCHEMAS["DungeonMap"] = SchemaDef(
    name="DungeonMap",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MapID", FieldType.INT),
        FieldDef("FloorIndex", FieldType.INT),
        FieldDef("MinX", FieldType.FLOAT),
        FieldDef("MaxX", FieldType.FLOAT),
        FieldDef("MinY", FieldType.FLOAT),
        FieldDef("MaxY", FieldType.FLOAT),
        FieldDef("ParentWorldMapID", FieldType.INT),
    ]
)

# DungeonMapChunk - 5 fields
BUILTIN_SCHEMAS["DungeonMapChunk"] = SchemaDef(
    name="DungeonMapChunk",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MapID", FieldType.INT),
        FieldDef("WmoGroupID", FieldType.INT),
        FieldDef("DungeonMapID", FieldType.INT),
        FieldDef("MinZ", FieldType.FLOAT),
    ]
)

# DurabilityCosts - 30 fields
BUILTIN_SCHEMAS["DurabilityCosts"] = SchemaDef(
    name="DurabilityCosts",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("WeaponSubClassCost_0", FieldType.INT),
        FieldDef("WeaponSubClassCost_1", FieldType.INT),
        FieldDef("WeaponSubClassCost_2", FieldType.INT),
        FieldDef("WeaponSubClassCost_3", FieldType.INT),
        FieldDef("WeaponSubClassCost_4", FieldType.INT),
        FieldDef("WeaponSubClassCost_5", FieldType.INT),
        FieldDef("WeaponSubClassCost_6", FieldType.INT),
        FieldDef("WeaponSubClassCost_7", FieldType.INT),
        FieldDef("WeaponSubClassCost_8", FieldType.INT),
        FieldDef("WeaponSubClassCost_9", FieldType.INT),
        FieldDef("WeaponSubClassCost_10", FieldType.INT),
        FieldDef("WeaponSubClassCost_11", FieldType.INT),
        FieldDef("WeaponSubClassCost_12", FieldType.INT),
        FieldDef("WeaponSubClassCost_13", FieldType.INT),
        FieldDef("WeaponSubClassCost_14", FieldType.INT),
        FieldDef("WeaponSubClassCost_15", FieldType.INT),
        FieldDef("WeaponSubClassCost_16", FieldType.INT),
        FieldDef("WeaponSubClassCost_17", FieldType.INT),
        FieldDef("WeaponSubClassCost_18", FieldType.INT),
        FieldDef("WeaponSubClassCost_19", FieldType.INT),
        FieldDef("WeaponSubClassCost_20", FieldType.INT),
        FieldDef("ArmorSubClassCost_0", FieldType.INT),
        FieldDef("ArmorSubClassCost_1", FieldType.INT),
        FieldDef("ArmorSubClassCost_2", FieldType.INT),
        FieldDef("ArmorSubClassCost_3", FieldType.INT),
        FieldDef("ArmorSubClassCost_4", FieldType.INT),
        FieldDef("ArmorSubClassCost_5", FieldType.INT),
        FieldDef("ArmorSubClassCost_6", FieldType.INT),
        FieldDef("ArmorSubClassCost_7", FieldType.INT),
    ]
)

# DurabilityQuality - 2 fields
BUILTIN_SCHEMAS["DurabilityQuality"] = SchemaDef(
    name="DurabilityQuality",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# Emotes - 7 fields
BUILTIN_SCHEMAS["Emotes"] = SchemaDef(
    name="Emotes",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("EmoteSlashCommand", FieldType.STRING),
        FieldDef("AnimID", FieldType.INT),
        FieldDef("EmoteFlags", FieldType.INT),
        FieldDef("EmoteSpecProc", FieldType.INT),
        FieldDef("EmoteSpecProcParam", FieldType.INT),
        FieldDef("EventSoundID", FieldType.INT),
    ]
)

# EmotesText - 19 fields
BUILTIN_SCHEMAS["EmotesText"] = SchemaDef(
    name="EmotesText",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("EmoteID", FieldType.INT),
        FieldDef("EmoteText_0", FieldType.INT),
        FieldDef("EmoteText_1", FieldType.INT),
        FieldDef("EmoteText_2", FieldType.INT),
        FieldDef("EmoteText_3", FieldType.INT),
        FieldDef("EmoteText_4", FieldType.INT),
        FieldDef("EmoteText_5", FieldType.INT),
        FieldDef("EmoteText_6", FieldType.INT),
        FieldDef("EmoteText_7", FieldType.INT),
        FieldDef("EmoteText_8", FieldType.INT),
        FieldDef("EmoteText_9", FieldType.INT),
        FieldDef("EmoteText_10", FieldType.INT),
        FieldDef("EmoteText_11", FieldType.INT),
        FieldDef("EmoteText_12", FieldType.INT),
        FieldDef("EmoteText_13", FieldType.INT),
        FieldDef("EmoteText_14", FieldType.INT),
        FieldDef("EmoteText_15", FieldType.INT),
    ]
)

# EmotesTextData - 18 fields
BUILTIN_SCHEMAS["EmotesTextData"] = SchemaDef(
    name="EmotesTextData",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Text_Lang_enUS", FieldType.STRING),
        FieldDef("Text_Lang_koKR", FieldType.STRING),
        FieldDef("Text_Lang_frFR", FieldType.STRING),
        FieldDef("Text_Lang_deDE", FieldType.STRING),
        FieldDef("Text_Lang_enCN", FieldType.STRING),
        FieldDef("Text_Lang_enTW", FieldType.STRING),
        FieldDef("Text_Lang_esES", FieldType.STRING),
        FieldDef("Text_Lang_esMX", FieldType.STRING),
        FieldDef("Text_Lang_ruRU", FieldType.STRING),
        FieldDef("Text_Lang_jaJP", FieldType.STRING),
        FieldDef("Text_Lang_ptPT", FieldType.STRING),
        FieldDef("Text_Lang_itIT", FieldType.STRING),
        FieldDef("Text_Lang_Unk12", FieldType.STRING),
        FieldDef("Text_Lang_Unk13", FieldType.STRING),
        FieldDef("Text_Lang_Unk14", FieldType.STRING),
        FieldDef("Text_Lang_Unk15", FieldType.STRING),
        FieldDef("Text_Lang_Flags", FieldType.UINT),
    ]
)

# EmotesTextSound - 5 fields
BUILTIN_SCHEMAS["EmotesTextSound"] = SchemaDef(
    name="EmotesTextSound",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("EmotesTextID", FieldType.INT),
        FieldDef("RaceID", FieldType.INT),
        FieldDef("SexID", FieldType.INT),
        FieldDef("SoundID", FieldType.INT),
    ]
)

# EnvironmentalDamage - 3 fields
BUILTIN_SCHEMAS["EnvironmentalDamage"] = SchemaDef(
    name="EnvironmentalDamage",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("EnumID", FieldType.INT),
        FieldDef("VisualkitID", FieldType.INT),
    ]
)

# Exhaustion - 23 fields
BUILTIN_SCHEMAS["Exhaustion"] = SchemaDef(
    name="Exhaustion",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Xp", FieldType.INT),
        FieldDef("Factor", FieldType.FLOAT),
        FieldDef("OutdoorHours", FieldType.FLOAT),
        FieldDef("InnHours", FieldType.FLOAT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("Threshold", FieldType.FLOAT),
    ]
)

# Faction - 57 fields
BUILTIN_SCHEMAS["Faction"] = SchemaDef(
    name="Faction",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ReputationIndex", FieldType.INT),
        FieldDef("ReputationRaceMask_0", FieldType.INT),
        FieldDef("ReputationRaceMask_1", FieldType.INT),
        FieldDef("ReputationRaceMask_2", FieldType.INT),
        FieldDef("ReputationRaceMask_3", FieldType.INT),
        FieldDef("ReputationClassMask_0", FieldType.INT),
        FieldDef("ReputationClassMask_1", FieldType.INT),
        FieldDef("ReputationClassMask_2", FieldType.INT),
        FieldDef("ReputationClassMask_3", FieldType.INT),
        FieldDef("ReputationBase_0", FieldType.INT),
        FieldDef("ReputationBase_1", FieldType.INT),
        FieldDef("ReputationBase_2", FieldType.INT),
        FieldDef("ReputationBase_3", FieldType.INT),
        FieldDef("ReputationFlags_0", FieldType.INT),
        FieldDef("ReputationFlags_1", FieldType.INT),
        FieldDef("ReputationFlags_2", FieldType.INT),
        FieldDef("ReputationFlags_3", FieldType.INT),
        FieldDef("ParentFactionID", FieldType.INT),
        FieldDef("ParentFactionMod_0", FieldType.FLOAT),
        FieldDef("ParentFactionMod_1", FieldType.FLOAT),
        FieldDef("ParentFactionCap_0", FieldType.INT),
        FieldDef("ParentFactionCap_1", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("Description_Lang_enUS", FieldType.STRING),
        FieldDef("Description_Lang_koKR", FieldType.STRING),
        FieldDef("Description_Lang_frFR", FieldType.STRING),
        FieldDef("Description_Lang_deDE", FieldType.STRING),
        FieldDef("Description_Lang_enCN", FieldType.STRING),
        FieldDef("Description_Lang_enTW", FieldType.STRING),
        FieldDef("Description_Lang_esES", FieldType.STRING),
        FieldDef("Description_Lang_esMX", FieldType.STRING),
        FieldDef("Description_Lang_ruRU", FieldType.STRING),
        FieldDef("Description_Lang_jaJP", FieldType.STRING),
        FieldDef("Description_Lang_ptPT", FieldType.STRING),
        FieldDef("Description_Lang_itIT", FieldType.STRING),
        FieldDef("Description_Lang_Unk12", FieldType.STRING),
        FieldDef("Description_Lang_Unk13", FieldType.STRING),
        FieldDef("Description_Lang_Unk14", FieldType.STRING),
        FieldDef("Description_Lang_Unk15", FieldType.STRING),
        FieldDef("Description_Lang_Flags", FieldType.UINT),
    ]
)

# FactionGroup - 20 fields
BUILTIN_SCHEMAS["FactionGroup"] = SchemaDef(
    name="FactionGroup",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MaskID", FieldType.INT),
        FieldDef("InternalName", FieldType.STRING),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
    ]
)

# FactionTemplate - 14 fields
BUILTIN_SCHEMAS["FactionTemplate"] = SchemaDef(
    name="FactionTemplate",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Faction", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("FactionGroup", FieldType.INT),
        FieldDef("FriendGroup", FieldType.INT),
        FieldDef("EnemyGroup", FieldType.INT),
        FieldDef("Enemies_0", FieldType.INT),
        FieldDef("Enemies_1", FieldType.INT),
        FieldDef("Enemies_2", FieldType.INT),
        FieldDef("Enemies_3", FieldType.INT),
        FieldDef("Friend_0", FieldType.INT),
        FieldDef("Friend_1", FieldType.INT),
        FieldDef("Friend_2", FieldType.INT),
        FieldDef("Friend_3", FieldType.INT),
    ]
)

# FileData - 3 fields
BUILTIN_SCHEMAS["FileData"] = SchemaDef(
    name="FileData",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Filename", FieldType.STRING),
        FieldDef("Filepath", FieldType.STRING),
    ]
)

# FootprintTextures - 2 fields
BUILTIN_SCHEMAS["FootprintTextures"] = SchemaDef(
    name="FootprintTextures",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("FootstepFilename", FieldType.STRING),
    ]
)

# FootstepTerrainLookup - 5 fields
BUILTIN_SCHEMAS["FootstepTerrainLookup"] = SchemaDef(
    name="FootstepTerrainLookup",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("CreatureFootstepID", FieldType.INT),
        FieldDef("TerrainSoundID", FieldType.INT),
        FieldDef("SoundID", FieldType.INT),
        FieldDef("SoundIDSplash", FieldType.INT),
    ]
)

# GMSurveyAnswers - 20 fields
BUILTIN_SCHEMAS["GMSurveyAnswers"] = SchemaDef(
    name="GMSurveyAnswers",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Sort_Index", FieldType.INT),
        FieldDef("GMSurveyQuestionID", FieldType.INT),
        FieldDef("Answer_Lang_enUS", FieldType.STRING),
        FieldDef("Answer_Lang_koKR", FieldType.STRING),
        FieldDef("Answer_Lang_frFR", FieldType.STRING),
        FieldDef("Answer_Lang_deDE", FieldType.STRING),
        FieldDef("Answer_Lang_enCN", FieldType.STRING),
        FieldDef("Answer_Lang_enTW", FieldType.STRING),
        FieldDef("Answer_Lang_esES", FieldType.STRING),
        FieldDef("Answer_Lang_esMX", FieldType.STRING),
        FieldDef("Answer_Lang_ruRU", FieldType.STRING),
        FieldDef("Answer_Lang_jaJP", FieldType.STRING),
        FieldDef("Answer_Lang_ptPT", FieldType.STRING),
        FieldDef("Answer_Lang_itIT", FieldType.STRING),
        FieldDef("Answer_Lang_Unk12", FieldType.STRING),
        FieldDef("Answer_Lang_Unk13", FieldType.STRING),
        FieldDef("Answer_Lang_Unk14", FieldType.STRING),
        FieldDef("Answer_Lang_Unk15", FieldType.STRING),
        FieldDef("Answer_Lang_Flags", FieldType.UINT),
    ]
)

# GMSurveyCurrentSurvey - 2 fields
BUILTIN_SCHEMAS["GMSurveyCurrentSurvey"] = SchemaDef(
    name="GMSurveyCurrentSurvey",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("GMSURVEY_ID", FieldType.INT),
    ]
)

# GMSurveyQuestions - 18 fields
BUILTIN_SCHEMAS["GMSurveyQuestions"] = SchemaDef(
    name="GMSurveyQuestions",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Question_Lang_enUS", FieldType.STRING),
        FieldDef("Question_Lang_koKR", FieldType.STRING),
        FieldDef("Question_Lang_frFR", FieldType.STRING),
        FieldDef("Question_Lang_deDE", FieldType.STRING),
        FieldDef("Question_Lang_enCN", FieldType.STRING),
        FieldDef("Question_Lang_enTW", FieldType.STRING),
        FieldDef("Question_Lang_esES", FieldType.STRING),
        FieldDef("Question_Lang_esMX", FieldType.STRING),
        FieldDef("Question_Lang_ruRU", FieldType.STRING),
        FieldDef("Question_Lang_jaJP", FieldType.STRING),
        FieldDef("Question_Lang_ptPT", FieldType.STRING),
        FieldDef("Question_Lang_itIT", FieldType.STRING),
        FieldDef("Question_Lang_Unk12", FieldType.STRING),
        FieldDef("Question_Lang_Unk13", FieldType.STRING),
        FieldDef("Question_Lang_Unk14", FieldType.STRING),
        FieldDef("Question_Lang_Unk15", FieldType.STRING),
        FieldDef("Question_Lang_Flags", FieldType.UINT),
    ]
)

# GMSurveySurveys - 11 fields
BUILTIN_SCHEMAS["GMSurveySurveys"] = SchemaDef(
    name="GMSurveySurveys",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Q_0", FieldType.INT),
        FieldDef("Q_1", FieldType.INT),
        FieldDef("Q_2", FieldType.INT),
        FieldDef("Q_3", FieldType.INT),
        FieldDef("Q_4", FieldType.INT),
        FieldDef("Q_5", FieldType.INT),
        FieldDef("Q_6", FieldType.INT),
        FieldDef("Q_7", FieldType.INT),
        FieldDef("Q_8", FieldType.INT),
        FieldDef("Q_9", FieldType.INT),
    ]
)

# GMTicketCategory - 18 fields
BUILTIN_SCHEMAS["GMTicketCategory"] = SchemaDef(
    name="GMTicketCategory",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Category_Lang_enUS", FieldType.STRING),
        FieldDef("Category_Lang_koKR", FieldType.STRING),
        FieldDef("Category_Lang_frFR", FieldType.STRING),
        FieldDef("Category_Lang_deDE", FieldType.STRING),
        FieldDef("Category_Lang_enCN", FieldType.STRING),
        FieldDef("Category_Lang_enTW", FieldType.STRING),
        FieldDef("Category_Lang_esES", FieldType.STRING),
        FieldDef("Category_Lang_esMX", FieldType.STRING),
        FieldDef("Category_Lang_ruRU", FieldType.STRING),
        FieldDef("Category_Lang_jaJP", FieldType.STRING),
        FieldDef("Category_Lang_ptPT", FieldType.STRING),
        FieldDef("Category_Lang_itIT", FieldType.STRING),
        FieldDef("Category_Lang_Unk12", FieldType.STRING),
        FieldDef("Category_Lang_Unk13", FieldType.STRING),
        FieldDef("Category_Lang_Unk14", FieldType.STRING),
        FieldDef("Category_Lang_Unk15", FieldType.STRING),
        FieldDef("Category_Lang_Flags", FieldType.UINT),
    ]
)

# GameObjectArtKit - 8 fields
BUILTIN_SCHEMAS["GameObjectArtKit"] = SchemaDef(
    name="GameObjectArtKit",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("TextureVariation_0", FieldType.STRING),
        FieldDef("TextureVariation_1", FieldType.STRING),
        FieldDef("TextureVariation_2", FieldType.STRING),
        FieldDef("AttachModel_0", FieldType.STRING),
        FieldDef("AttachModel_1", FieldType.STRING),
        FieldDef("AttachModel_2", FieldType.STRING),
        FieldDef("AttachModel_3", FieldType.STRING),
    ]
)

# GameObjectDisplayInfo - 19 fields
BUILTIN_SCHEMAS["GameObjectDisplayInfo"] = SchemaDef(
    name="GameObjectDisplayInfo",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ModelName", FieldType.STRING),
        FieldDef("Sound_0", FieldType.INT),
        FieldDef("Sound_1", FieldType.INT),
        FieldDef("Sound_2", FieldType.INT),
        FieldDef("Sound_3", FieldType.INT),
        FieldDef("Sound_4", FieldType.INT),
        FieldDef("Sound_5", FieldType.INT),
        FieldDef("Sound_6", FieldType.INT),
        FieldDef("Sound_7", FieldType.INT),
        FieldDef("Sound_8", FieldType.INT),
        FieldDef("Sound_9", FieldType.INT),
        FieldDef("GeoBoxMinX", FieldType.FLOAT),
        FieldDef("GeoBoxMinY", FieldType.FLOAT),
        FieldDef("GeoBoxMinZ", FieldType.FLOAT),
        FieldDef("GeoBoxMaxX", FieldType.FLOAT),
        FieldDef("GeoBoxMaxY", FieldType.FLOAT),
        FieldDef("GeoBoxMaxZ", FieldType.FLOAT),
        FieldDef("ObjectEffectPackageID", FieldType.INT),
    ]
)

# GameTables - 4 fields
BUILTIN_SCHEMAS["GameTables"] = SchemaDef(
    name="GameTables",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("NumRows", FieldType.INT),
        FieldDef("NumColumns", FieldType.INT),
    ]
)

# GameTips - 18 fields
BUILTIN_SCHEMAS["GameTips"] = SchemaDef(
    name="GameTips",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Text_Lang_enUS", FieldType.STRING),
        FieldDef("Text_Lang_koKR", FieldType.STRING),
        FieldDef("Text_Lang_frFR", FieldType.STRING),
        FieldDef("Text_Lang_deDE", FieldType.STRING),
        FieldDef("Text_Lang_enCN", FieldType.STRING),
        FieldDef("Text_Lang_enTW", FieldType.STRING),
        FieldDef("Text_Lang_esES", FieldType.STRING),
        FieldDef("Text_Lang_esMX", FieldType.STRING),
        FieldDef("Text_Lang_ruRU", FieldType.STRING),
        FieldDef("Text_Lang_jaJP", FieldType.STRING),
        FieldDef("Text_Lang_ptPT", FieldType.STRING),
        FieldDef("Text_Lang_itIT", FieldType.STRING),
        FieldDef("Text_Lang_Unk12", FieldType.STRING),
        FieldDef("Text_Lang_Unk13", FieldType.STRING),
        FieldDef("Text_Lang_Unk14", FieldType.STRING),
        FieldDef("Text_Lang_Unk15", FieldType.STRING),
        FieldDef("Text_Lang_Flags", FieldType.UINT),
    ]
)

# GemProperties - 5 fields
BUILTIN_SCHEMAS["GemProperties"] = SchemaDef(
    name="GemProperties",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Enchant_Id", FieldType.INT),
        FieldDef("Maxcount_Inv", FieldType.INT),
        FieldDef("Maxcount_Item", FieldType.INT),
        FieldDef("Type", FieldType.INT),
    ]
)

# GlyphProperties - 4 fields
BUILTIN_SCHEMAS["GlyphProperties"] = SchemaDef(
    name="GlyphProperties",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SpellID", FieldType.INT),
        FieldDef("GlyphSlotFlags", FieldType.INT),
        FieldDef("SpellIconID", FieldType.INT),
    ]
)

# GlyphSlot - 3 fields
BUILTIN_SCHEMAS["GlyphSlot"] = SchemaDef(
    name="GlyphSlot",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Type", FieldType.INT),
        FieldDef("Tooltip", FieldType.INT),
    ]
)

# GroundEffectDoodad - 3 fields
BUILTIN_SCHEMAS["GroundEffectDoodad"] = SchemaDef(
    name="GroundEffectDoodad",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Doodadpath", FieldType.STRING),
        FieldDef("Flags", FieldType.INT),
    ]
)

# GroundEffectTexture - 11 fields
BUILTIN_SCHEMAS["GroundEffectTexture"] = SchemaDef(
    name="GroundEffectTexture",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("DoodadId_0", FieldType.INT),
        FieldDef("DoodadId_1", FieldType.INT),
        FieldDef("DoodadId_2", FieldType.INT),
        FieldDef("DoodadId_3", FieldType.INT),
        FieldDef("DoodadWeight_0", FieldType.INT),
        FieldDef("DoodadWeight_1", FieldType.INT),
        FieldDef("DoodadWeight_2", FieldType.INT),
        FieldDef("DoodadWeight_3", FieldType.INT),
        FieldDef("Density", FieldType.INT),
        FieldDef("Sound", FieldType.INT),
    ]
)

# GtBarberShopCostBase - 2 fields
BUILTIN_SCHEMAS["GtBarberShopCostBase"] = SchemaDef(
    name="GtBarberShopCostBase",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# GtChanceToMeleeCrit - 2 fields
BUILTIN_SCHEMAS["GtChanceToMeleeCrit"] = SchemaDef(
    name="GtChanceToMeleeCrit",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# GtChanceToMeleeCritBase - 2 fields
BUILTIN_SCHEMAS["GtChanceToMeleeCritBase"] = SchemaDef(
    name="GtChanceToMeleeCritBase",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# GtChanceToSpellCrit - 2 fields
BUILTIN_SCHEMAS["GtChanceToSpellCrit"] = SchemaDef(
    name="GtChanceToSpellCrit",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# GtChanceToSpellCritBase - 2 fields
BUILTIN_SCHEMAS["GtChanceToSpellCritBase"] = SchemaDef(
    name="GtChanceToSpellCritBase",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# GtCombatRatings - 2 fields
BUILTIN_SCHEMAS["GtCombatRatings"] = SchemaDef(
    name="GtCombatRatings",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# GtNPCManaCostScaler - 2 fields
BUILTIN_SCHEMAS["GtNPCManaCostScaler"] = SchemaDef(
    name="GtNPCManaCostScaler",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# GtOCTClassCombatRatingScalar - 2 fields
BUILTIN_SCHEMAS["GtOCTClassCombatRatingScalar"] = SchemaDef(
    name="GtOCTClassCombatRatingScalar",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# GtOCTRegenHP - 2 fields
BUILTIN_SCHEMAS["GtOCTRegenHP"] = SchemaDef(
    name="GtOCTRegenHP",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# GtOCTRegenMP - 2 fields
BUILTIN_SCHEMAS["GtOCTRegenMP"] = SchemaDef(
    name="GtOCTRegenMP",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# GtRegenHPPerSpt - 2 fields
BUILTIN_SCHEMAS["GtRegenHPPerSpt"] = SchemaDef(
    name="GtRegenHPPerSpt",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# GtRegenMPPerSpt - 2 fields
BUILTIN_SCHEMAS["GtRegenMPPerSpt"] = SchemaDef(
    name="GtRegenMPPerSpt",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# GtSpellScaling - 2 fields
BUILTIN_SCHEMAS["GtSpellScaling"] = SchemaDef(
    name="GtSpellScaling",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# HelmetGeosetVisData - 8 fields
BUILTIN_SCHEMAS["HelmetGeosetVisData"] = SchemaDef(
    name="HelmetGeosetVisData",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("HideGeoset_0", FieldType.INT),
        FieldDef("HideGeoset_1", FieldType.INT),
        FieldDef("HideGeoset_2", FieldType.INT),
        FieldDef("HideGeoset_3", FieldType.INT),
        FieldDef("HideGeoset_4", FieldType.INT),
        FieldDef("HideGeoset_5", FieldType.INT),
        FieldDef("HideGeoset_6", FieldType.INT),
    ]
)

# HolidayDescriptions - 18 fields
BUILTIN_SCHEMAS["HolidayDescriptions"] = SchemaDef(
    name="HolidayDescriptions",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Description_Lang_enUS", FieldType.STRING),
        FieldDef("Description_Lang_koKR", FieldType.STRING),
        FieldDef("Description_Lang_frFR", FieldType.STRING),
        FieldDef("Description_Lang_deDE", FieldType.STRING),
        FieldDef("Description_Lang_enCN", FieldType.STRING),
        FieldDef("Description_Lang_enTW", FieldType.STRING),
        FieldDef("Description_Lang_esES", FieldType.STRING),
        FieldDef("Description_Lang_esMX", FieldType.STRING),
        FieldDef("Description_Lang_ruRU", FieldType.STRING),
        FieldDef("Description_Lang_jaJP", FieldType.STRING),
        FieldDef("Description_Lang_ptPT", FieldType.STRING),
        FieldDef("Description_Lang_itIT", FieldType.STRING),
        FieldDef("Description_Lang_Unk12", FieldType.STRING),
        FieldDef("Description_Lang_Unk13", FieldType.STRING),
        FieldDef("Description_Lang_Unk14", FieldType.STRING),
        FieldDef("Description_Lang_Unk15", FieldType.STRING),
        FieldDef("Description_Lang_Flags", FieldType.UINT),
    ]
)

# HolidayNames - 18 fields
BUILTIN_SCHEMAS["HolidayNames"] = SchemaDef(
    name="HolidayNames",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
    ]
)

# Holidays - 55 fields
BUILTIN_SCHEMAS["Holidays"] = SchemaDef(
    name="Holidays",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Duration_0", FieldType.INT),
        FieldDef("Duration_1", FieldType.INT),
        FieldDef("Duration_2", FieldType.INT),
        FieldDef("Duration_3", FieldType.INT),
        FieldDef("Duration_4", FieldType.INT),
        FieldDef("Duration_5", FieldType.INT),
        FieldDef("Duration_6", FieldType.INT),
        FieldDef("Duration_7", FieldType.INT),
        FieldDef("Duration_8", FieldType.INT),
        FieldDef("Duration_9", FieldType.INT),
        FieldDef("Date_0", FieldType.INT),
        FieldDef("Date_1", FieldType.INT),
        FieldDef("Date_2", FieldType.INT),
        FieldDef("Date_3", FieldType.INT),
        FieldDef("Date_4", FieldType.INT),
        FieldDef("Date_5", FieldType.INT),
        FieldDef("Date_6", FieldType.INT),
        FieldDef("Date_7", FieldType.INT),
        FieldDef("Date_8", FieldType.INT),
        FieldDef("Date_9", FieldType.INT),
        FieldDef("Date_10", FieldType.INT),
        FieldDef("Date_11", FieldType.INT),
        FieldDef("Date_12", FieldType.INT),
        FieldDef("Date_13", FieldType.INT),
        FieldDef("Date_14", FieldType.INT),
        FieldDef("Date_15", FieldType.INT),
        FieldDef("Date_16", FieldType.INT),
        FieldDef("Date_17", FieldType.INT),
        FieldDef("Date_18", FieldType.INT),
        FieldDef("Date_19", FieldType.INT),
        FieldDef("Date_20", FieldType.INT),
        FieldDef("Date_21", FieldType.INT),
        FieldDef("Date_22", FieldType.INT),
        FieldDef("Date_23", FieldType.INT),
        FieldDef("Date_24", FieldType.INT),
        FieldDef("Date_25", FieldType.INT),
        FieldDef("Region", FieldType.INT),
        FieldDef("Looping", FieldType.INT),
        FieldDef("CalendarFlags_0", FieldType.INT),
        FieldDef("CalendarFlags_1", FieldType.INT),
        FieldDef("CalendarFlags_2", FieldType.INT),
        FieldDef("CalendarFlags_3", FieldType.INT),
        FieldDef("CalendarFlags_4", FieldType.INT),
        FieldDef("CalendarFlags_5", FieldType.INT),
        FieldDef("CalendarFlags_6", FieldType.INT),
        FieldDef("CalendarFlags_7", FieldType.INT),
        FieldDef("CalendarFlags_8", FieldType.INT),
        FieldDef("CalendarFlags_9", FieldType.INT),
        FieldDef("HolidayNameID", FieldType.INT),
        FieldDef("HolidayDescriptionID", FieldType.INT),
        FieldDef("TextureFilename", FieldType.STRING),
        FieldDef("Priority", FieldType.INT),
        FieldDef("CalendarFilterType", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
    ]
)

# Item - 8 fields
BUILTIN_SCHEMAS["Item"] = SchemaDef(
    name="Item",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ClassID", FieldType.INT),
        FieldDef("SubclassID", FieldType.INT),
        FieldDef("Sound_Override_Subclassid", FieldType.INT),
        FieldDef("Material", FieldType.INT),
        FieldDef("DisplayInfoID", FieldType.INT),
        FieldDef("InventoryType", FieldType.INT),
        FieldDef("SheatheType", FieldType.INT),
    ]
)

# ItemArmorQuality - 9 fields
BUILTIN_SCHEMAS["ItemArmorQuality"] = SchemaDef(
    name="ItemArmorQuality",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Qualitymod_0", FieldType.FLOAT),
        FieldDef("Qualitymod_1", FieldType.FLOAT),
        FieldDef("Qualitymod_2", FieldType.FLOAT),
        FieldDef("Qualitymod_3", FieldType.FLOAT),
        FieldDef("Qualitymod_4", FieldType.FLOAT),
        FieldDef("Qualitymod_5", FieldType.FLOAT),
        FieldDef("Qualitymod_6", FieldType.FLOAT),
        FieldDef("ItemLevel", FieldType.INT),
    ]
)

# ItemArmorShield - 9 fields
BUILTIN_SCHEMAS["ItemArmorShield"] = SchemaDef(
    name="ItemArmorShield",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ItemLevel", FieldType.INT),
        FieldDef("Quality_0", FieldType.FLOAT),
        FieldDef("Quality_1", FieldType.FLOAT),
        FieldDef("Quality_2", FieldType.FLOAT),
        FieldDef("Quality_3", FieldType.FLOAT),
        FieldDef("Quality_4", FieldType.FLOAT),
        FieldDef("Quality_5", FieldType.FLOAT),
        FieldDef("Quality_6", FieldType.FLOAT),
    ]
)

# ItemArmorTotal - 6 fields
BUILTIN_SCHEMAS["ItemArmorTotal"] = SchemaDef(
    name="ItemArmorTotal",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ItemLevel", FieldType.INT),
        FieldDef("Cloth", FieldType.FLOAT),
        FieldDef("Leather", FieldType.FLOAT),
        FieldDef("Mail", FieldType.FLOAT),
        FieldDef("Plate", FieldType.FLOAT),
    ]
)

# ItemBagFamily - 18 fields
BUILTIN_SCHEMAS["ItemBagFamily"] = SchemaDef(
    name="ItemBagFamily",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
    ]
)

# ItemClass - 21 fields
BUILTIN_SCHEMAS["ItemClass"] = SchemaDef(
    name="ItemClass",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ClassID", FieldType.INT),
        FieldDef("SubclassMapID", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("ClassName_Lang_enUS", FieldType.STRING),
        FieldDef("ClassName_Lang_koKR", FieldType.STRING),
        FieldDef("ClassName_Lang_frFR", FieldType.STRING),
        FieldDef("ClassName_Lang_deDE", FieldType.STRING),
        FieldDef("ClassName_Lang_enCN", FieldType.STRING),
        FieldDef("ClassName_Lang_enTW", FieldType.STRING),
        FieldDef("ClassName_Lang_esES", FieldType.STRING),
        FieldDef("ClassName_Lang_esMX", FieldType.STRING),
        FieldDef("ClassName_Lang_ruRU", FieldType.STRING),
        FieldDef("ClassName_Lang_jaJP", FieldType.STRING),
        FieldDef("ClassName_Lang_ptPT", FieldType.STRING),
        FieldDef("ClassName_Lang_itIT", FieldType.STRING),
        FieldDef("ClassName_Lang_Unk12", FieldType.STRING),
        FieldDef("ClassName_Lang_Unk13", FieldType.STRING),
        FieldDef("ClassName_Lang_Unk14", FieldType.STRING),
        FieldDef("ClassName_Lang_Unk15", FieldType.STRING),
        FieldDef("ClassName_Lang_Flags", FieldType.UINT),
    ]
)

# ItemCondExtCosts - 4 fields
BUILTIN_SCHEMAS["ItemCondExtCosts"] = SchemaDef(
    name="ItemCondExtCosts",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Field01", FieldType.INT),
        FieldDef("ItemExtendedCost", FieldType.INT),
        FieldDef("Field03", FieldType.INT),
    ]
)

# ItemDamageAmmo - 9 fields
BUILTIN_SCHEMAS["ItemDamageAmmo"] = SchemaDef(
    name="ItemDamageAmmo",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Quality_0", FieldType.FLOAT),
        FieldDef("Quality_1", FieldType.FLOAT),
        FieldDef("Quality_2", FieldType.FLOAT),
        FieldDef("Quality_3", FieldType.FLOAT),
        FieldDef("Quality_4", FieldType.FLOAT),
        FieldDef("Quality_5", FieldType.FLOAT),
        FieldDef("Quality_6", FieldType.FLOAT),
        FieldDef("ItemLevel", FieldType.INT),
    ]
)

# ItemDamageOneHand - 9 fields
BUILTIN_SCHEMAS["ItemDamageOneHand"] = SchemaDef(
    name="ItemDamageOneHand",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Quality_0", FieldType.FLOAT),
        FieldDef("Quality_1", FieldType.FLOAT),
        FieldDef("Quality_2", FieldType.FLOAT),
        FieldDef("Quality_3", FieldType.FLOAT),
        FieldDef("Quality_4", FieldType.FLOAT),
        FieldDef("Quality_5", FieldType.FLOAT),
        FieldDef("Quality_6", FieldType.FLOAT),
        FieldDef("ItemLevel", FieldType.INT),
    ]
)

# ItemDamageOneHandCaster - 9 fields
BUILTIN_SCHEMAS["ItemDamageOneHandCaster"] = SchemaDef(
    name="ItemDamageOneHandCaster",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Quality_0", FieldType.FLOAT),
        FieldDef("Quality_1", FieldType.FLOAT),
        FieldDef("Quality_2", FieldType.FLOAT),
        FieldDef("Quality_3", FieldType.FLOAT),
        FieldDef("Quality_4", FieldType.FLOAT),
        FieldDef("Quality_5", FieldType.FLOAT),
        FieldDef("Quality_6", FieldType.FLOAT),
        FieldDef("ItemLevel", FieldType.INT),
    ]
)

# ItemDamageRanged - 9 fields
BUILTIN_SCHEMAS["ItemDamageRanged"] = SchemaDef(
    name="ItemDamageRanged",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Quality_0", FieldType.FLOAT),
        FieldDef("Quality_1", FieldType.FLOAT),
        FieldDef("Quality_2", FieldType.FLOAT),
        FieldDef("Quality_3", FieldType.FLOAT),
        FieldDef("Quality_4", FieldType.FLOAT),
        FieldDef("Quality_5", FieldType.FLOAT),
        FieldDef("Quality_6", FieldType.FLOAT),
        FieldDef("ItemLevel", FieldType.INT),
    ]
)

# ItemDamageThrown - 9 fields
BUILTIN_SCHEMAS["ItemDamageThrown"] = SchemaDef(
    name="ItemDamageThrown",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Quality_0", FieldType.FLOAT),
        FieldDef("Quality_1", FieldType.FLOAT),
        FieldDef("Quality_2", FieldType.FLOAT),
        FieldDef("Quality_3", FieldType.FLOAT),
        FieldDef("Quality_4", FieldType.FLOAT),
        FieldDef("Quality_5", FieldType.FLOAT),
        FieldDef("Quality_6", FieldType.FLOAT),
        FieldDef("ItemLevel", FieldType.INT),
    ]
)

# ItemDamageTwoHand - 9 fields
BUILTIN_SCHEMAS["ItemDamageTwoHand"] = SchemaDef(
    name="ItemDamageTwoHand",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Quality_0", FieldType.FLOAT),
        FieldDef("Quality_1", FieldType.FLOAT),
        FieldDef("Quality_2", FieldType.FLOAT),
        FieldDef("Quality_3", FieldType.FLOAT),
        FieldDef("Quality_4", FieldType.FLOAT),
        FieldDef("Quality_5", FieldType.FLOAT),
        FieldDef("Quality_6", FieldType.FLOAT),
        FieldDef("ItemLevel", FieldType.INT),
    ]
)

# ItemDamageTwoHandCaster - 9 fields
BUILTIN_SCHEMAS["ItemDamageTwoHandCaster"] = SchemaDef(
    name="ItemDamageTwoHandCaster",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Quality_0", FieldType.FLOAT),
        FieldDef("Quality_1", FieldType.FLOAT),
        FieldDef("Quality_2", FieldType.FLOAT),
        FieldDef("Quality_3", FieldType.FLOAT),
        FieldDef("Quality_4", FieldType.FLOAT),
        FieldDef("Quality_5", FieldType.FLOAT),
        FieldDef("Quality_6", FieldType.FLOAT),
        FieldDef("ItemLevel", FieldType.INT),
    ]
)

# ItemDamageWand - 9 fields
BUILTIN_SCHEMAS["ItemDamageWand"] = SchemaDef(
    name="ItemDamageWand",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Quality_0", FieldType.FLOAT),
        FieldDef("Quality_1", FieldType.FLOAT),
        FieldDef("Quality_2", FieldType.FLOAT),
        FieldDef("Quality_3", FieldType.FLOAT),
        FieldDef("Quality_4", FieldType.FLOAT),
        FieldDef("Quality_5", FieldType.FLOAT),
        FieldDef("Quality_6", FieldType.FLOAT),
        FieldDef("ItemLevel", FieldType.INT),
    ]
)

# ItemDisplayInfo - 25 fields
BUILTIN_SCHEMAS["ItemDisplayInfo"] = SchemaDef(
    name="ItemDisplayInfo",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ModelName_0", FieldType.STRING),
        FieldDef("ModelName_1", FieldType.STRING),
        FieldDef("ModelTexture_0", FieldType.STRING),
        FieldDef("ModelTexture_1", FieldType.STRING),
        FieldDef("InventoryIcon_0", FieldType.STRING),
        FieldDef("InventoryIcon_1", FieldType.STRING),
        FieldDef("GeosetGroup_0", FieldType.INT),
        FieldDef("GeosetGroup_1", FieldType.INT),
        FieldDef("GeosetGroup_2", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("SpellVisualID", FieldType.INT),
        FieldDef("GroupSoundIndex", FieldType.INT),
        FieldDef("HelmetGeosetVis_0", FieldType.INT),
        FieldDef("HelmetGeosetVis_1", FieldType.INT),
        FieldDef("Texture_0", FieldType.STRING),
        FieldDef("Texture_1", FieldType.STRING),
        FieldDef("Texture_2", FieldType.STRING),
        FieldDef("Texture_3", FieldType.STRING),
        FieldDef("Texture_4", FieldType.STRING),
        FieldDef("Texture_5", FieldType.STRING),
        FieldDef("Texture_6", FieldType.STRING),
        FieldDef("Texture_7", FieldType.STRING),
        FieldDef("ItemVisual", FieldType.INT),
        FieldDef("ParticleColorID", FieldType.INT),
    ]
)

# ItemExtendedCost - 16 fields
BUILTIN_SCHEMAS["ItemExtendedCost"] = SchemaDef(
    name="ItemExtendedCost",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("HonorPoints", FieldType.INT),
        FieldDef("ArenaPoints", FieldType.INT),
        FieldDef("ArenaBracket", FieldType.INT),
        FieldDef("ItemID_0", FieldType.INT),
        FieldDef("ItemID_1", FieldType.INT),
        FieldDef("ItemID_2", FieldType.INT),
        FieldDef("ItemID_3", FieldType.INT),
        FieldDef("ItemID_4", FieldType.INT),
        FieldDef("ItemCount_0", FieldType.INT),
        FieldDef("ItemCount_1", FieldType.INT),
        FieldDef("ItemCount_2", FieldType.INT),
        FieldDef("ItemCount_3", FieldType.INT),
        FieldDef("ItemCount_4", FieldType.INT),
        FieldDef("RequiredArenaRating", FieldType.INT),
        FieldDef("ItemPurchaseGroup", FieldType.INT),
    ]
)

# ItemGroupSounds - 5 fields
BUILTIN_SCHEMAS["ItemGroupSounds"] = SchemaDef(
    name="ItemGroupSounds",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Sound_0", FieldType.INT),
        FieldDef("Sound_1", FieldType.INT),
        FieldDef("Sound_2", FieldType.INT),
        FieldDef("Sound_3", FieldType.INT),
    ]
)

# ItemLimitCategory - 20 fields
BUILTIN_SCHEMAS["ItemLimitCategory"] = SchemaDef(
    name="ItemLimitCategory",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("Quantity", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
    ]
)

# ItemPetFood - 18 fields
BUILTIN_SCHEMAS["ItemPetFood"] = SchemaDef(
    name="ItemPetFood",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
    ]
)

# ItemPurchaseGroup - 26 fields
BUILTIN_SCHEMAS["ItemPurchaseGroup"] = SchemaDef(
    name="ItemPurchaseGroup",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ItemID_0", FieldType.INT),
        FieldDef("ItemID_1", FieldType.INT),
        FieldDef("ItemID_2", FieldType.INT),
        FieldDef("ItemID_3", FieldType.INT),
        FieldDef("ItemID_4", FieldType.INT),
        FieldDef("ItemID_5", FieldType.INT),
        FieldDef("ItemID_6", FieldType.INT),
        FieldDef("ItemID_7", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
    ]
)

# ItemRandomProperties - 24 fields
BUILTIN_SCHEMAS["ItemRandomProperties"] = SchemaDef(
    name="ItemRandomProperties",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("Enchantment_0", FieldType.INT),
        FieldDef("Enchantment_1", FieldType.INT),
        FieldDef("Enchantment_2", FieldType.INT),
        FieldDef("Enchantment_3", FieldType.INT),
        FieldDef("Enchantment_4", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
    ]
)

# ItemRandomSuffix - 29 fields
BUILTIN_SCHEMAS["ItemRandomSuffix"] = SchemaDef(
    name="ItemRandomSuffix",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("InternalName", FieldType.STRING),
        FieldDef("Enchantment_0", FieldType.INT),
        FieldDef("Enchantment_1", FieldType.INT),
        FieldDef("Enchantment_2", FieldType.INT),
        FieldDef("Enchantment_3", FieldType.INT),
        FieldDef("Enchantment_4", FieldType.INT),
        FieldDef("AllocationPct_0", FieldType.INT),
        FieldDef("AllocationPct_1", FieldType.INT),
        FieldDef("AllocationPct_2", FieldType.INT),
        FieldDef("AllocationPct_3", FieldType.INT),
        FieldDef("AllocationPct_4", FieldType.INT),
    ]
)

# ItemSet - 53 fields
BUILTIN_SCHEMAS["ItemSet"] = SchemaDef(
    name="ItemSet",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("ItemID_0", FieldType.INT),
        FieldDef("ItemID_1", FieldType.INT),
        FieldDef("ItemID_2", FieldType.INT),
        FieldDef("ItemID_3", FieldType.INT),
        FieldDef("ItemID_4", FieldType.INT),
        FieldDef("ItemID_5", FieldType.INT),
        FieldDef("ItemID_6", FieldType.INT),
        FieldDef("ItemID_7", FieldType.INT),
        FieldDef("ItemID_8", FieldType.INT),
        FieldDef("ItemID_9", FieldType.INT),
        FieldDef("ItemID_10", FieldType.INT),
        FieldDef("ItemID_11", FieldType.INT),
        FieldDef("ItemID_12", FieldType.INT),
        FieldDef("ItemID_13", FieldType.INT),
        FieldDef("ItemID_14", FieldType.INT),
        FieldDef("ItemID_15", FieldType.INT),
        FieldDef("ItemID_16", FieldType.INT),
        FieldDef("SetSpellID_0", FieldType.INT),
        FieldDef("SetSpellID_1", FieldType.INT),
        FieldDef("SetSpellID_2", FieldType.INT),
        FieldDef("SetSpellID_3", FieldType.INT),
        FieldDef("SetSpellID_4", FieldType.INT),
        FieldDef("SetSpellID_5", FieldType.INT),
        FieldDef("SetSpellID_6", FieldType.INT),
        FieldDef("SetSpellID_7", FieldType.INT),
        FieldDef("SetThreshold_0", FieldType.INT),
        FieldDef("SetThreshold_1", FieldType.INT),
        FieldDef("SetThreshold_2", FieldType.INT),
        FieldDef("SetThreshold_3", FieldType.INT),
        FieldDef("SetThreshold_4", FieldType.INT),
        FieldDef("SetThreshold_5", FieldType.INT),
        FieldDef("SetThreshold_6", FieldType.INT),
        FieldDef("SetThreshold_7", FieldType.INT),
        FieldDef("RequiredSkill", FieldType.INT),
        FieldDef("RequiredSkillRank", FieldType.INT),
    ]
)

# ItemSubClass - 45 fields
BUILTIN_SCHEMAS["ItemSubClass"] = SchemaDef(
    name="ItemSubClass",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ClassID", FieldType.INT),
        FieldDef("SubClassID", FieldType.INT),
        FieldDef("PrerequisiteProficiency", FieldType.INT),
        FieldDef("PostrequisiteProficiency", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("DisplayFlags", FieldType.INT),
        FieldDef("WeaponParrySeq", FieldType.INT),
        FieldDef("WeaponReadySeq", FieldType.INT),
        FieldDef("WeaponAttackSeq", FieldType.INT),
        FieldDef("WeaponSwingSize", FieldType.INT),
        FieldDef("DisplayName_Lang_enUS", FieldType.STRING),
        FieldDef("DisplayName_Lang_koKR", FieldType.STRING),
        FieldDef("DisplayName_Lang_frFR", FieldType.STRING),
        FieldDef("DisplayName_Lang_deDE", FieldType.STRING),
        FieldDef("DisplayName_Lang_enCN", FieldType.STRING),
        FieldDef("DisplayName_Lang_enTW", FieldType.STRING),
        FieldDef("DisplayName_Lang_esES", FieldType.STRING),
        FieldDef("DisplayName_Lang_esMX", FieldType.STRING),
        FieldDef("DisplayName_Lang_ruRU", FieldType.STRING),
        FieldDef("DisplayName_Lang_jaJP", FieldType.STRING),
        FieldDef("DisplayName_Lang_ptPT", FieldType.STRING),
        FieldDef("DisplayName_Lang_itIT", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk12", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk13", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk14", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk15", FieldType.STRING),
        FieldDef("DisplayName_Lang_Flags", FieldType.UINT),
        FieldDef("VerboseName_Lang_enUS", FieldType.STRING),
        FieldDef("VerboseName_Lang_koKR", FieldType.STRING),
        FieldDef("VerboseName_Lang_frFR", FieldType.STRING),
        FieldDef("VerboseName_Lang_deDE", FieldType.STRING),
        FieldDef("VerboseName_Lang_enCN", FieldType.STRING),
        FieldDef("VerboseName_Lang_enTW", FieldType.STRING),
        FieldDef("VerboseName_Lang_esES", FieldType.STRING),
        FieldDef("VerboseName_Lang_esMX", FieldType.STRING),
        FieldDef("VerboseName_Lang_ruRU", FieldType.STRING),
        FieldDef("VerboseName_Lang_jaJP", FieldType.STRING),
        FieldDef("VerboseName_Lang_ptPT", FieldType.STRING),
        FieldDef("VerboseName_Lang_itIT", FieldType.STRING),
        FieldDef("VerboseName_Lang_Unk12", FieldType.STRING),
        FieldDef("VerboseName_Lang_Unk13", FieldType.STRING),
        FieldDef("VerboseName_Lang_Unk14", FieldType.STRING),
        FieldDef("VerboseName_Lang_Unk15", FieldType.STRING),
        FieldDef("VerboseName_Lang_Flags", FieldType.UINT),
    ]
)

# ItemSubClassMask - 20 fields
BUILTIN_SCHEMAS["ItemSubClassMask"] = SchemaDef(
    name="ItemSubClassMask",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ClassID", FieldType.INT),
        FieldDef("Mask", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
    ]
)

# ItemVisualEffects - 2 fields
BUILTIN_SCHEMAS["ItemVisualEffects"] = SchemaDef(
    name="ItemVisualEffects",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Model", FieldType.STRING),
    ]
)

# ItemVisuals - 6 fields
BUILTIN_SCHEMAS["ItemVisuals"] = SchemaDef(
    name="ItemVisuals",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Slot_0", FieldType.INT),
        FieldDef("Slot_1", FieldType.INT),
        FieldDef("Slot_2", FieldType.INT),
        FieldDef("Slot_3", FieldType.INT),
        FieldDef("Slot_4", FieldType.INT),
    ]
)

# LanguageWords - 3 fields
BUILTIN_SCHEMAS["LanguageWords"] = SchemaDef(
    name="LanguageWords",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("LanguageID", FieldType.INT),
        FieldDef("Word", FieldType.STRING),
    ]
)

# Languages - 18 fields
BUILTIN_SCHEMAS["Languages"] = SchemaDef(
    name="Languages",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
    ]
)

# LfgDungeonExpansion - 8 fields
BUILTIN_SCHEMAS["LfgDungeonExpansion"] = SchemaDef(
    name="LfgDungeonExpansion",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Lfg_Id", FieldType.INT),
        FieldDef("Expansion_Level", FieldType.INT),
        FieldDef("Random_Id", FieldType.INT),
        FieldDef("Hard_Level_Min", FieldType.INT),
        FieldDef("Hard_Level_Max", FieldType.INT),
        FieldDef("Target_Level_Min", FieldType.INT),
        FieldDef("Target_Level_Max", FieldType.INT),
    ]
)

# LfgDungeonGroup - 21 fields
BUILTIN_SCHEMAS["LfgDungeonGroup"] = SchemaDef(
    name="LfgDungeonGroup",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("Order_Index", FieldType.INT),
        FieldDef("Parent_Group_Id", FieldType.INT),
        FieldDef("Typeid", FieldType.INT),
    ]
)

# LfgDungeons - 49 fields
BUILTIN_SCHEMAS["LfgDungeons"] = SchemaDef(
    name="LfgDungeons",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("MinLevel", FieldType.INT),
        FieldDef("MaxLevel", FieldType.INT),
        FieldDef("Target_Level", FieldType.INT),
        FieldDef("Target_Level_Min", FieldType.INT),
        FieldDef("Target_Level_Max", FieldType.INT),
        FieldDef("MapID", FieldType.INT),
        FieldDef("Difficulty", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("TypeID", FieldType.INT),
        FieldDef("Faction", FieldType.INT),
        FieldDef("TextureFilename", FieldType.STRING),
        FieldDef("ExpansionLevel", FieldType.INT),
        FieldDef("Order_Index", FieldType.INT),
        FieldDef("Group_Id", FieldType.INT),
        FieldDef("Description_Lang_enUS", FieldType.STRING),
        FieldDef("Description_Lang_koKR", FieldType.STRING),
        FieldDef("Description_Lang_frFR", FieldType.STRING),
        FieldDef("Description_Lang_deDE", FieldType.STRING),
        FieldDef("Description_Lang_enCN", FieldType.STRING),
        FieldDef("Description_Lang_enTW", FieldType.STRING),
        FieldDef("Description_Lang_esES", FieldType.STRING),
        FieldDef("Description_Lang_esMX", FieldType.STRING),
        FieldDef("Description_Lang_ruRU", FieldType.STRING),
        FieldDef("Description_Lang_jaJP", FieldType.STRING),
        FieldDef("Description_Lang_ptPT", FieldType.STRING),
        FieldDef("Description_Lang_itIT", FieldType.STRING),
        FieldDef("Description_Lang_Unk12", FieldType.STRING),
        FieldDef("Description_Lang_Unk13", FieldType.STRING),
        FieldDef("Description_Lang_Unk14", FieldType.STRING),
        FieldDef("Description_Lang_Unk15", FieldType.STRING),
        FieldDef("Description_Lang_Flags", FieldType.UINT),
    ]
)

# Light - 15 fields
BUILTIN_SCHEMAS["Light"] = SchemaDef(
    name="Light",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ContinentID", FieldType.INT),
        FieldDef("X", FieldType.FLOAT),
        FieldDef("Y", FieldType.FLOAT),
        FieldDef("Z", FieldType.FLOAT),
        FieldDef("FalloffStart", FieldType.FLOAT),
        FieldDef("FalloffEnd", FieldType.FLOAT),
        FieldDef("LightParamsID_0", FieldType.INT),
        FieldDef("LightParamsID_1", FieldType.INT),
        FieldDef("LightParamsID_2", FieldType.INT),
        FieldDef("LightParamsID_3", FieldType.INT),
        FieldDef("LightParamsID_4", FieldType.INT),
        FieldDef("LightParamsID_5", FieldType.INT),
        FieldDef("LightParamsID_6", FieldType.INT),
        FieldDef("LightParamsID_7", FieldType.INT),
    ]
)

# LightParams - 9 fields
BUILTIN_SCHEMAS["LightParams"] = SchemaDef(
    name="LightParams",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("HighlightSky", FieldType.INT),
        FieldDef("LightSkyboxID", FieldType.INT),
        FieldDef("CloudTypeID", FieldType.INT),
        FieldDef("Glow", FieldType.FLOAT),
        FieldDef("WaterShallowAlpha", FieldType.FLOAT),
        FieldDef("WaterDeepAlpha", FieldType.FLOAT),
        FieldDef("OceanShallowAlpha", FieldType.FLOAT),
        FieldDef("OceanDeepAlpha", FieldType.FLOAT),
    ]
)

# LightSkybox - 3 fields
BUILTIN_SCHEMAS["LightSkybox"] = SchemaDef(
    name="LightSkybox",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("Flags", FieldType.INT),
    ]
)

# LightfloatBand - 34 fields
BUILTIN_SCHEMAS["LightfloatBand"] = SchemaDef(
    name="LightfloatBand",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Num", FieldType.INT),
        FieldDef("Time_0", FieldType.INT),
        FieldDef("Time_1", FieldType.INT),
        FieldDef("Time_2", FieldType.INT),
        FieldDef("Time_3", FieldType.INT),
        FieldDef("Time_4", FieldType.INT),
        FieldDef("Time_5", FieldType.INT),
        FieldDef("Time_6", FieldType.INT),
        FieldDef("Time_7", FieldType.INT),
        FieldDef("Time_8", FieldType.INT),
        FieldDef("Time_9", FieldType.INT),
        FieldDef("Time_10", FieldType.INT),
        FieldDef("Time_11", FieldType.INT),
        FieldDef("Time_12", FieldType.INT),
        FieldDef("Time_13", FieldType.INT),
        FieldDef("Time_14", FieldType.INT),
        FieldDef("Time_15", FieldType.INT),
        FieldDef("Data_0", FieldType.FLOAT),
        FieldDef("Data_1", FieldType.FLOAT),
        FieldDef("Data_2", FieldType.FLOAT),
        FieldDef("Data_3", FieldType.FLOAT),
        FieldDef("Data_4", FieldType.FLOAT),
        FieldDef("Data_5", FieldType.FLOAT),
        FieldDef("Data_6", FieldType.FLOAT),
        FieldDef("Data_7", FieldType.FLOAT),
        FieldDef("Data_8", FieldType.FLOAT),
        FieldDef("Data_9", FieldType.FLOAT),
        FieldDef("Data_10", FieldType.FLOAT),
        FieldDef("Data_11", FieldType.FLOAT),
        FieldDef("Data_12", FieldType.FLOAT),
        FieldDef("Data_13", FieldType.FLOAT),
        FieldDef("Data_14", FieldType.FLOAT),
        FieldDef("Data_15", FieldType.FLOAT),
    ]
)

# LightintBand - 34 fields
BUILTIN_SCHEMAS["LightintBand"] = SchemaDef(
    name="LightintBand",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Num", FieldType.INT),
        FieldDef("Time_0", FieldType.INT),
        FieldDef("Time_1", FieldType.INT),
        FieldDef("Time_2", FieldType.INT),
        FieldDef("Time_3", FieldType.INT),
        FieldDef("Time_4", FieldType.INT),
        FieldDef("Time_5", FieldType.INT),
        FieldDef("Time_6", FieldType.INT),
        FieldDef("Time_7", FieldType.INT),
        FieldDef("Time_8", FieldType.INT),
        FieldDef("Time_9", FieldType.INT),
        FieldDef("Time_10", FieldType.INT),
        FieldDef("Time_11", FieldType.INT),
        FieldDef("Time_12", FieldType.INT),
        FieldDef("Time_13", FieldType.INT),
        FieldDef("Time_14", FieldType.INT),
        FieldDef("Time_15", FieldType.INT),
        FieldDef("Data_0", FieldType.INT),
        FieldDef("Data_1", FieldType.INT),
        FieldDef("Data_2", FieldType.INT),
        FieldDef("Data_3", FieldType.INT),
        FieldDef("Data_4", FieldType.INT),
        FieldDef("Data_5", FieldType.INT),
        FieldDef("Data_6", FieldType.INT),
        FieldDef("Data_7", FieldType.INT),
        FieldDef("Data_8", FieldType.INT),
        FieldDef("Data_9", FieldType.INT),
        FieldDef("Data_10", FieldType.INT),
        FieldDef("Data_11", FieldType.INT),
        FieldDef("Data_12", FieldType.INT),
        FieldDef("Data_13", FieldType.INT),
        FieldDef("Data_14", FieldType.INT),
        FieldDef("Data_15", FieldType.INT),
    ]
)

# LiquidMaterial - 3 fields
BUILTIN_SCHEMAS["LiquidMaterial"] = SchemaDef(
    name="LiquidMaterial",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("LVF", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
    ]
)

# LiquidType - 45 fields
BUILTIN_SCHEMAS["LiquidType"] = SchemaDef(
    name="LiquidType",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("Flags", FieldType.INT),
        FieldDef("Type", FieldType.INT),
        FieldDef("SoundID", FieldType.INT),
        FieldDef("SpellID", FieldType.INT),
        FieldDef("MaxDarkenDepth", FieldType.FLOAT),
        FieldDef("FogDarkenintensity", FieldType.FLOAT),
        FieldDef("AmbDarkenintensity", FieldType.FLOAT),
        FieldDef("DirDarkenintensity", FieldType.FLOAT),
        FieldDef("LightID", FieldType.INT),
        FieldDef("ParticleScale", FieldType.FLOAT),
        FieldDef("ParticleMovement", FieldType.INT),
        FieldDef("ParticleTexSlots", FieldType.INT),
        FieldDef("MaterialID", FieldType.INT),
        FieldDef("Texture_0", FieldType.STRING),
        FieldDef("Texture_1", FieldType.STRING),
        FieldDef("Texture_2", FieldType.STRING),
        FieldDef("Texture_3", FieldType.STRING),
        FieldDef("Texture_4", FieldType.STRING),
        FieldDef("Texture_5", FieldType.STRING),
        FieldDef("Color_0", FieldType.INT),
        FieldDef("Color_1", FieldType.INT),
        FieldDef("Float_0", FieldType.FLOAT),
        FieldDef("Float_1", FieldType.FLOAT),
        FieldDef("Float_2", FieldType.FLOAT),
        FieldDef("Float_3", FieldType.FLOAT),
        FieldDef("Float_4", FieldType.FLOAT),
        FieldDef("Float_5", FieldType.FLOAT),
        FieldDef("Float_6", FieldType.FLOAT),
        FieldDef("Float_7", FieldType.FLOAT),
        FieldDef("Float_8", FieldType.FLOAT),
        FieldDef("Float_9", FieldType.FLOAT),
        FieldDef("Float_10", FieldType.FLOAT),
        FieldDef("Float_11", FieldType.FLOAT),
        FieldDef("Float_12", FieldType.FLOAT),
        FieldDef("Float_13", FieldType.FLOAT),
        FieldDef("Float_14", FieldType.FLOAT),
        FieldDef("Float_15", FieldType.FLOAT),
        FieldDef("Float_16", FieldType.FLOAT),
        FieldDef("Float_17", FieldType.FLOAT),
        FieldDef("Int_0", FieldType.INT),
        FieldDef("Int_1", FieldType.INT),
        FieldDef("Int_2", FieldType.INT),
        FieldDef("Int_3", FieldType.INT),
    ]
)

# LoadingScreenTaxiSplines - 19 fields
BUILTIN_SCHEMAS["LoadingScreenTaxiSplines"] = SchemaDef(
    name="LoadingScreenTaxiSplines",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("PathID", FieldType.INT),
        FieldDef("Locx_0", FieldType.FLOAT),
        FieldDef("Locx_1", FieldType.FLOAT),
        FieldDef("Locx_2", FieldType.FLOAT),
        FieldDef("Locx_3", FieldType.FLOAT),
        FieldDef("Locx_4", FieldType.FLOAT),
        FieldDef("Locx_5", FieldType.FLOAT),
        FieldDef("Locx_6", FieldType.FLOAT),
        FieldDef("Locx_7", FieldType.FLOAT),
        FieldDef("Locy_0", FieldType.FLOAT),
        FieldDef("Locy_1", FieldType.FLOAT),
        FieldDef("Locy_2", FieldType.FLOAT),
        FieldDef("Locy_3", FieldType.FLOAT),
        FieldDef("Locy_4", FieldType.FLOAT),
        FieldDef("Locy_5", FieldType.FLOAT),
        FieldDef("Locy_6", FieldType.FLOAT),
        FieldDef("Locy_7", FieldType.FLOAT),
        FieldDef("LegIndex", FieldType.INT),
    ]
)

# LoadingScreens - 4 fields
BUILTIN_SCHEMAS["LoadingScreens"] = SchemaDef(
    name="LoadingScreens",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("FileName", FieldType.STRING),
        FieldDef("HasWideScreen", FieldType.INT),
    ]
)

# Lock - 33 fields
BUILTIN_SCHEMAS["Lock"] = SchemaDef(
    name="Lock",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Type_0", FieldType.INT),
        FieldDef("Type_1", FieldType.INT),
        FieldDef("Type_2", FieldType.INT),
        FieldDef("Type_3", FieldType.INT),
        FieldDef("Type_4", FieldType.INT),
        FieldDef("Type_5", FieldType.INT),
        FieldDef("Type_6", FieldType.INT),
        FieldDef("Type_7", FieldType.INT),
        FieldDef("Index_0", FieldType.INT),
        FieldDef("Index_1", FieldType.INT),
        FieldDef("Index_2", FieldType.INT),
        FieldDef("Index_3", FieldType.INT),
        FieldDef("Index_4", FieldType.INT),
        FieldDef("Index_5", FieldType.INT),
        FieldDef("Index_6", FieldType.INT),
        FieldDef("Index_7", FieldType.INT),
        FieldDef("Skill_0", FieldType.INT),
        FieldDef("Skill_1", FieldType.INT),
        FieldDef("Skill_2", FieldType.INT),
        FieldDef("Skill_3", FieldType.INT),
        FieldDef("Skill_4", FieldType.INT),
        FieldDef("Skill_5", FieldType.INT),
        FieldDef("Skill_6", FieldType.INT),
        FieldDef("Skill_7", FieldType.INT),
        FieldDef("Action_0", FieldType.INT),
        FieldDef("Action_1", FieldType.INT),
        FieldDef("Action_2", FieldType.INT),
        FieldDef("Action_3", FieldType.INT),
        FieldDef("Action_4", FieldType.INT),
        FieldDef("Action_5", FieldType.INT),
        FieldDef("Action_6", FieldType.INT),
        FieldDef("Action_7", FieldType.INT),
    ]
)

# LockType - 53 fields
BUILTIN_SCHEMAS["LockType"] = SchemaDef(
    name="LockType",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("ResourceName_Lang_enUS", FieldType.STRING),
        FieldDef("ResourceName_Lang_koKR", FieldType.STRING),
        FieldDef("ResourceName_Lang_frFR", FieldType.STRING),
        FieldDef("ResourceName_Lang_deDE", FieldType.STRING),
        FieldDef("ResourceName_Lang_enCN", FieldType.STRING),
        FieldDef("ResourceName_Lang_enTW", FieldType.STRING),
        FieldDef("ResourceName_Lang_esES", FieldType.STRING),
        FieldDef("ResourceName_Lang_esMX", FieldType.STRING),
        FieldDef("ResourceName_Lang_ruRU", FieldType.STRING),
        FieldDef("ResourceName_Lang_jaJP", FieldType.STRING),
        FieldDef("ResourceName_Lang_ptPT", FieldType.STRING),
        FieldDef("ResourceName_Lang_itIT", FieldType.STRING),
        FieldDef("ResourceName_Lang_Unk12", FieldType.STRING),
        FieldDef("ResourceName_Lang_Unk13", FieldType.STRING),
        FieldDef("ResourceName_Lang_Unk14", FieldType.STRING),
        FieldDef("ResourceName_Lang_Unk15", FieldType.STRING),
        FieldDef("ResourceName_Lang_Flags", FieldType.UINT),
        FieldDef("Verb_Lang_enUS", FieldType.STRING),
        FieldDef("Verb_Lang_koKR", FieldType.STRING),
        FieldDef("Verb_Lang_frFR", FieldType.STRING),
        FieldDef("Verb_Lang_deDE", FieldType.STRING),
        FieldDef("Verb_Lang_enCN", FieldType.STRING),
        FieldDef("Verb_Lang_enTW", FieldType.STRING),
        FieldDef("Verb_Lang_esES", FieldType.STRING),
        FieldDef("Verb_Lang_esMX", FieldType.STRING),
        FieldDef("Verb_Lang_ruRU", FieldType.STRING),
        FieldDef("Verb_Lang_jaJP", FieldType.STRING),
        FieldDef("Verb_Lang_ptPT", FieldType.STRING),
        FieldDef("Verb_Lang_itIT", FieldType.STRING),
        FieldDef("Verb_Lang_Unk12", FieldType.STRING),
        FieldDef("Verb_Lang_Unk13", FieldType.STRING),
        FieldDef("Verb_Lang_Unk14", FieldType.STRING),
        FieldDef("Verb_Lang_Unk15", FieldType.STRING),
        FieldDef("Verb_Lang_Flags", FieldType.UINT),
        FieldDef("CursorName", FieldType.STRING),
    ]
)

# MailTemplate - 35 fields
BUILTIN_SCHEMAS["MailTemplate"] = SchemaDef(
    name="MailTemplate",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Subject_Lang_enUS", FieldType.STRING),
        FieldDef("Subject_Lang_koKR", FieldType.STRING),
        FieldDef("Subject_Lang_frFR", FieldType.STRING),
        FieldDef("Subject_Lang_deDE", FieldType.STRING),
        FieldDef("Subject_Lang_enCN", FieldType.STRING),
        FieldDef("Subject_Lang_enTW", FieldType.STRING),
        FieldDef("Subject_Lang_esES", FieldType.STRING),
        FieldDef("Subject_Lang_esMX", FieldType.STRING),
        FieldDef("Subject_Lang_ruRU", FieldType.STRING),
        FieldDef("Subject_Lang_jaJP", FieldType.STRING),
        FieldDef("Subject_Lang_ptPT", FieldType.STRING),
        FieldDef("Subject_Lang_itIT", FieldType.STRING),
        FieldDef("Subject_Lang_Unk12", FieldType.STRING),
        FieldDef("Subject_Lang_Unk13", FieldType.STRING),
        FieldDef("Subject_Lang_Unk14", FieldType.STRING),
        FieldDef("Subject_Lang_Unk15", FieldType.STRING),
        FieldDef("Subject_Lang_Flags", FieldType.UINT),
        FieldDef("Body_Lang_enUS", FieldType.STRING),
        FieldDef("Body_Lang_koKR", FieldType.STRING),
        FieldDef("Body_Lang_frFR", FieldType.STRING),
        FieldDef("Body_Lang_deDE", FieldType.STRING),
        FieldDef("Body_Lang_enCN", FieldType.STRING),
        FieldDef("Body_Lang_enTW", FieldType.STRING),
        FieldDef("Body_Lang_esES", FieldType.STRING),
        FieldDef("Body_Lang_esMX", FieldType.STRING),
        FieldDef("Body_Lang_ruRU", FieldType.STRING),
        FieldDef("Body_Lang_jaJP", FieldType.STRING),
        FieldDef("Body_Lang_ptPT", FieldType.STRING),
        FieldDef("Body_Lang_itIT", FieldType.STRING),
        FieldDef("Body_Lang_Unk12", FieldType.STRING),
        FieldDef("Body_Lang_Unk13", FieldType.STRING),
        FieldDef("Body_Lang_Unk14", FieldType.STRING),
        FieldDef("Body_Lang_Unk15", FieldType.STRING),
        FieldDef("Body_Lang_Flags", FieldType.UINT),
    ]
)

# Map - 66 fields
BUILTIN_SCHEMAS["Map"] = SchemaDef(
    name="Map",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Directory", FieldType.STRING),
        FieldDef("InstanceType", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("PVP", FieldType.INT),
        FieldDef("MapName_Lang_enUS", FieldType.STRING),
        FieldDef("MapName_Lang_koKR", FieldType.STRING),
        FieldDef("MapName_Lang_frFR", FieldType.STRING),
        FieldDef("MapName_Lang_deDE", FieldType.STRING),
        FieldDef("MapName_Lang_enCN", FieldType.STRING),
        FieldDef("MapName_Lang_enTW", FieldType.STRING),
        FieldDef("MapName_Lang_esES", FieldType.STRING),
        FieldDef("MapName_Lang_esMX", FieldType.STRING),
        FieldDef("MapName_Lang_ruRU", FieldType.STRING),
        FieldDef("MapName_Lang_jaJP", FieldType.STRING),
        FieldDef("MapName_Lang_ptPT", FieldType.STRING),
        FieldDef("MapName_Lang_itIT", FieldType.STRING),
        FieldDef("MapName_Lang_Unk12", FieldType.STRING),
        FieldDef("MapName_Lang_Unk13", FieldType.STRING),
        FieldDef("MapName_Lang_Unk14", FieldType.STRING),
        FieldDef("MapName_Lang_Unk15", FieldType.STRING),
        FieldDef("MapName_Lang_Flags", FieldType.UINT),
        FieldDef("AreaTableID", FieldType.INT),
        FieldDef("MapDescription0_Lang_enUS", FieldType.STRING),
        FieldDef("MapDescription0_Lang_koKR", FieldType.STRING),
        FieldDef("MapDescription0_Lang_frFR", FieldType.STRING),
        FieldDef("MapDescription0_Lang_deDE", FieldType.STRING),
        FieldDef("MapDescription0_Lang_enCN", FieldType.STRING),
        FieldDef("MapDescription0_Lang_enTW", FieldType.STRING),
        FieldDef("MapDescription0_Lang_esES", FieldType.STRING),
        FieldDef("MapDescription0_Lang_esMX", FieldType.STRING),
        FieldDef("MapDescription0_Lang_ruRU", FieldType.STRING),
        FieldDef("MapDescription0_Lang_jaJP", FieldType.STRING),
        FieldDef("MapDescription0_Lang_ptPT", FieldType.STRING),
        FieldDef("MapDescription0_Lang_itIT", FieldType.STRING),
        FieldDef("MapDescription0_Lang_Unk12", FieldType.STRING),
        FieldDef("MapDescription0_Lang_Unk13", FieldType.STRING),
        FieldDef("MapDescription0_Lang_Unk14", FieldType.STRING),
        FieldDef("MapDescription0_Lang_Unk15", FieldType.STRING),
        FieldDef("MapDescription0_Lang_Flags", FieldType.UINT),
        FieldDef("MapDescription1_Lang_enUS", FieldType.STRING),
        FieldDef("MapDescription1_Lang_koKR", FieldType.STRING),
        FieldDef("MapDescription1_Lang_frFR", FieldType.STRING),
        FieldDef("MapDescription1_Lang_deDE", FieldType.STRING),
        FieldDef("MapDescription1_Lang_enCN", FieldType.STRING),
        FieldDef("MapDescription1_Lang_enTW", FieldType.STRING),
        FieldDef("MapDescription1_Lang_esES", FieldType.STRING),
        FieldDef("MapDescription1_Lang_esMX", FieldType.STRING),
        FieldDef("MapDescription1_Lang_ruRU", FieldType.STRING),
        FieldDef("MapDescription1_Lang_jaJP", FieldType.STRING),
        FieldDef("MapDescription1_Lang_ptPT", FieldType.STRING),
        FieldDef("MapDescription1_Lang_itIT", FieldType.STRING),
        FieldDef("MapDescription1_Lang_Unk12", FieldType.STRING),
        FieldDef("MapDescription1_Lang_Unk13", FieldType.STRING),
        FieldDef("MapDescription1_Lang_Unk14", FieldType.STRING),
        FieldDef("MapDescription1_Lang_Unk15", FieldType.STRING),
        FieldDef("MapDescription1_Lang_Flags", FieldType.UINT),
        FieldDef("LoadingScreenID", FieldType.INT),
        FieldDef("MinimapIconScale", FieldType.FLOAT),
        FieldDef("CorpseMapID", FieldType.INT),
        FieldDef("CorpseX", FieldType.FLOAT),
        FieldDef("CorpseY", FieldType.FLOAT),
        FieldDef("TimeOfDayOverride", FieldType.INT),
        FieldDef("ExpansionID", FieldType.INT),
        FieldDef("RaidOffset", FieldType.INT),
        FieldDef("MaxPlayers", FieldType.INT),
    ]
)

# MapDifficulty - 23 fields
BUILTIN_SCHEMAS["MapDifficulty"] = SchemaDef(
    name="MapDifficulty",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MapID", FieldType.INT),
        FieldDef("Difficulty", FieldType.INT),
        FieldDef("Message_Lang_enUS", FieldType.STRING),
        FieldDef("Message_Lang_koKR", FieldType.STRING),
        FieldDef("Message_Lang_frFR", FieldType.STRING),
        FieldDef("Message_Lang_deDE", FieldType.STRING),
        FieldDef("Message_Lang_enCN", FieldType.STRING),
        FieldDef("Message_Lang_enTW", FieldType.STRING),
        FieldDef("Message_Lang_esES", FieldType.STRING),
        FieldDef("Message_Lang_esMX", FieldType.STRING),
        FieldDef("Message_Lang_ruRU", FieldType.STRING),
        FieldDef("Message_Lang_jaJP", FieldType.STRING),
        FieldDef("Message_Lang_ptPT", FieldType.STRING),
        FieldDef("Message_Lang_itIT", FieldType.STRING),
        FieldDef("Message_Lang_Unk12", FieldType.STRING),
        FieldDef("Message_Lang_Unk13", FieldType.STRING),
        FieldDef("Message_Lang_Unk14", FieldType.STRING),
        FieldDef("Message_Lang_Unk15", FieldType.STRING),
        FieldDef("Message_Lang_Flags", FieldType.UINT),
        FieldDef("RaidDuration", FieldType.INT),
        FieldDef("MaxPlayers", FieldType.INT),
        FieldDef("Difficultystring", FieldType.STRING),
    ]
)

# Material - 5 fields
BUILTIN_SCHEMAS["Material"] = SchemaDef(
    name="Material",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("FoleySoundID", FieldType.INT),
        FieldDef("SheatheSoundID", FieldType.INT),
        FieldDef("UnsheatheSoundID", FieldType.INT),
    ]
)

# Movie - 3 fields
BUILTIN_SCHEMAS["Movie"] = SchemaDef(
    name="Movie",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Filename", FieldType.STRING),
        FieldDef("Volume", FieldType.INT),
    ]
)

# MovieFileData - 2 fields
BUILTIN_SCHEMAS["MovieFileData"] = SchemaDef(
    name="MovieFileData",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Resolution", FieldType.INT),
    ]
)

# MovieVariation - 3 fields
BUILTIN_SCHEMAS["MovieVariation"] = SchemaDef(
    name="MovieVariation",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MovieID", FieldType.INT),
        FieldDef("FileDataID", FieldType.INT),
    ]
)

# NPCSounds - 5 fields
BUILTIN_SCHEMAS["NPCSounds"] = SchemaDef(
    name="NPCSounds",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SoundID_0", FieldType.INT),
        FieldDef("SoundID_1", FieldType.INT),
        FieldDef("SoundID_2", FieldType.INT),
        FieldDef("SoundID_3", FieldType.INT),
    ]
)

# NameGen - 4 fields
BUILTIN_SCHEMAS["NameGen"] = SchemaDef(
    name="NameGen",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("RaceID", FieldType.INT),
        FieldDef("Sex", FieldType.INT),
    ]
)

# NamesProfanity - 3 fields
BUILTIN_SCHEMAS["NamesProfanity"] = SchemaDef(
    name="NamesProfanity",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("Language", FieldType.INT),
    ]
)

# NamesReserved - 3 fields
BUILTIN_SCHEMAS["NamesReserved"] = SchemaDef(
    name="NamesReserved",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("Language", FieldType.INT),
    ]
)

# ObjectEffect - 12 fields
BUILTIN_SCHEMAS["ObjectEffect"] = SchemaDef(
    name="ObjectEffect",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("ObjectEffectGroupID", FieldType.INT),
        FieldDef("TriggerType", FieldType.INT),
        FieldDef("EventType", FieldType.INT),
        FieldDef("EffectRecType", FieldType.INT),
        FieldDef("EffectRecID", FieldType.INT),
        FieldDef("Attachment", FieldType.INT),
        FieldDef("OffsetX", FieldType.FLOAT),
        FieldDef("OffsetY", FieldType.FLOAT),
        FieldDef("OffsetZ", FieldType.FLOAT),
        FieldDef("ObjectEffectModifierID", FieldType.INT),
    ]
)

# ObjectEffectGroup - 2 fields
BUILTIN_SCHEMAS["ObjectEffectGroup"] = SchemaDef(
    name="ObjectEffectGroup",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
    ]
)

# ObjectEffectModifier - 8 fields
BUILTIN_SCHEMAS["ObjectEffectModifier"] = SchemaDef(
    name="ObjectEffectModifier",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("InputType", FieldType.INT),
        FieldDef("MapType", FieldType.INT),
        FieldDef("OutputType", FieldType.INT),
        FieldDef("Param_0", FieldType.FLOAT),
        FieldDef("Param_1", FieldType.FLOAT),
        FieldDef("Param_2", FieldType.FLOAT),
        FieldDef("Param_3", FieldType.FLOAT),
    ]
)

# ObjectEffectPackage - 2 fields
BUILTIN_SCHEMAS["ObjectEffectPackage"] = SchemaDef(
    name="ObjectEffectPackage",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
    ]
)

# ObjectEffectPackageElem - 4 fields
BUILTIN_SCHEMAS["ObjectEffectPackageElem"] = SchemaDef(
    name="ObjectEffectPackageElem",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ObjectEffectPackageID", FieldType.INT),
        FieldDef("ObjectEffectGroupID", FieldType.INT),
        FieldDef("StateType", FieldType.INT),
    ]
)

# OverrideSpellData - 12 fields
BUILTIN_SCHEMAS["OverrideSpellData"] = SchemaDef(
    name="OverrideSpellData",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Spells_0", FieldType.INT),
        FieldDef("Spells_1", FieldType.INT),
        FieldDef("Spells_2", FieldType.INT),
        FieldDef("Spells_3", FieldType.INT),
        FieldDef("Spells_4", FieldType.INT),
        FieldDef("Spells_5", FieldType.INT),
        FieldDef("Spells_6", FieldType.INT),
        FieldDef("Spells_7", FieldType.INT),
        FieldDef("Spells_8", FieldType.INT),
        FieldDef("Spells_9", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
    ]
)

# Package - 20 fields
BUILTIN_SCHEMAS["Package"] = SchemaDef(
    name="Package",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Icon", FieldType.STRING),
        FieldDef("Cost", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
    ]
)

# PageTextMaterial - 2 fields
BUILTIN_SCHEMAS["PageTextMaterial"] = SchemaDef(
    name="PageTextMaterial",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
    ]
)

# PaperDollItemFrame - 4 fields
BUILTIN_SCHEMAS["PaperDollItemFrame"] = SchemaDef(
    name="PaperDollItemFrame",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ItemButtonName", FieldType.STRING),
        FieldDef("SlotIcon", FieldType.STRING),
        FieldDef("SlotNumber", FieldType.INT),
    ]
)

# ParticleColor - 10 fields
BUILTIN_SCHEMAS["ParticleColor"] = SchemaDef(
    name="ParticleColor",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Start_0", FieldType.INT),
        FieldDef("Start_1", FieldType.INT),
        FieldDef("Start_2", FieldType.INT),
        FieldDef("Mid_0", FieldType.INT),
        FieldDef("Mid_1", FieldType.INT),
        FieldDef("Mid_2", FieldType.INT),
        FieldDef("End_0", FieldType.INT),
        FieldDef("End_1", FieldType.INT),
        FieldDef("End_2", FieldType.INT),
    ]
)

# PetPersonality - 24 fields
BUILTIN_SCHEMAS["PetPersonality"] = SchemaDef(
    name="PetPersonality",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("HappinessThreshold_0", FieldType.INT),
        FieldDef("HappinessThreshold_1", FieldType.INT),
        FieldDef("HappinessThreshold_2", FieldType.INT),
        FieldDef("HappinessDamage_0", FieldType.FLOAT),
        FieldDef("HappinessDamage_1", FieldType.FLOAT),
        FieldDef("HappinessDamage_2", FieldType.FLOAT),
    ]
)

# PetitionType - 3 fields
BUILTIN_SCHEMAS["PetitionType"] = SchemaDef(
    name="PetitionType",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("RefName", FieldType.INT),
        FieldDef("Field02", FieldType.INT),
    ]
)

# Phase - 8 fields
BUILTIN_SCHEMAS["Phase"] = SchemaDef(
    name="Phase",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MapID", FieldType.INT),
        FieldDef("PhaseShift", FieldType.INT),
        FieldDef("ChildMap_0", FieldType.INT),
        FieldDef("ChildMap_1", FieldType.INT),
        FieldDef("ChildMap_2", FieldType.INT),
        FieldDef("ChildMap_3", FieldType.INT),
        FieldDef("ChildMap_4", FieldType.INT),
    ]
)

# PowerDisplay - 6 fields
BUILTIN_SCHEMAS["PowerDisplay"] = SchemaDef(
    name="PowerDisplay",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ActualType", FieldType.INT),
        FieldDef("GlobalstringBaseTag", FieldType.STRING),
        FieldDef("Red", FieldType.UINT),
        FieldDef("Green", FieldType.UINT),
        FieldDef("Blue", FieldType.UINT),
    ]
)

# PvpDifficulty - 6 fields
BUILTIN_SCHEMAS["PvpDifficulty"] = SchemaDef(
    name="PvpDifficulty",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MapID", FieldType.INT),
        FieldDef("RangeIndex", FieldType.INT),
        FieldDef("MinLevel", FieldType.INT),
        FieldDef("MaxLevel", FieldType.INT),
        FieldDef("Difficulty", FieldType.INT),
    ]
)

# QuestFactionReward - 11 fields
BUILTIN_SCHEMAS["QuestFactionReward"] = SchemaDef(
    name="QuestFactionReward",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Difficulty_0", FieldType.INT),
        FieldDef("Difficulty_1", FieldType.INT),
        FieldDef("Difficulty_2", FieldType.INT),
        FieldDef("Difficulty_3", FieldType.INT),
        FieldDef("Difficulty_4", FieldType.INT),
        FieldDef("Difficulty_5", FieldType.INT),
        FieldDef("Difficulty_6", FieldType.INT),
        FieldDef("Difficulty_7", FieldType.INT),
        FieldDef("Difficulty_8", FieldType.INT),
        FieldDef("Difficulty_9", FieldType.INT),
    ]
)

# QuestInfo - 18 fields
BUILTIN_SCHEMAS["QuestInfo"] = SchemaDef(
    name="QuestInfo",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("InfoName_Lang_enUS", FieldType.STRING),
        FieldDef("InfoName_Lang_koKR", FieldType.STRING),
        FieldDef("InfoName_Lang_frFR", FieldType.STRING),
        FieldDef("InfoName_Lang_deDE", FieldType.STRING),
        FieldDef("InfoName_Lang_enCN", FieldType.STRING),
        FieldDef("InfoName_Lang_enTW", FieldType.STRING),
        FieldDef("InfoName_Lang_esES", FieldType.STRING),
        FieldDef("InfoName_Lang_esMX", FieldType.STRING),
        FieldDef("InfoName_Lang_ruRU", FieldType.STRING),
        FieldDef("InfoName_Lang_jaJP", FieldType.STRING),
        FieldDef("InfoName_Lang_ptPT", FieldType.STRING),
        FieldDef("InfoName_Lang_itIT", FieldType.STRING),
        FieldDef("InfoName_Lang_Unk12", FieldType.STRING),
        FieldDef("InfoName_Lang_Unk13", FieldType.STRING),
        FieldDef("InfoName_Lang_Unk14", FieldType.STRING),
        FieldDef("InfoName_Lang_Unk15", FieldType.STRING),
        FieldDef("InfoName_Lang_Flags", FieldType.UINT),
    ]
)

# QuestSort - 18 fields
BUILTIN_SCHEMAS["QuestSort"] = SchemaDef(
    name="QuestSort",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SortName_Lang_enUS", FieldType.STRING),
        FieldDef("SortName_Lang_koKR", FieldType.STRING),
        FieldDef("SortName_Lang_frFR", FieldType.STRING),
        FieldDef("SortName_Lang_deDE", FieldType.STRING),
        FieldDef("SortName_Lang_enCN", FieldType.STRING),
        FieldDef("SortName_Lang_enTW", FieldType.STRING),
        FieldDef("SortName_Lang_esES", FieldType.STRING),
        FieldDef("SortName_Lang_esMX", FieldType.STRING),
        FieldDef("SortName_Lang_ruRU", FieldType.STRING),
        FieldDef("SortName_Lang_jaJP", FieldType.STRING),
        FieldDef("SortName_Lang_ptPT", FieldType.STRING),
        FieldDef("SortName_Lang_itIT", FieldType.STRING),
        FieldDef("SortName_Lang_Unk12", FieldType.STRING),
        FieldDef("SortName_Lang_Unk13", FieldType.STRING),
        FieldDef("SortName_Lang_Unk14", FieldType.STRING),
        FieldDef("SortName_Lang_Unk15", FieldType.STRING),
        FieldDef("SortName_Lang_Flags", FieldType.UINT),
    ]
)

# QuestXP - 11 fields
BUILTIN_SCHEMAS["QuestXP"] = SchemaDef(
    name="QuestXP",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Difficulty_0", FieldType.INT),
        FieldDef("Difficulty_1", FieldType.INT),
        FieldDef("Difficulty_2", FieldType.INT),
        FieldDef("Difficulty_3", FieldType.INT),
        FieldDef("Difficulty_4", FieldType.INT),
        FieldDef("Difficulty_5", FieldType.INT),
        FieldDef("Difficulty_6", FieldType.INT),
        FieldDef("Difficulty_7", FieldType.INT),
        FieldDef("Difficulty_8", FieldType.INT),
        FieldDef("Difficulty_9", FieldType.INT),
    ]
)

# RandPropPoints - 16 fields
BUILTIN_SCHEMAS["RandPropPoints"] = SchemaDef(
    name="RandPropPoints",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Epic_0", FieldType.INT),
        FieldDef("Epic_1", FieldType.INT),
        FieldDef("Epic_2", FieldType.INT),
        FieldDef("Epic_3", FieldType.INT),
        FieldDef("Epic_4", FieldType.INT),
        FieldDef("Superior_0", FieldType.INT),
        FieldDef("Superior_1", FieldType.INT),
        FieldDef("Superior_2", FieldType.INT),
        FieldDef("Superior_3", FieldType.INT),
        FieldDef("Superior_4", FieldType.INT),
        FieldDef("Good_0", FieldType.INT),
        FieldDef("Good_1", FieldType.INT),
        FieldDef("Good_2", FieldType.INT),
        FieldDef("Good_3", FieldType.INT),
        FieldDef("Good_4", FieldType.INT),
    ]
)

# Resistances - 20 fields
BUILTIN_SCHEMAS["Resistances"] = SchemaDef(
    name="Resistances",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("FizzleSoundID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
    ]
)

# ScalingStatDistribution - 22 fields
BUILTIN_SCHEMAS["ScalingStatDistribution"] = SchemaDef(
    name="ScalingStatDistribution",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("StatID_0", FieldType.INT),
        FieldDef("StatID_1", FieldType.INT),
        FieldDef("StatID_2", FieldType.INT),
        FieldDef("StatID_3", FieldType.INT),
        FieldDef("StatID_4", FieldType.INT),
        FieldDef("StatID_5", FieldType.INT),
        FieldDef("StatID_6", FieldType.INT),
        FieldDef("StatID_7", FieldType.INT),
        FieldDef("StatID_8", FieldType.INT),
        FieldDef("StatID_9", FieldType.INT),
        FieldDef("Bonus_0", FieldType.INT),
        FieldDef("Bonus_1", FieldType.INT),
        FieldDef("Bonus_2", FieldType.INT),
        FieldDef("Bonus_3", FieldType.INT),
        FieldDef("Bonus_4", FieldType.INT),
        FieldDef("Bonus_5", FieldType.INT),
        FieldDef("Bonus_6", FieldType.INT),
        FieldDef("Bonus_7", FieldType.INT),
        FieldDef("Bonus_8", FieldType.INT),
        FieldDef("Bonus_9", FieldType.INT),
        FieldDef("Maxlevel", FieldType.INT),
    ]
)

# ScalingStatValues - 24 fields
BUILTIN_SCHEMAS["ScalingStatValues"] = SchemaDef(
    name="ScalingStatValues",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Charlevel", FieldType.INT),
        FieldDef("ShoulderBudget", FieldType.INT),
        FieldDef("TrinketBudget", FieldType.INT),
        FieldDef("WeaponBudget1H", FieldType.INT),
        FieldDef("RangedBudget", FieldType.INT),
        FieldDef("ClothShoulderArmor", FieldType.INT),
        FieldDef("LeatherShoulderArmor", FieldType.INT),
        FieldDef("MailShoulderArmor", FieldType.INT),
        FieldDef("PlateShoulderArmor", FieldType.INT),
        FieldDef("WeaponDPS1H", FieldType.INT),
        FieldDef("WeaponDPS2H", FieldType.INT),
        FieldDef("SpellcasterDPS1H", FieldType.INT),
        FieldDef("SpellcasterDPS2H", FieldType.INT),
        FieldDef("RangedDPS", FieldType.INT),
        FieldDef("WandDPS", FieldType.INT),
        FieldDef("SpellPower", FieldType.INT),
        FieldDef("PrimaryBudget", FieldType.INT),
        FieldDef("TertiaryBudget", FieldType.INT),
        FieldDef("ClothCloakArmor", FieldType.INT),
        FieldDef("ClothChestArmor", FieldType.INT),
        FieldDef("LeatherChestArmor", FieldType.INT),
        FieldDef("MailChestArmor", FieldType.INT),
        FieldDef("PlateChestArmor", FieldType.INT),
    ]
)

# ScreenEffect - 10 fields
BUILTIN_SCHEMAS["ScreenEffect"] = SchemaDef(
    name="ScreenEffect",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("Effect", FieldType.INT),
        FieldDef("Param_0", FieldType.INT),
        FieldDef("Param_1", FieldType.INT),
        FieldDef("Param_2", FieldType.INT),
        FieldDef("Param_3", FieldType.INT),
        FieldDef("LightParamsID", FieldType.INT),
        FieldDef("SoundAmbienceID", FieldType.INT),
        FieldDef("ZoneMusicID", FieldType.INT),
    ]
)

# ServerMessages - 18 fields
BUILTIN_SCHEMAS["ServerMessages"] = SchemaDef(
    name="ServerMessages",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Text_Lang_enUS", FieldType.STRING),
        FieldDef("Text_Lang_koKR", FieldType.STRING),
        FieldDef("Text_Lang_frFR", FieldType.STRING),
        FieldDef("Text_Lang_deDE", FieldType.STRING),
        FieldDef("Text_Lang_enCN", FieldType.STRING),
        FieldDef("Text_Lang_enTW", FieldType.STRING),
        FieldDef("Text_Lang_esES", FieldType.STRING),
        FieldDef("Text_Lang_esMX", FieldType.STRING),
        FieldDef("Text_Lang_ruRU", FieldType.STRING),
        FieldDef("Text_Lang_jaJP", FieldType.STRING),
        FieldDef("Text_Lang_ptPT", FieldType.STRING),
        FieldDef("Text_Lang_itIT", FieldType.STRING),
        FieldDef("Text_Lang_Unk12", FieldType.STRING),
        FieldDef("Text_Lang_Unk13", FieldType.STRING),
        FieldDef("Text_Lang_Unk14", FieldType.STRING),
        FieldDef("Text_Lang_Unk15", FieldType.STRING),
        FieldDef("Text_Lang_Flags", FieldType.UINT),
    ]
)

# SheatheSoundLookups - 7 fields
BUILTIN_SCHEMAS["SheatheSoundLookups"] = SchemaDef(
    name="SheatheSoundLookups",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ItemClass", FieldType.INT),
        FieldDef("ItemSubclass", FieldType.INT),
        FieldDef("ItemEnvTypes", FieldType.INT),
        FieldDef("IsShield", FieldType.INT),
        FieldDef("SheathSoundID", FieldType.INT),
        FieldDef("UnsheathSoundID", FieldType.INT),
    ]
)

# SkillCostsData - 5 fields
BUILTIN_SCHEMAS["SkillCostsData"] = SchemaDef(
    name="SkillCostsData",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SkillCostsID", FieldType.INT),
        FieldDef("Cost_0", FieldType.INT),
        FieldDef("Cost_1", FieldType.INT),
        FieldDef("Cost_2", FieldType.INT),
    ]
)

# SkillLine - 56 fields
BUILTIN_SCHEMAS["SkillLine"] = SchemaDef(
    name="SkillLine",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("CategoryID", FieldType.INT),
        FieldDef("SkillCostsID", FieldType.INT),
        FieldDef("DisplayName_Lang_enUS", FieldType.STRING),
        FieldDef("DisplayName_Lang_koKR", FieldType.STRING),
        FieldDef("DisplayName_Lang_frFR", FieldType.STRING),
        FieldDef("DisplayName_Lang_deDE", FieldType.STRING),
        FieldDef("DisplayName_Lang_enCN", FieldType.STRING),
        FieldDef("DisplayName_Lang_enTW", FieldType.STRING),
        FieldDef("DisplayName_Lang_esES", FieldType.STRING),
        FieldDef("DisplayName_Lang_esMX", FieldType.STRING),
        FieldDef("DisplayName_Lang_ruRU", FieldType.STRING),
        FieldDef("DisplayName_Lang_jaJP", FieldType.STRING),
        FieldDef("DisplayName_Lang_ptPT", FieldType.STRING),
        FieldDef("DisplayName_Lang_itIT", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk12", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk13", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk14", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk15", FieldType.STRING),
        FieldDef("DisplayName_Lang_Flags", FieldType.UINT),
        FieldDef("Description_Lang_enUS", FieldType.STRING),
        FieldDef("Description_Lang_koKR", FieldType.STRING),
        FieldDef("Description_Lang_frFR", FieldType.STRING),
        FieldDef("Description_Lang_deDE", FieldType.STRING),
        FieldDef("Description_Lang_enCN", FieldType.STRING),
        FieldDef("Description_Lang_enTW", FieldType.STRING),
        FieldDef("Description_Lang_esES", FieldType.STRING),
        FieldDef("Description_Lang_esMX", FieldType.STRING),
        FieldDef("Description_Lang_ruRU", FieldType.STRING),
        FieldDef("Description_Lang_jaJP", FieldType.STRING),
        FieldDef("Description_Lang_ptPT", FieldType.STRING),
        FieldDef("Description_Lang_itIT", FieldType.STRING),
        FieldDef("Description_Lang_Unk12", FieldType.STRING),
        FieldDef("Description_Lang_Unk13", FieldType.STRING),
        FieldDef("Description_Lang_Unk14", FieldType.STRING),
        FieldDef("Description_Lang_Unk15", FieldType.STRING),
        FieldDef("Description_Lang_Flags", FieldType.UINT),
        FieldDef("SpellIconID", FieldType.INT),
        FieldDef("AlternateVerb_Lang_enUS", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_koKR", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_frFR", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_deDE", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_enCN", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_enTW", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_esES", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_esMX", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_ruRU", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_jaJP", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_ptPT", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_itIT", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_Unk12", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_Unk13", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_Unk14", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_Unk15", FieldType.STRING),
        FieldDef("AlternateVerb_Lang_Flags", FieldType.UINT),
        FieldDef("CanLink", FieldType.INT),
    ]
)

# SkillLineAbility - 13 fields
BUILTIN_SCHEMAS["SkillLineAbility"] = SchemaDef(
    name="SkillLineAbility",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SkillLine", FieldType.INT),
        FieldDef("Spell", FieldType.INT),
        FieldDef("RaceMask", FieldType.INT),
        FieldDef("ClassMask", FieldType.INT),
        FieldDef("MinSkillLineRank", FieldType.INT),
        FieldDef("SupercededBySpell", FieldType.INT),
        FieldDef("AcquireMethod", FieldType.INT),
        FieldDef("TrivialSkillLineRankHigh", FieldType.INT),
        FieldDef("TrivialSkillLineRankLow", FieldType.INT),
        FieldDef("CharacterPoints_0", FieldType.INT),
        FieldDef("CharacterPoints_1", FieldType.INT),
        FieldDef("TradeSkillCategoryID", FieldType.INT),
    ]
)

# SkillLineCategory - 19 fields
BUILTIN_SCHEMAS["SkillLineCategory"] = SchemaDef(
    name="SkillLineCategory",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("SortIndex", FieldType.INT),
    ]
)

# SkillRaceClassInfo - 8 fields
BUILTIN_SCHEMAS["SkillRaceClassInfo"] = SchemaDef(
    name="SkillRaceClassInfo",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SkillID", FieldType.INT),
        FieldDef("RaceMask", FieldType.INT),
        FieldDef("ClassMask", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("MinLevel", FieldType.INT),
        FieldDef("SkillTierID", FieldType.INT),
        FieldDef("SkillCostIndex", FieldType.INT),
    ]
)

# SkillTiers - 33 fields
BUILTIN_SCHEMAS["SkillTiers"] = SchemaDef(
    name="SkillTiers",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Cost_0", FieldType.INT),
        FieldDef("Cost_1", FieldType.INT),
        FieldDef("Cost_2", FieldType.INT),
        FieldDef("Cost_3", FieldType.INT),
        FieldDef("Cost_4", FieldType.INT),
        FieldDef("Cost_5", FieldType.INT),
        FieldDef("Cost_6", FieldType.INT),
        FieldDef("Cost_7", FieldType.INT),
        FieldDef("Cost_8", FieldType.INT),
        FieldDef("Cost_9", FieldType.INT),
        FieldDef("Cost_10", FieldType.INT),
        FieldDef("Cost_11", FieldType.INT),
        FieldDef("Cost_12", FieldType.INT),
        FieldDef("Cost_13", FieldType.INT),
        FieldDef("Cost_14", FieldType.INT),
        FieldDef("Cost_15", FieldType.INT),
        FieldDef("Value_0", FieldType.INT),
        FieldDef("Value_1", FieldType.INT),
        FieldDef("Value_2", FieldType.INT),
        FieldDef("Value_3", FieldType.INT),
        FieldDef("Value_4", FieldType.INT),
        FieldDef("Value_5", FieldType.INT),
        FieldDef("Value_6", FieldType.INT),
        FieldDef("Value_7", FieldType.INT),
        FieldDef("Value_8", FieldType.INT),
        FieldDef("Value_9", FieldType.INT),
        FieldDef("Value_10", FieldType.INT),
        FieldDef("Value_11", FieldType.INT),
        FieldDef("Value_12", FieldType.INT),
        FieldDef("Value_13", FieldType.INT),
        FieldDef("Value_14", FieldType.INT),
        FieldDef("Value_15", FieldType.INT),
    ]
)

# SoundAmbience - 3 fields
BUILTIN_SCHEMAS["SoundAmbience"] = SchemaDef(
    name="SoundAmbience",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("AmbienceID_0", FieldType.INT),
        FieldDef("AmbienceID_1", FieldType.INT),
    ]
)

# SoundEmitters - 10 fields
BUILTIN_SCHEMAS["SoundEmitters"] = SchemaDef(
    name="SoundEmitters",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("PositionX", FieldType.FLOAT),
        FieldDef("PositionY", FieldType.FLOAT),
        FieldDef("PositionZ", FieldType.FLOAT),
        FieldDef("DirectionX", FieldType.FLOAT),
        FieldDef("DirectionY", FieldType.FLOAT),
        FieldDef("DirectionZ", FieldType.FLOAT),
        FieldDef("SoundEntriesID", FieldType.INT),
        FieldDef("MapID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
    ]
)

# SoundEntries - 30 fields
BUILTIN_SCHEMAS["SoundEntries"] = SchemaDef(
    name="SoundEntries",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SoundType", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("File_0", FieldType.STRING),
        FieldDef("File_1", FieldType.STRING),
        FieldDef("File_2", FieldType.STRING),
        FieldDef("File_3", FieldType.STRING),
        FieldDef("File_4", FieldType.STRING),
        FieldDef("File_5", FieldType.STRING),
        FieldDef("File_6", FieldType.STRING),
        FieldDef("File_7", FieldType.STRING),
        FieldDef("File_8", FieldType.STRING),
        FieldDef("File_9", FieldType.STRING),
        FieldDef("Freq_0", FieldType.INT),
        FieldDef("Freq_1", FieldType.INT),
        FieldDef("Freq_2", FieldType.INT),
        FieldDef("Freq_3", FieldType.INT),
        FieldDef("Freq_4", FieldType.INT),
        FieldDef("Freq_5", FieldType.INT),
        FieldDef("Freq_6", FieldType.INT),
        FieldDef("Freq_7", FieldType.INT),
        FieldDef("Freq_8", FieldType.INT),
        FieldDef("Freq_9", FieldType.INT),
        FieldDef("DirectoryBase", FieldType.STRING),
        FieldDef("Volumefloat", FieldType.FLOAT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("MinDistance", FieldType.FLOAT),
        FieldDef("DistanceCutoff", FieldType.FLOAT),
        FieldDef("EAXDef", FieldType.INT),
        FieldDef("SoundEntriesAdvancedID", FieldType.INT),
    ]
)

# SoundEntriesAdvanced - 24 fields
BUILTIN_SCHEMAS["SoundEntriesAdvanced"] = SchemaDef(
    name="SoundEntriesAdvanced",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SoundEntryID", FieldType.INT),
        FieldDef("InnerRadius2D", FieldType.FLOAT),
        FieldDef("TimeA", FieldType.INT),
        FieldDef("TimeB", FieldType.INT),
        FieldDef("TimeC", FieldType.INT),
        FieldDef("TimeD", FieldType.INT),
        FieldDef("RandomOffsetRange", FieldType.INT),
        FieldDef("Usage", FieldType.INT),
        FieldDef("TimeintervalMin", FieldType.INT),
        FieldDef("TimeintervalMax", FieldType.INT),
        FieldDef("VolumeSliderCategory", FieldType.INT),
        FieldDef("DuckToSFX", FieldType.FLOAT),
        FieldDef("DuckToMusic", FieldType.FLOAT),
        FieldDef("DuckToAmbience", FieldType.FLOAT),
        FieldDef("InnerRadiusOfInfluence", FieldType.FLOAT),
        FieldDef("OuterRadiusOfInfluence", FieldType.FLOAT),
        FieldDef("TimeToDuck", FieldType.INT),
        FieldDef("TimeToUnduck", FieldType.INT),
        FieldDef("InsideAngle", FieldType.FLOAT),
        FieldDef("OutsideAngle", FieldType.FLOAT),
        FieldDef("OutsideVolume", FieldType.FLOAT),
        FieldDef("OuterRadius2D", FieldType.FLOAT),
        FieldDef("Name", FieldType.STRING),
    ]
)

# SoundFilter - 2 fields
BUILTIN_SCHEMAS["SoundFilter"] = SchemaDef(
    name="SoundFilter",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
    ]
)

# SoundFilterElem - 13 fields
BUILTIN_SCHEMAS["SoundFilterElem"] = SchemaDef(
    name="SoundFilterElem",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SoundFilterID", FieldType.INT),
        FieldDef("OrderIndex", FieldType.INT),
        FieldDef("FilterType", FieldType.INT),
        FieldDef("Params_0", FieldType.FLOAT),
        FieldDef("Params_1", FieldType.FLOAT),
        FieldDef("Params_2", FieldType.FLOAT),
        FieldDef("Params_3", FieldType.FLOAT),
        FieldDef("Params_4", FieldType.FLOAT),
        FieldDef("Params_5", FieldType.FLOAT),
        FieldDef("Params_6", FieldType.FLOAT),
        FieldDef("Params_7", FieldType.FLOAT),
        FieldDef("Params_8", FieldType.FLOAT),
    ]
)

# SoundProviderPreferences - 24 fields
BUILTIN_SCHEMAS["SoundProviderPreferences"] = SchemaDef(
    name="SoundProviderPreferences",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Description", FieldType.STRING),
        FieldDef("Flags", FieldType.INT),
        FieldDef("EAXEnvironmentSelection", FieldType.INT),
        FieldDef("EAXDecayTime", FieldType.FLOAT),
        FieldDef("EAX2EnvironmentSize", FieldType.FLOAT),
        FieldDef("EAX2EnvironmentDiffusion", FieldType.FLOAT),
        FieldDef("EAX2Room", FieldType.INT),
        FieldDef("EAX2RoomHF", FieldType.INT),
        FieldDef("EAX2DecayHFRatio", FieldType.FLOAT),
        FieldDef("EAX2Reflections", FieldType.INT),
        FieldDef("EAX2ReflectionsDelay", FieldType.FLOAT),
        FieldDef("EAX2Reverb", FieldType.INT),
        FieldDef("EAX2ReverbDelay", FieldType.FLOAT),
        FieldDef("EAX2RoomRolloff", FieldType.FLOAT),
        FieldDef("EAX2AirAbsorption", FieldType.FLOAT),
        FieldDef("EAX3RoomLF", FieldType.INT),
        FieldDef("EAX3DecayLFRatio", FieldType.FLOAT),
        FieldDef("EAX3EchoTime", FieldType.FLOAT),
        FieldDef("EAX3EchoDepth", FieldType.FLOAT),
        FieldDef("EAX3ModulationTime", FieldType.FLOAT),
        FieldDef("EAX3ModulationDepth", FieldType.FLOAT),
        FieldDef("EAX3HFReference", FieldType.FLOAT),
        FieldDef("EAX3LFReference", FieldType.FLOAT),
    ]
)

# SoundSamplePreferences - 17 fields
BUILTIN_SCHEMAS["SoundSamplePreferences"] = SchemaDef(
    name="SoundSamplePreferences",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Field01", FieldType.INT),
        FieldDef("Field02", FieldType.INT),
        FieldDef("Field03", FieldType.INT),
        FieldDef("Field04", FieldType.INT),
        FieldDef("Field05", FieldType.INT),
        FieldDef("Field06", FieldType.INT),
        FieldDef("Field07", FieldType.INT),
        FieldDef("Field08", FieldType.FLOAT),
        FieldDef("Field09", FieldType.FLOAT),
        FieldDef("Field10", FieldType.INT),
        FieldDef("Field11", FieldType.INT),
        FieldDef("Field12", FieldType.INT),
        FieldDef("Field13", FieldType.FLOAT),
        FieldDef("Field14", FieldType.INT),
        FieldDef("Field15", FieldType.FLOAT),
        FieldDef("Field16", FieldType.INT),
    ]
)

# SoundWaterType - 4 fields
BUILTIN_SCHEMAS["SoundWaterType"] = SchemaDef(
    name="SoundWaterType",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("LiquidTypeID", FieldType.INT),
        FieldDef("FluidSpeed", FieldType.INT),
        FieldDef("SoundID", FieldType.INT),
    ]
)

# SpamMessages - 2 fields
BUILTIN_SCHEMAS["SpamMessages"] = SchemaDef(
    name="SpamMessages",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Text", FieldType.STRING),
    ]
)

# Spell - 232 fields
BUILTIN_SCHEMAS["Spell"] = SchemaDef(
    name="Spell",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Category", FieldType.UINT),
        FieldDef("DispelType", FieldType.UINT),
        FieldDef("Mechanic", FieldType.UINT),
        FieldDef("Attributes", FieldType.UINT),
        FieldDef("AttributesEx", FieldType.UINT),
        FieldDef("AttributesExB", FieldType.UINT),
        FieldDef("AttributesExC", FieldType.UINT),
        FieldDef("AttributesExD", FieldType.UINT),
        FieldDef("AttributesExE", FieldType.UINT),
        FieldDef("AttributesExF", FieldType.UINT),
        FieldDef("AttributesExG", FieldType.UINT),
        FieldDef("ShapeshiftMask", FieldType.UINT),
        FieldDef("ShapeshiftExclude", FieldType.UINT),
        FieldDef("Targets", FieldType.UINT),
        FieldDef("TargetCreatureType", FieldType.UINT),
        FieldDef("RequiresSpellFocus", FieldType.UINT),
        FieldDef("FacingCasterFlags", FieldType.UINT),
        FieldDef("CasterAuraState", FieldType.UINT),
        FieldDef("TargetAuraState", FieldType.UINT),
        FieldDef("ExcludeCasterAuraState", FieldType.UINT),
        FieldDef("ExcludeTargetAuraState", FieldType.UINT),
        FieldDef("CasterAuraSpell", FieldType.UINT),
        FieldDef("TargetAuraSpell", FieldType.UINT),
        FieldDef("ExcludeCasterAuraSpell", FieldType.UINT),
        FieldDef("ExcludeTargetAuraSpell", FieldType.UINT),
        FieldDef("CastingTimeIndex", FieldType.UINT),
        FieldDef("RecoveryTime", FieldType.UINT),
        FieldDef("CategoryRecoveryTime", FieldType.UINT),
        FieldDef("InterruptFlags", FieldType.UINT),
        FieldDef("AuraInterruptFlags", FieldType.UINT),
        FieldDef("ChannelInterruptFlags", FieldType.UINT),
        FieldDef("ProcTypeMask", FieldType.UINT),
        FieldDef("ProcChance", FieldType.UINT),
        FieldDef("ProcCharges", FieldType.UINT),
        FieldDef("MaxLevel", FieldType.UINT),
        FieldDef("BaseLevel", FieldType.UINT),
        FieldDef("SpellLevel", FieldType.UINT),
        FieldDef("DurationIndex", FieldType.UINT),
        FieldDef("PowerType", FieldType.INT),
        FieldDef("ManaCost", FieldType.UINT),
        FieldDef("ManaCostPerLevel", FieldType.UINT),
        FieldDef("ManaPerSecond", FieldType.UINT),
        FieldDef("ManaPerSecondPerLevel", FieldType.UINT),
        FieldDef("RangeIndex", FieldType.UINT),
        FieldDef("Speed", FieldType.FLOAT),
        FieldDef("ModalNextSpell", FieldType.UINT),
        FieldDef("CumulativeAura", FieldType.UINT),
        FieldDef("Totem_0", FieldType.UINT),
        FieldDef("Totem_1", FieldType.UINT),
        FieldDef("Reagent_0", FieldType.INT),
        FieldDef("Reagent_1", FieldType.INT),
        FieldDef("Reagent_2", FieldType.INT),
        FieldDef("Reagent_3", FieldType.INT),
        FieldDef("Reagent_4", FieldType.INT),
        FieldDef("Reagent_5", FieldType.INT),
        FieldDef("Reagent_6", FieldType.INT),
        FieldDef("Reagent_7", FieldType.INT),
        FieldDef("ReagentCount_0", FieldType.INT),
        FieldDef("ReagentCount_1", FieldType.INT),
        FieldDef("ReagentCount_2", FieldType.INT),
        FieldDef("ReagentCount_3", FieldType.INT),
        FieldDef("ReagentCount_4", FieldType.INT),
        FieldDef("ReagentCount_5", FieldType.INT),
        FieldDef("ReagentCount_6", FieldType.INT),
        FieldDef("ReagentCount_7", FieldType.INT),
        FieldDef("EquippedItemClass", FieldType.INT),
        FieldDef("EquippedItemSubclass", FieldType.INT),
        FieldDef("EquippedItemInvTypes", FieldType.INT),
        FieldDef("Effect_0", FieldType.UINT),
        FieldDef("Effect_1", FieldType.UINT),
        FieldDef("Effect_2", FieldType.UINT),
        FieldDef("EffectDieSides_0", FieldType.INT),
        FieldDef("EffectDieSides_1", FieldType.INT),
        FieldDef("EffectDieSides_2", FieldType.INT),
        FieldDef("EffectRealPointsPerLevel_0", FieldType.FLOAT),
        FieldDef("EffectRealPointsPerLevel_1", FieldType.FLOAT),
        FieldDef("EffectRealPointsPerLevel_2", FieldType.FLOAT),
        FieldDef("EffectBasePoints_0", FieldType.INT),
        FieldDef("EffectBasePoints_1", FieldType.INT),
        FieldDef("EffectBasePoints_2", FieldType.INT),
        FieldDef("EffectMechanic_0", FieldType.UINT),
        FieldDef("EffectMechanic_1", FieldType.UINT),
        FieldDef("EffectMechanic_2", FieldType.UINT),
        FieldDef("ImplicitTargetA_0", FieldType.UINT),
        FieldDef("ImplicitTargetA_1", FieldType.UINT),
        FieldDef("ImplicitTargetA_2", FieldType.UINT),
        FieldDef("ImplicitTargetB_0", FieldType.UINT),
        FieldDef("ImplicitTargetB_1", FieldType.UINT),
        FieldDef("ImplicitTargetB_2", FieldType.UINT),
        FieldDef("EffectRadiusIndex_0", FieldType.UINT),
        FieldDef("EffectRadiusIndex_1", FieldType.UINT),
        FieldDef("EffectRadiusIndex_2", FieldType.UINT),
        FieldDef("EffectAura_0", FieldType.UINT),
        FieldDef("EffectAura_1", FieldType.UINT),
        FieldDef("EffectAura_2", FieldType.UINT),
        FieldDef("EffectAuraPeriod_0", FieldType.UINT),
        FieldDef("EffectAuraPeriod_1", FieldType.UINT),
        FieldDef("EffectAuraPeriod_2", FieldType.UINT),
        FieldDef("EffectMultipleValue_0", FieldType.FLOAT),
        FieldDef("EffectMultipleValue_1", FieldType.FLOAT),
        FieldDef("EffectMultipleValue_2", FieldType.FLOAT),
        FieldDef("EffectChainTargets_0", FieldType.UINT),
        FieldDef("EffectChainTargets_1", FieldType.UINT),
        FieldDef("EffectChainTargets_2", FieldType.UINT),
        FieldDef("EffectItemType_0", FieldType.UINT),
        FieldDef("EffectItemType_1", FieldType.UINT),
        FieldDef("EffectItemType_2", FieldType.UINT),
        FieldDef("EffectMiscValue_0", FieldType.INT),
        FieldDef("EffectMiscValue_1", FieldType.INT),
        FieldDef("EffectMiscValue_2", FieldType.INT),
        FieldDef("EffectMiscValueB_0", FieldType.INT),
        FieldDef("EffectMiscValueB_1", FieldType.INT),
        FieldDef("EffectMiscValueB_2", FieldType.INT),
        FieldDef("EffectTriggerSpell_0", FieldType.UINT),
        FieldDef("EffectTriggerSpell_1", FieldType.UINT),
        FieldDef("EffectTriggerSpell_2", FieldType.UINT),
        FieldDef("EffectPointsPerCombo_0", FieldType.FLOAT),
        FieldDef("EffectPointsPerCombo_1", FieldType.FLOAT),
        FieldDef("EffectPointsPerCombo_2", FieldType.FLOAT),
        FieldDef("EffectSpellClassMaskA_0", FieldType.UINT),
        FieldDef("EffectSpellClassMaskA_1", FieldType.UINT),
        FieldDef("EffectSpellClassMaskA_2", FieldType.UINT),
        FieldDef("EffectSpellClassMaskB_0", FieldType.UINT),
        FieldDef("EffectSpellClassMaskB_1", FieldType.UINT),
        FieldDef("EffectSpellClassMaskB_2", FieldType.UINT),
        FieldDef("EffectSpellClassMaskC_0", FieldType.UINT),
        FieldDef("EffectSpellClassMaskC_1", FieldType.UINT),
        FieldDef("EffectSpellClassMaskC_2", FieldType.UINT),
        FieldDef("SpellVisualID_0", FieldType.UINT),
        FieldDef("SpellVisualID_1", FieldType.UINT),
        FieldDef("SpellIconID", FieldType.UINT),
        FieldDef("ActiveIconID", FieldType.UINT),
        FieldDef("SpellPriority", FieldType.UINT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("NameSubtext_Lang_enUS", FieldType.STRING),
        FieldDef("NameSubtext_Lang_koKR", FieldType.STRING),
        FieldDef("NameSubtext_Lang_frFR", FieldType.STRING),
        FieldDef("NameSubtext_Lang_deDE", FieldType.STRING),
        FieldDef("NameSubtext_Lang_enCN", FieldType.STRING),
        FieldDef("NameSubtext_Lang_enTW", FieldType.STRING),
        FieldDef("NameSubtext_Lang_esES", FieldType.STRING),
        FieldDef("NameSubtext_Lang_esMX", FieldType.STRING),
        FieldDef("NameSubtext_Lang_ruRU", FieldType.STRING),
        FieldDef("NameSubtext_Lang_jaJP", FieldType.STRING),
        FieldDef("NameSubtext_Lang_ptPT", FieldType.STRING),
        FieldDef("NameSubtext_Lang_itIT", FieldType.STRING),
        FieldDef("NameSubtext_Lang_Unk12", FieldType.STRING),
        FieldDef("NameSubtext_Lang_Unk13", FieldType.STRING),
        FieldDef("NameSubtext_Lang_Unk14", FieldType.STRING),
        FieldDef("NameSubtext_Lang_Unk15", FieldType.STRING),
        FieldDef("NameSubtext_Lang_Flags", FieldType.UINT),
        FieldDef("Description_Lang_enUS", FieldType.STRING),
        FieldDef("Description_Lang_koKR", FieldType.STRING),
        FieldDef("Description_Lang_frFR", FieldType.STRING),
        FieldDef("Description_Lang_deDE", FieldType.STRING),
        FieldDef("Description_Lang_enCN", FieldType.STRING),
        FieldDef("Description_Lang_enTW", FieldType.STRING),
        FieldDef("Description_Lang_esES", FieldType.STRING),
        FieldDef("Description_Lang_esMX", FieldType.STRING),
        FieldDef("Description_Lang_ruRU", FieldType.STRING),
        FieldDef("Description_Lang_jaJP", FieldType.STRING),
        FieldDef("Description_Lang_ptPT", FieldType.STRING),
        FieldDef("Description_Lang_itIT", FieldType.STRING),
        FieldDef("Description_Lang_Unk12", FieldType.STRING),
        FieldDef("Description_Lang_Unk13", FieldType.STRING),
        FieldDef("Description_Lang_Unk14", FieldType.STRING),
        FieldDef("Description_Lang_Unk15", FieldType.STRING),
        FieldDef("Description_Lang_Flags", FieldType.UINT),
        FieldDef("AuraDescription_Lang_enUS", FieldType.STRING),
        FieldDef("AuraDescription_Lang_koKR", FieldType.STRING),
        FieldDef("AuraDescription_Lang_frFR", FieldType.STRING),
        FieldDef("AuraDescription_Lang_deDE", FieldType.STRING),
        FieldDef("AuraDescription_Lang_enCN", FieldType.STRING),
        FieldDef("AuraDescription_Lang_enTW", FieldType.STRING),
        FieldDef("AuraDescription_Lang_esES", FieldType.STRING),
        FieldDef("AuraDescription_Lang_esMX", FieldType.STRING),
        FieldDef("AuraDescription_Lang_ruRU", FieldType.STRING),
        FieldDef("AuraDescription_Lang_jaJP", FieldType.STRING),
        FieldDef("AuraDescription_Lang_ptPT", FieldType.STRING),
        FieldDef("AuraDescription_Lang_itIT", FieldType.STRING),
        FieldDef("AuraDescription_Lang_Unk12", FieldType.STRING),
        FieldDef("AuraDescription_Lang_Unk13", FieldType.STRING),
        FieldDef("AuraDescription_Lang_Unk14", FieldType.STRING),
        FieldDef("AuraDescription_Lang_Unk15", FieldType.STRING),
        FieldDef("AuraDescription_Lang_Flags", FieldType.UINT),
        FieldDef("ManaCostPct", FieldType.UINT),
        FieldDef("StartRecoveryCategory", FieldType.UINT),
        FieldDef("StartRecoveryTime", FieldType.UINT),
        FieldDef("MaxTargetLevel", FieldType.UINT),
        FieldDef("SpellClassSet", FieldType.UINT),
        FieldDef("SpellClassMask_0", FieldType.UINT),
        FieldDef("SpellClassMask_1", FieldType.UINT),
        FieldDef("SpellClassMask_2", FieldType.UINT),
        FieldDef("MaxTargets", FieldType.UINT),
        FieldDef("DefenseType", FieldType.UINT),
        FieldDef("PreventionType", FieldType.UINT),
        FieldDef("StanceBarOrder", FieldType.UINT),
        FieldDef("EffectChainAmplitude_0", FieldType.FLOAT),
        FieldDef("EffectChainAmplitude_1", FieldType.FLOAT),
        FieldDef("EffectChainAmplitude_2", FieldType.FLOAT),
        FieldDef("MinFactionID", FieldType.UINT),
        FieldDef("MinReputation", FieldType.UINT),
        FieldDef("RequiredAuraVision", FieldType.UINT),
        FieldDef("RequiredTotemCategoryID_0", FieldType.UINT),
        FieldDef("RequiredTotemCategoryID_1", FieldType.UINT),
        FieldDef("RequiredAreasID", FieldType.INT),
        FieldDef("SchoolMask", FieldType.UINT),
        FieldDef("RuneCostID", FieldType.UINT),
        FieldDef("SpellMissileID", FieldType.UINT),
        FieldDef("PowerDisplayID", FieldType.INT),
        FieldDef("Field227", FieldType.FLOAT),
        FieldDef("Field228", FieldType.FLOAT),
        FieldDef("Field229", FieldType.FLOAT),
        FieldDef("SpellDescriptionVariableID", FieldType.UINT),
        FieldDef("SpellDifficultyID", FieldType.UINT),
    ]
)

# SpellCastTimes - 4 fields
BUILTIN_SCHEMAS["SpellCastTimes"] = SchemaDef(
    name="SpellCastTimes",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Base", FieldType.INT),
        FieldDef("PerLevel", FieldType.INT),
        FieldDef("Minimum", FieldType.INT),
    ]
)

# SpellCategory - 2 fields
BUILTIN_SCHEMAS["SpellCategory"] = SchemaDef(
    name="SpellCategory",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
    ]
)

# SpellChainEffects - 48 fields
BUILTIN_SCHEMAS["SpellChainEffects"] = SchemaDef(
    name="SpellChainEffects",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("AvgSegLen", FieldType.FLOAT),
        FieldDef("Width", FieldType.FLOAT),
        FieldDef("NoiseScale", FieldType.FLOAT),
        FieldDef("TexCoordScale", FieldType.FLOAT),
        FieldDef("SegDuration", FieldType.INT),
        FieldDef("SegDelay", FieldType.INT),
        FieldDef("Texture", FieldType.STRING),
        FieldDef("Flags", FieldType.INT),
        FieldDef("JointCount", FieldType.INT),
        FieldDef("JointOffsetRadius", FieldType.FLOAT),
        FieldDef("JointsPerMinorJoint", FieldType.INT),
        FieldDef("MinorJointsPerMajorJoint", FieldType.INT),
        FieldDef("MinorJointScale", FieldType.FLOAT),
        FieldDef("MajorJointScale", FieldType.FLOAT),
        FieldDef("JointMoveSpeed", FieldType.FLOAT),
        FieldDef("JointSmoothness", FieldType.FLOAT),
        FieldDef("MinDurationBetweenJointJumps", FieldType.FLOAT),
        FieldDef("MaxDurationBetweenJointJumps", FieldType.FLOAT),
        FieldDef("WaveHeight", FieldType.FLOAT),
        FieldDef("WaveFreq", FieldType.FLOAT),
        FieldDef("WaveSpeed", FieldType.FLOAT),
        FieldDef("MinWaveAngle", FieldType.FLOAT),
        FieldDef("MaxWaveAngle", FieldType.FLOAT),
        FieldDef("MinWaveSpin", FieldType.FLOAT),
        FieldDef("MaxWaveSpin", FieldType.FLOAT),
        FieldDef("ArcHeight", FieldType.FLOAT),
        FieldDef("MinArcAngle", FieldType.FLOAT),
        FieldDef("MaxArcAngle", FieldType.FLOAT),
        FieldDef("MinArcSpin", FieldType.FLOAT),
        FieldDef("MaxArcSpin", FieldType.FLOAT),
        FieldDef("DelayBetweenEffects", FieldType.FLOAT),
        FieldDef("MinFlickerOnDuration", FieldType.FLOAT),
        FieldDef("MaxFlickerOnDuration", FieldType.FLOAT),
        FieldDef("MinFlickerOffDuration", FieldType.FLOAT),
        FieldDef("MaxFlickerOffDuration", FieldType.FLOAT),
        FieldDef("PulseSpeed", FieldType.FLOAT),
        FieldDef("PulseOnLength", FieldType.FLOAT),
        FieldDef("PulseFadeLength", FieldType.FLOAT),
        FieldDef("Alpha", FieldType.UINT),
        FieldDef("Red", FieldType.UINT),
        FieldDef("Green", FieldType.UINT),
        FieldDef("Blue", FieldType.UINT),
        FieldDef("BlendMode", FieldType.UINT),
        FieldDef("Combo", FieldType.STRING),
        FieldDef("RenderLayer", FieldType.INT),
        FieldDef("TextureLength", FieldType.FLOAT),
        FieldDef("WavePhase", FieldType.FLOAT),
    ]
)

# SpellDescriptionVariables - 2 fields
BUILTIN_SCHEMAS["SpellDescriptionVariables"] = SchemaDef(
    name="SpellDescriptionVariables",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Variables", FieldType.STRING),
    ]
)

# SpellDifficulty - 5 fields
BUILTIN_SCHEMAS["SpellDifficulty"] = SchemaDef(
    name="SpellDifficulty",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("DifficultySpellID_0", FieldType.INT),
        FieldDef("DifficultySpellID_1", FieldType.INT),
        FieldDef("DifficultySpellID_2", FieldType.INT),
        FieldDef("DifficultySpellID_3", FieldType.INT),
    ]
)

# SpellDispelType - 21 fields
BUILTIN_SCHEMAS["SpellDispelType"] = SchemaDef(
    name="SpellDispelType",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("Mask", FieldType.INT),
        FieldDef("ImmunityPossible", FieldType.INT),
        FieldDef("InternalName", FieldType.STRING),
    ]
)

# SpellDuration - 4 fields
BUILTIN_SCHEMAS["SpellDuration"] = SchemaDef(
    name="SpellDuration",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Duration", FieldType.INT),
        FieldDef("DurationPerLevel", FieldType.INT),
        FieldDef("MaxDuration", FieldType.INT),
    ]
)

# SpellEffectCameraShakes - 4 fields
BUILTIN_SCHEMAS["SpellEffectCameraShakes"] = SchemaDef(
    name="SpellEffectCameraShakes",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("CameraShake_0", FieldType.INT),
        FieldDef("CameraShake_1", FieldType.INT),
        FieldDef("CameraShake_2", FieldType.INT),
    ]
)

# SpellFocusObject - 18 fields
BUILTIN_SCHEMAS["SpellFocusObject"] = SchemaDef(
    name="SpellFocusObject",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
    ]
)

# SpellIcon - 2 fields
BUILTIN_SCHEMAS["SpellIcon"] = SchemaDef(
    name="SpellIcon",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("TextureFilename", FieldType.STRING),
    ]
)

# SpellItemEnchantment - 38 fields
BUILTIN_SCHEMAS["SpellItemEnchantment"] = SchemaDef(
    name="SpellItemEnchantment",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Charges", FieldType.INT),
        FieldDef("Effect_0", FieldType.INT),
        FieldDef("Effect_1", FieldType.INT),
        FieldDef("Effect_2", FieldType.INT),
        FieldDef("EffectPointsMin_0", FieldType.INT),
        FieldDef("EffectPointsMin_1", FieldType.INT),
        FieldDef("EffectPointsMin_2", FieldType.INT),
        FieldDef("EffectPointsMax_0", FieldType.INT),
        FieldDef("EffectPointsMax_1", FieldType.INT),
        FieldDef("EffectPointsMax_2", FieldType.INT),
        FieldDef("EffectArg_0", FieldType.INT),
        FieldDef("EffectArg_1", FieldType.INT),
        FieldDef("EffectArg_2", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("ItemVisual", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("Src_ItemID", FieldType.INT),
        FieldDef("Condition_Id", FieldType.INT),
        FieldDef("RequiredSkillID", FieldType.INT),
        FieldDef("RequiredSkillRank", FieldType.INT),
        FieldDef("MinLevel", FieldType.INT),
    ]
)

# SpellItemEnchantmentCondition - 31 fields
BUILTIN_SCHEMAS["SpellItemEnchantmentCondition"] = SchemaDef(
    name="SpellItemEnchantmentCondition",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Lt_OperandType_0", FieldType.UINT),
        FieldDef("Lt_OperandType_1", FieldType.UINT),
        FieldDef("Lt_OperandType_2", FieldType.UINT),
        FieldDef("Lt_OperandType_3", FieldType.UINT),
        FieldDef("Lt_OperandType_4", FieldType.UINT),
        FieldDef("Lt_Operand_0", FieldType.INT),
        FieldDef("Lt_Operand_1", FieldType.INT),
        FieldDef("Lt_Operand_2", FieldType.INT),
        FieldDef("Lt_Operand_3", FieldType.INT),
        FieldDef("Lt_Operand_4", FieldType.INT),
        FieldDef("Operator_0", FieldType.UINT),
        FieldDef("Operator_1", FieldType.UINT),
        FieldDef("Operator_2", FieldType.UINT),
        FieldDef("Operator_3", FieldType.UINT),
        FieldDef("Operator_4", FieldType.UINT),
        FieldDef("Rt_OperandType_0", FieldType.UINT),
        FieldDef("Rt_OperandType_1", FieldType.UINT),
        FieldDef("Rt_OperandType_2", FieldType.UINT),
        FieldDef("Rt_OperandType_3", FieldType.UINT),
        FieldDef("Rt_OperandType_4", FieldType.UINT),
        FieldDef("Rt_Operand_0", FieldType.INT),
        FieldDef("Rt_Operand_1", FieldType.INT),
        FieldDef("Rt_Operand_2", FieldType.INT),
        FieldDef("Rt_Operand_3", FieldType.INT),
        FieldDef("Rt_Operand_4", FieldType.INT),
        FieldDef("Logic_0", FieldType.UINT),
        FieldDef("Logic_1", FieldType.UINT),
        FieldDef("Logic_2", FieldType.UINT),
        FieldDef("Logic_3", FieldType.UINT),
        FieldDef("Logic_4", FieldType.UINT),
    ]
)

# SpellMechanic - 18 fields
BUILTIN_SCHEMAS["SpellMechanic"] = SchemaDef(
    name="SpellMechanic",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("StateName_Lang_enUS", FieldType.STRING),
        FieldDef("StateName_Lang_koKR", FieldType.STRING),
        FieldDef("StateName_Lang_frFR", FieldType.STRING),
        FieldDef("StateName_Lang_deDE", FieldType.STRING),
        FieldDef("StateName_Lang_enCN", FieldType.STRING),
        FieldDef("StateName_Lang_enTW", FieldType.STRING),
        FieldDef("StateName_Lang_esES", FieldType.STRING),
        FieldDef("StateName_Lang_esMX", FieldType.STRING),
        FieldDef("StateName_Lang_ruRU", FieldType.STRING),
        FieldDef("StateName_Lang_jaJP", FieldType.STRING),
        FieldDef("StateName_Lang_ptPT", FieldType.STRING),
        FieldDef("StateName_Lang_itIT", FieldType.STRING),
        FieldDef("StateName_Lang_Unk12", FieldType.STRING),
        FieldDef("StateName_Lang_Unk13", FieldType.STRING),
        FieldDef("StateName_Lang_Unk14", FieldType.STRING),
        FieldDef("StateName_Lang_Unk15", FieldType.STRING),
        FieldDef("StateName_Lang_Flags", FieldType.UINT),
    ]
)

# SpellMissile - 15 fields
BUILTIN_SCHEMAS["SpellMissile"] = SchemaDef(
    name="SpellMissile",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("DefaultPitchMin", FieldType.FLOAT),
        FieldDef("DefaultPitchMax", FieldType.FLOAT),
        FieldDef("DefaultSpeedMin", FieldType.FLOAT),
        FieldDef("DefaultSpeedMax", FieldType.FLOAT),
        FieldDef("RandomizeFacingMin", FieldType.FLOAT),
        FieldDef("RandomizeFacingMax", FieldType.FLOAT),
        FieldDef("RandomizePitchMin", FieldType.FLOAT),
        FieldDef("RandomizePitchMax", FieldType.FLOAT),
        FieldDef("RandomizeSpeedMin", FieldType.FLOAT),
        FieldDef("RandomizeSpeedMax", FieldType.FLOAT),
        FieldDef("Gravity", FieldType.FLOAT),
        FieldDef("MaxDuration", FieldType.FLOAT),
        FieldDef("CollisionRadius", FieldType.FLOAT),
    ]
)

# SpellMissileMotion - 5 fields
BUILTIN_SCHEMAS["SpellMissileMotion"] = SchemaDef(
    name="SpellMissileMotion",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("ScriptBody", FieldType.STRING),
        FieldDef("Flags", FieldType.INT),
        FieldDef("MissileCount", FieldType.INT),
    ]
)

# SpellRadius - 4 fields
BUILTIN_SCHEMAS["SpellRadius"] = SchemaDef(
    name="SpellRadius",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Radius", FieldType.FLOAT),
        FieldDef("RadiusPerLevel", FieldType.FLOAT),
        FieldDef("RadiusMax", FieldType.FLOAT),
    ]
)

# SpellRange - 40 fields
BUILTIN_SCHEMAS["SpellRange"] = SchemaDef(
    name="SpellRange",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("RangeMin_0", FieldType.FLOAT),
        FieldDef("RangeMin_1", FieldType.FLOAT),
        FieldDef("RangeMax_0", FieldType.FLOAT),
        FieldDef("RangeMax_1", FieldType.FLOAT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("DisplayName_Lang_enUS", FieldType.STRING),
        FieldDef("DisplayName_Lang_koKR", FieldType.STRING),
        FieldDef("DisplayName_Lang_frFR", FieldType.STRING),
        FieldDef("DisplayName_Lang_deDE", FieldType.STRING),
        FieldDef("DisplayName_Lang_enCN", FieldType.STRING),
        FieldDef("DisplayName_Lang_enTW", FieldType.STRING),
        FieldDef("DisplayName_Lang_esES", FieldType.STRING),
        FieldDef("DisplayName_Lang_esMX", FieldType.STRING),
        FieldDef("DisplayName_Lang_ruRU", FieldType.STRING),
        FieldDef("DisplayName_Lang_jaJP", FieldType.STRING),
        FieldDef("DisplayName_Lang_ptPT", FieldType.STRING),
        FieldDef("DisplayName_Lang_itIT", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk12", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk13", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk14", FieldType.STRING),
        FieldDef("DisplayName_Lang_Unk15", FieldType.STRING),
        FieldDef("DisplayName_Lang_Flags", FieldType.UINT),
        FieldDef("DisplayNameShort_Lang_enUS", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_koKR", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_frFR", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_deDE", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_enCN", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_enTW", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_esES", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_esMX", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_ruRU", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_jaJP", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_ptPT", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_itIT", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_Unk12", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_Unk13", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_Unk14", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_Unk15", FieldType.STRING),
        FieldDef("DisplayNameShort_Lang_Flags", FieldType.UINT),
    ]
)

# SpellRuneCost - 5 fields
BUILTIN_SCHEMAS["SpellRuneCost"] = SchemaDef(
    name="SpellRuneCost",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Blood", FieldType.INT),
        FieldDef("Unholy", FieldType.INT),
        FieldDef("Frost", FieldType.INT),
        FieldDef("RunicPower", FieldType.INT),
    ]
)

# SpellScaling - 14 fields
BUILTIN_SCHEMAS["SpellScaling"] = SchemaDef(
    name="SpellScaling",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("CastTimeMin", FieldType.INT),
        FieldDef("CastTimeMax", FieldType.INT),
        FieldDef("CastTimeMaxLevel", FieldType.INT),
        FieldDef("Class", FieldType.INT),
        FieldDef("Coefficient_0", FieldType.FLOAT),
        FieldDef("Coefficient_1", FieldType.FLOAT),
        FieldDef("Coefficient_2", FieldType.FLOAT),
        FieldDef("Variance_0", FieldType.FLOAT),
        FieldDef("Variance_1", FieldType.FLOAT),
        FieldDef("Variance_2", FieldType.FLOAT),
        FieldDef("ComboPointsCoefficient_0", FieldType.FLOAT),
        FieldDef("ComboPointsCoefficient_1", FieldType.FLOAT),
        FieldDef("ComboPointsCoefficient_2", FieldType.FLOAT),
    ]
)

# SpellShapeshiftForm - 35 fields
BUILTIN_SCHEMAS["SpellShapeshiftForm"] = SchemaDef(
    name="SpellShapeshiftForm",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("BonusActionBar", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("CreatureType", FieldType.INT),
        FieldDef("AttackIconID", FieldType.INT),
        FieldDef("CombatRoundTime", FieldType.INT),
        FieldDef("CreatureDisplayID_0", FieldType.INT),
        FieldDef("CreatureDisplayID_1", FieldType.INT),
        FieldDef("CreatureDisplayID_2", FieldType.INT),
        FieldDef("CreatureDisplayID_3", FieldType.INT),
        FieldDef("PresetSpellID_0", FieldType.INT),
        FieldDef("PresetSpellID_1", FieldType.INT),
        FieldDef("PresetSpellID_2", FieldType.INT),
        FieldDef("PresetSpellID_3", FieldType.INT),
        FieldDef("PresetSpellID_4", FieldType.INT),
        FieldDef("PresetSpellID_5", FieldType.INT),
        FieldDef("PresetSpellID_6", FieldType.INT),
        FieldDef("PresetSpellID_7", FieldType.INT),
    ]
)

# SpellVisual - 32 fields
BUILTIN_SCHEMAS["SpellVisual"] = SchemaDef(
    name="SpellVisual",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("PrecastKit", FieldType.INT),
        FieldDef("CastKit", FieldType.INT),
        FieldDef("ImpactKit", FieldType.INT),
        FieldDef("StateKit", FieldType.INT),
        FieldDef("StateDoneKit", FieldType.INT),
        FieldDef("ChannelKit", FieldType.INT),
        FieldDef("HasMissile", FieldType.INT),
        FieldDef("MissileModel", FieldType.INT),
        FieldDef("MissilePathType", FieldType.INT),
        FieldDef("MissileDestinationAttachment", FieldType.INT),
        FieldDef("MissileSound", FieldType.INT),
        FieldDef("AnimEventSoundID", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("CasterImpactKit", FieldType.INT),
        FieldDef("TargetImpactKit", FieldType.INT),
        FieldDef("MissileAttachment", FieldType.INT),
        FieldDef("MissileFollowGroundHeight", FieldType.INT),
        FieldDef("MissileFollowGroundDropSpeed", FieldType.INT),
        FieldDef("MissileFollowGroundApproach", FieldType.INT),
        FieldDef("MissileFollowGroundFlags", FieldType.INT),
        FieldDef("MissileMotion", FieldType.INT),
        FieldDef("MissileTargetingKit", FieldType.INT),
        FieldDef("InstantAreaKit", FieldType.INT),
        FieldDef("ImpactAreaKit", FieldType.INT),
        FieldDef("PersistentAreaKit", FieldType.INT),
        FieldDef("MissileCastOffsetX", FieldType.FLOAT),
        FieldDef("MissileCastOffsetY", FieldType.FLOAT),
        FieldDef("MissileCastOffsetZ", FieldType.FLOAT),
        FieldDef("MissileImpactOffsetX", FieldType.FLOAT),
        FieldDef("MissileImpactOffsetY", FieldType.FLOAT),
        FieldDef("MissileImpactOffsetZ", FieldType.FLOAT),
    ]
)

# SpellVisualEffectName - 7 fields
BUILTIN_SCHEMAS["SpellVisualEffectName"] = SchemaDef(
    name="SpellVisualEffectName",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("FileName", FieldType.STRING),
        FieldDef("AreaEffectSize", FieldType.FLOAT),
        FieldDef("Scale", FieldType.FLOAT),
        FieldDef("MinAllowedScale", FieldType.FLOAT),
        FieldDef("MaxAllowedScale", FieldType.FLOAT),
    ]
)

# SpellVisualKit - 37 fields
BUILTIN_SCHEMAS["SpellVisualKit"] = SchemaDef(
    name="SpellVisualKit",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("StartAnimID", FieldType.INT),
        FieldDef("AnimID", FieldType.INT),
        FieldDef("HeadEffect", FieldType.INT),
        FieldDef("ChestEffect", FieldType.INT),
        FieldDef("BaseEffect", FieldType.INT),
        FieldDef("LeftHandEffect", FieldType.INT),
        FieldDef("RightHandEffect", FieldType.INT),
        FieldDef("BreathEffect", FieldType.INT),
        FieldDef("LeftWeaponEffect", FieldType.INT),
        FieldDef("RightWeaponEffect", FieldType.INT),
        FieldDef("SpecialEffect_0", FieldType.INT),
        FieldDef("SpecialEffect_1", FieldType.INT),
        FieldDef("SpecialEffect_2", FieldType.INT),
        FieldDef("WorldEffect", FieldType.INT),
        FieldDef("SoundID", FieldType.INT),
        FieldDef("ShakeID", FieldType.INT),
        FieldDef("CharProc_0", FieldType.INT),
        FieldDef("CharProc_1", FieldType.INT),
        FieldDef("CharProc_2", FieldType.INT),
        FieldDef("CharProc_3", FieldType.INT),
        FieldDef("CharParamZero_0", FieldType.FLOAT),
        FieldDef("CharParamZero_1", FieldType.FLOAT),
        FieldDef("CharParamZero_2", FieldType.FLOAT),
        FieldDef("CharParamZero_3", FieldType.FLOAT),
        FieldDef("CharParamOne_0", FieldType.FLOAT),
        FieldDef("CharParamOne_1", FieldType.FLOAT),
        FieldDef("CharParamOne_2", FieldType.FLOAT),
        FieldDef("CharParamOne_3", FieldType.FLOAT),
        FieldDef("CharParamTwo_0", FieldType.FLOAT),
        FieldDef("CharParamTwo_1", FieldType.FLOAT),
        FieldDef("CharParamTwo_2", FieldType.FLOAT),
        FieldDef("CharParamTwo_3", FieldType.FLOAT),
        FieldDef("CharParamThree_0", FieldType.FLOAT),
        FieldDef("CharParamThree_1", FieldType.FLOAT),
        FieldDef("CharParamThree_2", FieldType.FLOAT),
        FieldDef("CharParamThree_3", FieldType.FLOAT),
    ]
)

# SpellVisualKitAreaModel - 3 fields
BUILTIN_SCHEMAS["SpellVisualKitAreaModel"] = SchemaDef(
    name="SpellVisualKitAreaModel",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("EnumID", FieldType.INT),
    ]
)

# SpellVisualKitModelAttach - 10 fields
BUILTIN_SCHEMAS["SpellVisualKitModelAttach"] = SchemaDef(
    name="SpellVisualKitModelAttach",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ParentSpellVisualKitID", FieldType.INT),
        FieldDef("SpellVisualEffectNameID", FieldType.INT),
        FieldDef("AttachmentID", FieldType.INT),
        FieldDef("OffsetX", FieldType.FLOAT),
        FieldDef("OffsetY", FieldType.FLOAT),
        FieldDef("OffsetZ", FieldType.FLOAT),
        FieldDef("Yaw", FieldType.FLOAT),
        FieldDef("Pitch", FieldType.FLOAT),
        FieldDef("Roll", FieldType.FLOAT),
    ]
)

# SpellVisualPrecastTransitions - 3 fields
BUILTIN_SCHEMAS["SpellVisualPrecastTransitions"] = SchemaDef(
    name="SpellVisualPrecastTransitions",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("LoadAnimation", FieldType.STRING),
        FieldDef("HoldAnimation", FieldType.STRING),
    ]
)

# StableSlotPrices - 2 fields
BUILTIN_SCHEMAS["StableSlotPrices"] = SchemaDef(
    name="StableSlotPrices",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Cost", FieldType.INT),
    ]
)

# Startup_strings - 19 fields
BUILTIN_SCHEMAS["Startup_strings"] = SchemaDef(
    name="Startup_strings",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("Message_Lang_enUS", FieldType.STRING),
        FieldDef("Message_Lang_koKR", FieldType.STRING),
        FieldDef("Message_Lang_frFR", FieldType.STRING),
        FieldDef("Message_Lang_deDE", FieldType.STRING),
        FieldDef("Message_Lang_enCN", FieldType.STRING),
        FieldDef("Message_Lang_enTW", FieldType.STRING),
        FieldDef("Message_Lang_esES", FieldType.STRING),
        FieldDef("Message_Lang_esMX", FieldType.STRING),
        FieldDef("Message_Lang_ruRU", FieldType.STRING),
        FieldDef("Message_Lang_jaJP", FieldType.STRING),
        FieldDef("Message_Lang_ptPT", FieldType.STRING),
        FieldDef("Message_Lang_itIT", FieldType.STRING),
        FieldDef("Message_Lang_Unk12", FieldType.STRING),
        FieldDef("Message_Lang_Unk13", FieldType.STRING),
        FieldDef("Message_Lang_Unk14", FieldType.STRING),
        FieldDef("Message_Lang_Unk15", FieldType.STRING),
        FieldDef("Message_Lang_Flags", FieldType.UINT),
    ]
)

# Stationery - 4 fields
BUILTIN_SCHEMAS["Stationery"] = SchemaDef(
    name="Stationery",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ItemID", FieldType.INT),
        FieldDef("Texture", FieldType.STRING),
        FieldDef("Flags", FieldType.INT),
    ]
)

# StringLookups - 2 fields
BUILTIN_SCHEMAS["StringLookups"] = SchemaDef(
    name="StringLookups",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("String", FieldType.STRING),
    ]
)

# SummonProperties - 6 fields
BUILTIN_SCHEMAS["SummonProperties"] = SchemaDef(
    name="SummonProperties",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Control", FieldType.INT),
        FieldDef("Faction", FieldType.INT),
        FieldDef("Title", FieldType.INT),
        FieldDef("Slot", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
    ]
)

# Talent - 23 fields
BUILTIN_SCHEMAS["Talent"] = SchemaDef(
    name="Talent",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("TabID", FieldType.INT),
        FieldDef("TierID", FieldType.INT),
        FieldDef("ColumnIndex", FieldType.INT),
        FieldDef("SpellRank_0", FieldType.INT),
        FieldDef("SpellRank_1", FieldType.INT),
        FieldDef("SpellRank_2", FieldType.INT),
        FieldDef("SpellRank_3", FieldType.INT),
        FieldDef("SpellRank_4", FieldType.INT),
        FieldDef("SpellRank_5", FieldType.INT),
        FieldDef("SpellRank_6", FieldType.INT),
        FieldDef("SpellRank_7", FieldType.INT),
        FieldDef("SpellRank_8", FieldType.INT),
        FieldDef("PrereqTalent_0", FieldType.INT),
        FieldDef("PrereqTalent_1", FieldType.INT),
        FieldDef("PrereqTalent_2", FieldType.INT),
        FieldDef("PrereqRank_0", FieldType.INT),
        FieldDef("PrereqRank_1", FieldType.INT),
        FieldDef("PrereqRank_2", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("RequiredSpellID", FieldType.INT),
        FieldDef("CategoryMask_0", FieldType.INT),
        FieldDef("CategoryMask_1", FieldType.INT),
    ]
)

# TalentTab - 24 fields
BUILTIN_SCHEMAS["TalentTab"] = SchemaDef(
    name="TalentTab",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("SpellIconID", FieldType.INT),
        FieldDef("RaceMask", FieldType.INT),
        FieldDef("ClassMask", FieldType.INT),
        FieldDef("PetTalentMask", FieldType.INT),
        FieldDef("OrderIndex", FieldType.INT),
        FieldDef("BackgroundFile", FieldType.STRING),
    ]
)

# TaxiNodes - 24 fields
BUILTIN_SCHEMAS["TaxiNodes"] = SchemaDef(
    name="TaxiNodes",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ContinentID", FieldType.INT),
        FieldDef("X", FieldType.FLOAT),
        FieldDef("Y", FieldType.FLOAT),
        FieldDef("Z", FieldType.FLOAT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("MountCreatureID_0", FieldType.INT),
        FieldDef("MountCreatureID_1", FieldType.INT),
    ]
)

# TaxiPath - 4 fields
BUILTIN_SCHEMAS["TaxiPath"] = SchemaDef(
    name="TaxiPath",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("FromTaxiNode", FieldType.INT),
        FieldDef("ToTaxiNode", FieldType.INT),
        FieldDef("Cost", FieldType.INT),
    ]
)

# TaxiPathNode - 11 fields
BUILTIN_SCHEMAS["TaxiPathNode"] = SchemaDef(
    name="TaxiPathNode",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("PathID", FieldType.INT),
        FieldDef("NodeIndex", FieldType.INT),
        FieldDef("ContinentID", FieldType.INT),
        FieldDef("LocX", FieldType.FLOAT),
        FieldDef("LocY", FieldType.FLOAT),
        FieldDef("LocZ", FieldType.FLOAT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("Delay", FieldType.INT),
        FieldDef("ArrivalEventID", FieldType.INT),
        FieldDef("DepartureEventID", FieldType.INT),
    ]
)

# TeamContributionPoints - 2 fields
BUILTIN_SCHEMAS["TeamContributionPoints"] = SchemaDef(
    name="TeamContributionPoints",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Data", FieldType.FLOAT),
    ]
)

# Terraintype - 7 fields
BUILTIN_SCHEMAS["Terraintype"] = SchemaDef(
    name="Terraintype",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("TerrainID", FieldType.INT),
        FieldDef("TerrainDesc", FieldType.STRING),
        FieldDef("FootstepSprayRun", FieldType.INT),
        FieldDef("FootstepSprayWalk", FieldType.INT),
        FieldDef("SoundID", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
    ]
)

# TerraintypeSounds - 1 fields
BUILTIN_SCHEMAS["TerraintypeSounds"] = SchemaDef(
    name="TerraintypeSounds",
    fields=[
        FieldDef("ID", FieldType.INT),
    ]
)

# TotemCategory - 20 fields
BUILTIN_SCHEMAS["TotemCategory"] = SchemaDef(
    name="TotemCategory",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name_Lang_enUS", FieldType.STRING),
        FieldDef("Name_Lang_koKR", FieldType.STRING),
        FieldDef("Name_Lang_frFR", FieldType.STRING),
        FieldDef("Name_Lang_deDE", FieldType.STRING),
        FieldDef("Name_Lang_enCN", FieldType.STRING),
        FieldDef("Name_Lang_enTW", FieldType.STRING),
        FieldDef("Name_Lang_esES", FieldType.STRING),
        FieldDef("Name_Lang_esMX", FieldType.STRING),
        FieldDef("Name_Lang_ruRU", FieldType.STRING),
        FieldDef("Name_Lang_jaJP", FieldType.STRING),
        FieldDef("Name_Lang_ptPT", FieldType.STRING),
        FieldDef("Name_Lang_itIT", FieldType.STRING),
        FieldDef("Name_Lang_Unk12", FieldType.STRING),
        FieldDef("Name_Lang_Unk13", FieldType.STRING),
        FieldDef("Name_Lang_Unk14", FieldType.STRING),
        FieldDef("Name_Lang_Unk15", FieldType.STRING),
        FieldDef("Name_Lang_Flags", FieldType.UINT),
        FieldDef("TotemCategoryType", FieldType.INT),
        FieldDef("TotemCategoryMask", FieldType.INT),
    ]
)

# TransportAnimation - 7 fields
BUILTIN_SCHEMAS["TransportAnimation"] = SchemaDef(
    name="TransportAnimation",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("TransportID", FieldType.INT),
        FieldDef("TimeIndex", FieldType.INT),
        FieldDef("PosX", FieldType.FLOAT),
        FieldDef("PosY", FieldType.FLOAT),
        FieldDef("PosZ", FieldType.FLOAT),
        FieldDef("SequenceID", FieldType.INT),
    ]
)

# TransportPhysics - 11 fields
BUILTIN_SCHEMAS["TransportPhysics"] = SchemaDef(
    name="TransportPhysics",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("WaveAmp", FieldType.FLOAT),
        FieldDef("WaveTimeScale", FieldType.FLOAT),
        FieldDef("RollAmp", FieldType.FLOAT),
        FieldDef("RollTimeScale", FieldType.FLOAT),
        FieldDef("PitchAmp", FieldType.FLOAT),
        FieldDef("PitchTimeScale", FieldType.FLOAT),
        FieldDef("MaxBank", FieldType.FLOAT),
        FieldDef("MaxBankTurnSpeed", FieldType.FLOAT),
        FieldDef("SpeedDampThresh", FieldType.FLOAT),
        FieldDef("SpeedDamp", FieldType.FLOAT),
    ]
)

# TransportRotation - 7 fields
BUILTIN_SCHEMAS["TransportRotation"] = SchemaDef(
    name="TransportRotation",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("GameObjectsID", FieldType.INT),
        FieldDef("TimeIndex", FieldType.INT),
        FieldDef("RotX", FieldType.FLOAT),
        FieldDef("RotY", FieldType.FLOAT),
        FieldDef("RotZ", FieldType.FLOAT),
        FieldDef("RotW", FieldType.FLOAT),
    ]
)

# UISoundLookups - 3 fields
BUILTIN_SCHEMAS["UISoundLookups"] = SchemaDef(
    name="UISoundLookups",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SoundID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
    ]
)

# UnitBlood - 10 fields
BUILTIN_SCHEMAS["UnitBlood"] = SchemaDef(
    name="UnitBlood",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("CombatBloodSpurtFront_0", FieldType.INT),
        FieldDef("CombatBloodSpurtFront_1", FieldType.INT),
        FieldDef("CombatBloodSpurtBack_0", FieldType.INT),
        FieldDef("CombatBloodSpurtBack_1", FieldType.INT),
        FieldDef("GroundBlood_0", FieldType.STRING),
        FieldDef("GroundBlood_1", FieldType.STRING),
        FieldDef("GroundBlood_2", FieldType.STRING),
        FieldDef("GroundBlood_3", FieldType.STRING),
        FieldDef("GroundBlood_4", FieldType.STRING),
    ]
)

# UnitBloodLevels - 4 fields
BUILTIN_SCHEMAS["UnitBloodLevels"] = SchemaDef(
    name="UnitBloodLevels",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Violencelevel_0", FieldType.INT),
        FieldDef("Violencelevel_1", FieldType.INT),
        FieldDef("Violencelevel_2", FieldType.INT),
    ]
)

# Vehicle - 40 fields
BUILTIN_SCHEMAS["Vehicle"] = SchemaDef(
    name="Vehicle",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("TurnSpeed", FieldType.FLOAT),
        FieldDef("PitchSpeed", FieldType.FLOAT),
        FieldDef("PitchMin", FieldType.FLOAT),
        FieldDef("PitchMax", FieldType.FLOAT),
        FieldDef("SeatID_0", FieldType.INT),
        FieldDef("SeatID_1", FieldType.INT),
        FieldDef("SeatID_2", FieldType.INT),
        FieldDef("SeatID_3", FieldType.INT),
        FieldDef("SeatID_4", FieldType.INT),
        FieldDef("SeatID_5", FieldType.INT),
        FieldDef("SeatID_6", FieldType.INT),
        FieldDef("SeatID_7", FieldType.INT),
        FieldDef("MouseLookOffsetPitch", FieldType.FLOAT),
        FieldDef("CameraFadeDistScalarMin", FieldType.FLOAT),
        FieldDef("CameraFadeDistScalarMax", FieldType.FLOAT),
        FieldDef("CameraPitchOffset", FieldType.FLOAT),
        FieldDef("FacingLimitRight", FieldType.FLOAT),
        FieldDef("FacingLimitLeft", FieldType.FLOAT),
        FieldDef("MsslTrgtTurnLingering", FieldType.FLOAT),
        FieldDef("MsslTrgtPitchLingering", FieldType.FLOAT),
        FieldDef("MsslTrgtMouseLingering", FieldType.FLOAT),
        FieldDef("MsslTrgtEndOpacity", FieldType.FLOAT),
        FieldDef("MsslTrgtArcSpeed", FieldType.FLOAT),
        FieldDef("MsslTrgtArcRepeat", FieldType.FLOAT),
        FieldDef("MsslTrgtArcWidth", FieldType.FLOAT),
        FieldDef("MsslTrgtImpactRadius_0", FieldType.FLOAT),
        FieldDef("MsslTrgtImpactRadius_1", FieldType.FLOAT),
        FieldDef("MsslTrgtArcTexture", FieldType.STRING),
        FieldDef("MsslTrgtImpactTexture", FieldType.STRING),
        FieldDef("MsslTrgtImpactModel_0", FieldType.STRING),
        FieldDef("MsslTrgtImpactModel_1", FieldType.STRING),
        FieldDef("CameraYawOffset", FieldType.FLOAT),
        FieldDef("UilocomotionType", FieldType.INT),
        FieldDef("MsslTrgtImpactTexRadius", FieldType.FLOAT),
        FieldDef("VehicleUIIndicatorID", FieldType.INT),
        FieldDef("PowerDisplayID_0", FieldType.INT),
        FieldDef("PowerDisplayID_1", FieldType.INT),
        FieldDef("PowerDisplayID_2", FieldType.INT),
    ]
)

# VehicleSeat - 58 fields
BUILTIN_SCHEMAS["VehicleSeat"] = SchemaDef(
    name="VehicleSeat",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("AttachmentID", FieldType.INT),
        FieldDef("AttachmentOffsetX", FieldType.FLOAT),
        FieldDef("AttachmentOffsetY", FieldType.FLOAT),
        FieldDef("AttachmentOffsetZ", FieldType.FLOAT),
        FieldDef("EnterPreDelay", FieldType.FLOAT),
        FieldDef("EnterSpeed", FieldType.FLOAT),
        FieldDef("EnterGravity", FieldType.FLOAT),
        FieldDef("EnterMinDuration", FieldType.FLOAT),
        FieldDef("EnterMaxDuration", FieldType.FLOAT),
        FieldDef("EnterMinArcHeight", FieldType.FLOAT),
        FieldDef("EnterMaxArcHeight", FieldType.FLOAT),
        FieldDef("EnterAnimStart", FieldType.INT),
        FieldDef("EnterAnimLoop", FieldType.INT),
        FieldDef("RideAnimStart", FieldType.INT),
        FieldDef("RideAnimLoop", FieldType.INT),
        FieldDef("RideUpperAnimStart", FieldType.INT),
        FieldDef("RideUpperAnimLoop", FieldType.INT),
        FieldDef("ExitPreDelay", FieldType.FLOAT),
        FieldDef("ExitSpeed", FieldType.FLOAT),
        FieldDef("ExitGravity", FieldType.FLOAT),
        FieldDef("ExitMinDuration", FieldType.FLOAT),
        FieldDef("ExitMaxDuration", FieldType.FLOAT),
        FieldDef("ExitMinArcHeight", FieldType.FLOAT),
        FieldDef("ExitMaxArcHeight", FieldType.FLOAT),
        FieldDef("ExitAnimStart", FieldType.INT),
        FieldDef("ExitAnimLoop", FieldType.INT),
        FieldDef("ExitAnimEnd", FieldType.INT),
        FieldDef("PassengerYaw", FieldType.FLOAT),
        FieldDef("PassengerPitch", FieldType.FLOAT),
        FieldDef("PassengerRoll", FieldType.FLOAT),
        FieldDef("PassengerAttachmentID", FieldType.INT),
        FieldDef("VehicleEnterAnim", FieldType.INT),
        FieldDef("VehicleExitAnim", FieldType.INT),
        FieldDef("VehicleRideAnimLoop", FieldType.INT),
        FieldDef("VehicleEnterAnimBone", FieldType.INT),
        FieldDef("VehicleExitAnimBone", FieldType.INT),
        FieldDef("VehicleRideAnimLoopBone", FieldType.INT),
        FieldDef("VehicleEnterAnimDelay", FieldType.FLOAT),
        FieldDef("VehicleExitAnimDelay", FieldType.FLOAT),
        FieldDef("VehicleAbilityDisplay", FieldType.INT),
        FieldDef("EnterUISoundID", FieldType.INT),
        FieldDef("ExitUISoundID", FieldType.INT),
        FieldDef("UiSkin", FieldType.INT),
        FieldDef("FlagsB", FieldType.INT),
        FieldDef("CameraEnteringDelay", FieldType.FLOAT),
        FieldDef("CameraEnteringDuration", FieldType.FLOAT),
        FieldDef("CameraExitingDelay", FieldType.FLOAT),
        FieldDef("CameraExitingDuration", FieldType.FLOAT),
        FieldDef("CameraOffsetX", FieldType.FLOAT),
        FieldDef("CameraOffsetY", FieldType.FLOAT),
        FieldDef("CameraOffsetZ", FieldType.FLOAT),
        FieldDef("CameraPosChaseRate", FieldType.FLOAT),
        FieldDef("CameraFacingChaseRate", FieldType.FLOAT),
        FieldDef("CameraEnteringZoom", FieldType.FLOAT),
        FieldDef("CameraSeatZoomMin", FieldType.FLOAT),
        FieldDef("CameraSeatZoomMax", FieldType.FLOAT),
    ]
)

# VehicleUIIndSeat - 5 fields
BUILTIN_SCHEMAS["VehicleUIIndSeat"] = SchemaDef(
    name="VehicleUIIndSeat",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("VehicleUIIndicatorID", FieldType.INT),
        FieldDef("VirtualSeatIndex", FieldType.INT),
        FieldDef("XPos", FieldType.FLOAT),
        FieldDef("YPos", FieldType.FLOAT),
    ]
)

# VehicleUIIndicator - 2 fields
BUILTIN_SCHEMAS["VehicleUIIndicator"] = SchemaDef(
    name="VehicleUIIndicator",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("BackgroundTexture", FieldType.STRING),
    ]
)

# VideoHardware - 23 fields
BUILTIN_SCHEMAS["VideoHardware"] = SchemaDef(
    name="VideoHardware",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("VendorID", FieldType.INT),
        FieldDef("DeviceID", FieldType.INT),
        FieldDef("FarclipIdx", FieldType.INT),
        FieldDef("TerrainLODDistIdx", FieldType.INT),
        FieldDef("TerrainShadowLOD", FieldType.INT),
        FieldDef("DetailDoodadDensityIdx", FieldType.INT),
        FieldDef("DetailDoodadAlpha", FieldType.INT),
        FieldDef("AnimatingDoodadIdx", FieldType.INT),
        FieldDef("Trilinear", FieldType.INT),
        FieldDef("NumLights", FieldType.INT),
        FieldDef("Specularity", FieldType.INT),
        FieldDef("WaterLODIdx", FieldType.INT),
        FieldDef("ParticleDensityIdx", FieldType.INT),
        FieldDef("UnitDrawDistIdx", FieldType.INT),
        FieldDef("SmallCullDistIdx", FieldType.INT),
        FieldDef("ResolutionIdx", FieldType.INT),
        FieldDef("BaseMipLevel", FieldType.INT),
        FieldDef("OglOverrides", FieldType.STRING),
        FieldDef("D3dOverrides", FieldType.STRING),
        FieldDef("FixLag", FieldType.INT),
        FieldDef("Multisample", FieldType.INT),
        FieldDef("Atlasdisable", FieldType.INT),
    ]
)

# VocalUISounds - 7 fields
BUILTIN_SCHEMAS["VocalUISounds"] = SchemaDef(
    name="VocalUISounds",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("VocalUIEnum", FieldType.INT),
        FieldDef("RaceID", FieldType.INT),
        FieldDef("NormalSoundID_0", FieldType.INT),
        FieldDef("NormalSoundID_1", FieldType.INT),
        FieldDef("PissedSoundID_0", FieldType.INT),
        FieldDef("PissedSoundID_1", FieldType.INT),
    ]
)

# WMOAreaTable - 28 fields
BUILTIN_SCHEMAS["WMOAreaTable"] = SchemaDef(
    name="WMOAreaTable",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("WMOID", FieldType.INT),
        FieldDef("NameSetID", FieldType.INT),
        FieldDef("WMOGroupID", FieldType.INT),
        FieldDef("SoundProviderPref", FieldType.INT),
        FieldDef("SoundProviderPrefUnderwater", FieldType.INT),
        FieldDef("AmbienceID", FieldType.INT),
        FieldDef("ZoneMusic", FieldType.INT),
        FieldDef("IntroSound", FieldType.INT),
        FieldDef("Flags", FieldType.INT),
        FieldDef("AreaTableID", FieldType.INT),
        FieldDef("AreaName_Lang_enUS", FieldType.STRING),
        FieldDef("AreaName_Lang_koKR", FieldType.STRING),
        FieldDef("AreaName_Lang_frFR", FieldType.STRING),
        FieldDef("AreaName_Lang_deDE", FieldType.STRING),
        FieldDef("AreaName_Lang_enCN", FieldType.STRING),
        FieldDef("AreaName_Lang_enTW", FieldType.STRING),
        FieldDef("AreaName_Lang_esES", FieldType.STRING),
        FieldDef("AreaName_Lang_esMX", FieldType.STRING),
        FieldDef("AreaName_Lang_ruRU", FieldType.STRING),
        FieldDef("AreaName_Lang_jaJP", FieldType.STRING),
        FieldDef("AreaName_Lang_ptPT", FieldType.STRING),
        FieldDef("AreaName_Lang_itIT", FieldType.STRING),
        FieldDef("AreaName_Lang_Unk12", FieldType.STRING),
        FieldDef("AreaName_Lang_Unk13", FieldType.STRING),
        FieldDef("AreaName_Lang_Unk14", FieldType.STRING),
        FieldDef("AreaName_Lang_Unk15", FieldType.STRING),
        FieldDef("AreaName_Lang_Flags", FieldType.UINT),
    ]
)

# WeaponImpactSounds - 23 fields
BUILTIN_SCHEMAS["WeaponImpactSounds"] = SchemaDef(
    name="WeaponImpactSounds",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("WeaponSubClassID", FieldType.INT),
        FieldDef("ParrySoundType", FieldType.INT),
        FieldDef("ImpactSoundID_0", FieldType.INT),
        FieldDef("ImpactSoundID_1", FieldType.INT),
        FieldDef("ImpactSoundID_2", FieldType.INT),
        FieldDef("ImpactSoundID_3", FieldType.INT),
        FieldDef("ImpactSoundID_4", FieldType.INT),
        FieldDef("ImpactSoundID_5", FieldType.INT),
        FieldDef("ImpactSoundID_6", FieldType.INT),
        FieldDef("ImpactSoundID_7", FieldType.INT),
        FieldDef("ImpactSoundID_8", FieldType.INT),
        FieldDef("ImpactSoundID_9", FieldType.INT),
        FieldDef("CritImpactSoundID_0", FieldType.INT),
        FieldDef("CritImpactSoundID_1", FieldType.INT),
        FieldDef("CritImpactSoundID_2", FieldType.INT),
        FieldDef("CritImpactSoundID_3", FieldType.INT),
        FieldDef("CritImpactSoundID_4", FieldType.INT),
        FieldDef("CritImpactSoundID_5", FieldType.INT),
        FieldDef("CritImpactSoundID_6", FieldType.INT),
        FieldDef("CritImpactSoundID_7", FieldType.INT),
        FieldDef("CritImpactSoundID_8", FieldType.INT),
        FieldDef("CritImpactSoundID_9", FieldType.INT),
    ]
)

# WeaponSwingSounds2 - 4 fields
BUILTIN_SCHEMAS["WeaponSwingSounds2"] = SchemaDef(
    name="WeaponSwingSounds2",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SwingType", FieldType.INT),
        FieldDef("Crit", FieldType.INT),
        FieldDef("SoundID", FieldType.INT),
    ]
)

# Weather - 8 fields
BUILTIN_SCHEMAS["Weather"] = SchemaDef(
    name="Weather",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("AmbienceID", FieldType.INT),
        FieldDef("EffectType", FieldType.INT),
        FieldDef("TransitionSkyBox", FieldType.FLOAT),
        FieldDef("EffectColor_0", FieldType.FLOAT),
        FieldDef("EffectColor_1", FieldType.FLOAT),
        FieldDef("EffectColor_2", FieldType.FLOAT),
        FieldDef("EffectTexture", FieldType.STRING),
    ]
)

# WorldChunkSounds - 10 fields
BUILTIN_SCHEMAS["WorldChunkSounds"] = SchemaDef(
    name="WorldChunkSounds",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("WorldMapContinentID", FieldType.INT),
        FieldDef("ChunkX", FieldType.INT),
        FieldDef("ChunkY", FieldType.INT),
        FieldDef("SubchunkX", FieldType.INT),
        FieldDef("SubchunkY", FieldType.INT),
        FieldDef("ZoneintroMusicID", FieldType.INT),
        FieldDef("ZoneMusicID", FieldType.INT),
        FieldDef("SoundAmbienceID", FieldType.INT),
        FieldDef("SoundProviderPreferencesID", FieldType.INT),
    ]
)

# WorldMapArea - 11 fields
BUILTIN_SCHEMAS["WorldMapArea"] = SchemaDef(
    name="WorldMapArea",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MapID", FieldType.INT),
        FieldDef("AreaID", FieldType.INT),
        FieldDef("AreaName", FieldType.STRING),
        FieldDef("LocLeft", FieldType.FLOAT),
        FieldDef("LocRight", FieldType.FLOAT),
        FieldDef("LocTop", FieldType.FLOAT),
        FieldDef("LocBottom", FieldType.FLOAT),
        FieldDef("DisplayMapID", FieldType.INT),
        FieldDef("DefaultDungeonFloor", FieldType.INT),
        FieldDef("ParentWorldMapID", FieldType.INT),
    ]
)

# WorldMapContinent - 14 fields
BUILTIN_SCHEMAS["WorldMapContinent"] = SchemaDef(
    name="WorldMapContinent",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MapID", FieldType.INT),
        FieldDef("LeftBoundary", FieldType.INT),
        FieldDef("RightBoundary", FieldType.INT),
        FieldDef("TopBoundary", FieldType.INT),
        FieldDef("BottomBoundary", FieldType.INT),
        FieldDef("ContinentOffsetX", FieldType.FLOAT),
        FieldDef("ContinentOffsetY", FieldType.FLOAT),
        FieldDef("Scale", FieldType.FLOAT),
        FieldDef("TaxiMinX", FieldType.FLOAT),
        FieldDef("TaxiMinY", FieldType.FLOAT),
        FieldDef("TaxiMaxX", FieldType.FLOAT),
        FieldDef("TaxiMaxY", FieldType.FLOAT),
        FieldDef("WorldMapID", FieldType.INT),
    ]
)

# WorldMapOverlay - 17 fields
BUILTIN_SCHEMAS["WorldMapOverlay"] = SchemaDef(
    name="WorldMapOverlay",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MapAreaID", FieldType.INT),
        FieldDef("AreaID_0", FieldType.INT),
        FieldDef("AreaID_1", FieldType.INT),
        FieldDef("AreaID_2", FieldType.INT),
        FieldDef("AreaID_3", FieldType.INT),
        FieldDef("MapPointX", FieldType.INT),
        FieldDef("MapPointY", FieldType.INT),
        FieldDef("TextureName", FieldType.STRING),
        FieldDef("TextureWidth", FieldType.INT),
        FieldDef("TextureHeight", FieldType.INT),
        FieldDef("OffsetX", FieldType.INT),
        FieldDef("OffsetY", FieldType.INT),
        FieldDef("HitRectTop", FieldType.INT),
        FieldDef("HitRectLeft", FieldType.INT),
        FieldDef("HitRectBottom", FieldType.INT),
        FieldDef("HitRectRight", FieldType.INT),
    ]
)

# WorldMapTransforms - 10 fields
BUILTIN_SCHEMAS["WorldMapTransforms"] = SchemaDef(
    name="WorldMapTransforms",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MapID", FieldType.INT),
        FieldDef("RegionMinX", FieldType.FLOAT),
        FieldDef("RegionMinY", FieldType.FLOAT),
        FieldDef("RegionMaxX", FieldType.FLOAT),
        FieldDef("RegionMaxY", FieldType.FLOAT),
        FieldDef("NewMapID", FieldType.INT),
        FieldDef("RegionOffsetX", FieldType.FLOAT),
        FieldDef("RegionOffsetY", FieldType.FLOAT),
        FieldDef("NewDungeonMapID", FieldType.INT),
    ]
)

# WorldSafelocs - 22 fields
BUILTIN_SCHEMAS["WorldSafelocs"] = SchemaDef(
    name="WorldSafelocs",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Continent", FieldType.INT),
        FieldDef("LocX", FieldType.FLOAT),
        FieldDef("LocY", FieldType.FLOAT),
        FieldDef("LocZ", FieldType.FLOAT),
        FieldDef("AreaName_Lang_enUS", FieldType.STRING),
        FieldDef("AreaName_Lang_koKR", FieldType.STRING),
        FieldDef("AreaName_Lang_frFR", FieldType.STRING),
        FieldDef("AreaName_Lang_deDE", FieldType.STRING),
        FieldDef("AreaName_Lang_enCN", FieldType.STRING),
        FieldDef("AreaName_Lang_enTW", FieldType.STRING),
        FieldDef("AreaName_Lang_esES", FieldType.STRING),
        FieldDef("AreaName_Lang_esMX", FieldType.STRING),
        FieldDef("AreaName_Lang_ruRU", FieldType.STRING),
        FieldDef("AreaName_Lang_jaJP", FieldType.STRING),
        FieldDef("AreaName_Lang_ptPT", FieldType.STRING),
        FieldDef("AreaName_Lang_itIT", FieldType.STRING),
        FieldDef("AreaName_Lang_Unk12", FieldType.STRING),
        FieldDef("AreaName_Lang_Unk13", FieldType.STRING),
        FieldDef("AreaName_Lang_Unk14", FieldType.STRING),
        FieldDef("AreaName_Lang_Unk15", FieldType.STRING),
        FieldDef("AreaName_Lang_Flags", FieldType.UINT),
    ]
)

# WorldStateUI - 63 fields
BUILTIN_SCHEMAS["WorldStateUI"] = SchemaDef(
    name="WorldStateUI",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("MapID", FieldType.INT),
        FieldDef("AreaID", FieldType.INT),
        FieldDef("PhaseShift", FieldType.INT),
        FieldDef("Icon", FieldType.STRING),
        FieldDef("String_Lang_enUS", FieldType.STRING),
        FieldDef("String_Lang_koKR", FieldType.STRING),
        FieldDef("String_Lang_frFR", FieldType.STRING),
        FieldDef("String_Lang_deDE", FieldType.STRING),
        FieldDef("String_Lang_enCN", FieldType.STRING),
        FieldDef("String_Lang_enTW", FieldType.STRING),
        FieldDef("String_Lang_esES", FieldType.STRING),
        FieldDef("String_Lang_esMX", FieldType.STRING),
        FieldDef("String_Lang_ruRU", FieldType.STRING),
        FieldDef("String_Lang_jaJP", FieldType.STRING),
        FieldDef("String_Lang_ptPT", FieldType.STRING),
        FieldDef("String_Lang_itIT", FieldType.STRING),
        FieldDef("String_Lang_Unk12", FieldType.STRING),
        FieldDef("String_Lang_Unk13", FieldType.STRING),
        FieldDef("String_Lang_Unk14", FieldType.STRING),
        FieldDef("String_Lang_Unk15", FieldType.STRING),
        FieldDef("String_Lang_Flags", FieldType.UINT),
        FieldDef("Tooltip_Lang_enUS", FieldType.STRING),
        FieldDef("Tooltip_Lang_koKR", FieldType.STRING),
        FieldDef("Tooltip_Lang_frFR", FieldType.STRING),
        FieldDef("Tooltip_Lang_deDE", FieldType.STRING),
        FieldDef("Tooltip_Lang_enCN", FieldType.STRING),
        FieldDef("Tooltip_Lang_enTW", FieldType.STRING),
        FieldDef("Tooltip_Lang_esES", FieldType.STRING),
        FieldDef("Tooltip_Lang_esMX", FieldType.STRING),
        FieldDef("Tooltip_Lang_ruRU", FieldType.STRING),
        FieldDef("Tooltip_Lang_jaJP", FieldType.STRING),
        FieldDef("Tooltip_Lang_ptPT", FieldType.STRING),
        FieldDef("Tooltip_Lang_itIT", FieldType.STRING),
        FieldDef("Tooltip_Lang_Unk12", FieldType.STRING),
        FieldDef("Tooltip_Lang_Unk13", FieldType.STRING),
        FieldDef("Tooltip_Lang_Unk14", FieldType.STRING),
        FieldDef("Tooltip_Lang_Unk15", FieldType.STRING),
        FieldDef("Tooltip_Lang_Flags", FieldType.UINT),
        FieldDef("StateVariable", FieldType.INT),
        FieldDef("Type", FieldType.INT),
        FieldDef("DynamicIcon", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_enUS", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_koKR", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_frFR", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_deDE", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_enCN", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_enTW", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_esES", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_esMX", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_ruRU", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_jaJP", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_ptPT", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_itIT", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_Unk12", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_Unk13", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_Unk14", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_Unk15", FieldType.STRING),
        FieldDef("DynamicTooltip_Lang_Flags", FieldType.UINT),
        FieldDef("ExtendedUI", FieldType.STRING),
        FieldDef("ExtendedUIStateVariable_0", FieldType.INT),
        FieldDef("ExtendedUIStateVariable_1", FieldType.INT),
        FieldDef("ExtendedUIStateVariable_2", FieldType.INT),
    ]
)

# WorldStateZoneSounds - 9 fields
BUILTIN_SCHEMAS["WorldStateZoneSounds"] = SchemaDef(
    name="WorldStateZoneSounds",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("WorldStateID", FieldType.INT),
        FieldDef("WorldStateValue", FieldType.INT),
        FieldDef("AreaID", FieldType.INT),
        FieldDef("WMOAreaID", FieldType.INT),
        FieldDef("ZoneintroMusicID", FieldType.INT),
        FieldDef("ZoneMusicID", FieldType.INT),
        FieldDef("SoundAmbienceID", FieldType.INT),
        FieldDef("SoundProviderPreferencesID", FieldType.INT),
    ]
)

# WowError_Strings - 19 fields
BUILTIN_SCHEMAS["WowError_Strings"] = SchemaDef(
    name="WowError_Strings",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("ErrorName", FieldType.STRING),
        FieldDef("ErrorString_enUS", FieldType.STRING),
        FieldDef("ErrorString_koKR", FieldType.STRING),
        FieldDef("ErrorString_frFR", FieldType.STRING),
        FieldDef("ErrorString_deDE", FieldType.STRING),
        FieldDef("ErrorString_enCN", FieldType.STRING),
        FieldDef("ErrorString_enTW", FieldType.STRING),
        FieldDef("ErrorString_esES", FieldType.STRING),
        FieldDef("ErrorString_esMX", FieldType.STRING),
        FieldDef("ErrorString_ruRU", FieldType.STRING),
        FieldDef("ErrorString_jaJP", FieldType.STRING),
        FieldDef("ErrorString_ptPT", FieldType.STRING),
        FieldDef("ErrorString_itIT", FieldType.STRING),
        FieldDef("ErrorString_Unk12", FieldType.STRING),
        FieldDef("ErrorString_Unk13", FieldType.STRING),
        FieldDef("ErrorString_Unk14", FieldType.STRING),
        FieldDef("ErrorString_Unk15", FieldType.STRING),
        FieldDef("ErrorString_Flags", FieldType.UINT),
    ]
)

# ZoneMusic - 8 fields
BUILTIN_SCHEMAS["ZoneMusic"] = SchemaDef(
    name="ZoneMusic",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("SetName", FieldType.STRING),
        FieldDef("SilenceintervalMin_0", FieldType.INT),
        FieldDef("SilenceintervalMin_1", FieldType.INT),
        FieldDef("SilenceintervalMax_0", FieldType.INT),
        FieldDef("SilenceintervalMax_1", FieldType.INT),
        FieldDef("Sounds_0", FieldType.INT),
        FieldDef("Sounds_1", FieldType.INT),
    ]
)

# ZoneintroMusicTable - 5 fields
BUILTIN_SCHEMAS["ZoneintroMusicTable"] = SchemaDef(
    name="ZoneintroMusicTable",
    fields=[
        FieldDef("ID", FieldType.INT),
        FieldDef("Name", FieldType.STRING),
        FieldDef("SoundID", FieldType.INT),
        FieldDef("Priority", FieldType.INT),
        FieldDef("MinDelayMinutes", FieldType.INT),
    ]
)


class SchemaManager:
    """Manages DBC schemas."""

    def __init__(self):
        self.schemas = dict(BUILTIN_SCHEMAS)

    def get_schema(self, dbc_name: str) -> Optional[SchemaDef]:
        """Get schema for a DBC file."""
        # Try exact match first
        if dbc_name in self.schemas:
            return self.schemas[dbc_name]
        # Try case-insensitive
        for name, schema in self.schemas.items():
            if name.lower() == dbc_name.lower():
                return schema
        return None

    def generate_fallback_schema(self, field_count: int, name: str = "Unknown") -> SchemaDef:
        """Generate a fallback schema with generic field names."""
        fields = [FieldDef(f"field_{i}", FieldType.UINT) for i in range(field_count)]
        return SchemaDef(name=name, fields=fields)

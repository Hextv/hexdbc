from typing import Dict

# The key relationships are derived from https://wowdev.wiki/Category:DBC_WotLK
DBC_RELATIONS: Dict[str, Dict[str, str]] = {
    # CreatureDisplayInfo - appearance info
    "CreatureDisplayInfo": {
        "ModelID": "CreatureModelData",
        "SoundID": "CreatureSoundData",
        "ExtendedDisplayInfoID": "CreatureDisplayInfoExtra",
        "BloodID": "UnitBlood",
        "NPCSoundID": "NPCSounds",
        "ParticleColorID": "ParticleColor",
        "ObjectEffectPackageID": "ObjectEffectPackage",
    },

    # CreatureModelData - model references
    "CreatureModelData": {
        "SoundID": "CreatureSoundData",
        "BloodID": "UnitBlood",
        "FootprintTextureID": "FootprintTextures",
        "FoleyMaterialID": "Material",
        "FootstepShakeSize": "CameraShakes",
        "DeathThudShakeSize": "CameraShakes",
    },

    # Items
    "Item": {
        "DisplayInfoID": "ItemDisplayInfo",
        "ClassID": "ItemClass",
    },

    "ItemDisplayInfo": {
        "SpellVisualID": "SpellVisual",
        "ItemVisual": "ItemVisuals",
        "ParticleColorID": "ParticleColor",
    },

    # Races
    "ChrRaces": {
        "FactionID": "Faction",
        "MaleDisplayId": "CreatureDisplayInfo",
        "FemaleDisplayId": "CreatureDisplayInfo",
        "ExplorationSoundID": "SoundEntries",
        "SplashSoundID": "SoundEntries",
        "ResSicknessSpellID": "Spell",
        "CinematicSequenceID": "CinematicSequences",
    },

    # Classes
    "ChrClasses": {
        "CinematicSequenceID": "CinematicSequences",
    },

    # Factions
    "Faction": {
        "ParentFactionID": "Faction",
    },

    # Area / zones
    "AreaTable": {
        "ContinentID": "Map",
        "ParentAreaID": "AreaTable",
        "SoundProviderPref": "SoundProviderPreferences",
        "SoundProviderPrefUnderwater": "SoundProviderPreferences",
        "AmbienceID": "SoundAmbience",
        "ZoneMusic": "ZoneMusic",
        "IntroSound": "ZoneIntroMusicTable",
        "Lightid": "Light",
    },

    # Map references
    "Map": {
        "AreaTableID": "AreaTable",
        "LoadingScreenID": "LoadingScreens",
        "CorpseMapID": "Map",
    },

    # Spells (key references only)
    "Spell": {
        "Category": "SpellCategory",
        "DispelType": "SpellDispelType",
        "Mechanic": "SpellMechanic",
        "CasterAuraSpell": "Spell",
        "TargetAuraSpell": "Spell",
        "ExcludeCasterAuraSpell": "Spell",
        "ExcludeTargetAuraSpell": "Spell",
        "CastingTimeIndex": "SpellCastTimes",
        "DurationIndex": "SpellDuration",
        "RangeIndex": "SpellRange",
        "ModalNextSpell": "Spell",
        "SpellIconID": "SpellIcon",
        "ActiveIconID": "SpellIcon",
        "RequiresSpellFocus": "SpellFocusObject",
        "RuneCostID": "SpellRuneCost",
        "SpellMissileID": "SpellMissile",
        "PowerDisplayID": "PowerDisplay",
        "SpellDescriptionVariableID": "SpellDescriptionVariables",
        "SpellDifficultyID": "SpellDifficulty",
    },

    # Talent trees
    "Talent": {
        "TabID": "TalentTab",
        "RequiredSpellID": "Spell",
    },

    "TalentTab": {
        "SpellIconID": "SpellIcon",
    },

    # Achievements
    "Achievement": {
        "Instance_Id": "Map",
        "Supercedes": "Achievement",
        "Category": "Achievement_Category",
        "IconID": "SpellIcon",
        "Shares_Criteria": "Achievement",
    },

    "Achievement_Category": {
        "Parent": "Achievement_Category",
    },

    "Achievement_Criteria": {
        "Achievement_Id": "Achievement",
    },
}


def get_reference(dbc_name: str, field_name: str) -> str | None:

    if "_" in field_name and field_name.rsplit("_", 1)[1].isdigit():
        base_field = field_name.rsplit("_", 1)[0]
    else:
        base_field = field_name

    relations = DBC_RELATIONS.get(dbc_name, {})
    target = relations.get(field_name) or relations.get(base_field)
    return target


def get_all_references(dbc_name: str) -> Dict[str, str]:
    return dict(DBC_RELATIONS.get(dbc_name, {}))

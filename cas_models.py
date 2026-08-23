from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, Field


class ControlType(str, Enum):
    TYPE_1 = "Type 1"
    TYPE_2 = "Type 2"
    TYPE_3 = "Type 3"


class MethodOfAttack(str, Enum):
    BOT = "Bomb on Target"
    BOC = "Bomb on Coordinate"


class CheckInBrief(BaseModel):
    """MNPOPA Check-In Structure for CAS Aircraft"""
    callsign: str = Field(..., description="Aircraft Call Sign (e.g., Slayer 01)")
    mission_number: str = Field(..., description="Mission/Flight designation")
    number_type_aircraft: str = Field(..., description="Number & Type of aircraft (e.g., 2x AH-64)")
    position: str = Field(..., description="Current holding area/position")
    ordnance: str = Field(..., description="Available weapons loadout")
    playtime: str = Field(..., description="Remaining time on station")
    capabilities: str = Field(..., description="Sensors and limitations (NVG, FLIR, etc.)")


class NineLineBrief(BaseModel):
    """NATO / Joint Standard 9-Line CAS Briefing"""
    line1_ip_bp: str = Field(..., description="IP or Battle Position (BP)")
    line2_heading_offset: str = Field(..., description="Heading in degrees & Offset")
    line3_distance: str = Field(..., description="Distance in meters/nautical miles")
    line4_elevation: str = Field(..., description="Target Elevation (Feet MSL) - Mandatory Readback")
    line5_description: str = Field(..., description="Target Description")
    line6_location: str = Field(..., description="Target Location (MGRS/Grid) - Mandatory Readback")
    line7_mark_type: str = Field(..., description="Target Mark Type (WP, Laser Code, IR)")
    line8_friendlies: str = Field(..., description="Friendly location relative to target")
    line9_egress: str = Field(..., description="Egress direction/routing")
    remarks: Optional[str] = Field(None, description="Remarks, Danger Close, TOT")
    restrictions: Optional[str] = Field(None, description="FAH, Cleared Hot conditions - Mandatory Readback")


class ReadbackVerification(BaseModel):
    line4_correct: bool
    line6_correct: bool
    restrictions_correct: bool
    is_valid: bool
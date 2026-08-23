import re
from cas_models import NineLineBrief, ReadbackVerification

class CASEngine:
    """Core Engine to validate CAS Readbacks and Brevity Codes"""

    @staticmethod
    def verify_readback(brief: NineLineBrief, readback_text: str) -> ReadbackVerification:
        """
        Validates if pilot's readback correctly includes mandatory items:
        Line 4 (Elevation), Line 6 (Grid Location), and Restrictions.
        """
        # Clean text for checking
        text = readback_text.lower()
        
        # Simple extraction check (Can be enhanced with NLP)
        line4_match = brief.line4_elevation.lower() in text or any(char.isdigit() for char in brief.line4_elevation)
        line6_match = brief.line6_location.replace(" ", "").lower() in text.replace(" ", "")
        
        restrictions_match = True
        if brief.restrictions:
            restrictions_match = brief.restrictions.lower() in text

        is_valid = line4_match and line6_match and restrictions_match

        return ReadbackVerification(
            line4_correct=line4_match,
            line6_correct=line6_match,
            restrictions_correct=restrictions_match,
            is_valid=is_valid
        )

# --- Example Usage ---
if __name__ == "__main__":
    # Create sample 9-Line from JTAC
    sample_9line = NineLineBrief(
        line1_ip_bp="BP Python",
        line2_heading_offset="240 degrees",
        line3_distance="1500 meters",
        line4_elevation="350 FT",
        line5_description="1x BMP Armored Vehicle",
        line6_location="UT 12345678",
        line7_mark_type="Laser Code 1688",
        line8_friendlies="South 400m",
        line9_egress="North",
        remarks="Danger Close",
        restrictions="FAH 360"
    )

    # Simulated Pilot Readback
    pilot_readback = "Slayer 01 readback: Elevation 350 FT, Grid UT 12345678, FAH 360"

    # Validate
    result = CASEngine.verify_readback(sample_9line, pilot_readback)
    print(f"Readback Valid: {result.is_valid}")
    print(f"Details: {result.model_dump_json(indent=2)}")
"""
Bag model for Legend of Dragon's Legacy.

Each character has exactly 2 bag slots for consumable items.
Slot capacities:
  - HP Potion / Mana Potion: max 12 per slot
  - Power Potion: max 7 per slot
"""

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from dragons_legacy.database import Base


# Max quantities per slot by item name
BAG_SLOT_MAX = {
    "HP Potion": 12,
    "Mana Potion": 12,
    "Power Potion": 7,
}

BAG_SLOT_COUNT = 2  # Total number of bag slots


class BagSlot(Base):
    __tablename__ = "bag_slots"

    id = Column(Integer, primary_key=True, index=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    slot_index = Column(Integer, nullable=False)  # 0 or 1
    item_catalog_id = Column(Integer, nullable=True)  # None = empty slot
    quantity = Column(Integer, default=0)

    # Relationships
    character = relationship("Character", back_populates="bag_slots")

    def __repr__(self):
        return (
            "<BagSlot(id=" + str(self.id)
            + ", character_id=" + str(self.character_id)
            + ", slot=" + str(self.slot_index)
            + ", item=" + str(self.item_catalog_id)
            + ", qty=" + str(self.quantity) + ")>"
        )
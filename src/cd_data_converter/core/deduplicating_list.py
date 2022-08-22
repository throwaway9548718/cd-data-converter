from typing import Any, Dict, List

from pybloom import ScalableBloomFilter


class DeduplicatingList:
    """
    A list-like datastructure that tracks if the same value has previously been appended to it.
    """

    def __init__(self) -> None:
        self._values: List[Dict] = []
        self._filter = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)

    @property
    def values(self) -> List[Dict]:
        """The content of the list."""
        return self._values

    def append(self, value: Any) -> bool:
        """
        Add a new value to the list.

        Args:
            value: The value to be added.

        Returns:
            True if value was new and subsequently added, else False.
        """
        if value not in self._filter:
            return self._append(value)
        if value not in self._values:
            return self._append(value)
        return False

    def _append(self, value: Any) -> bool:
        self._filter.add(value)
        self._values.append(value)
        return True

    def __repr__(self) -> str:
        return str(self._values)

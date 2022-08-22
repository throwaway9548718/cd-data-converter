import logging
from typing import Dict, List, Optional, Set

import defusedxml.ElementTree as ET
from defusedxml.ElementTree import ParseError

from cd_data_converter.core.deduplicating_list import DeduplicatingList
from cd_data_converter.models.cd import CD


class Parser:
    def __init__(self, logger: logging.Logger, countries: Set[str]) -> None:
        self.parsed_items = DeduplicatingList()
        self.logger = logger
        self.countries = countries

    def parse_cd_catalog(self, data: str) -> List[Dict]:
        """Parse the CD catalog.

        Args:
            data: XML representing the CD catalog.

        Returns:
            Parsed CD catalog.
        """
        try:
            catalog_tree = ET.fromstring(data)
        except ParseError as e:
            self.logger.error(f"Failed to parse XML file: {e}")
            return self.parsed_items.values

        for child in catalog_tree:
            item = self.parse_cd(child)
            if item and not self.parsed_items.append(item):
                self.logger.info(f"Filtered out duplicate: {ET.tostring(child)}")

        return self.parsed_items.values

    def parse_cd(self, data: ET) -> Optional[Dict]:
        """Parse a CD element in the catalog.

        Args:
            data: XML element representing the CD.

        Returns:
            Dict representation of the CD if successful, else None.
        """
        try:
            return self._lookup_country(CD.from_orm(data).dict())
        except Exception as e:
            message = f"Failed to parse item {ET.tostring(data)}. {e.__class__.__name__}: {e}"
            self.logger.error(message)
            return None

    def _lookup_country(self, cd: Dict) -> Dict:
        if cd["origin"] not in self.countries:
            self.logger.info(f"Unknown country: {cd['origin']} in {cd}")
        return cd

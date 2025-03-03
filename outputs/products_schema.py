# generated by datamodel-codegen:
#   filename:  products.schema.json
#   timestamp: 2025-03-03T11:58:30+00:00

from __future__ import annotations

from typing import List

from pydantic import Field, RootModel


class Products(RootModel[List[str]]):
    root: List[str] = Field(
        ..., description='The products in the catalog', title='Products'
    )

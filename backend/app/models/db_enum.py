from enum import Enum

from sqlalchemy import Enum as SQLEnum


def enum_type(enum_cls: type[Enum], name: str) -> SQLEnum:
    return SQLEnum(
        enum_cls,
        name=name,
        native_enum=True,
        create_type=False,
        values_callable=lambda members: [item.value for item in members],
    )
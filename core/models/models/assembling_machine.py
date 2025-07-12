from pydantic import BaseModel, computed_field
from sympy import Rational

from core.enums.assembling_machine import AssemblingMachine as AssemblingMachineEnum
from core.enums.operation_category import OperationCategory
from core.models.data.assembling_machine import (
    ALLOWED_EFFECTS,
    CATEGORIES,
    ENERGY_USAGE_KW,
    MODULE_SLOTS,
    SPEED,
    TYPES,
)


class AssemblingMachine(BaseModel):
    id: AssemblingMachineEnum

    @computed_field(return_type=str, repr=False)  # type: ignore[prop-decorator]
    @property
    def machine_type(self) -> str:
        """
        装置のタイプを返す.
        """
        try:
            return TYPES[self.id]
        except KeyError as e:
            raise ValueError(f"Invalid machine type for: {self.id}") from e

    @computed_field(return_type=Rational, repr=False)  # type: ignore[prop-decorator]
    @property
    def speed(self) -> Rational:
        """
        装置の処理速度を返す.
        """
        try:
            return SPEED[self.id]
        except KeyError as e:
            raise ValueError(f"Invalid speed for machine: {self.id}") from e

    @computed_field(return_type=set[OperationCategory], repr=False)  # type: ignore[prop-decorator]
    @property
    def categories(self) -> set[OperationCategory]:
        """
        装置が受け入れ可能な処理カテゴリを返す.
        """
        try:
            return CATEGORIES[self.id]
        except KeyError as e:
            raise ValueError(f"Invalid categories for machine: {self.id}") from e

    @computed_field(return_type=Rational, repr=False)  # type: ignore[prop-decorator]
    @property
    def energy_usage_kw(self) -> Rational:
        """
        装置のエネルギー使用量をキロワット単位で返す.
        """
        try:
            return ENERGY_USAGE_KW[self.id]
        except KeyError as e:
            raise ValueError(f"Invalid energy usage for machine: {self.id}") from e

    @computed_field(return_type=set[str], repr=False)  # type: ignore[prop-decorator]
    @property
    def allowed_effects(self) -> set[str]:
        """
        装置が受け入れ可能な効果のセットを返す.
        """
        try:
            return ALLOWED_EFFECTS[self.id]
        except KeyError as e:
            raise ValueError(f"Invalid allowed effects for machine: {self.id}") from e

    @computed_field(return_type=int, repr=False)  # type: ignore[prop-decorator]
    @property
    def module_slots(self) -> int:
        """
        装置に装着可能なモジュールのスロット数を返す.
        """
        try:
            return MODULE_SLOTS[self.id]
        except KeyError as e:
            raise ValueError(f"Invalid module slots for machine: {self.id}") from e

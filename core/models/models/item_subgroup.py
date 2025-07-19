from pydantic import BaseModel, computed_field

from core.enums.item_subgroup import ItemSubgroup as ItemSubgroupEnum
from core.models.data.item_subgroup import GROUP_OF_SUBGROUP
from core.models.models.item_group import ItemGroup


class ItemSubgroup(BaseModel):
    id: ItemSubgroupEnum

    class Config:
        frozen = True  # ハッシュ化・キャッシュしやすくする

    @computed_field(return_type=ItemGroup, repr=False)  # type: ignore[prop-decorator]
    @property
    def group(self) -> ItemGroup:
        """
        アイテムサブグループに対応するアイテムグループを返す.
        """
        try:
            return ItemGroup(id=GROUP_OF_SUBGROUP[self.id])
        except KeyError as e:
            raise ValueError(f"Invalid item subgroup: {self.id}") from e

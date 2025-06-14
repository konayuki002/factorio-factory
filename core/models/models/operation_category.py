from pydantic import BaseModel

from core.enums.operation_category import OperationCategory as OperationCategoryEnum


class OperationCategory(BaseModel):
    id: OperationCategoryEnum

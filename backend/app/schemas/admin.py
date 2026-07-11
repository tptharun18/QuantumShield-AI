from pydantic import BaseModel, Field


class UpdateUserRole(BaseModel):
    role: str = Field(
        ...,
        description="New role for the user",
        examples=["Admin"],
    )


class UpdateUserStatus(BaseModel):
    is_active: bool = Field(
        ...,
        description="Enable or disable the user account",
        examples=[True],
    )
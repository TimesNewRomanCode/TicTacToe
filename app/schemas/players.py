from pydantic import BaseModel, Field

class RegistrationScheme(BaseModel):
    username: str = Field(..., min_length=5, max_length=50, description="Username")
    password: str = Field(
        ..., min_length=8, max_length=128, description="Password from 8 characters"
    )

class LoginScheme(BaseModel):
    username: str
    password: str

class SuccessResponse(BaseModel):
    message: str
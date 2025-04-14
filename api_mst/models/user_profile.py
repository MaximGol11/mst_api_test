from typing import List, Optional
from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from enum import Enum


# --- ENUM'ы --- #

class EmailStatusEnum(str, Enum):
    confirmation_waiting = "confirmation_waiting"
    confirmed = "confirmed"


class BonusTypeEnum(str, Enum):
    casino = "casino"
    sport = "sport"


class UserVirtualStatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"


class RegistrationMethodEnum(str, Enum):
    full = "full"
    quick = "quick"


class KycStatusEnum(str, Enum):
    not_required = "not_required"
    pending = "pending"
    verified = "verified"


# --- Подмодели --- #

class StatusValue(BaseModel):
    value: str


class Country(BaseModel):
    title: str
    title_en: str
    currency: str
    alpha2: str
    alpha3: str
    phone_prefix: int
    phone_sample: str
    phone_mask: Optional[str]
    id: int


class SecurityQuestion(BaseModel):
    id: int
    title: str
    transKey: str


class NotificationMode(BaseModel):
    value: int
    mode: str
    transKey: str


class UserProfileData(BaseModel):
    phone_number_to_check: Optional[str]
    security_questions: List[SecurityQuestion]
    ticket_notification_modes: List[NotificationMode]
    event_notification_modes: List[NotificationMode]


# --- Основная модель пользователя --- #

class UserProfile(BaseModel):
    id: int
    username: str
    email: str
    status_email: StatusValue
    selected_bonus_type: StatusValue
    is_full: bool
    ticket_notification_array: List[int]
    event_notification_array: List[int]
    currency: str
    timezone_offset: int
    nickname: Optional[str]
    user_virtual_status: UserVirtualStatusEnum
    has_extended_profile_data: bool
    city_title: Optional[str]
    phone: Optional[str]
    postal_code: Optional[str]
    user_cookie_key: Optional[str]
    email_attach_date: datetime
    country: Country
    region: Optional[str]
    city: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    patronymic: Optional[str]
    locale: str
    phone_number: Optional[str]
    date_of_birth: Optional[datetime]
    place_of_birth: Optional[str]
    passport_data: Optional[str]
    issued_date_passport: Optional[datetime]
    issued_by_passport: Optional[str]
    address_of_permanent_residence: Optional[str]
    skype: Optional[str]
    security_question: Optional[str]
    security_answer: Optional[str]
    ticket_notification: int
    event_notification: int
    favorite_sport: Optional[str]
    favorite_teams: List
    odd_format: Optional[str]
    registration_method: RegistrationMethodEnum
    sex: Optional[str]
    email_status: EmailStatusEnum
    phone_status: Optional[str]
    waiting_email_confirm: Optional[str]
    created_at: datetime
    kyc_status: KycStatusEnum
    ticket_enabled: bool
    p2p_ticket_enabled: bool
    user_profile_data: Optional[UserProfileData] = Field(None, serialization_alias="_user_profile_data")
    first_deposit_date: Optional[datetime]
    is_vip: bool


    @field_validator("created_at", mode="before")
    def convert_created_at(cls, v):
        if isinstance(v, int):
            return datetime.fromtimestamp(v)
        return v

    model_config = {
        "populate_by_name": True,
        "use_enum_values": True,
        "arbitrary_types_allowed": True,
    }

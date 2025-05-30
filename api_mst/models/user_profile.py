from typing import List, Optional
from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from enum import Enum
from enum import StrEnum

"""
{
    "id": 11896,
    "username": "17447176172551164434@yahoo.com",
    "email": null,
    "status_email": {
        "value": null
    },
    "selected_bonus_type": {
        "value": "casino"
    },
    "is_full": false,
    "ticket_notification_array": [
        1
    ],
    "event_notification_array": [
        4
    ],
    "currency": "AZN",
    "timezone_offset": 10800,
    "nickname": null,
    "user_virtual_status": "active",
    "has_extended_profile_data": false,
    "city_title": null,
    "phone": null,
    "postal_code": null,
    "user_cookie_key": null,
    "email_attach_date": null,
    "country": {
        "title": "Азербайджан",
        "title_en": "Azerbaijan",
        "currency": "AZN",
        "alpha2": "AZ",
        "alpha3": "AZE",
        "phone_prefix": 994,
        "phone_sample": "40 123 45 67",
        "phone_mask": "40 123 45 67",
        "id": 81
    },
    "region": null,
    "city": null,
    "first_name": null,
    "last_name": null,
    "patronymic": null,
    "locale": "ru",
    "phone_number": null,
    "date_of_birth": null,
    "place_of_birth": null,
    "passport_data": null,
    "issued_date_passport": null,
    "issued_by_passport": null,
    "address_of_permanent_residence": null,
    "skype": null,
    "security_question": null,
    "security_answer": null,
    "ticket_notification": 1,
    "event_notification": 1004,
    "favorite_sport": null,
    "favorite_teams": [],
    "odd_format": "decimal",
    "registration_method": "one_click",
    "sex": null,
    "email_status": null,
    "phone_status": null,
    "waiting_email_confirm": null,
    "created_at": 1744717617,
    "kyc_status": "not_required",
    "ticket_enabled": true,
    "p2p_ticket_enabled": false,
    "_user_profile_data": {
        "phone_number_to_check": null,
        "security_questions": [
            {
                "id": 0,
                "title": "Фамилия вашего любимого музыканта",
                "transKey": "Security question1"
            },
            {
                "id": 1,
                "title": "Название улицы, на которой вы выросли",
                "transKey": "Security question2"
            },
            {
                "id": 2,
                "title": "Ваш любимый киногерой",
                "transKey": "Security question3"
            },
            {
                "id": 3,
                "title": "Дата рождения бабушки",
                "transKey": "Security question4"
            },
            {
                "id": 4,
                "title": "Почтовый индекс родителей",
                "transKey": "Security question5"
            },
            {
                "id": 5,
                "title": "Марка вашей первой машины",
                "transKey": "Security question6"
            },
            {
                "id": 6,
                "title": "Фамилия вашего любимого учителя",
                "transKey": "Security question7"
            },
            {
                "id": 7,
                "title": "Ваша любимая книга в детстве",
                "transKey": "Security question8"
            },
            {
                "id": 8,
                "title": "Ваша любимая компьютерная игра",
                "transKey": "Security question9"
            }
        ],
        "ticket_notification_modes": [
            {
                "value": 1,
                "mode": "Уведомления о новых тикетах по e-mail",
                "transKey": "NOTIFICATION_TICKET_EMAIL"
            }
        ],
        "event_notification_modes": [
            {
                "value": 0,
                "mode": "Не получать",
                "transKey": "SUBSCRIPTION_NONE"
            },
            {
                "value": 1000,
                "mode": "SUBSCRIPTION_EMAIL_NEED_CONFIRMATION",
                "transKey": "SUBSCRIPTION_EMAIL_NEED_CONFIRMATION"
            },
            {
                "value": 1,
                "mode": "Получать на свой e-mail новости о событиях",
                "transKey": "SUBSCRIPTION_EVENT_EMAIL"
            },
            {
                "value": 2,
                "mode": "Получать на свой e-mail результаты моих ставок",
                "transKey": "SUBSCRIPTION_COUPON_EMAIL"
            },
            {
                "value": 4,
                "mode": "Получать информацию о рекламных акциях по смс",
                "transKey": "SUBSCRIPTION_AD_SMS"
            }
        ]
    },
    "first_deposit_date": null,
    "is_vip": false
}

"""


# --- ENUM'ы --- #

class EmailStatusEnum(StrEnum):
    confirmation_waiting = "confirmation_waiting"
    confirmed = "confirmed"


class BonusTypeEnum(StrEnum):
    casino = "casino"
    sport = "sport"


class UserVirtualStatusEnum(StrEnum):
    active = "active"
    inactive = "inactive"


class RegistrationMethodEnum(StrEnum):
    full = "full"
    quick = "mobile"


class KycStatusEnum(StrEnum):
    not_required = "not_required"
    pending = "pending"
    verified = "verified"


# --- Подмодели --- #

class StatusValue(BaseModel):
    value: Optional[str]


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
    email: Optional[str] = Field(None)
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

from typing import (
    List,
    Optional,
    Union,
    Literal,
)
from pydantic import BaseModel

"""
{
  "refillMethodList": [
    {
      "name": "credit_card_maestro",
      "title": "Maestro",
      "paymentRouteId": "377",
      "isManualPaymentMethod": false,
      "verification": {
        "required": false,
        "messageKey": "refill.route.not_available.phone_number_verification_required"
      },
      "form": {
        "action": "/api/v1/finance/refill",
        "method": "POST",
        "fieldList": [
          {
            "name": "amount",
            "title": "Amount",
            "hint": "Minimum: 2.00 EUR",
            "attr": [
              {
                "key": "max",
                "value": "3000.0000"
              },
              {
                "key": "min",
                "value": "2.0000"
              },
              {
                "key": "step",
                "value": "0.01"
              },
              {
                "key": "stepAmount",
                "value": "2.0000"
              },
              {
                "key": "lastRefill",
                "value": "0"
              },
              {
                "key": "fee",
                "value": "0"
              },
              {
                "key": "feeDescription",
                "value": ""
              }
            ],
            "quickTips": [],
            "type": "number"
          },
          {
            "name": "flowId",
            "title": "hidden",
            "value": "0",
            "type": "hidden"
          }
        ],
        "description": ""
      },
      "type": "form"
    },
  ],
  "showHowToRefillButton": false,
  "unfoldFirstRefillMethod": true
}

"""


class Attr(BaseModel):
    key: str
    value: str
    isDefault: Optional[bool] = None


class Field(BaseModel):
    name: str
    title: str
    type: str
    hint: Optional[str] = None
    value: Optional[str] = None
    countries: Optional[List] = None
    attr: List[Attr]
    quickTips: Optional[List] = []


class Link(BaseModel):
    anchor: str
    href: str


class PlankPosition(BaseModel):
    vertical: str
    horizontal: str


class Plank(BaseModel):
    type: str
    position: PlankPosition
    link: Link
    content: str


class DescriptionItem(BaseModel):
    type: str
    link: str
    link_text: str
    position: PlankPosition


class TemplateDescription(BaseModel):
    templateType: str
    parameterList: List = []


class Verification(BaseModel):
    required: bool
    messageKey: str


class Form(BaseModel):
    action: str
    method: str
    fieldList: List[Field]
    description: Optional[Union[str, List[DescriptionItem], TemplateDescription]] = None
    plank: Optional[Plank] = None


class RefillMethod(BaseModel):
    name: str
    title: str
    paymentRouteId: str
    isManualPaymentMethod: bool
    verification: Verification
    form: Form
    type: Literal[
        "form", "template_description_form", "rich_description_form"
    ]


class RefillMethodsResponse(BaseModel):
    refillMethodList: List[RefillMethod]
    showHowToRefillButton: bool
    unfoldFirstRefillMethod: bool

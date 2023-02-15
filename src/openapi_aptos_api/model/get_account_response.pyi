# coding: utf-8

"""
    aptos-api

    The aptos-api provider  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_aptos_api import schemas  # noqa: F401


class GetAccountResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "sequence_number",
            "authentication_key",
        }
        
        class properties:
            sequence_number = schemas.StrSchema
            authentication_key = schemas.StrSchema
            __annotations__ = {
                "sequence_number": sequence_number,
                "authentication_key": authentication_key,
            }
    
    sequence_number: MetaOapg.properties.sequence_number
    authentication_key: MetaOapg.properties.authentication_key
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequence_number"]) -> MetaOapg.properties.sequence_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authentication_key"]) -> MetaOapg.properties.authentication_key: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sequence_number", "authentication_key", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sequence_number"]) -> MetaOapg.properties.sequence_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authentication_key"]) -> MetaOapg.properties.authentication_key: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sequence_number", "authentication_key", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sequence_number: typing.Union[MetaOapg.properties.sequence_number, str, ],
        authentication_key: typing.Union[MetaOapg.properties.authentication_key, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetAccountResponse':
        return super().__new__(
            cls,
            *args,
            sequence_number=sequence_number,
            authentication_key=authentication_key,
            _configuration=_configuration,
            **kwargs,
        )

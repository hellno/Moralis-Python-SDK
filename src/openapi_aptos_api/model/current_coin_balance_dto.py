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


class CurrentCoinBalanceDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "last_transaction_version",
            "amount",
            "coin_type_hash",
            "last_transaction_timestamp",
            "coin_type",
            "owner_address",
        }
        
        class properties:
            
            
            class amount(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 200
                    min_length = 1
            
            
            class coin_type(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 5000
                    min_length = 1
            
            
            class coin_type_hash(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
                    min_length = 64
            last_transaction_timestamp = schemas.StrSchema
            last_transaction_version = schemas.StrSchema
            
            
            class owner_address(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 66
                    min_length = 66
            __annotations__ = {
                "amount": amount,
                "coin_type": coin_type,
                "coin_type_hash": coin_type_hash,
                "last_transaction_timestamp": last_transaction_timestamp,
                "last_transaction_version": last_transaction_version,
                "owner_address": owner_address,
            }
    
    last_transaction_version: MetaOapg.properties.last_transaction_version
    amount: MetaOapg.properties.amount
    coin_type_hash: MetaOapg.properties.coin_type_hash
    last_transaction_timestamp: MetaOapg.properties.last_transaction_timestamp
    coin_type: MetaOapg.properties.coin_type
    owner_address: MetaOapg.properties.owner_address
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coin_type"]) -> MetaOapg.properties.coin_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coin_type_hash"]) -> MetaOapg.properties.coin_type_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_transaction_timestamp"]) -> MetaOapg.properties.last_transaction_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_transaction_version"]) -> MetaOapg.properties.last_transaction_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner_address"]) -> MetaOapg.properties.owner_address: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "coin_type", "coin_type_hash", "last_transaction_timestamp", "last_transaction_version", "owner_address", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coin_type"]) -> MetaOapg.properties.coin_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coin_type_hash"]) -> MetaOapg.properties.coin_type_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_transaction_timestamp"]) -> MetaOapg.properties.last_transaction_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_transaction_version"]) -> MetaOapg.properties.last_transaction_version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner_address"]) -> MetaOapg.properties.owner_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "coin_type", "coin_type_hash", "last_transaction_timestamp", "last_transaction_version", "owner_address", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        last_transaction_version: typing.Union[MetaOapg.properties.last_transaction_version, str, ],
        amount: typing.Union[MetaOapg.properties.amount, str, ],
        coin_type_hash: typing.Union[MetaOapg.properties.coin_type_hash, str, ],
        last_transaction_timestamp: typing.Union[MetaOapg.properties.last_transaction_timestamp, str, ],
        coin_type: typing.Union[MetaOapg.properties.coin_type, str, ],
        owner_address: typing.Union[MetaOapg.properties.owner_address, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CurrentCoinBalanceDto':
        return super().__new__(
            cls,
            *args,
            last_transaction_version=last_transaction_version,
            amount=amount,
            coin_type_hash=coin_type_hash,
            last_transaction_timestamp=last_transaction_timestamp,
            coin_type=coin_type,
            owner_address=owner_address,
            _configuration=_configuration,
            **kwargs,
        )

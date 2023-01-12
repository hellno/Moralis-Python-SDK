# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.1
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

from openapi_evm_api import schemas  # noqa: F401


class Erc20Metadata(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "symbol",
            "address",
            "decimals",
            "name",
        }
        
        class properties:
            address = schemas.StrSchema
            name = schemas.StrSchema
            symbol = schemas.StrSchema
            decimals = schemas.StrSchema
            logo = schemas.StrSchema
            logo_hash = schemas.StrSchema
            thumbnail = schemas.StrSchema
            block_number = schemas.StrSchema
            validated = schemas.StrSchema
            __annotations__ = {
                "address": address,
                "name": name,
                "symbol": symbol,
                "decimals": decimals,
                "logo": logo,
                "logo_hash": logo_hash,
                "thumbnail": thumbnail,
                "block_number": block_number,
                "validated": validated,
            }

    
    symbol: MetaOapg.properties.symbol
    address: MetaOapg.properties.address
    decimals: MetaOapg.properties.decimals
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decimals"]) -> MetaOapg.properties.decimals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo_hash"]) -> MetaOapg.properties.logo_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumbnail"]) -> MetaOapg.properties.thumbnail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validated"]) -> MetaOapg.properties.validated: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["address", "name", "symbol", "decimals", "logo", "logo_hash", "thumbnail", "block_number", "validated", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decimals"]) -> MetaOapg.properties.decimals: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> typing.Union[MetaOapg.properties.logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo_hash"]) -> typing.Union[MetaOapg.properties.logo_hash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumbnail"]) -> typing.Union[MetaOapg.properties.thumbnail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_number"]) -> typing.Union[MetaOapg.properties.block_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validated"]) -> typing.Union[MetaOapg.properties.validated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["address", "name", "symbol", "decimals", "logo", "logo_hash", "thumbnail", "block_number", "validated", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        address: typing.Union[MetaOapg.properties.address, str, ],
        decimals: typing.Union[MetaOapg.properties.decimals, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        logo: typing.Union[MetaOapg.properties.logo, str, schemas.Unset] = schemas.unset,
        logo_hash: typing.Union[MetaOapg.properties.logo_hash, str, schemas.Unset] = schemas.unset,
        thumbnail: typing.Union[MetaOapg.properties.thumbnail, str, schemas.Unset] = schemas.unset,
        block_number: typing.Union[MetaOapg.properties.block_number, str, schemas.Unset] = schemas.unset,
        validated: typing.Union[MetaOapg.properties.validated, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Erc20Metadata':
        return super().__new__(
            cls,
            *args,
            symbol=symbol,
            address=address,
            decimals=decimals,
            name=name,
            logo=logo,
            logo_hash=logo_hash,
            thumbnail=thumbnail,
            block_number=block_number,
            validated=validated,
            _configuration=_configuration,
            **kwargs,
        )

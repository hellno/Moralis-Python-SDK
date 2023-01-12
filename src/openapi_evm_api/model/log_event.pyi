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


class LogEvent(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "address",
            "data",
            "block_timestamp",
            "block_hash",
            "block_number",
            "transaction_hash",
        }
        
        class properties:
            transaction_hash = schemas.StrSchema
            address = schemas.StrSchema
            block_timestamp = schemas.StrSchema
            block_number = schemas.StrSchema
            block_hash = schemas.StrSchema
            
            
            class data(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        _from = schemas.StrSchema
                        to = schemas.StrSchema
                        value = schemas.StrSchema
                        __annotations__ = {
                            "from": _from,
                            "to": to,
                            "value": value,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["from"]) -> MetaOapg.properties._from: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["from", "to", "value", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["from"]) -> typing.Union[MetaOapg.properties._from, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> typing.Union[MetaOapg.properties.to, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["from", "to", "value", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    to: typing.Union[MetaOapg.properties.to, str, schemas.Unset] = schemas.unset,
                    value: typing.Union[MetaOapg.properties.value, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'data':
                    return super().__new__(
                        cls,
                        *args,
                        to=to,
                        value=value,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "transaction_hash": transaction_hash,
                "address": address,
                "block_timestamp": block_timestamp,
                "block_number": block_number,
                "block_hash": block_hash,
                "data": data,
            }

    
    address: MetaOapg.properties.address
    data: MetaOapg.properties.data
    block_timestamp: MetaOapg.properties.block_timestamp
    block_hash: MetaOapg.properties.block_hash
    block_number: MetaOapg.properties.block_number
    transaction_hash: MetaOapg.properties.transaction_hash
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["transaction_hash", "address", "block_timestamp", "block_number", "block_hash", "data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["transaction_hash", "address", "block_timestamp", "block_number", "block_hash", "data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        address: typing.Union[MetaOapg.properties.address, str, ],
        data: typing.Union[MetaOapg.properties.data, dict, frozendict.frozendict, ],
        block_timestamp: typing.Union[MetaOapg.properties.block_timestamp, str, ],
        block_hash: typing.Union[MetaOapg.properties.block_hash, str, ],
        block_number: typing.Union[MetaOapg.properties.block_number, str, ],
        transaction_hash: typing.Union[MetaOapg.properties.transaction_hash, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LogEvent':
        return super().__new__(
            cls,
            *args,
            address=address,
            data=data,
            block_timestamp=block_timestamp,
            block_hash=block_hash,
            block_number=block_number,
            transaction_hash=transaction_hash,
            _configuration=_configuration,
            **kwargs,
        )

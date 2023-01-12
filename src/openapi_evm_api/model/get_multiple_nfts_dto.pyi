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


class GetMultipleNftsDto(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "tokens",
        }
        
        class properties:
            
            
            class tokens(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TokenItem']:
                        return TokenItem
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TokenItem'], typing.List['TokenItem']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tokens':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TokenItem':
                    return super().__getitem__(i)
            normalizeMetadata = schemas.BoolSchema
            __annotations__ = {
                "tokens": tokens,
                "normalizeMetadata": normalizeMetadata,
            }

    
    tokens: MetaOapg.properties.tokens
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokens"]) -> MetaOapg.properties.tokens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalizeMetadata"]) -> MetaOapg.properties.normalizeMetadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tokens", "normalizeMetadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokens"]) -> MetaOapg.properties.tokens: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalizeMetadata"]) -> typing.Union[MetaOapg.properties.normalizeMetadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tokens", "normalizeMetadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        tokens: typing.Union[MetaOapg.properties.tokens, list, tuple, ],
        normalizeMetadata: typing.Union[MetaOapg.properties.normalizeMetadata, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetMultipleNftsDto':
        return super().__new__(
            cls,
            *args,
            tokens=tokens,
            normalizeMetadata=normalizeMetadata,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_evm_api.model.token_item import TokenItem

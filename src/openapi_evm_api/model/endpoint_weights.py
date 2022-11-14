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


class EndpointWeights(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "path",
            "endpoint",
            "rateLimitWeight",
            "price",
        }
        
        class properties:
            endpoint = schemas.StrSchema
            path = schemas.StrSchema
            rateLimitWeight = schemas.StrSchema
            price = schemas.StrSchema
            __annotations__ = {
                "endpoint": endpoint,
                "path": path,
                "rateLimitWeight": rateLimitWeight,
                "price": price,
            }

    
    path: MetaOapg.properties.path
    endpoint: MetaOapg.properties.endpoint
    rateLimitWeight: MetaOapg.properties.rateLimitWeight
    price: MetaOapg.properties.price
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpoint"]) -> MetaOapg.properties.endpoint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rateLimitWeight"]) -> MetaOapg.properties.rateLimitWeight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["endpoint", "path", "rateLimitWeight", "price", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpoint"]) -> MetaOapg.properties.endpoint: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rateLimitWeight"]) -> MetaOapg.properties.rateLimitWeight: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["endpoint", "path", "rateLimitWeight", "price", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        path: typing.Union[MetaOapg.properties.path, str, ],
        endpoint: typing.Union[MetaOapg.properties.endpoint, str, ],
        rateLimitWeight: typing.Union[MetaOapg.properties.rateLimitWeight, str, ],
        price: typing.Union[MetaOapg.properties.price, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EndpointWeights':
        return super().__new__(
            cls,
            *args,
            path=path,
            endpoint=endpoint,
            rateLimitWeight=rateLimitWeight,
            price=price,
            _configuration=_configuration,
            **kwargs,
        )
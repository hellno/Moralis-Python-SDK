# coding: utf-8

"""
    Streams Api

    API that provides access to Moralis Streams  # noqa: E501

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

from openapi_streams import schemas  # noqa: F401


class InternalTransaction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "gas",
            "from",
            "to",
            "value",
            "transactionHash",
        }
        
        class properties:
            
            
            class _from(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> '_from':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class to(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'to':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class value(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'value':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            transactionHash = schemas.StrSchema
            
            
            class gas(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'gas':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "from": _from,
                "to": to,
                "value": value,
                "transactionHash": transactionHash,
                "gas": gas,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    gas: MetaOapg.properties.gas
    to: MetaOapg.properties.to
    value: MetaOapg.properties.value
    transactionHash: MetaOapg.properties.transactionHash
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gas"]) -> MetaOapg.properties.gas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactionHash"]) -> MetaOapg.properties.transactionHash: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["gas"], typing_extensions.Literal["from"], typing_extensions.Literal["to"], typing_extensions.Literal["value"], typing_extensions.Literal["transactionHash"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gas"]) -> MetaOapg.properties.gas: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactionHash"]) -> MetaOapg.properties.transactionHash: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gas"], typing_extensions.Literal["from"], typing_extensions.Literal["to"], typing_extensions.Literal["value"], typing_extensions.Literal["transactionHash"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        gas: typing.Union[MetaOapg.properties.gas, None, str, ],
        to: typing.Union[MetaOapg.properties.to, None, str, ],
        value: typing.Union[MetaOapg.properties.value, None, str, ],
        transactionHash: typing.Union[MetaOapg.properties.transactionHash, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'InternalTransaction':
        return super().__new__(
            cls,
            *args,
            gas=gas,
            to=to,
            value=value,
            transactionHash=transactionHash,
            _configuration=_configuration,
        )

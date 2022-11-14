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


class Transaction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "receiptGasUsed",
            "transactionIndex",
            "type",
            "nonce",
            "toAddress",
            "receiptRoot",
            "input",
            "r",
            "receiptCumulativeGasUsed",
            "s",
            "v",
            "gas",
            "fromAddress",
            "receiptContractAddress",
            "value",
            "hash",
            "receiptStatus",
            "gasPrice",
        }
        
        class properties:
            hash = schemas.StrSchema
            
            
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
            
            
            class gasPrice(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'gasPrice':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class nonce(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nonce':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class input(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'input':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            transactionIndex = schemas.StrSchema
            fromAddress = schemas.StrSchema
            
            
            class toAddress(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'toAddress':
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
            
            
            class type(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'type':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class v(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'v':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class r(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'r':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class s(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 's':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class receiptCumulativeGasUsed(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'receiptCumulativeGasUsed':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class receiptGasUsed(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'receiptGasUsed':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class receiptContractAddress(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'receiptContractAddress':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class receiptRoot(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'receiptRoot':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class receiptStatus(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'receiptStatus':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "hash": hash,
                "gas": gas,
                "gasPrice": gasPrice,
                "nonce": nonce,
                "input": input,
                "transactionIndex": transactionIndex,
                "fromAddress": fromAddress,
                "toAddress": toAddress,
                "value": value,
                "type": type,
                "v": v,
                "r": r,
                "s": s,
                "receiptCumulativeGasUsed": receiptCumulativeGasUsed,
                "receiptGasUsed": receiptGasUsed,
                "receiptContractAddress": receiptContractAddress,
                "receiptRoot": receiptRoot,
                "receiptStatus": receiptStatus,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    receiptGasUsed: MetaOapg.properties.receiptGasUsed
    transactionIndex: MetaOapg.properties.transactionIndex
    type: MetaOapg.properties.type
    nonce: MetaOapg.properties.nonce
    toAddress: MetaOapg.properties.toAddress
    receiptRoot: MetaOapg.properties.receiptRoot
    input: MetaOapg.properties.input
    r: MetaOapg.properties.r
    receiptCumulativeGasUsed: MetaOapg.properties.receiptCumulativeGasUsed
    s: MetaOapg.properties.s
    v: MetaOapg.properties.v
    gas: MetaOapg.properties.gas
    fromAddress: MetaOapg.properties.fromAddress
    receiptContractAddress: MetaOapg.properties.receiptContractAddress
    value: MetaOapg.properties.value
    hash: MetaOapg.properties.hash
    receiptStatus: MetaOapg.properties.receiptStatus
    gasPrice: MetaOapg.properties.gasPrice
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiptGasUsed"]) -> MetaOapg.properties.receiptGasUsed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactionIndex"]) -> MetaOapg.properties.transactionIndex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toAddress"]) -> MetaOapg.properties.toAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiptRoot"]) -> MetaOapg.properties.receiptRoot: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input"]) -> MetaOapg.properties.input: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["r"]) -> MetaOapg.properties.r: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiptCumulativeGasUsed"]) -> MetaOapg.properties.receiptCumulativeGasUsed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["s"]) -> MetaOapg.properties.s: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["v"]) -> MetaOapg.properties.v: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gas"]) -> MetaOapg.properties.gas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromAddress"]) -> MetaOapg.properties.fromAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiptContractAddress"]) -> MetaOapg.properties.receiptContractAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hash"]) -> MetaOapg.properties.hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiptStatus"]) -> MetaOapg.properties.receiptStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gasPrice"]) -> MetaOapg.properties.gasPrice: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["receiptGasUsed"], typing_extensions.Literal["transactionIndex"], typing_extensions.Literal["type"], typing_extensions.Literal["nonce"], typing_extensions.Literal["toAddress"], typing_extensions.Literal["receiptRoot"], typing_extensions.Literal["input"], typing_extensions.Literal["r"], typing_extensions.Literal["receiptCumulativeGasUsed"], typing_extensions.Literal["s"], typing_extensions.Literal["v"], typing_extensions.Literal["gas"], typing_extensions.Literal["fromAddress"], typing_extensions.Literal["receiptContractAddress"], typing_extensions.Literal["value"], typing_extensions.Literal["hash"], typing_extensions.Literal["receiptStatus"], typing_extensions.Literal["gasPrice"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiptGasUsed"]) -> MetaOapg.properties.receiptGasUsed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactionIndex"]) -> MetaOapg.properties.transactionIndex: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toAddress"]) -> MetaOapg.properties.toAddress: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiptRoot"]) -> MetaOapg.properties.receiptRoot: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input"]) -> MetaOapg.properties.input: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["r"]) -> MetaOapg.properties.r: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiptCumulativeGasUsed"]) -> MetaOapg.properties.receiptCumulativeGasUsed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["s"]) -> MetaOapg.properties.s: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["v"]) -> MetaOapg.properties.v: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gas"]) -> MetaOapg.properties.gas: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromAddress"]) -> MetaOapg.properties.fromAddress: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiptContractAddress"]) -> MetaOapg.properties.receiptContractAddress: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hash"]) -> MetaOapg.properties.hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiptStatus"]) -> MetaOapg.properties.receiptStatus: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gasPrice"]) -> MetaOapg.properties.gasPrice: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["receiptGasUsed"], typing_extensions.Literal["transactionIndex"], typing_extensions.Literal["type"], typing_extensions.Literal["nonce"], typing_extensions.Literal["toAddress"], typing_extensions.Literal["receiptRoot"], typing_extensions.Literal["input"], typing_extensions.Literal["r"], typing_extensions.Literal["receiptCumulativeGasUsed"], typing_extensions.Literal["s"], typing_extensions.Literal["v"], typing_extensions.Literal["gas"], typing_extensions.Literal["fromAddress"], typing_extensions.Literal["receiptContractAddress"], typing_extensions.Literal["value"], typing_extensions.Literal["hash"], typing_extensions.Literal["receiptStatus"], typing_extensions.Literal["gasPrice"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        receiptGasUsed: typing.Union[MetaOapg.properties.receiptGasUsed, None, str, ],
        transactionIndex: typing.Union[MetaOapg.properties.transactionIndex, str, ],
        type: typing.Union[MetaOapg.properties.type, None, str, ],
        nonce: typing.Union[MetaOapg.properties.nonce, None, str, ],
        toAddress: typing.Union[MetaOapg.properties.toAddress, None, str, ],
        receiptRoot: typing.Union[MetaOapg.properties.receiptRoot, None, str, ],
        input: typing.Union[MetaOapg.properties.input, None, str, ],
        r: typing.Union[MetaOapg.properties.r, None, str, ],
        receiptCumulativeGasUsed: typing.Union[MetaOapg.properties.receiptCumulativeGasUsed, None, str, ],
        s: typing.Union[MetaOapg.properties.s, None, str, ],
        v: typing.Union[MetaOapg.properties.v, None, str, ],
        gas: typing.Union[MetaOapg.properties.gas, None, str, ],
        fromAddress: typing.Union[MetaOapg.properties.fromAddress, str, ],
        receiptContractAddress: typing.Union[MetaOapg.properties.receiptContractAddress, None, str, ],
        value: typing.Union[MetaOapg.properties.value, None, str, ],
        hash: typing.Union[MetaOapg.properties.hash, str, ],
        receiptStatus: typing.Union[MetaOapg.properties.receiptStatus, None, str, ],
        gasPrice: typing.Union[MetaOapg.properties.gasPrice, None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'Transaction':
        return super().__new__(
            cls,
            *args,
            receiptGasUsed=receiptGasUsed,
            transactionIndex=transactionIndex,
            type=type,
            nonce=nonce,
            toAddress=toAddress,
            receiptRoot=receiptRoot,
            input=input,
            r=r,
            receiptCumulativeGasUsed=receiptCumulativeGasUsed,
            s=s,
            v=v,
            gas=gas,
            fromAddress=fromAddress,
            receiptContractAddress=receiptContractAddress,
            value=value,
            hash=hash,
            receiptStatus=receiptStatus,
            gasPrice=gasPrice,
            _configuration=_configuration,
        )
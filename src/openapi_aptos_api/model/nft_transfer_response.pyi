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


class NFTTransferResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "coin_amount",
            "token_data_id_hash",
            "coin_type",
            "event_sequence_number",
            "to_address",
            "transaction_timestamp",
            "event_creation_number",
            "event_account_address",
            "collection_data_id_hash",
            "name",
            "token_amount",
            "creator_address",
            "property_version",
            "transfer_type",
            "transaction_version",
            "from_address",
            "collection_name",
        }
        
        class properties:
            coin_amount = schemas.StrSchema
            coin_type = schemas.StrSchema
            
            
            class collection_data_id_hash(
                schemas.StrSchema
            ):
                pass
            
            
            class collection_name(
                schemas.StrSchema
            ):
                pass
            
            
            class creator_address(
                schemas.StrSchema
            ):
                pass
            event_account_address = schemas.StrSchema
            event_creation_number = schemas.StrSchema
            event_sequence_number = schemas.StrSchema
            
            
            class from_address(
                schemas.StrSchema
            ):
                pass
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            property_version = schemas.StrSchema
            
            
            class to_address(
                schemas.StrSchema
            ):
                pass
            token_amount = schemas.StrSchema
            
            
            class token_data_id_hash(
                schemas.StrSchema
            ):
                pass
            transaction_timestamp = schemas.StrSchema
            transaction_version = schemas.StrSchema
            transfer_type = schemas.StrSchema
            __annotations__ = {
                "coin_amount": coin_amount,
                "coin_type": coin_type,
                "collection_data_id_hash": collection_data_id_hash,
                "collection_name": collection_name,
                "creator_address": creator_address,
                "event_account_address": event_account_address,
                "event_creation_number": event_creation_number,
                "event_sequence_number": event_sequence_number,
                "from_address": from_address,
                "name": name,
                "property_version": property_version,
                "to_address": to_address,
                "token_amount": token_amount,
                "token_data_id_hash": token_data_id_hash,
                "transaction_timestamp": transaction_timestamp,
                "transaction_version": transaction_version,
                "transfer_type": transfer_type,
            }
    
    coin_amount: MetaOapg.properties.coin_amount
    token_data_id_hash: MetaOapg.properties.token_data_id_hash
    coin_type: MetaOapg.properties.coin_type
    event_sequence_number: MetaOapg.properties.event_sequence_number
    to_address: MetaOapg.properties.to_address
    transaction_timestamp: MetaOapg.properties.transaction_timestamp
    event_creation_number: MetaOapg.properties.event_creation_number
    event_account_address: MetaOapg.properties.event_account_address
    collection_data_id_hash: MetaOapg.properties.collection_data_id_hash
    name: MetaOapg.properties.name
    token_amount: MetaOapg.properties.token_amount
    creator_address: MetaOapg.properties.creator_address
    property_version: MetaOapg.properties.property_version
    transfer_type: MetaOapg.properties.transfer_type
    transaction_version: MetaOapg.properties.transaction_version
    from_address: MetaOapg.properties.from_address
    collection_name: MetaOapg.properties.collection_name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coin_amount"]) -> MetaOapg.properties.coin_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coin_type"]) -> MetaOapg.properties.coin_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection_data_id_hash"]) -> MetaOapg.properties.collection_data_id_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection_name"]) -> MetaOapg.properties.collection_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creator_address"]) -> MetaOapg.properties.creator_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_account_address"]) -> MetaOapg.properties.event_account_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_creation_number"]) -> MetaOapg.properties.event_creation_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_sequence_number"]) -> MetaOapg.properties.event_sequence_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["property_version"]) -> MetaOapg.properties.property_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_amount"]) -> MetaOapg.properties.token_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_data_id_hash"]) -> MetaOapg.properties.token_data_id_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_timestamp"]) -> MetaOapg.properties.transaction_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_version"]) -> MetaOapg.properties.transaction_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transfer_type"]) -> MetaOapg.properties.transfer_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["coin_amount", "coin_type", "collection_data_id_hash", "collection_name", "creator_address", "event_account_address", "event_creation_number", "event_sequence_number", "from_address", "name", "property_version", "to_address", "token_amount", "token_data_id_hash", "transaction_timestamp", "transaction_version", "transfer_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coin_amount"]) -> MetaOapg.properties.coin_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coin_type"]) -> MetaOapg.properties.coin_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection_data_id_hash"]) -> MetaOapg.properties.collection_data_id_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection_name"]) -> MetaOapg.properties.collection_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creator_address"]) -> MetaOapg.properties.creator_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_account_address"]) -> MetaOapg.properties.event_account_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_creation_number"]) -> MetaOapg.properties.event_creation_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_sequence_number"]) -> MetaOapg.properties.event_sequence_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["property_version"]) -> MetaOapg.properties.property_version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_amount"]) -> MetaOapg.properties.token_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_data_id_hash"]) -> MetaOapg.properties.token_data_id_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_timestamp"]) -> MetaOapg.properties.transaction_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_version"]) -> MetaOapg.properties.transaction_version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transfer_type"]) -> MetaOapg.properties.transfer_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["coin_amount", "coin_type", "collection_data_id_hash", "collection_name", "creator_address", "event_account_address", "event_creation_number", "event_sequence_number", "from_address", "name", "property_version", "to_address", "token_amount", "token_data_id_hash", "transaction_timestamp", "transaction_version", "transfer_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        coin_amount: typing.Union[MetaOapg.properties.coin_amount, str, ],
        token_data_id_hash: typing.Union[MetaOapg.properties.token_data_id_hash, str, ],
        coin_type: typing.Union[MetaOapg.properties.coin_type, str, ],
        event_sequence_number: typing.Union[MetaOapg.properties.event_sequence_number, str, ],
        to_address: typing.Union[MetaOapg.properties.to_address, str, ],
        transaction_timestamp: typing.Union[MetaOapg.properties.transaction_timestamp, str, ],
        event_creation_number: typing.Union[MetaOapg.properties.event_creation_number, str, ],
        event_account_address: typing.Union[MetaOapg.properties.event_account_address, str, ],
        collection_data_id_hash: typing.Union[MetaOapg.properties.collection_data_id_hash, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        token_amount: typing.Union[MetaOapg.properties.token_amount, str, ],
        creator_address: typing.Union[MetaOapg.properties.creator_address, str, ],
        property_version: typing.Union[MetaOapg.properties.property_version, str, ],
        transfer_type: typing.Union[MetaOapg.properties.transfer_type, str, ],
        transaction_version: typing.Union[MetaOapg.properties.transaction_version, str, ],
        from_address: typing.Union[MetaOapg.properties.from_address, str, ],
        collection_name: typing.Union[MetaOapg.properties.collection_name, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NFTTransferResponse':
        return super().__new__(
            cls,
            *args,
            coin_amount=coin_amount,
            token_data_id_hash=token_data_id_hash,
            coin_type=coin_type,
            event_sequence_number=event_sequence_number,
            to_address=to_address,
            transaction_timestamp=transaction_timestamp,
            event_creation_number=event_creation_number,
            event_account_address=event_account_address,
            collection_data_id_hash=collection_data_id_hash,
            name=name,
            token_amount=token_amount,
            creator_address=creator_address,
            property_version=property_version,
            transfer_type=transfer_type,
            transaction_version=transaction_version,
            from_address=from_address,
            collection_name=collection_name,
            _configuration=_configuration,
            **kwargs,
        )

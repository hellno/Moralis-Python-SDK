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


class Media(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "media_collection",
            "mimetype",
            "original_media_url",
            "category",
            "parent_hash",
        }
        
        class properties:
            mimetype = schemas.StrSchema
            
            
            class category(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def IMAGE(cls):
                    return cls("image")
                
                @schemas.classproperty
                def AUDIO(cls):
                    return cls("audio")
                
                @schemas.classproperty
                def VIDEO(cls):
                    return cls("video")
            original_media_url = schemas.StrSchema
            parent_hash = schemas.StrSchema
        
            @staticmethod
            def media_collection() -> typing.Type['MediaCollection']:
                return MediaCollection
            __annotations__ = {
                "mimetype": mimetype,
                "category": category,
                "original_media_url": original_media_url,
                "parent_hash": parent_hash,
                "media_collection": media_collection,
            }

    
    media_collection: 'MediaCollection'
    mimetype: MetaOapg.properties.mimetype
    original_media_url: MetaOapg.properties.original_media_url
    category: MetaOapg.properties.category
    parent_hash: MetaOapg.properties.parent_hash
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mimetype"]) -> MetaOapg.properties.mimetype: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["original_media_url"]) -> MetaOapg.properties.original_media_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_hash"]) -> MetaOapg.properties.parent_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["media_collection"]) -> 'MediaCollection': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["mimetype", "category", "original_media_url", "parent_hash", "media_collection", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mimetype"]) -> MetaOapg.properties.mimetype: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["original_media_url"]) -> MetaOapg.properties.original_media_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_hash"]) -> MetaOapg.properties.parent_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["media_collection"]) -> 'MediaCollection': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["mimetype", "category", "original_media_url", "parent_hash", "media_collection", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        media_collection: 'MediaCollection',
        mimetype: typing.Union[MetaOapg.properties.mimetype, str, ],
        original_media_url: typing.Union[MetaOapg.properties.original_media_url, str, ],
        category: typing.Union[MetaOapg.properties.category, str, ],
        parent_hash: typing.Union[MetaOapg.properties.parent_hash, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Media':
        return super().__new__(
            cls,
            *args,
            media_collection=media_collection,
            mimetype=mimetype,
            original_media_url=original_media_url,
            category=category,
            parent_hash=parent_hash,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_evm_api.model.media_collection import MediaCollection

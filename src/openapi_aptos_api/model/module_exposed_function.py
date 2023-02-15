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


class ModuleExposedFunction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "visibility",
            "generic_type_params",
            "name",
            "is_entry",
            "params",
            "return",
        }
        
        class properties:
            name = schemas.StrSchema
            visibility = schemas.StrSchema
            is_entry = schemas.BoolSchema
            
            
            class generic_type_params(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['GenericTypeParam']:
                        return GenericTypeParam
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['GenericTypeParam'], typing.List['GenericTypeParam']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'generic_type_params':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'GenericTypeParam':
                    return super().__getitem__(i)
            
            
            class params(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'params':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class _return(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> '_return':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "visibility": visibility,
                "is_entry": is_entry,
                "generic_type_params": generic_type_params,
                "params": params,
                "return": _return,
            }
    
    visibility: MetaOapg.properties.visibility
    generic_type_params: MetaOapg.properties.generic_type_params
    name: MetaOapg.properties.name
    is_entry: MetaOapg.properties.is_entry
    params: MetaOapg.properties.params
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibility"]) -> MetaOapg.properties.visibility: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_entry"]) -> MetaOapg.properties.is_entry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["generic_type_params"]) -> MetaOapg.properties.generic_type_params: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["params"]) -> MetaOapg.properties.params: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["return"]) -> MetaOapg.properties._return: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "visibility", "is_entry", "generic_type_params", "params", "return", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibility"]) -> MetaOapg.properties.visibility: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_entry"]) -> MetaOapg.properties.is_entry: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["generic_type_params"]) -> MetaOapg.properties.generic_type_params: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["params"]) -> MetaOapg.properties.params: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["return"]) -> MetaOapg.properties._return: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "visibility", "is_entry", "generic_type_params", "params", "return", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        visibility: typing.Union[MetaOapg.properties.visibility, str, ],
        generic_type_params: typing.Union[MetaOapg.properties.generic_type_params, list, tuple, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        is_entry: typing.Union[MetaOapg.properties.is_entry, bool, ],
        params: typing.Union[MetaOapg.properties.params, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModuleExposedFunction':
        return super().__new__(
            cls,
            *args,
            visibility=visibility,
            generic_type_params=generic_type_params,
            name=name,
            is_entry=is_entry,
            params=params,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_aptos_api.model.generic_type_param import GenericTypeParam

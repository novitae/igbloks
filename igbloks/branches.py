from pydantic import BaseModel, Field, validator
import typing

class _UnSet:
    def __repr__(self) -> str:
        return "(UnSet)"
    
UnSet = _UnSet()

class Branch(BaseModel):
    @property
    def attrs(self) -> dict[str, int | float | str | bool]:
        result = self.dict(exclude_unset=True)
        return { key: value for key, value in result.items()
                 if not isinstance(value, (list, dict)) }
    
    # def find_all(
    #     self,
    #     cls: type | list[type] = None,
    #     attrs: dict[tuple[str] | str, typing.Any] = {},
    #     recursive: bool = True,
    #     *,
    #     _clean: bool = False
    # ) -> list:
    #     if _clean:
    #         cleaned_attrs = attrs
    #         cleaned_classes = cls
    #     else:
    #         cleaned_attrs = {}
    #         for key, value in attrs.items():
    #             if isinstance(key, (tuple, list, set)):
    #                 keys = list(key)
    #             else:
    #                 keys = [key]
    #             if isinstance(value, (tuple, set, list)):
    #                 values = list(value)
    #             else:
    #                 values = [value]
    #             cleaned_attrs.update({
    #                 key: value
    #                 for key in keys
    #                 for value in values
    #             })
            
    #         if isinstance(cls, (list, tuple, set)):
    #             cleaned_classes = tuple(cls)
    #         elif cls is None:
    #             cleaned_classes = None
    #         else:
    #             cleaned_classes = (cls, )

    #     result = []
    #     for key, value in self._iter(exclude_unset=True):
    #         if cleaned_classes is None or isinstance(value, cleaned_classes):
    #             for attr_name, attr_val in cleaned_attrs:
    #                 if hasattr(value, attr_name) and getattr(value, attr_val) == value:
    #                     result.append(value)
    #                 elif isinstance(value, Branch) and recursive:
    #                     result += value.find_all(cleaned_classes, cleaned_attrs, _clean=True)
        
    #     return result

class bk_components_AccessibilityExtension__㐁(Branch):
    enabled: bool = Field(UnSet, alias='#')
    label: str = Field(UnSet, alias='$')
    role: str = Field(UnSet, alias='&')
    disabled: bool = Field(UnSet, alias='+')

class bk_components_internal_Action__㐟(Branch):
    handler: str = Field(UnSet, alias='#')

class bk_types_ThemedColor__㐵(Branch):
    dark_color: str = Field(UnSet, alias='#')
    light_color: str = Field(UnSet, alias='$')

class flex__㐵(Branch):
    height: str = Field(UnSet, alias='#')
    width: str = Field(UnSet, alias='$')

class flex__㐸(Branch):
    grow: int = Field(UnSet, alias=')')
    height: str = Field(UnSet, alias='*')
    margin_bottom: str = Field(UnSet, alias=',')
    margin_end: str = Field(UnSet, alias='-')
    margin_left: str = Field(UnSet, alias='.')
    margin_right: str = Field(UnSet, alias='0')
    margin_start: str = Field(UnSet, alias='1')
    margin_top: str = Field(UnSet, alias='2')
    min_height: str = Field(UnSet, alias='5')
    padding_bottom: str = Field(UnSet, alias='7')
    padding_end: str = Field(UnSet, alias='8')
    padding_start: str = Field(UnSet, alias=';')
    padding_top: str = Field(UnSet, alias='=')
    shrink: int = Field(UnSet, alias='A')
    width: str = Field(UnSet, alias='D')

class bk_components_Text__㐗(Branch):
    line_height_multiplier: float = Field(UnSet, alias='$')
    text: str = Field(UnSet, alias=')')
    text_size: str = Field(UnSet, alias='-')
    text_style: str = Field(UnSet, alias='.')
    text_themed_color: bk_types_ThemedColor__㐵 = Field(UnSet, alias='0')
    _style: flex__㐸 = Field(UnSet, alias='')

class bk_components_TextSpan__㐛(Branch):
    id: int = Field(UnSet, alias='!')
    on_click: str = Field(UnSet, alias='$')
    text: str = Field(UnSet, alias='&')
    text_size: str = Field(UnSet, alias='*')
    text_style: str = Field(UnSet, alias='+')
    text_themed_color: bk_types_ThemedColor__㐵 = Field(UnSet, alias=',')
    on_bind: str = Field(UnSet, alias='')

class bk_components_ThemedColorDrawable__㐜(Branch):
    color: bk_types_ThemedColor__㐵 = Field(UnSet, alias='#')

class ig_components_Icon__㑄(Branch):
    height: str = Field(UnSet, alias='#')
    resource_name: str = Field(UnSet, alias='$')
    tint_themed_color: bk_types_ThemedColor__㐵 = Field(UnSet, alias='(')
    url: str = Field(UnSet, alias=')')
    width: str = Field(UnSet, alias='*')
    _style: flex__㐸 = Field(UnSet, alias='')

class ig_components_Spinner__㑍(Branch):
    state: str = Field(UnSet, alias='#')
    _style: flex__㐵 = Field(UnSet, alias='$')
    _style: flex__㐸 = Field(UnSet, alias='')

class bk_components_RichText__㐑(Branch):
    children: list[bk_components_TextSpan__㐛] = Field(UnSet, alias=' ')
    line_height_multiplier: float = Field(UnSet, alias='&')
    text_align: str = Field(UnSet, alias='*')
    _style: flex__㐸 = Field(UnSet, alias='')

class bk_components_StateDrawableItem__㐕(Branch):
    drawable: bk_components_ThemedColorDrawable__㐜 = Field(UnSet, alias='#')
    state: str = Field(UnSet, alias='$')

class bk_components_StateDrawable__㐔(Branch):
    state_items: list[bk_components_StateDrawableItem__㐕] = Field(UnSet, alias='#')

class ig_components_ViewpointExtension__㑒(Branch):
    key: str = Field(UnSet, alias='#')

class bk_components_VisibilityExtension__㓢(Branch):
    on_appear: str = Field(UnSet, alias='#')
    key: str = Field(UnSet, alias='&')

class bk_components_BoxDecoration__㐂(Branch):
    background: bk_components_ThemedColorDrawable__㐜 | bk_components_StateDrawable__㐔 = Field(UnSet, alias='#')
    border_themed_color: bk_types_ThemedColor__㐵 = Field(UnSet, alias='&')
    border_width: str = Field(UnSet, alias='(')
    clipping: bool = Field(UnSet, alias='+')
    corner_radius: str = Field(UnSet, alias='.')
    foreground: bk_components_StateDrawable__㐔 = Field(UnSet, alias='1')

    @validator('background', pre=True)
    def validate(cls, value) -> Branch:
        def find_type(v):
            if '㐜' in v:
                return bk_components_ThemedColorDrawable__㐜(**v)
            if '㐔' in v:
                return bk_components_StateDrawable__㐔(**v)
            else:
                raise ValueError(f'class not found for {v}')

        return find_type(value)

class bk_components_Image__㐋(Branch):
    scale_type: str = Field(UnSet, alias='(')
    url: str = Field(UnSet, alias=')')
    extensions: list[list] = Field(UnSet, alias='')

class bk_components_Collection__㐅(Branch):
    children: list["bk_components_Flexbox__㐈"] = Field(UnSet, alias=' ')
    direction: str = Field(UnSet, alias='*')
    use_correct_measure: bool = Field(UnSet, alias='?')
    _style: flex__㐸 = Field(UnSet, alias='')
    extensions: list[bk_components_VisibilityExtension__㓢] = Field(UnSet, alias='')

class bk_components_AutomationTestExtension__㓾(Branch):
    testing_id: str = Field(UnSet, alias='#')

class bk_components_Flexbox__㐈(Branch):
    children: list[Branch] = Field(UnSet, alias=' ')
    id: int = Field(UnSet, alias='!')
    align_items: str = Field(UnSet, alias='$')
    decoration: bk_components_BoxDecoration__㐂 = Field(UnSet, alias='&')
    enabled: bool = Field(UnSet, alias='(')
    flex_direction: str = Field(UnSet, alias=')')
    justify_content: str = Field(UnSet, alias=',')
    on_click: str = Field(UnSet, alias='-')
    _style: flex__㐸 = Field(UnSet, alias='')
    extensions: list[bk_components_VisibilityExtension__㓢 | ig_components_ViewpointExtension__㑒 | bk_components_AccessibilityExtension__㐁 | bk_components_AutomationTestExtension__㓾] = Field(UnSet, alias='')
    on_bind: str = Field(UnSet, alias='')

    @validator('children', 'extensions', pre=True)
    def validate(cls, value) -> Branch:
        def find_type(v):
            if '㐑' in v:
                return bk_components_RichText__㐑(**v)
            if '㐗' in v:
                return bk_components_Text__㐗(**v)
            if '㐈' in v:
                return bk_components_Flexbox__㐈(**v)
            if '㐋' in v:
                return bk_components_Image__㐋(**v)
            if '㐅' in v:
                return bk_components_Collection__㐅(**v)
            if '㑍' in v:
                return ig_components_Spinner__㑍(**v)
            if '㑄' in v:
                return ig_components_Icon__㑄(**v)
            elif '㓢' in v:
                return bk_components_VisibilityExtension__㓢(**v)
            elif '㑒' in v:
                return ig_components_ViewpointExtension__㑒(**v)
            elif '㐁' in v:
                return bk_components_AccessibilityExtension__㐁(**v)
            elif '㓾' in v:
                return bk_components_AutomationTestExtension__㓾(**v)
            else:
                raise ValueError(f'class not found for {v}')

        return [find_type(item) for item in value]
bk_components_Flexbox__㐈.update_forward_refs()

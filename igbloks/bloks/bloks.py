from typing import Any, Self, ForwardRef, get_type_hints
from .branches import BlokField, Branch
from ..utils import get_branch_name
from ..errors import InvalidRawBranchError, NonMatchingBKIDError

class BkTypesThemedcolor(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐵",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.types.ThemedColor", }
    light_color: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "$",
                                           "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "light_color", })
    dark_color: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "#",
                                          "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "dark_color", })

class Flex(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐸",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "flex", }
    width: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "D",
                                     "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "width", })
    height: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "*",
                                      "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "height", })
    padding_top: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "=",
                                           "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "padding_top", })
    padding_bottom: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "7",
                                              "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "padding_bottom", })
    grow: int = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": ")",
                                    "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "grow", })
    padding_start: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": ";",
                                             "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "padding_start", })
    padding_end: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "8",
                                           "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "padding_end", })
    shrink: int = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "A",
                                      "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "shrink", })

class BkComponentsVisibilityextension(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㓢",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.VisibilityExtension", }
    key: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "&",
                                   "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "key", })
    on_appear: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "#",
                                         "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "on_appear", })

class BkComponentsTextspan(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐛",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.TextSpan", }
    text: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "&",
                                    "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "text", })
    text_size: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "*",
                                         "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "text_size", })
    text_themed_color: BkTypesThemedcolor | str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": ",",
                                                                      "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "text_themed_color", })
    on_click: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "$",
                                        "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "on_click", })
    on_bind: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "",
                                       "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "on_bind", })
    id: int = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "!",
                                  "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "id", })

class BkComponentsAccessibilityextension(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐁",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.AccessibilityExtension", }
    enabled: bool = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "#",
                                        "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "enabled", })
    label: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "$",
                                     "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "label", })
    role: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "&",
                                    "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "role", })

class BkComponentsAutomationtestextension(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㓾",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.AutomationTestExtension", }
    testing_id: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "#",
                                          "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "testing_id", })

class BkComponentsBoxdecoration(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐂",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.BoxDecoration", }
    corner_radius: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": ".",
                                             "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "corner_radius", })
    border_width: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "(",
                                            "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "border_width", })
    clipping: bool = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "+",
                                         "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "clipping", })
    border_themed_color: BkTypesThemedcolor | str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "&",
                                                                        "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "border_themed_color", })

class BkComponentsCollection(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐅",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Collection", }
    direction: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "*",
                                         "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "direction", })
    children: list[str | ForwardRef("BkComponentsFlexbox")] = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": " ",
                                                                                  "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "children", })
    extensions: list[str | BkComponentsVisibilityextension] = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "",
                                                                                  "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "extensions", })
    _style: str | Flex = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "",
                                             "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "_style", })

class IgComponentsIcon(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㑄",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "ig.components.Icon", }
    url: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": ")",
                                   "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "url", })
    resource_name: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "$",
                                             "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "resource_name", })
    height: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "#",
                                      "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "height", })
    width: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "*",
                                     "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "width", })
    tint_themed_color: BkTypesThemedcolor | str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "(",
                                                                      "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "tint_themed_color", })

class BkComponentsImage(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐋",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Image", }
    url: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": ")",
                                   "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "url", })
    scale_type: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "(",
                                          "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "scale_type", })
    extensions: list[Any] = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "",
                                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "extensions", })

class BkComponentsRichtext(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐑",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.RichText", }
    children: list[str | BkComponentsTextspan] = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": " ",
                                                                     "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "children", })
    text_align: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "*",
                                          "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "text_align", })
    line_height_multiplier: float = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "&",
                                                        "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "line_height_multiplier", })
    _style: str | Flex = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "",
                                             "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "_style", })

class BkComponentsText(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐗",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Text", }
    text: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": ")",
                                    "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "text", })
    text_size: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "-",
                                         "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "text_size", })
    text_style: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": ".",
                                          "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "text_style", })
    line_height_multiplier: float = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "$",
                                                        "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "line_height_multiplier", })
    text_themed_color: BkTypesThemedcolor | str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "0",
                                                                      "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "text_themed_color", })

class BkComponentsFlexbox(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐈",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Flexbox", }
    flex_direction: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": ")",
                                              "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "flex_direction", })
    children: list[BkComponentsCollection | BkComponentsRichtext | Self | BkComponentsText | IgComponentsIcon | str | BkComponentsImage] = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": " ",
                                                                                                                                                               "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "children", })
    align_items: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "$",
                                           "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "align_items", })
    justify_content: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": ",",
                                               "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "justify_content", })
    decoration: str | BkComponentsBoxdecoration = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "&",
                                                                      "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "decoration", })
    _style: str | Flex = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "",
                                             "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "_style", })
    extensions: list[str | BkComponentsAutomationtestextension | BkComponentsAccessibilityextension] = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "",
                                                                                                                           "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "extensions", })
    on_click: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "-",
                                        "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "on_click", })

BkComponentsCollection.__annotations__ = get_type_hints(BkComponentsCollection)

def __to_py_obj__(
    content: dict,
    bkid: str,
    *args,
    **kwargs
) -> BkComponentsFlexbox:
    if (branch_name := get_branch_name(content)) is not None:
        for branch in [ BkComponentsFlexbox, ]:
            if branch_name == branch.aliases.get(bkid):
                return branch.__to_py_obj__( content=content,
                                             bkid=bkid,
                                             *args, **kwargs, )
        else:
            raise NonMatchingBKIDError()
    else:
        raise InvalidRawBranchError()

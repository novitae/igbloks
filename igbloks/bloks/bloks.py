from typing import Any, Self, ForwardRef, get_type_hints

from .branches import BlokField, Branch
from ..utils import get_branch_name
from ..errors import InvalidRawBranchError, NonMatchingBKIDError

class BkTypesThemedcolor(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐵",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.types.ThemedColor", }
    light_color: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐵",
                                           "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.types.ThemedColor", })
    dark_color: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐵",
                                          "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.types.ThemedColor", })

class Flex(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐸",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "flex", }
    width: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐸",
                                     "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "flex", })
    height: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐸",
                                      "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "flex", })
    padding_top: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐸",
                                           "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "flex", })
    padding_bottom: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐸",
                                              "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "flex", })
    grow: int = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐸",
                                    "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "flex", })
    padding_start: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐸",
                                             "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "flex", })
    padding_end: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐸",
                                           "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "flex", })
    shrink: int = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐸",
                                      "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "flex", })

class BkComponentsTextspan(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐛",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.TextSpan", }
    text: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐛",
                                    "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.TextSpan", })
    text_size: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐛",
                                         "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.TextSpan", })
    text_themed_color: str | BkTypesThemedcolor = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐛",
                                                                      "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.TextSpan", })
    on_click: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐛",
                                        "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.TextSpan", })
    on_bind: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐛",
                                       "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.TextSpan", })
    id: int = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐛",
                                  "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.TextSpan", })

class BkComponentsAccessibilityextension(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐁",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.AccessibilityExtension", }
    enabled: bool = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐁",
                                        "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.AccessibilityExtension", })
    label: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐁",
                                     "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.AccessibilityExtension", })
    role: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐁",
                                    "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.AccessibilityExtension", })

class BkComponentsAutomationtestextension(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㓾",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.AutomationTestExtension", }
    testing_id: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㓾",
                                          "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.AutomationTestExtension", })

class BkComponentsBoxdecoration(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐂",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.BoxDecoration", }
    corner_radius: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐂",
                                             "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.BoxDecoration", })
    border_width: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐂",
                                            "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.BoxDecoration", })
    clipping: bool = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐂",
                                         "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.BoxDecoration", })
    border_themed_color: str | BkTypesThemedcolor = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐂",
                                                                        "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.BoxDecoration", })

class IgComponentsIcon(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㑄",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "ig.components.Icon", }
    url: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㑄",
                                   "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "ig.components.Icon", })
    resource_name: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㑄",
                                             "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "ig.components.Icon", })
    height: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㑄",
                                      "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "ig.components.Icon", })
    width: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㑄",
                                     "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "ig.components.Icon", })
    tint_themed_color: str | BkTypesThemedcolor = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㑄",
                                                                      "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "ig.components.Icon", })

class BkComponentsImage(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐋",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Image", }
    url: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐋",
                                   "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Image", })
    scale_type: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐋",
                                          "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Image", })
    extensions: list[Any] = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐋",
                                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Image", })

class BkComponentsText(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐗",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Text", }
    text: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐗",
                                    "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Text", })
    text_size: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐗",
                                         "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Text", })
    text_style: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐗",
                                          "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Text", })
    line_height_multiplier: float = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐗",
                                                        "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Text", })
    text_themed_color: str | BkTypesThemedcolor = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐗",
                                                                      "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Text", })

class BkComponentsRichtext(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐑",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.RichText", }
    children: list[BkComponentsTextspan | str] = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐑",
                                                                     "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.RichText", })
    text_align: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐑",
                                          "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.RichText", })
    line_height_multiplier: float = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐑",
                                                        "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.RichText", })
    _style: Flex | str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐑",
                                             "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.RichText", })

class BkComponentsVisibilityextension(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㓢",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.VisibilityExtension", }
    key: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㓢",
                                   "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.VisibilityExtension", })
    on_appear: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㓢",
                                         "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.VisibilityExtension", })

class BkComponentsCollection(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐅",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Collection", }
    direction: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐅",
                                         "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Collection", })
    children: list[ForwardRef("BkComponentsFlexbox") | str] = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐅",
                                                                                  "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Collection", })
    extensions: list[str | BkComponentsVisibilityextension] = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐅",
                                                                                  "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Collection", })
    _style: Flex | str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐅",
                                             "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Collection", })

class BkComponentsFlexbox(Branch):
    aliases: dict[str, str] = { "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐈",
                                "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Flexbox", }
    flex_direction: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐈",
                                              "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Flexbox", })
    children: list[BkComponentsImage | BkComponentsRichtext | IgComponentsIcon | Self | BkComponentsText | BkComponentsCollection | str] = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐈",
                                                                                                                                                               "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Flexbox", })
    align_items: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐈",
                                           "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Flexbox", })
    justify_content: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐈",
                                               "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Flexbox", })
    decoration: BkComponentsBoxdecoration | str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐈",
                                                                      "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Flexbox", })
    _style: Flex | str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐈",
                                             "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Flexbox", })
    extensions: list[str | BkComponentsAutomationtestextension | BkComponentsAccessibilityextension] = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐈",
                                                                                                                           "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Flexbox", })
    on_click: str = BlokField(aliases={ "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604": "㐈",
                                        "456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6": "bk.components.Flexbox", })

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

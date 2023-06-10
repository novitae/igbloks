# Instagram Bloks Knowledges
Instagram recently created a technology to make their new app [`Instagram Lite`](https://play.google.com/store/apps/details?id=com.instagram.lite) very light. Instead of using an API that gives back the data to the app, then parsing it, then displaying it, they are now returning the data, and the displaying method. The concept is the same HTML pages, containing what to show and how to show it. [Here's an article talking about it](https://thenewstack.io/instagram-lite-is-no-longer-a-progressive-web-app-now-a-native-app-built-with-bloks/). Will be the `bs4` for `bloks`.

## Requests
The requests sent to instagram to get bloks responses are very specific. All the resquests are POST, and must be sent with authorizations.
### App
The urls are looking as following:
- `https://i.instagram.com/api/v1/bloks/apps/{APP_NAME}/`
- `APP_NAME` is the name of the blok endpoint to call.
- As an example, using the `com.instagram.interactions.about_this_account` will make the url:
    `https://i.instagram.com/api/v1/bloks/apps/com.instagram.interactions.about_this_account/`.
    
### Web
*Not precised yet.*

## Responses
The response is a json, structured as following:
```py
{
    "status": bool,
    "layout": {
        "bloks_payload": {
            "tree": {}, # See Tree section below
            "data": [], # See Data section below
            "error_attribution": {
                "logging_id": "", # See Error Attribution below
            }, 
        }
    }
}
```
### Tree
This is what it is looked at by the app to render the content of the response. It is a nested assembly of `dict` / `list` objects. It might seem to be very chaotic at first look, but in reality it is very organized.
#### Bloks
- The tree is composed of objects, that we are calling bloks.
- A blok looks like the following:
    ```py
    {
        "bk.components.Flexbox": { # Class name of the object
            # Key values pairs of the object
            "flex_direction": "column",
            "children": [ # `children` key leads to a list of objects
                {
                    "bk.components.Flexbox": { # Class name of the object
                        # Key values pairs of the object
                        "flex_direction": "column",
                        "align_items": "stretch",
                        "children": [...], # `children` key leads to another list of objects
                        "_style": { # `_style` key leads to another object
                            "flex": { # Class name of the object
                                # Key values pairs of the object
                                "width": "100%",
                                "height": "100%"
                            }
                        }
                    }
                }
            ],
            "_style": { # `_style` key leads to another object
                "flex": { # Class name of the object
                    # Key values pairs of the object
                    "grow": 1
                }
            }
        }
    }
    ```
- Every class is defined in the app / web script, and it recognizes the fields, its values, and what impact each one have on the rendering.

## Blok Scripts
Scripts are an important parts of the bloks system, since they act like the Javascript of our bloks. I didn't find a specific name for them in instagram executables, so we will call them "blok script".

They have a specific syntax, looking quiet like json array, but instead of `[]`, it uses `()`. Here is an example of what it looks like raw:
```
(bk.action.map.Make, (bk.action.array.Make, \"serialized_logging_context\", \"INTERNAL_INFRA_screen_id\", \"INTERNAL_INFRA_THEME\"), (bk.action.array.Make, \"{\\\"entrypoint\\\":\\\"settings_menu\\\"}\", \"?\", \"harm_f\"))
```
We can decode it using `igbloks.scripts.parser.deserialize(...)`, and its return value to json looks like this:
```json
[
    "bk.action.map.Make",
    [
        "bk.action.array.Make",
        "serialized_logging_context",
        "INTERNAL_INFRA_screen_id",
        "INTERNAL_INFRA_THEME"
    ],
    [
        "bk.action.array.Make",
        "{\\\"entrypoint\\\":\\\"settings_menu\\\"}",
        "?",
        "harm_f"
    ]
]
```
Every first value of each list is a function. It is taking as argument the following items in its list. They are executing from the deepest index back to first ones (as an example, the functions at `[0][0][0][0]` will be executed, then with its results, `[0][0][0]` will be executed, then with its result `[0][0]` will be executed, and so on ...). The execution would look like this view from python:
1. ```py
    [
        "bk.action.map.Make",
            [
                "bk.action.array.Make", # This will create an array with the following args
                "serialized_logging_context",
                "INTERNAL_INFRA_screen_id",
                "INTERNAL_INFRA_THEME"
            ],
            [
                "bk.action.array.Make", # Same thing as previous
                "{\\\"entrypoint\\\":\\\"settings_menu\\\"}",
                "?",
                "harm_f"
            ]
        ]
    ```
2. ```py
    [
        "bk.action.map.Make", # This will make a map of the two arrays. It is like doing
                # `map([...], [...])` in python.

            # We created our two arrays. It seems we just removed the function's name,
            # but in reality the function name shouldn't be looking on the same plan as
            # its arguments.
            [
                "serialized_logging_context",
                "INTERNAL_INFRA_screen_id",
                "INTERNAL_INFRA_THEME"
            ],
            [
                "{\\\"entrypoint\\\":\\\"settings_menu\\\"}",
                "?",
                "harm_f"
            ]
        ]
    ```
3. ```py
    [
        # I turned the map into a dict so we can have an accurate representation of it
        {
            "serialized_logging_context": "{\\\"entrypoint\\\":\\\"settings_menu\\\"}",
            "INTERNAL_INFRA_screen_id": "?",
            "INTERNAL_INFRA_THEME": "harm_f"
        }
    ]
    ```

All the functions are hardcoded in the app / specified in the web javascript. I don't know at this day how much there is, nor what each does, but some are very straightforward.

## Blok Version ID
Blok version id (aka `bkid`) is an hexadecimal identifer of 64 chars long (so 32 bytes long in turned to bytes from hex). It is sent by the client in the blok requests. It is gaven by instagram in function of your client and its version. It will affect the keys of the tree in the response.

Here are examples of `bkid`:
- `0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052` (Android `v265.0.0.19.301`)
- `c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604` (iOS `v285.0.0.0.62`)
- `456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6` (Web)

### Finding the bkid of an app
#### Android
*No way has been found yet.*
#### iOS
- Use [frida-ios-dump](https://github.com/AloneMonkey/frida-ios-dump) to dump `Instagram.ipa` on your cumputer.
- Unzip the dumped ipa via `unzip Instagram.ipa`. It will be unzipped in a dir named `Payload`.
- In the `Payload` directory, open `Instagram.app` content, and the open `prepackaged_bloks_config.json`.
- You version is at json path `["versioning"]["bloks_versioning_id"]`
#### Web
You can find the bkid in the request to the page of `https://www.instagram.com/`, or any other html subpages.
You can extract it from the page using the function `get_web_bkid` from `../tools/get_web_bkid.py`.
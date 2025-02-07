# R&D Documentation
This document talks about how meta's bloks system works, based on my observations, especially on instagram.
## Introduction
Bloks is an internal framework developed by Meta (formerly Facebook) to enhance the performance and efficiency of its applications. Originally built for Instagram Lite, Bloks moves most of the application’s logic to the server-side and renders it as a native app, resulting in a lightweight application that is less than 2 MB in size, compared to the full-size version, which is close to 30 MB.[^1]
[^1]: [thenewstack.io](https://thenewstack.io/instagram-lite-is-no-longer-a-progressive-web-app-now-a-native-app-built-with-bloks/)

At its core, Bloks represents application structures as a JSON-based tree, similar to how HTML defines a document structure. This tree-based architecture dictates the UI and behavior of applications across Android, iOS, and web platforms. Bloks also features its own scripting language, developed by Meta, to handle dynamic logic and interactions within the app.
## Requests
### Sending
Here are the main elements needed to perform a request to bloks.
#### Bloks version
The bloks version is a 64 long hexadecimal string. It is required in any bloks request for the server to understand what app version it is dealing with, and how to adapt its response accordingly.
> [!NOTE]
> The bloks versionning id of [Instagram v361.0.0.46.88 (android)](https://github.com/Eltion/Instagram-SSL-Pinning-Bypass/releases/tag/v361.0.0.46.88) is `16e9197b928710eafdf1e803935ed8c450a1a2e3eb696bff1184df088b900bcf`
#### App ID
The app ID is the name of the blok app that will be hit. As an example:
- `com.instagram.interactions.about_this_account`: Will return more informations about the given account.
- `com.bloks.www.bloks.caa.reg.username.async`: The step where the username of the account being registered is set.
#### Params
The params are used as variables to give to the blok app. As an example, `com.instagram.interactions.about_this_account` takes two params:
- `target_user_id`: The user id of the account we want to get the informations from.
- `referer_type`: The referer from which we are calling the blok app (`ProfileMore` or `ProfileUsername`)
#### Request/Response shape
The bloks payload is contained inside the `{"layout": {"bloks_payload": ...}}`. The important data is represented as `...`. Check [the bloks payload section](#bloks-payload) for more informations.
<details>
  <summary>Bloks API endpoint (App)</summary>
  
  This request below hits the app id `com.instagram.interactions.about_this_account`, with the bloks version `c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604`, and the params `{"target_user_id": "317404151", "referer_type": "ProfileMore"}`.

  > [!INFO]
  > The API bloks endpoint is `/api/v1/bloks/{TYPE}/{APP_ID}`
  > `TYPE` can be:
  >  - `apps`
  >  - `async_action`
  >  - `async_component_query`
  >  - *There might be more.*
  ```
  POST /api/v1/bloks/apps/com.instagram.interactions.about_this_account/ HTTP/2
  Host: i.instagram.com
  Accept: */*
  Content-Length: 300
  User-Agent: Instagram 285.0.0.13.63 (iPhone9,4; iOS 15_8; fr_FR; fr; scale=3.00; 1242x2208; 478871389) AppleWebKit/420+
  Accept-Encoding: gzip, deflate, br
  Authorization: Bearer IGT:2:...
  Content-Type: application/x-www-form-urlencoded; charset=UTF-8

  signed_body=SIGNATURE.%7B%22_uuid%22%3A%22XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX%22%2C%22target_user_id%22%3A%22317404151%22%2C%22referer_type%22%3A%22ProfileMore%22%2C%22_uid%22%3A%2272511486263%22%2C%22bloks_versioning_id%22%3A%22c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604%22%7D
  ```
  Beautified request content:
  ```json
  {
    "_uuid": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    "target_user_id": "317404151",
    "referer_type": "ProfileMore",
    "_uid": "72511486263",
    "bloks_versioning_id": "c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604"
  }
  ```
  The response body will look like:
  ```json
  {
    "layout": {
      "bloks_payload": ...
    },
    "status": "ok"
  }
  ```
  To load such a response, you can use:
  - `igbloks.BlokResponse.from_app_response`
  - `igbloks.BlokResponse.from_app_response_dict`
</details>
<details>
  <summary>graphql_www endpoint (App)</summary>
  
  This request below hits the app id `com.bloks.www.ig.about_this_account`, with the bloks version `aefdaa2f3d1015a63ba3aad22681e79d11eb872e8614a959b33f6d9a7f265ec0`, and the params `{"referer_type": "ProfileMore", "target_user_id": "317404151"}`.

  ```
  POST /graphql_www HTTP/2
  Host: i.instagram.com
  Authorization: Bearer IGT:2:...
  Content-Type: application/x-www-form-urlencoded; charset=UTF-8
  User-Agent: Instagram 365.0.0.33.88 (iPhone9,4; iOS 15_8; fr_FR; fr; scale=3.00; 1242x2208; 690008027) AppleWebKit/420+
  Content-Length: 877
  Accept-Encoding: gzip, deflate, br

  method=post&pretty=false&format=json&server_timestamps=true&locale=fr_FR&purpose=fetch&fb_api_req_friendly_name=IGBloksAppRootQuery&client_doc_id=253360298310718582719188438574&enable_canonical_naming=true&enable_canonical_variable_overrides=true&enable_canonical_naming_ambiguous_type_prefixing=true&variables=%7B%22bk_context%22%3A%7B%22pixel_ratio%22%3A3%2C%22styles_id%22%3A%22instagram%22%7D%2C%22params%22%3A%7B%22bloks_versioning_id%22%3A%22aefdaa2f3d1015a63ba3aad22681e79d11eb872e8614a959b33f6d9a7f265ec0%22%2C%22app_id%22%3A%22com.bloks.www.ig.about_this_account%22%2C%22params%22%3A%22%7B%5C%22bk_client_context%5C%22%3A%5C%22%7B%5C%5C%5C%22styles_id%5C%5C%5C%22%3A%5C%5C%5C%22instagram%5C%5C%5C%22%2C%5C%5C%5C%22pixel_ratio%5C%5C%5C%22%3A3%7D%5C%22%2C%5C%22referer_type%5C%22%3A%5C%22ProfileMore%5C%22%2C%5C%22target_user_id%5C%22%3A%5C%22317404151%5C%22%7D%22%7D%7D
  ```
  Beautified variables:
  ```json
  {
    "bk_context": {
      "pixel_ratio": 3,
      "styles_id": "instagram"
    },
    "params": {
      "bloks_versioning_id": "aefdaa2f3d1015a63ba3aad22681e79d11eb872e8614a959b33f6d9a7f265ec0",
      "app_id": "com.bloks.www.ig.about_this_account",
      "params": "{\"bk_client_context\":\"{\\\"styles_id\\\":\\\"instagram\\\",\\\"pixel_ratio\\\":3}\",\"referer_type\":\"ProfileMore\",\"target_user_id\":\"317404151\"}"
    }
  }
  ```
  The response body will look like:
  ```json
  {
    "data": {
      "__typename": "Query",
      "strong_id__": null,
      "1$bloks_app(bk_context:$bk_context,params:$params)": {
        "screen_content": {
          "component": {
            "bundle": {
              "bloks_bundle_tree": "{\"layout\":{\"bloks_payload\": ...}}",
            }
          }
        }
      }
    }
  }
  ```
  To load such a response, you can use `igbloks.BlokResponse.from_web_response`.
</details>
<details>
  <summary>Web bloks (Web)</summary>

  This request below hits the app id `com.bloks.www.ig.about_this_account`, with the bloks version `8cfdad7160042d1ecf8a994bb406cbfffb9a769a304d39560d6486a34ea8a53e`, and the params `{"referer_type": "ProfileUsername", "target_user_id": "317404151"}`.

  ```
  POST /async/wbloks/fetch/?appid=com.bloks.www.ig.about_this_account&type=app&__bkv=8cfdad7160042d1ecf8a994bb406cbfffb9a769a304d39560d6486a34ea8a53e HTTP/1.1
  Host: www.instagram.com
  Accept: */*
  Content-Type: application/x-www-form-urlencoded;charset=UTF-8
  Sec-Fetch-Site: same-origin
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Safari/605.1.15
  Accept-Encoding: gzip, deflate, br
  Cookie: sessionid=27694553604%3A3sI5QfTu0wZ3gq%3A29%3AAYdHV2KDage4JFxqrLI1DasRQIMOKKVl0ZxmZQgx-ho
  Connection: close
  Content-Length: 195
  Pragma: no-cache
  Cache-Control: no-cache

  __a=1&fb_dtsg=...&params=%7B%22referer_type%22%3A%22ProfileMore%22%2C%22target_user_id%22%3A%22317404151%22%7D
  ```
  Beautified body params:
  ```json
  {
    "referer_type": "ProfileUsername",
    "target_user_id": "317404151"
  }
  ```
  Beautified url params:
  ```json
  {
    "appid": "com.bloks.www.ig.about_this_account",
    "type": "app",
    "__bkv": "8cfdad7160042d1ecf8a994bb406cbfffb9a769a304d39560d6486a34ea8a53e",
  }
  ```
  The response body will look like:
  ```js
  for (;;);{"__ar":1,"payload":{"layout":{"bloks_payload": ...}}}
  ```
  To load such a response, you can use `igbloks.BlokResponse.from_graphql_response`.
</details>

## Bloks payload
### Tree
### Data
### Scripts
Certains operations from mobile app aren't possible on web.
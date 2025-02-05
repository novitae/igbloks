# R&D Documentation
This document talks about how the bloks system works, based on my observations.
### Introduction
Bloks is an internal framework developed by Meta (formerly Facebook) to enhance the performance and efficiency of its applications. Originally built for Instagram Lite, Bloks moves most of the application’s logic to the server-side and renders it as a native app, resulting in a lightweight application that is less than 2 MB in size, compared to the full-size version, which is close to 30 MB.[^1]
[^1]: [thenewstack.io](https://thenewstack.io/instagram-lite-is-no-longer-a-progressive-web-app-now-a-native-app-built-with-bloks/)

At its core, Bloks represents application structures as a JSON-based tree, similar to how HTML defines a document structure. This tree-based architecture dictates the UI and behavior of applications across Android, iOS, and web platforms. Bloks also features its own scripting language, developed by Meta, to handle dynamic logic and interactions within the app.
### Requests
#### Sending
Here are the main elements needed to perform a request to bloks.
##### Bloks version
The bloks version is a 64 long hexadecimal string. It is required in any bloks request for the server to understand what app version it is dealing with, and how to adapt its response accordingly.
> [!NOTE]
> The bloks versionning id of [Instagram v361.0.0.46.88 (android)](https://github.com/Eltion/Instagram-SSL-Pinning-Bypass/releases/tag/v361.0.0.46.88) is `16e9197b928710eafdf1e803935ed8c450a1a2e3eb696bff1184df088b900bcf`
##### Params

##### App ID

##### Request shape
<details>
    <summary>Bloks API endpoint</summary>

    The bloks api endpoint hits the endpoint `https://i.instagram.com/api/v1/bloks/apps/com.instagram.interactions.about_this_account/`.

    ```
    POST /api/v1/bloks/apps/com.instagram.interactions.about_this_account/ HTTP/2
    Host: i.instagram.com
    Accept: */*
    Content-Length: 300
    User-Agent: Instagram 285.0.0.13.63 (iPhone9,4; iOS 15_8; fr_FR; fr; scale=3.00; 1242x2208; 478871389) AppleWebKit/420+
    Accept-Encoding: gzip, deflate, br
    Authorization: Bearer IGT:2:eyJkc191c2VyX2lkIjoiNzI1MTE0ODYyNjMiLCJzZXNzaW9uaWQiOiI3MjUxMTQ4NjI2MyUzQVROSGdHNWFZY0w0cVhGJTNBNSUzQUFZZGJLZE1Hb0V2OFJ5UG5ET0lKTHB4dHdObUZrZU1UcldUaUJtOVB5dyJ9
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8

    signed_body=SIGNATURE.%7B%22_uuid%22%3A%22DE968CE9-9BE2-4812-B52E-7C8D5086C06E%22%2C%22target_user_id%22%3A%22317404151%22%2C%22referer_type%22%3A%22ProfileMore%22%2C%22_uid%22%3A%2272511486263%22%2C%22bloks_versioning_id%22%3A%22c48de7e714bc4ad7ea5c9b1f004e5b0a40f24369494f20c705bd9c27451a0604%22%7D
    ```
</details>

There are different ways to obtain a bloks response. 
### Payload structure
#### 
### Tree
### Data
### Scripts
Certains operations from mobile app aren't possible on web.
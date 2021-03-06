# tahskr API

All dates and datetimes should be formatted to ISO 8601 standards.

## Methods

- [System Information](#system-information)
- [Create a User](#create-a-user)
- [Get a User](#get-a-user)
- [Update a User](#update-a-user)
- [Delete a User](#delete-a-user)
- [Authenticate](#authenticate)
- [Create a To-Do List](#create-a-to-do-list)
- [Get All To-Do Lists](#get-all-to-do-lists)
- [Get a To-Do List](#get-a-to-do-list)
- [Update a To-Do List](#update-a-to-do-list)
- [Delete a To-Do List](#delete-a-to-do-list)
- [Create a To-Do](#create-a-to-do)
- [Get All To-Dos](#get-all-to-dos)
- [Get a To-Do](#get-a-to-do)
- [Update a To-Do](#update-a-to-do)
- [Delete a To-Do](#delete-a-to-do)

## System Information

#### Method

GET

#### URL

/

#### Headers

None

#### URL Parameters

None

#### Data Parameters

None

#### Response Examples

![](https://img.shields.io/badge/200-OK-4DC292?style=flat-square)

```json
{
  "appVersion": "20.4.13",
  "schemaVersion": "1"
}
```

## Create a User

#### Method

POST

#### URL

/user

#### Headers

| Name         | Value                                                                          | Required? |
| ------------ | ------------------------------------------------------------------------------ | --------- |
| Content-Type | application/json                                                               | Yes       |
| x-admin      | The admin password set using the environment variable "TAHSKR_ADMIN_PASSWORD". | Yes       |

#### URL Parameters

None

#### Data Parameters

| Name     | Data Type | Required? | Details |
| -------- | --------- | --------- | ------- |
| username | string    | Yes       |         |
| password | string    | Yes       |         |
| config   | object    | No        |         |

#### Response Examples

![](https://img.shields.io/badge/201-Created-4DC292?style=flat-square)

```json
{
  "config": {
    "showCompleted": false
  },
  "created": "2019-09-25T13:13:14.702375",
  "username": "john@example.com",
  "id": 243
}
```

![](https://img.shields.io/badge/400-Client%20Error-DC555C?style=flat-square)

```json
{
  "message": {
    "password": ["Missing data for required field."]
  }
}
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Incorrect admin password."
}
```

## Get a User

#### Method

GET

#### URL

/user/<id>

#### Headers

| Name    | Value                                                                         | Required?                                                                                                      |
| ------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| x-token | An authentication token retrieved using the /auth service.                    | Either x-token or x-admin required. x-token will only authorise access to the user for which the token is for. |
| x-admin | The admin password set using the environment variable "TAHSKR_ADMIN_PASSWORD" | As above.                                                                                                      |

#### URL Parameters

None

#### Data Parameters

None

#### Responses Examples

![](https://img.shields.io/badge/200-OK-4DC292?style=flat-square)

```json
{
  "config": {
    "showCompleted": false
  },
  "created": "2019-09-25T13:13:14.702375",
  "username": "john@example.com",
  "id": 243
}
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Authentication token invalid."
}
```

![](https://img.shields.io/badge/404-Not%20Found-DC555C?style=flat-square)

```json
{
  "message": "The requested resource was not found."
}
```

## Update a User

#### Method

PATCH

#### URL

/user/<id>

#### Headers

| Name         | Value                                                                         | Required?                                                                                                      |
| ------------ | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| x-token      | An authentication token retrieved using the /auth service.                    | Either x-token or x-admin required. x-token will only authorise access to the user for which the token is for. |
| x-admin      | The admin password set using the environment variable "TAHSKR_ADMIN_PASSWORD" | As above.                                                                                                      |
| Content-Type | application/json                                                              | Yes                                                                                                            |

#### URL Parameters

None

#### Data Parameters

| Name     | Data Type | Required? | Details         |
| -------- | --------- | --------- | --------------- |
| username | string    | No        | Cannot be null. |
| password | string    | No        | Cannot be null. |
| config   | object    | No        |                 |

#### Responses Examples

![](https://img.shields.io/badge/200-OK-4DC292?style=flat-square)

```json
{
  "config": {
    "showCompleted": false
  },
  "created": "2019-09-25T13:13:14.702375",
  "username": "john@example.com",
  "id": 243
}
```

![](https://img.shields.io/badge/400-Client%20Error-DC555C?style=flat-square)

```json
{
  "message": {
    "password": ["Field may not be null."]
  }
}
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Authentication token invalid."
}
```

![](https://img.shields.io/badge/404-Not%20Found-DC555C?style=flat-square)

```json
{
  "message": "The requested resource was not found."
}
```

## Delete a User

#### Method

DELETE

#### URL

/user/<id>

#### Headers

| Name    | Value                                                                         | Required?                                                                                                      |
| ------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| x-token | An authentication token retrieved using the /auth service.                    | Either x-token or x-admin required. x-token will only authorise access to the user for which the token is for. |
| x-admin | The admin password set using the environment variable "TAHSKR_ADMIN_PASSWORD" | As above.                                                                                                      |

#### URL Parameters

None

#### Data Parameters

None

#### Responses Examples

![](https://img.shields.io/badge/200-OK-4DC292?style=flat-square)

```json
{
  "message": "Deletion successful."
}
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Authentication token invalid."
}
```

![](https://img.shields.io/badge/404-Not%20Found-DC555C?style=flat-square)

```json
{
  "message": "The requested resource was not found."
}
```

## Authenticate

Authenticate a username and password to retrieve an authentication token.

#### Method

POST

#### URL

/auth

#### Headers

| Name         | Value            | Required? |
| ------------ | ---------------- | --------- |
| Content-Type | application/json | Yes       |

#### URL Parameters

None

#### Data Parameters

| Name     | Data Type | Required? | Details |
| -------- | --------- | --------- | ------- |
| username | string    | Yes       |         |
| password | string    | Yes       |         |

#### Responses Examples

![](https://img.shields.io/badge/200-OK-4DC292?style=flat-square)

```json
{
  "created": "2019-09-25T13:17:34.742383",
  "expiry": "2019-10-25T13:17:34.742383",
  "lastUsed": "2019-09-25T13:17:34.742383",
  "token": "f1737df5-65f3-48dh-8665-3074d112de39",
  "userId": 567
}
```

![](https://img.shields.io/badge/400-Client%20Error-DC555C?style=flat-square)

```json
{
  "message": {
    "username": ["Missing data for required field."]
  }
}
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Invalid email address or password."
}
```

## Create a To-Do List

#### Method

POST

#### URL

/todolist

#### Headers

| Name         | Value                                                      | Required? |
| ------------ | ---------------------------------------------------------- | --------- |
| x-token      | An authentication token retrieved using the /auth service. | Yes       |
| Content-Type | application/json                                           | Yes       |

#### URL Parameters

None

#### Data Parameters

| Name | Data Type | Required? | Details |
| ---- | --------- | --------- | ------- |
| name | string    | Yes       |         |

#### Responses Examples

![](https://img.shields.io/badge/201-Created-4DC292?style=flat-square)

```json
{
  "created": "2019-09-25T13:20:56.676620",
  "id": 567,
  "name": "Personal"
}
```

![](https://img.shields.io/badge/400-Client%20Error-DC555C?style=flat-square)

```json
{
  "message": {
    "name": ["Field may not be null."]
  }
}
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Authentication token invalid."
}
```

## Get All To-Do Lists

#### Method

GET

#### URL

/todolist

#### Headers

| Name    | Value                                                      | Required? |
| ------- | ---------------------------------------------------------- | --------- |
| x-token | An authentication token retrieved using the /auth service. | Yes       |

#### URL Parameters

None

#### Data Parameters

None

#### Responses Examples

![](https://img.shields.io/badge/200-OK-4DC292?style=flat-square)

```json
[
  {
    "created": "2019-09-25T13:20:52.966185",
    "id": 567,
    "name": "Personal"
  },
  {
    "created": "2019-09-25T13:20:56.676620",
    "id": 598,
    "name": "Work"
  }
]
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Authentication token invalid."
}
```

## Get a To-Do List

#### Method

GET

#### URL

/todolist/<id>

#### Headers

| Name    | Value                                                      | Required? |
| ------- | ---------------------------------------------------------- | --------- |
| x-token | An authentication token retrieved using the /auth service. | Yes       |

#### URL Parameters

None

#### Data Parameters

None

#### Responses Examples

![](https://img.shields.io/badge/200-OK-4DC292?style=flat-square)

```json
{
  "created": "2019-09-25T13:20:56.676620",
  "id": 567,
  "name": "Personal"
}
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Authentication token invalid."
}
```

![](https://img.shields.io/badge/404-Not%20Found-DC555C?style=flat-square)

```json
{
  "message": "The requested resource was not found."
}
```

## Update a To-Do List

#### Method

PATCH

#### URL

/todolist/<id>

#### Headers

| Name         | Value                                                      | Required? |
| ------------ | ---------------------------------------------------------- | --------- |
| x-token      | An authentication token retrieved using the /auth service. | Yes       |
| Content-Type | application/json                                           | Yes       |

#### URL Parameters

None

#### Data Parameters

| Name | Data Type | Required? | Details         |
| ---- | --------- | --------- | --------------- |
| name | String    | No        | Cannot be null. |

#### Responses Examples

![](https://img.shields.io/badge/200-OK-4DC292?style=flat-square)

```json
{
  "created": "2019-09-25T13:20:56.676620",
  "id": 567,
  "name": "Home"
}
```

![](https://img.shields.io/badge/400-Client%20Error-DC555C?style=flat-square)

```json
{
  "message": {
    "name": ["Field may not be null."]
  }
}
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Authentication token invalid."
}
```

![](https://img.shields.io/badge/404-Not%20Found-DC555C?style=flat-square)

```json
{
  "message": "The requested resource was not found."
}
```

## Delete a To-Do List

#### Method

DELETE

#### URL

/todolist/<id>

#### Headers

| Name    | Value                                                      | Required? |
| ------- | ---------------------------------------------------------- | --------- |
| x-token | An authentication token retrieved using the /auth service. | Yes       |

#### URL Parameters

None

#### Data Parameters

None

#### Responses Examples

![](https://img.shields.io/badge/200-OK-4DC292?style=flat-square)

```json
{
  "message": "Deletion successful."
}
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Authentication token invalid."
}
```

![](https://img.shields.io/badge/404-Not%20Found-DC555C?style=flat-square)

```json
{
  "message": "The requested resource was not found."
}
```

## Create a To-Do

#### Method

POST

#### URL

/todo

#### Headers

| Name         | Value                                                      | Required? |
| ------------ | ---------------------------------------------------------- | --------- |
| x-token      | An authentication token retrieved using the /auth service. | Yes       |
| Content-Type | application/json                                           | Yes       |

#### URL Parameters

None

#### Data Parameters

| Name              | Data Type | Required? | Details                                 |
| ----------------- | --------- | --------- | --------------------------------------- |
| summary           | string    | Yes       |                                         |
| parentId          | int       | No        | Set to create a sub-task of the parent. |
| listId            | int       | No        | A To-Do List id.                        |
| notes             | string    | No        |                                         |
| important         | boolean   | No        | Defaults to false.                      |
| snoozeDatetime    | string    | No        |                                         |
| completedDatetime | string    | No        |                                         |

#### Responses Examples

![](https://img.shields.io/badge/201-Created-4DC292?style=flat-square)

```json
{
  "completedDatetime": null,
  "created": "2019-09-25T20:10:35.943554",
  "id": 2,
  "important": false,
  "listId": null,
  "notes": null,
  "parentId": null,
  "snoozeDatetime": null,
  "summary": "My First To Do"
}
```

![](https://img.shields.io/badge/400-Client%20Error-DC555C?style=flat-square)

```json
{
  "message": {
    "important": ["Not a valid boolean."]
  }
}
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Authentication token invalid."
}
```

## Get All To-Dos

#### Method

GET

#### URL

/todo

#### Headers

| Name    | Value                                                      | Required? |
| ------- | ---------------------------------------------------------- | --------- |
| x-token | An authentication token retrieved using the /auth service. | Yes       |

#### URL Parameters

| Name           | Required? | Details                                                                                    |
| -------------- | --------- | ------------------------------------------------------------------------------------------ |
| parentId       | No        | Return sub-tasks of this To-Do. Defaults to null.                                          |
| completed      | No        | null (default) = Return all. true = Return only completed. false = Return only incomplete. |
| excludeSnoozed | No        | If true, exclude To-Dos with a snoozedDate in the future. Defaults to false.               |

#### Data Parameters

None

#### Responses Examples

![](https://img.shields.io/badge/200-OK-4DC292?style=flat-square)

```json
[
  {
    "completedDatetime": null,
    "created": "2019-09-25T20:10:35.943554",
    "id": 1345,
    "important": false,
    "listId": null,
    "notes": null,
    "parentId": null,
    "snoozeDatetime": null,
    "summary": "My First To Do"
  },
  {
    "completedDatetime": null,
    "created": "2019-09-25T20:10:36.643565",
    "id": 1367,
    "important": true,
    "listId": null,
    "notes": "Think of better dummy data.",
    "parentId": null,
    "snoozeDatetime": "2019-09-26T00:00:00.000",
    "summary": "Another To Do"
  }
]
```

![](https://img.shields.io/badge/400-Client%20Error-DC555C?style=flat-square)

```json
{
  "message": {
    "parentId": ["Not a valid integer."]
  }
}
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Authentication token invalid."
}
```

## Get a To-Do

#### Method

GET

#### URL

/todo/<id>

#### Headers

| Name    | Value                                                      | Required? |
| ------- | ---------------------------------------------------------- | --------- |
| x-token | An authentication token retrieved using the /auth service. | Yes       |

#### URL Parameters

None

#### Data Parameters

None

#### Responses Examples

![](https://img.shields.io/badge/200-OK-4DC292?style=flat-square)

```json
{
  "completedDatetime": null,
  "created": "2019-09-25T20:10:35.943554",
  "id": 1345,
  "important": false,
  "listId": null,
  "notes": null,
  "parentId": null,
  "snoozeDatetime": null,
  "summary": "My First To Do"
}
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Authentication token invalid."
}
```

![](https://img.shields.io/badge/404-Not%20Found-DC555C?style=flat-square)

```json
{
  "message": "The requested resource was not found."
}
```

## Update a To-Do

#### Method

PATCH

#### URL

/todo/<id>

#### Headers

| Name         | Value                                                      | Required? |
| ------------ | ---------------------------------------------------------- | --------- |
| x-token      | An authentication token retrieved using the /auth service. | Yes       |
| Content-Type | application/json                                           | Yes       |

#### URL Parameters

None

#### Data Parameters

| Name              | Data Type | Required? | Details                                 |
| ----------------- | --------- | --------- | --------------------------------------- |
| summary           | string    | No        | Cannot be null.                         |
| parentId          | int       | No        | Set to create a sub-task of the parent. |
| listId            | int       | No        | A To-Do List id.                        |
| notes             | string    | No        |                                         |
| important         | boolean   | No        |                                         |
| snoozeDatetime    | string    | No        |                                         |
| completedDatetime | string    | No        |                                         |

#### Responses Examples

![](https://img.shields.io/badge/200-OK-4DC292?style=flat-square)

```json
{
  "completedDatetime": null,
  "created": "2019-09-25T20:10:35.943554",
  "id": 1345,
  "important": true,
  "listId": null,
  "notes": null,
  "parentId": null,
  "snoozeDatetime": null,
  "summary": "My First To Do - Updated"
}
```

![](https://img.shields.io/badge/400-Client%20Error-DC555C?style=flat-square)

```json
{
  "message": {
    "summary": ["Field may not be null."]
  }
}
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Authentication token invalid."
}
```

![](https://img.shields.io/badge/404-Not%20Found-DC555C?style=flat-square)

```json
{
  "message": "The requested resource was not found."
}
```

## Delete a To-Do

#### Method

DELETE

#### URL

/todo/<id>

#### Headers

None

#### URL Parameters

None

#### Data Parameters

None

#### Responses Examples

![](https://img.shields.io/badge/200-OK-4DC292?style=flat-square)

```json
{
  "message": "Deletion successful."
}
```

![](https://img.shields.io/badge/401-Unauthorised-DC555C?style=flat-square)

```json
{
  "message": "Authentication token invalid."
}
```

![](https://img.shields.io/badge/404-Not%20Found-DC555C?style=flat-square)

```json
{
  "message": "The requested resource was not found."
}
```

## API Reference

### Chat Blueprint

#### New Chat

```http
GET /chat
```

Renders the chat page.

#### Chat based on previous chat

```http
@login_required
GET /chat/<chat_id>
```

Renders the chat page, along with any messages that have been passed in internally, based on the chat_id route param.

#### See Chats History

```http
@login_required
GET /chat/history
```

Renders the chat history page, containing a list of all chats that have been created by the user

#### Get a welcome message

```http
GET /chat/api
```

Returns a welcome message in JSON format.

#### Generate a new model response

```http
POST /chat/api/generate
```

Returns a new model response in JSON format, treating it as a new chat.

#### Generate a new model response, and append it to an existing chat

```http
@login_required
POST /chat/<string:id>/api/generate
```

Returns a new model response in JSON format, appending it to the existing chat.

#### Get a list of all chats that have been created by the user

```http
@login_required
GET /chat/api/history
```

Returns a list of all chats that have been created by the user, in JSON format.

#### Get a list of all messages in a chat

```http
@login_required
GET /chat/<string:id>/api/history
```

Returns a list of all messages in a chat, in JSON format.

### Auth Blueprint

#### Login

```http
GET /login
```

Renders the login page.

#### Login

```http
POST /login
```

Logs the user in, and redirects them to the chat page.

#### Logout

```http
GET /logout
```

Logs the user out, and redirects them to the login page.

#### Register

```http
GET /register
```

Renders the register page.

#### Register

```http
POST /register
```

Registers the user, and redirects them to the chat page.

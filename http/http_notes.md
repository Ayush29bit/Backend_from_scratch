# HTTP Notes

HTTP (Hypertext Transfer Protocol) is the application-layer protocol
that enables communication between clients and servers on the web.

It is built on top of TCP and follows a request–response model.

Understanding HTTP is essential because every backend system
is fundamentally an HTTP processing machine.

---

## 1. The Request–Response Model

HTTP follows a strict cycle:

Client → Request → Server  
Server → Response → Client  

Each request is independent.
Each response completes the interaction.

There is no memory between requests by default.

This is called **statelessness**.

---

## 2. Statelessness

HTTP does not remember previous requests.

If a user logs in, the server does not automatically
"remember" that user on the next request.

State must be transported explicitly using:
- Cookies
- Headers (e.g., Authorization)
- Tokens
- Sessions

Statelessness improves scalability because:
- Servers do not need to store connection state.
- Requests can be handled by any server instance.
- Horizontal scaling becomes easier.

---

## 3. Anatomy of an HTTP Request

An HTTP request consists of:

1. Request Line
   METHOD PATH VERSION
   Example:
   GET /users/42 HTTP/1.1

2. Headers
   Key-value metadata
   Example:
   Host: example.com
   Content-Type: application/json

3. Blank Line

4. Body (optional)
   Present for methods like POST, PUT

---

### Important Components

Method:
- Defines the intent of the request.

Path:
- Identifies the resource.

Headers:
- Provide metadata.

Body:
- Carries payload data.

---

## 4. Common HTTP Methods

GET:
- Retrieve data.
- Should not modify server state.
- Idempotent.

POST:
- Create a resource.
- Not idempotent.

PUT:
- Replace a resource.
- Idempotent.

PATCH:
- Partially update a resource.

DELETE:
- Remove a resource.
- Idempotent (ideally).

Idempotent means:
Making the same request multiple times
results in the same outcome.

---

## 5. Anatomy of an HTTP Response

An HTTP response consists of:

1. Status Line
   VERSION STATUS_CODE STATUS_TEXT
   Example:
   HTTP/1.1 200 OK

2. Headers
   Example:
   Content-Type: application/json
   Content-Length: 123

3. Blank Line

4. Body (optional)

---

## 6. Status Codes

Status codes communicate outcome.

1xx – Informational  
2xx – Success  
3xx – Redirection  
4xx – Client errors  
5xx – Server errors  

Examples:

200 OK  
201 Created  
204 No Content  
400 Bad Request  
401 Unauthorized  
403 Forbidden  
404 Not Found  
500 Internal Server Error  

Clients rely heavily on status codes for behavior decisions.

---

## 7. Headers

Headers are metadata attached to requests or responses.

Common request headers:
- Host
- Authorization
- Content-Type
- Accept
- User-Agent

Common response headers:
- Content-Type
- Content-Length
- Set-Cookie
- Cache-Control

Headers are:
- Case-insensitive
- Key-value pairs
- Extensible

They are critical for:
- Authentication
- Caching
- Content

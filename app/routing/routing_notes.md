# Routing Notes

Routing is the mechanism that maps an incoming HTTP request
to a specific handler function in the backend application.

At a high level:

Incoming Request → Routing Table → Handler Function

Routing is not business logic.
Routing is dispatch logic.

---

## 1. What is Routing?

Routing answers one question:

"Given this HTTP method and URL, which function should execute?"

A route is defined by:
- HTTP method (GET, POST, PUT, DELETE, etc.)
- Path (e.g. /users/123)

Together, method + path uniquely identify a handler.

Example:

GET /users/123
POST /users/123

Same path, different methods → different handlers.

---

## 2. How Routing Tables Work

At application startup, FastAPI builds a routing table.

This routing table contains entries like:

(Method, Path Pattern) → Handler Function

Example:

(GET, /users/{user_id}) → get_user()
(GET, /users/me)        → current_user()

When a request arrives:
1. The method is matched first.
2. The path is matched against patterns.
3. Path parameters are extracted.
4. The corresponding handler is executed.

Routing happens before:
- Business logic
- Database queries
- Service layer calls

It is part of the HTTP handling layer.

---

## 3. Path Parameters vs Query Parameters

Path Parameters:
- Embedded in the URL path.
- Represent identity.
- Example: /users/42

Query Parameters:
- Appended after ?
- Represent filtering or optional modifiers.
- Example: /users?active=true

Good API design rule:

Identity → Path  
Filtering / Optional State → Query

---

## 4. Route Specificity and Conflicts

Static routes are more specific than dynamic routes.

Example:

/users/me
/users/{id}

If not handled carefully, /users/me could be interpreted as:
id = "me"

Frameworks resolve this using specificity rules.

Understanding this matters because:
- Ambiguous routes cause production bugs.
- Security-sensitive routes can be shadowed accidentally.

Always define static routes before dynamic ones when necessary.

---

## 5. Dependency Injection at Routing Time

In FastAPI, dependencies are resolved during routing.

This means:
- Authentication checks
- Authorization checks
- Request validation
- DB session creation

Can all happen before your handler executes.

Conceptually:

Request → Routing → Dependencies → Handler

Dependencies are similar to middleware,
but scoped to specific routes.

---

## 6. Why Routing Exists Separately from Business Logic

Routing:
- Decides *where* a request goes.

Business Logic:
- Decides *what* happens once it gets there.

Keeping them separate:
- Improves testability
- Prevents tight coupling
- Makes refactoring easier
- Enables framework migration (e.g., FastAPI → Go)

---

## 7. Performance Considerations

Routing must be fast because:
- It executes on every request.
- It happens before caching, DB calls, or heavy work.

Frameworks optimize routing by:
- Precomputing route trees.
- Using prefix matching.
- Avoiding runtime reflection where possible.

In lower-level systems (e.g., Go),
routing may be implemented manually using:
- Trie structures
- Switch statements
- Pattern matching libraries

---

## 8. Routing and API Versioning

Proper route organization enables:

/api/v1/users
/api/v2/users

Route grouping (prefixes) makes versioning manageable.

Without structured routing:
- APIs become impossible to evolve cleanly.

---

## 9. Common Routing Mistakes

- Mixing business logic directly into routing files.
- Overloading query parameters to simulate complex filtering.
- Creating deeply nested paths.
- Returning incorrect status codes.
- Ignoring method semantics (e.g., using GET for state changes).

---

## 10. What FastAPI Abstracts Away

FastAPI handles:
- URL parsing
- Path matching
- Parameter extraction
- Type validation
- Dependency resolution

In lower-level implementations (e.g., Go),
these concerns must be handled explicitly.

Understanding routing in FastAPI prepares for
manual routing implementation later.

---

## 11. Mental Model

Routing is the switchboard of the backend.

HTTP brings the call.
Routing connects the line.
The handler answers.

If routing is poorly designed,
the entire system becomes fragile.

---

## Final Takeaway

Routing is infrastructure.
It determines structure, scalability, and maintainability.

If you understand routing deeply,
you understand how requests flow through a backend system.

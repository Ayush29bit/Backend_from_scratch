# Serialization Notes

Serialization is the process of converting in-memory objects
into a transferable format (usually JSON).

Deserialization is the reverse:
converting incoming JSON into structured in-memory objects.

Every backend system lives at this boundary.

Raw HTTP → Structured Data → Business Logic → Structured Data → JSON

Understanding this boundary is critical for building reliable APIs.

---

## 1. Why Serialization Exists

HTTP transports bytes.

Your backend operates on structured objects.

Serialization bridges the gap between:
- Network representation (text/bytes)
- Application representation (objects)

Without serialization:
- Data cannot move between systems.
- Validation becomes impossible.
- Contracts become unclear.

---

## 2. JSON as the Default Format

Most modern APIs use JSON.

JSON supports:
- Strings
- Numbers
- Booleans
- Arrays
- Objects
- Null

JSON does NOT support:
- datetime
- UUID
- Decimal
- Custom classes

Frameworks handle this conversion automatically,
but the underlying limitations still exist.

---

## 3. Deserialization (Input Handling)

When a client sends JSON:

POST /users
{
  "email": "test@example.com",
  "age": 25
}

The backend must:
1. Parse the JSON.
2. Validate the structure.
3. Validate types.
4. Convert into a structured object.
5. Reject malformed input.

In FastAPI, Pydantic performs this validation.

Validation occurs BEFORE business logic executes.

If validation fails:
- A 422 response is returned.
- The handler function is not executed.

This protects the system boundary.

---

## 4. Schema-Driven Development

Schemas define:

- Required fields
- Field types
- Constraints
- Transformations

Example schema responsibilities:
- Ensure age is an integer.
- Ensure email is valid.
- Reject unexpected fields.
- Apply default values.

Schemas create API contracts.

Contracts:
- Stabilize APIs.
- Improve maintainability.
- Enable documentation generation.
- Prevent accidental breaking changes.

---

## 5. Type Coercion

Pydantic performs type coercion.

Example:
- "25" (string) → 25 (int)

This is convenient but must be understood.

Coercion:
- Improves usability.
- Can hide input mistakes.
- May introduce ambiguity.

Strict validation modes can disable coercion.

Understanding this tradeoff is important for critical systems.

---

## 6. Custom Types & Encoding

JSON cannot represent:
- datetime
- UUID
- Decimal

Frameworks serialize these into strings.

Example:
datetime → ISO 8601 string

Encoding rules must be:
- Consistent
- Documented
- Stable

Inconsistent encoding breaks clients.

Custom encoders define how complex types
are converted into JSON-compatible forms.

---

## 7. Response Serialization

Serialization also happens on output.

Python object → JSON

If no response model is defined:
- Internal fields may leak.
- Sensitive data may be exposed.
- Structure may change accidentally.

Using explicit response models:
- Filters output.
- Enforces shape.
- Protects contracts.

This is a major security and stability practice.

---

## 8. Separation of Models

There are typically three types of models:

1. Request Models
   Used for input validation.

2. Domain Models
   Used internally in business logic.

3. Response Models
   Used for output shaping.

Never:
- Use database models directly as response models.
- Trust incoming data without validation.

Separation prevents:
- Data leakage
- Tight coupling
- Versioning chaos

---

## 9. Validation Errors

Validation failures return structured error responses.

Example:
422 Unprocessable Entity

Validation errors include:
- Field location
- Error message
- Error type

This makes APIs predictable and debuggable.

Validation is not optional.
It is a security layer.

---

## 10. Serialization as a Security Boundary

Most injection attacks begin at input boundaries.

Proper validation:
- Prevents malformed input.
- Blocks unexpected structures.
- Limits attack surface.

Never trust client input.
Always validate at the boundary.

---

## 11. Performance Considerations

Serialization has a cost.

Large payloads:
- Increase CPU usage.
- Increase memory pressure.
- Increase network latency.

Nested objects:
- Increase parsing complexity.

Optimizing APIs may involve:
- Reducing payload size.
- Avoiding deeply nested structures.
- Returning only necessary fields.

---

## 12. Versioning & Backward Compatibility

When APIs evolve:
- Adding fields is usually safe.
- Removing fields breaks clients.
- Changing types breaks clients.

Explicit schemas:
- Make versioning manageable.
- Enable controlled evolution.

Without schemas:
- API drift becomes inevitable.

---

## 13. What FastAPI Abstracts

FastAPI automatically:
- Parses JSON.
- Validates data.
- Serializes responses.
- Handles content negotiation.

But the underlying process still exists.

In lower-level systems (e.g., Go),
you must:
- Decode JSON manually.
- Validate explicitly.
- Encode responses manually.

Understanding serialization makes framework usage intentional.

---

## 14. Mental Model

Client JSON
    ↓
Deserialization
    ↓
Validation
    ↓
Safe Python Object
    ↓
Business Logic
    ↓
Response Object
    ↓
Serialization
    ↓
JSON Response

Serialization is the gatekeeper
between untrusted input and trusted logic.

---

## 15. Common Mistakes

- Accepting raw dictionaries everywhere.
- Returning database models directly.
- Skipping response models.
- Ignoring validation errors.
- Allowing overly flexible schemas.
- Using inconsistent datetime formats.

These mistakes:
- Create security risks.
- Break API stability.
- Increase technical debt.

---

## Final Takeaway

Serialization defines the API contract.

It is not just data conversion.
It is:
- Validation
- Security
- Documentation
- Stability
- Boundary protection

If routing is the switchboard,
serialization is the security checkpoint.

Mastering serialization means
you control how data enters and leaves your system.

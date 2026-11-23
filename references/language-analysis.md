# Language-aware investigation

Read only the sections for languages and boundaries actually found in the target module. Never assume a language boundary exists from file extensions alone. Trace behavior rather than translating syntax into requirements.

## C
- Identify exported headers and functions, compilation units, macros, `#if` guards and build definitions.
- Follow function pointers, callback registrations, dispatch tables and indirect calls; mark unresolved targets.
- Track ownership of global/static state, buffers, resource handles, return values, `errno` and error codes.
- Distinguish compile-time alternatives from paths present in the selected build.

## C++
- Inspect public classes/interfaces, virtual dispatch and concrete implementations reachable from factories/registrations.
- Check overload resolution, templates/specializations where relevant, callbacks, exceptions and error-return conventions.
- Follow RAII ownership, destructor side effects, moves and lifetime-sensitive asynchronous operations.
- Do not assume all subclasses are reachable in the selected product/build.

## Java
- Trace public methods, interface implementations, inheritance, overrides and dependency injection.
- Inspect exceptions, nullability, callbacks, threading, synchronization, executor/handler dispatch and persistent state.
- For reflection/service loaders, identify configuration or registration evidence; mark unresolved runtime targets.
- Distinguish API declarations and annotations from enforced behavior.

## JNI and mixed-language boundaries
- Map Java `native` declarations to registered JNI functions (`RegisterNatives` or naming convention) with evidence.
- Track argument/value conversion, ownership and lifetime, exception translation, status/error propagation, and thread attachment where relevant.
- Trace across the boundary only until the module's observable behavior is explained. If mapping cannot be proven, label the edge unresolved.
- For other mixed-language FFI or IPC, apply the same boundary-contract approach rather than forcing a JNI model.

## Cross-language call-edge record
| From (language/symbol) | To (language/symbol) | Binding mechanism | Condition / effect | Evidence | Status |
|---|---|---|---|---|---|
| | | direct / virtual / pointer / callback / JNI / IPC | | | verified / inferred / unresolved |

A call edge is not automatically a requirement. Extract a requirement only after identifying a verifiable trigger, condition and observable result.

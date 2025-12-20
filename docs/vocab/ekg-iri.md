---
author:
- Jacobus Geluk
description: >-
  An EKG/IRI is an HTTPS-based Internationalised Resource Identifier that forms
  the primary identifier of an object in the EKG. Learn about EKG identity and
  web-resolvable identifiers.
keywords:
  - EKG/IRI
  - IRI
  - internationalised resource identifier
  - web-resolvable identifier
  - EKG method
  - enterprise knowledge graph
schema_type: "Article"
---
# EKG/IRI

An EKG/IRI is an HTTPS-based[^https] _Internationalised Resource Identifier (IRI)_ 
that forms the primary identifier of an object[^object] in the EKG.

According to the first---and most important---of the ten principles 
of the EKGF, [Principle 1: Identity](https://principles.ekgf.org/principle/01-identity):

_Any EKG/IRI is [universally unique](ekg-id.md#universally-unique), 
[opaque](ekg-id.md#opaque), [permanent](ekg-id.md#permanent), 
[non-reassignable](ekg-id.md#non-reassignable) and 
[web-resolvable](ekg-id.md#web-resolvable)._

An EKG/IRI consists of a locator-part and an identifier-part: `[locator][identifier]`.
Where the `[identifier]` is an [EKG/ID](ekg-id.md).
For instance, it could look as follows:

`https://acme.com/id/uuid:e3f0f238-81f2-4434-a441-bb5f5cf10caa`

Where `https://acme.com/id/` is the locator part that assures that any user or system
in your enterprise can resolve the EKG/IRI: a user can click on the link and see
a meaningful webpage representing the object, a system can fetch all the RDF triples
for the given object.

The `uuid:e3f0f238-81f2-4434-a441-bb5f5cf10caa` part is the identifier aka EKG/ID.

There are many other acceptable forms of EKG/IRIs, besides being based on
the UUID v4 standard (a random number), it can also be based on other standards:

- SHA-128+ (hash based)
- Web DID (but only when opaque)

See also [Principle 1: Identity](https://principles.ekgf.org/principle/01-identity).

[^https]: Many RDF datasets are still using `http://*` URLs for their identifiers
rather than `https://*` URLs. This is not secure, proliferation of such URLs across
the enterprise or beyond cannot be promoted due to security concerns. Therefore,
all EKG/IRIs shall be using the SSL/TLS-based variant of HTTP: use `https://`-urls.

[^object]: There are many more or less equivalent terms for object, in some literature
in the semantic technology world it's called "a Thing" or "an Individual" or "a Resource".
Programmers with an object-oriented background could call it "an Instance" (although
its not exactly the same). 

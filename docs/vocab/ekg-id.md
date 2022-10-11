# EKG Identifier (EKG/ID)

_An EKG Identifier identifies an object[^object] in an [EKG](ekg.md)
and is [universally unique](#universally-unique), [opaque](#opaque),
[permanent](#permanent), [resolvable](#resolvable) and 
[non-reassignable](#non-reassignable)._

!!! note inline end "Web-resolvability"

    Usually the EKG/ID is part of an [EKG/IRI](ekg-iri.md) which
    makes it "web-resolvable" as well, but at higher levels of 
    technical EKG maturity there may be other technical ways to
    ensure "resolvability". It may not be required anymore to
    mandate the use of the HTTP protocol for that, there may be
    other more advanced protocols that deliver full resolvability
    with additional features that cannot be provided by HTTP.

Not to be confused with _Canonical Identifiers_.

## Universally Unique

A universally unique opaque (i.e. meaningless) number,
either based on a hash or a random number, optionally signed
that uniquely identifies an object[^object] in the EKG.

## Opaque

An identifier is "opaque" if it provides no information about
the thing it identifies other than being a seemingly random string
or number.

An EKG/ID needs to be opaque because one of the most impactful and
important objectives of EKG is to maximise proliferation of web-resolvable
EKG Identifiers (i.e. [EKG/IRIs](ekg-iri.md)) across not only the
internal enterprise but also its larger ecosystem or even beyond that.
These identifiers end up for years, perhaps decades, in all kinds of
databases, spreadsheets, documents, long term storage etc.
Therefore, no user or system should be able to derive any meaning
or actual information from these identifiers.

## Permanent

The EKG/IRI identifier is permanent and can safely be proliferated across
the enterprise's universe---including its ecosystem---and will be used
for the expression of facts about the object including relationships
between objects.

## Non-reassignable

An EKG Identifier cannot be reused for another object.
Once attached to a given thing in the EKG, it remains the identifier
of that thing forever, even until after the end of the logical life-cycle
of that thing.

## Resolvable

_Resolving_ an identifier can be done in three ways:

1. using it in a transaction---i.e. a query or update statement---submitted or routed via an
   internet protocol (e.q. HTTP API) or other means (e.g. Kafka) to a "lookup service" that 
   translates one or more given "features" of an object to its corresponding _EKG Identifier_ 
   (i.e. an EKG/ID or an EKG/IRI).
2. constructing it via a standardized policy from key components and applying a hash and optionally
   signing it---where the object represented by the EKG identifier may or may not already exist.
3. constructing it by giving the object an EKG identifier based on a random number in case 
   the EKG is the authoritative source for the given object.

## Web-resolvable

An EKG Identifier (EKG/ID) (currently, see side box) becomes "web-resolvable", 
by making it part of an EKG/IRI, i.e. by making it a URL and thereby prefixing
the "identifier part" with "a locator":

`[locator][identifier]`

Where `[locator]` could be something like `https://acme.com/id/`.

If an external dataset is loaded into your organization's EKG then
you could decide _not_ to give each object in that dataset to have
a standard EKG/IRI and just use the provided identifiers, whatever
they may be.
However, that could mean that it will be technically more difficult
to make these external IRIs resolvable to your organization's EKG
and that the proliferation of those external identifiers across your
data and technical landscape could create a dependency towards the
organization that provided the dataset.

[^object]: there are many more or less equivalent terms for object, in some literature
in the semantic technology world it's called "a Thing" or "an Individual" or "a Resource".
Programmers with an object-oriented background could call it "an Instance" (although
its not exactly the same). 

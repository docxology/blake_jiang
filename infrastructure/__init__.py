"""Standalone infrastructure shim.

The blake_jiang project was originally developed inside the
docxology/template research workspace, which supplies a richer
infrastructure layer (logging, pipeline orchestration, validation,
rendering). This shim provides the minimum compatible API so the project
runs as a standalone repository as well. When the project is dropped back
into the template workspace, the template's infrastructure package takes
precedence by ordinary Python import resolution.
"""

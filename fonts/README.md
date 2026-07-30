# Ocelotl Fonts

Ocelotl Roku includes bundled fonts for subtitle rendering and supports
custom fonts provided by the Jellyfin server.

## Server fonts

When custom server fonts are enabled, Ocelotl downloads the fonts provided
by the server and creates two independent font groups.

The first valid server font family is used for application UI elements.

This allows Roku UI text to display additional character sets because Roku
does not provide automatic font fallback.

Example:

```text
NotoSans.ttf
NotoSansJP.ttf
```

Result:

```text
UI font:
NotoSans.ttf

Caption font:
NotoSansJP.ttf
```

## Caption fonts

Subtitle rendering uses a separate font selection process.

A server font can be detected as a caption font when its filename contains
one of the following identifiers:

```text
CC
Caption
Subtitle
CJK
JP
Japan
KR
Korea
HK
Chinese
ZH
```

Examples:

```text
Arial-CC.ttf
NotoSansJP.ttf
NotoSansKR.ttf
```

These fonts are used only for caption rendering.

## Caption font family

Ocelotl builds a complete font family:

```text
Regular
Bold
Italic
BoldItalic
```

If a style is missing, the available style is reused.

Example:

```text
NotoSansJP.ttf
```

becomes:

```text
Regular NotoSansJP.ttf
Bold NotoSansJP.ttf
Italic NotoSansJP.ttf
BoldItalic NotoSansJP.ttf
```

## Bundled caption fonts

If no server caption font is found, Ocelotl uses its bundled fonts according
to the Roku caption font preference.

Mapping:

```text
Default OcelotlSans
Proportional Serif OcelotlSerif
Monospaced Serif OcelotlMono
Monospaced Sans-Serif OcelotlMono
Small Caps OcelotlSansSmallCaps
```

## Why this exists

Roku does not support automatic font fallback.

Without an appropriate font, characters outside the selected font coverage
may appear as missing glyphs.

Providing fonts such as:

```text
NotoSansJP.ttf
NotoSansKR.ttf
NotoSansCJK.ttf
```

allows subtitles and metadata containing additional character sets to render
correctly.

## Design notes

Server fonts and caption fonts are intentionally separated.

Server fonts improve UI character coverage, while caption fonts are selected
specifically for subtitle rendering.

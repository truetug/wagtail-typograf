wagtail-typograf
================

A Wagtail plugin to add [typo](https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index) functionality to rich text field (draftail).

Demo
----

![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)
demo.gif

![demo](https://raw.githubusercontent.com/truetug/wagtail-typograf/master/demo.gif)

Installation
------------

- Install with pip
```pip install wagtail-typograf```
- Add app name to your list of installed apps
```
INSTALLED_APPS = [
  ...
  "wagtail_typograf",
]```
- Add typograf url to your urlpatterns (for now "/api/typograf/" is strongly hardcoded in js)
```
urlpatterns = [
  ...
  path('api/', include('wagtail_typograf.urls')),
  ...
]
```
- If you use limit number of features in RichTextBlock, don't forget to add `typograf` to its list
```text_block = RichTextBlock(
        features=[
            "bold", "italic", "ol", "ul", "hr", 
            "link", "document-link", "typograf",
        ],
        ...
)```

Usage
-----

Write or paste text content, push the ¶-button.

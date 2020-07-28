# text-manipulation-koans

Are you effective with your text editor? Editing text is breathing to
computer people ([and you should practice breathing, as
well](https://www.health.harvard.edu/lung-health-and-disease/learning-diaphragmatic-breathing)).

You can practice or demonstrate your prowess with this tool.

## Criteria for being "fluent" with a text editor, borrowed from The Pragmatic Programmer

* When editing text, move and make selections by character, word, line, and paragraph.
* When editing code, move by various syntactic units (matching delimiters, functions, modules, ...)
* Reindent code following changes.
* Comment and uncomment blocks of code with a single command.
* Undo and redo changes.
* Split the editor window into multiple panels, and navigate between them.
* Navigate to a particular line number.
* Sort selected lines.
* Search for both strings and regular expressions, and repeat previous searches.
* Temporarily create multiple cursors based on a selection or on a pattern match, and edit the text at each in parallel.
* Display compilation errors in the current project.
* Run the current project's tests.


## Requirements
1. [fswatch](https://github.com/emcrisostomo/fswatch)
2. [Python wrapper for fswatch](https://pypi.org/project/fswatch/)

## Running

Execute `./illuminate_the_way.py` .

Follow the directions it prints out.

It will tell you to open new files it generates with your text
editor. It will then time from the moment you open to the moment you
save the correct result.


## Future work

1. Add many more tests in some coherent way.
2. Save scores (and allow sharing for maximum glory).
3. Finally end the [editor war](https://en.wikipedia.org/wiki/Editor_war).

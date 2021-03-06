Readme
=======

Made in Python3 and PyQt5

Source: 
* Japanese: Core 10k context sentences, WaniKani context sentences, Grammar sentences from Jtest4you
* Chinese: Chinese grammar Wiki, SpoonFed Chinese

Sorted by WaniKani levels and JLPT level.

For Chinese, sorted by Hanzi level and grammar level

Sentence randomizer and sentence timer. Try to read as many sentences as possible in 1 minute.

Text-to-speech also implemented.

Tested only on Mac

## Build instructions

* Mac OSX: `python setup.py py2app`
* Windows: `python setup.py py2exe`
* Linux: `python setup.py install`

## Executables

* [Mac OSX](https://www.dropbox.com/sh/3u8z8fhjvhjblrx/AADuCE9GYROUMPMz3Pe0Ildsa?dl=0)

## Command line

Duendecat can now be evoked from command line,

```
$ duendecat
$ duendecat-gui   # an equivalent of duendecat --gui
```

### Command-line arguments
```
usage: duendecat [-h] [--gui] [--lang LANG] [--level LEVEL] [--sheet SHEET]
                 [--times TIMES] [--lang-first] [--reverse] [--silent]
                 [--speak] [--auto] [--no-auto]
                 [--show-answer-lapse SHOW_ANSWER_LAPSE]
                 [--new-question-lapse NEW_QUESTION_LAPSE]
                 [--speech-engine SPEECH_ENGINE] [--log]

optional arguments:
  -h, --help            show this help message and exit
  --gui                 Invoke GUI mode
  --lang LANG           cn or jp (default: jp)
  --level LEVEL         Kanji/Hanzi level (default: 20)
  --sheet SHEET         Worksheet to read (default: depends)
  --times TIMES         Number of times to repeat (CLI) (default: 60)
  --lang-first          Lang JP/CN before EN
  --reverse             EN before Lang JP/CN (default: False)
  --silent              No vocal output
  --speak               Vocal output (default: True)
  --auto                Loop automatically (default: True)
  --no-auto             Do not loop automatically
  --show-answer-lapse SHOW_ANSWER_LAPSE
                        Lapse in seconds to show answer (default: 3)
  --new-question-lapse NEW_QUESTION_LAPSE
                        Lapse in seconds to show new question (default: 1)
  --speech-engine SPEECH_ENGINE
                        Set speech engine. "google" for google_speech
                        (default: not_set)
  --log                 Activate debugging mode (default: False)
```

## maKeys.py


maKeys is a module dedicated to emulating keypresses for macOS. It utilizes [Quartz Core Graphics](https://developer.apple.com/documentation/coregraphics) for its processing of low-level, user input events.

One thing to note about maKeys.py is the lack of high-level, keyboard event emulation that some other libraries offer. This was an intentional decision as maKeys.py was written specifically for piano.py and my goals for the project, requiring low-level manipulation of keyboard events for macOS that I couldn't find in other libraries.

If you desire to use maKeys.py outside of this project, bear in mind that some code statements can be entirely omitted without loss in functionality, as particular aspects exist for the sake of piano.py. Which statements could be removed will be dependent on your use-case. 

For the rest of this document, I will explain the functions of maKeys.py, along with the reasoning behind particular aspects of its implementation.

## Functions:

[pressLetter(singleChar)](#pressLettersingleChar)
[releaseLetter(singleChar)](#releaseLettersingleChar)
[typeLetter(singleChar)](#typeLettersingleChar)

## pressLetter(singleChar)
```pressLetter``` is a function that has three main cases of execution dependent on the ``singleChar`` that is passed. 
### Case 1: Lowercase Keys
If ```singleChar``` is a lowercase key, the function will create a keyboard event of pressing down the key. Once this is done, the function will check that the lowercase key event does not contain the flag for the Shift key modifier being held. If that is the case, the event will be set with the Shift flag XOR'd out. This is to ensure that the event posted will be recognized as a lowercase key. The event is then posted.
### Case 2: Uppercase Keys
If ``singleChar`` is an uppercase key, the function will first create, and post a keyboard event of pressing down the Shift key. This mainly came as a necessity for virtual pianos to recognize that an uppercase key was being pressed. From there, the event of pressing down ``singleChar`` is created. However, prior to posting it, the Shift flag of the event must be set to produce an uppercase character. This is done, and then the event is posted. Promptly after this, a ``shiftUp`` event is created and posted, indicating that the Shift key is released. This statement is necessary for the functionality of piano.py, as the holding of the Shift key would cause all subsequent notes within the chord to be capitalized.
### Case 3: Unknown Key
``singleChar``is not present in any of the dictionaries, meaning it is ignored and no keyboard event is created.

## releaseLetter(singleChar)
``releaseLetter`` is a function that serves to be used after``pressLetter``. It essentially just creates and posts release key events for the provided ``singleChar``. For the sake of brevity I won't go into much detail about this function. Most of the explanation for the prior function can be extrapolated to this one, albeit with press events now being release events. One thing to make note of is the lack of a Shift key release event when given an uppercase key. This is intentional, as the release of the Shift key is already handled in ``pressLetter``.

## typeLetter(singleChar)
``typeLetter`` is a function that combines the procedures of ``pressLetter`` and ``releaseLetter``, simplifying the number of functions needed to type a letter.

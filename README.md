# Document-Feature-Space

# To Run Code
```
python main.py
```

# To Run Tests
```
python -m unittest discover -s tests -p '*_test.py'
```

# Notes
- Does not account for prossessive apostrophes
- Considers multiple contractions ya'll've -> ya will have
- When vowel/y removed from middle of a word it was replaced with z (a consonant) to keep word_length the same for looping

## file representation
The following prases:

Hello. My name is Keira. I am in my final year of univeristy.

Would be stored as follows (an array of sentences which are arrays of words)
[
    [
        ['hello']
    ],
    [
        ['my'], ['name'], ['is'], ['keira']
    ],
    [
        ['i'], ['am'], ['in'], ['my'], ['final'], ['year'], ['of'], ['university']
    ]
]

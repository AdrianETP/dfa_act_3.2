"""
DFA que Reconoce operaciones aritmetivas
Implementacion de metodos computacionales
"""

transiciones = {
    "start": {
        "//": "comentario", "=": "igualdad", ".": "error",

        "A": "variable", "B": "variable", "C": "variable", "D": "variable", "E": "variable",
        "F": "variable", "G": "variable", "H": "variable", "I": "variable", "J": "variable",
        "K": "variable", "L": "variable", "M": "variable", "N": "variable", "O": "variable",
        "P": "variable", "Q": "variable", "R": "variable", "S": "variable", "T": "variable",
        "U": "variable", "V": "variable", "W": "variable", "X": "variable", "Y": "variable",
        "Z": "variable", "a": "variable", "b": "variable", "c": "variable", "d": "variable",
        "e": "variable", "f": "variable", "g": "variable", "h": "variable", "i": "variable",
        "j": "variable", "k": "variable", "l": "variable", "m": "variable", "n": "variable",
        "o": "variable", "p": "variable", "q": "variable", "r": "variable", "s": "variable",
        "t": "variable", "u": "variable", "v": "variable", "w": "variable", "x": "variable",
        "y": "variable", "z": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "suma", "-": "resta", "*": "multiplicacion", "/": "division", "^": "poder",
        "(": "parentesisA", ")": "parentesisC", " ": "espacio"
    },
    "numero": {
        "//": "comentario", "=": "igualdad", ".": "float",

        "A": "variable", "B": "variable", "C": "variable", "D": "variable", "E": "numExp",
        "F": "variable", "G": "variable", "H": "variable", "I": "variable", "J": "variable",
        "K": "variable", "L": "variable", "M": "variable", "N": "variable", "O": "variable",
        "P": "variable", "Q": "variable", "R": "variable", "S": "variable", "T": "variable",
        "U": "variable", "V": "variable", "W": "variable", "X": "variable", "Y": "variable",
        "Z": "variable", "a": "variable", "b": "variable", "c": "variable", "d": "variable",
        "e": "variable", "f": "variable", "g": "variable", "h": "variable", "i": "variable",
        "j": "variable", "k": "variable", "l": "variable", "m": "variable", "n": "variable",
        "o": "variable", "p": "variable", "q": "variable", "r": "variable", "s": "variable",
        "t": "variable", "u": "variable", "v": "variable", "w": "variable", "x": "variable",
        "y": "variable", "z": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "suma", "-": "resta", "*": "multiplicacion", "/": "division", "^": "poder",
        "(": "parentesisA", ")": "parentesisC", " ": "espacio"
    },
    "numExp": {
        "//": "comentario", "=": "igualdad", ".": "float",

        "A": "error", "B": "error", "C": "error", "D": "error", "E": "error",
        "F": "error", "G": "error", "H": "error", "I": "error", "J": "error",
        "K": "error", "L": "error", "M": "error", "N": "error", "O": "error",
        "P": "error", "Q": "error", "R": "error", "S": "error", "T": "error",
        "U": "error", "V": "error", "W": "error", "X": "error", "Y": "error",
        "Z": "error", "a": "error", "b": "error", "c": "error", "d": "error",
        "e": "error", "f": "error", "g": "error", "h": "error", "i": "error",
        "j": "error", "k": "error", "l": "error", "m": "error", "n": "error",
        "o": "error", "p": "error", "q": "error", "r": "error", "s": "error",
        "t": "error", "u": "error", "v": "error", "w": "error", "x": "error",
        "y": "error", "z": "error",

        "0": "numExp", "1": "numExp", "2": "numExp", "3": "numExp", "4": "numExp",
        "5": "numExp", "6": "numExp", "7": "numExp", "8": "numExp", "9": "numExp",

        "+": "error", "-": "numExp", "*": "error", "/": "erroe", "^": "error",
        "(": "error", ")": "error", " ": "espacio"

    },
    "floatExp": {
        "//": "comentario", "=": "igualdad", ".": "float",

        "A": "error", "B": "error", "C": "error", "D": "error", "E": "error",
        "F": "error", "G": "error", "H": "error", "I": "error", "J": "error",
        "K": "error", "L": "error", "M": "error", "N": "error", "O": "error",
        "P": "error", "Q": "error", "R": "error", "S": "error", "T": "error",
        "U": "error", "V": "error", "W": "error", "X": "error", "Y": "error",
        "Z": "error", "a": "error", "b": "error", "c": "error", "d": "error",
        "e": "error", "f": "error", "g": "error", "h": "error", "i": "error",
        "j": "error", "k": "error", "l": "error", "m": "error", "n": "error",
        "o": "error", "p": "error", "q": "error", "r": "error", "s": "error",
        "t": "error", "u": "error", "v": "error", "w": "error", "x": "error",
        "y": "error", "z": "error",

        "0": "floatExp", "1": "floatExp", "2": "floatExp", "3": "floatExp", "4": "floatExp",
        "5": "floatExp", "6": "floatExp", "7": "floatExp", "8": "floatExp", "9": "floatExp",

        "+": "error", "-": "floatExp", "*": "error", "/": "erroe", "^": "error",
        "(": "error", ")": "error", " ": "espacio"

    },
    "variable": {
        "//": "comentario", "=": "igualdad", ".": "error",

        "A": "variable", "B": "variable", "C": "variable", "D": "variable", "E": "variable",
        "F": "variable", "G": "variable", "H": "variable", "I": "variable", "J": "variable",
        "K": "variable", "L": "variable", "M": "variable", "N": "variable", "O": "variable",
        "P": "variable", "Q": "variable", "R": "variable", "S": "variable", "T": "variable",
        "U": "variable", "V": "variable", "W": "variable", "X": "variable", "Y": "variable",
        "Z": "variable", "a": "variable", "b": "variable", "c": "variable", "d": "variable",
        "e": "variable", "f": "variable", "g": "variable", "h": "variable", "i": "variable",
        "j": "variable", "k": "variable", "l": "variable", "m": "variable", "n": "variable",
        "o": "variable", "p": "variable", "q": "variable", "r": "variable", "s": "variable",
        "t": "variable", "u": "variable", "v": "variable", "w": "variable", "x": "variable",
        "y": "variable", "z": "variable",

        "0": "variable", "1": "variable", "2": "variable", "3": "variable", "4": "variable",
        "5": "variable", "6": "variable", "7": "variable", "8": "variable", "9": "variable",

        "+": "suma", "-": "resta", "*": "multiplicacion", "/": "division", "^": "poder",
        "(": "parentesisA", ")": "parentesisC", " ": "espacio"
    },
    "suma": {
        "//": "comentario", "=": "error", ".": "error",

        "A": "variable", "B": "variable", "C": "variable", "D": "variable", "E": "variable",
        "F": "variable", "G": "variable", "H": "variable", "I": "variable", "J": "variable",
        "K": "variable", "L": "variable", "M": "variable", "N": "variable", "O": "variable",
        "P": "variable", "Q": "variable", "R": "variable", "S": "variable", "T": "variable",
        "U": "variable", "V": "variable", "W": "variable", "X": "variable", "Y": "variable",
        "Z": "variable", "a": "variable", "b": "variable", "c": "variable", "d": "variable",
        "e": "variable", "f": "variable", "g": "variable", "h": "variable", "i": "variable",
        "j": "variable", "k": "variable", "l": "variable", "m": "variable", "n": "variable",
        "o": "variable", "p": "variable", "q": "variable", "r": "variable", "s": "variable",
        "t": "variable", "u": "variable", "v": "variable", "w": "variable", "x": "variable",
        "y": "variable", "z": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "error", "-": "error", "*": "error", "/": "error", "^": "error",
        "(": "parentesisA", ")": "parentesisC", " ": "espacio"
    },

    "poder": {
        "//": "comentario", "=": "error", ".": "error",

        "A": "variable", "B": "variable", "C": "variable", "D": "variable", "E": "variable",
        "F": "variable", "G": "variable", "H": "variable", "I": "variable", "J": "variable",
        "K": "variable", "L": "variable", "M": "variable", "N": "variable", "O": "variable",
        "P": "variable", "Q": "variable", "R": "variable", "S": "variable", "T": "variable",
        "U": "variable", "V": "variable", "W": "variable", "X": "variable", "Y": "variable",
        "Z": "variable", "a": "variable", "b": "variable", "c": "variable", "d": "variable",
        "e": "variable", "f": "variable", "g": "variable", "h": "variable", "i": "variable",
        "j": "variable", "k": "variable", "l": "variable", "m": "variable", "n": "variable",
        "o": "variable", "p": "variable", "q": "variable", "r": "variable", "s": "variable",
        "t": "variable", "u": "variable", "v": "variable", "w": "variable", "x": "variable",
        "y": "variable", "z": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "error", "-": "error", "*": "error", "/": "error", "^": "error",
        "(": "parentesisA", ")": "parentesisC", " ": "espacio"
    },
    "resta": {
        "//": "comentario", "=": "error", ".": "error",

        "A": "variable", "B": "variable", "C": "variable", "D": "variable", "E": "variable",
        "F": "variable", "G": "variable", "H": "variable", "I": "variable", "J": "variable",
        "K": "variable", "L": "variable", "M": "variable", "N": "variable", "O": "variable",
        "P": "variable", "Q": "variable", "R": "variable", "S": "variable", "T": "variable",
        "U": "variable", "V": "variable", "W": "variable", "X": "variable", "Y": "variable",
        "Z": "variable", "a": "variable", "b": "variable", "c": "variable", "d": "variable",
        "e": "variable", "f": "variable", "g": "variable", "h": "variable", "i": "variable",
        "j": "variable", "k": "variable", "l": "variable", "m": "variable", "n": "variable",
        "o": "variable", "p": "variable", "q": "variable", "r": "variable", "s": "variable",
        "t": "variable", "u": "variable", "v": "variable", "w": "variable", "x": "variable",
        "y": "variable", "z": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "error", "-": "error", "*": "error", "/": "error", "^": "error",
        "(": "parentesisA", ")": "parentesisC", " ": "espacio"
    },
    "multiplicacion": {
        "//": "comentario", "=": "error", ".": "error",

        "A": "variable", "B": "variable", "C": "variable", "D": "variable", "E": "variable",
        "F": "variable", "G": "variable", "H": "variable", "I": "variable", "J": "variable",
        "K": "variable", "L": "variable", "M": "variable", "N": "variable", "O": "variable",
        "P": "variable", "Q": "variable", "R": "variable", "S": "variable", "T": "variable",
        "U": "variable", "V": "variable", "W": "variable", "X": "variable", "Y": "variable",
        "Z": "variable", "a": "variable", "b": "variable", "c": "variable", "d": "variable",
        "e": "variable", "f": "variable", "g": "variable", "h": "variable", "i": "variable",
        "j": "variable", "k": "variable", "l": "variable", "m": "variable", "n": "variable",
        "o": "variable", "p": "variable", "q": "variable", "r": "variable", "s": "variable",
        "t": "variable", "u": "variable", "v": "variable", "w": "variable", "x": "variable",
        "y": "variable", "z": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "error", "-": "error", "*": "error", "/": "error", "^": "error",
        "(": "parentesisA", ")": "parentesisC", " ": "espacio"
    },
    "division": {
        "//": "comentario", "=": "error", ".": "error",

        "A": "variable", "B": "variable", "C": "variable", "D": "variable", "E": "variable",
        "F": "variable", "G": "variable", "H": "variable", "I": "variable", "J": "variable",
        "K": "variable", "L": "variable", "M": "variable", "N": "variable", "O": "variable",
        "P": "variable", "Q": "variable", "R": "variable", "S": "variable", "T": "variable",
        "U": "variable", "V": "variable", "W": "variable", "X": "variable", "Y": "variable",
        "Z": "variable", "a": "variable", "b": "variable", "c": "variable", "d": "variable",
        "e": "variable", "f": "variable", "g": "variable", "h": "variable", "i": "variable",
        "j": "variable", "k": "variable", "l": "variable", "m": "variable", "n": "variable",
        "o": "variable", "p": "variable", "q": "variable", "r": "variable", "s": "variable",
        "t": "variable", "u": "variable", "v": "variable", "w": "variable", "x": "variable",
        "y": "variable", "z": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "error", "-": "error", "*": "error", "/": "comentario", "^": "error",
        "(": "parentesisA", ")": "parentesisC", " ": "espacio"
    },
    "parentesisA": {
        "//": "comentario", "=": "igualdad", ".": "error",

        "A": "variable", "B": "variable", "C": "variable", "D": "variable", "E": "variable",
        "F": "variable", "G": "variable", "H": "variable", "I": "variable", "J": "variable",
        "K": "variable", "L": "variable", "M": "variable", "N": "variable", "O": "variable",
        "P": "variable", "Q": "variable", "R": "variable", "S": "variable", "T": "variable",
        "U": "variable", "V": "variable", "W": "variable", "X": "variable", "Y": "variable",
        "Z": "variable", "a": "variable", "b": "variable", "c": "variable", "d": "variable",
        "e": "variable", "f": "variable", "g": "variable", "h": "variable", "i": "variable",
        "j": "variable", "k": "variable", "l": "variable", "m": "variable", "n": "variable",
        "o": "variable", "p": "variable", "q": "variable", "r": "variable", "s": "variable",
        "t": "variable", "u": "variable", "v": "variable", "w": "variable", "x": "variable",
        "y": "variable", "z": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "suma", "-": "resta", "*": "multiplicacion", "/": "division", "^": "poder",
        "(": "parentesisA", ")": "parentesisC", " ": "espacio"
    },
    "parentesisC": {
        "//": "comentario", "=": "igualdad", ".": "error",

        "A": "variable", "B": "variable", "C": "variable", "D": "variable", "E": "variable",
        "F": "variable", "G": "variable", "H": "variable", "I": "variable", "J": "variable",
        "K": "variable", "L": "variable", "M": "variable", "N": "variable", "O": "variable",
        "P": "variable", "Q": "variable", "R": "variable", "S": "variable", "T": "variable",
        "U": "variable", "V": "variable", "W": "variable", "X": "variable", "Y": "variable",
        "Z": "variable", "a": "variable", "b": "variable", "c": "variable", "d": "variable",
        "e": "variable", "f": "variable", "g": "variable", "h": "variable", "i": "variable",
        "j": "variable", "k": "variable", "l": "variable", "m": "variable", "n": "variable",
        "o": "variable", "p": "variable", "q": "variable", "r": "variable", "s": "variable",
        "t": "variable", "u": "variable", "v": "variable", "w": "variable", "x": "variable",
        "y": "variable", "z": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "suma", "-": "resta", "*": "multiplicacion", "/": "division", "^": "poder",
        "(": "parentesisA", ")": "parentesisC", " ": "espacio"
    },
    "igualdad": {
        "//": "comentario", "=": "error", ".": "error",

        "A": "variable", "B": "variable", "C": "variable", "D": "variable", "E": "variable",
        "F": "variable", "G": "variable", "H": "variable", "I": "variable", "J": "variable",
        "K": "variable", "L": "variable", "M": "variable", "N": "variable", "O": "variable",
        "P": "variable", "Q": "variable", "R": "variable", "S": "variable", "T": "variable",
        "U": "variable", "V": "variable", "W": "variable", "X": "variable", "Y": "variable",
        "Z": "variable", "a": "variable", "b": "variable", "c": "variable", "d": "variable",
        "e": "variable", "f": "variable", "g": "variable", "h": "variable", "i": "variable",
        "j": "variable", "k": "variable", "l": "variable", "m": "variable", "n": "variable",
        "o": "variable", "p": "variable", "q": "variable", "r": "variable", "s": "variable",
        "t": "variable", "u": "variable", "v": "variable", "w": "variable", "x": "variable",
        "y": "variable", "z": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "error", "-": "error", "*": "error", "/": "error", "^": "error",
        "(": "parentesisA", ")": "parentesisC", " ": "espacio"
    },
    "float": {
        "//": "error", "=": "error", ".": "error",

        "A": "error", "B": "error", "C": "error", "D": "error", "E": "floatExp",
        "F": "error", "G": "error", "H": "error", "I": "error", "J": "error",
        "K": "error", "L": "error", "M": "error", "N": "error", "O": "error",
        "P": "error", "Q": "error", "R": "error", "S": "error", "T": "error",
        "U": "error", "V": "error", "W": "error", "X": "error", "Y": "error",
        "Z": "error", "a": "error", "b": "error", "c": "error", "d": "error",
        "e": "error", "f": "error", "g": "error", "h": "error", "i": "error",
        "j": "error", "k": "error", "l": "error", "m": "error", "n": "error",
        "o": "error", "p": "error", "q": "error", "r": "error", "s": "error",
        "t": "error", "u": "error", "v": "error", "w": "error", "x": "error",
        "y": "error", "z": "error",

        "0": "float", "1": "float", "2": "float", "3": "float", "4": "float",
        "5": "float", "6": "float", "7": "float", "8": "float", "9": "float",

        "+": "suma", "-": "resta", "*": "multiplicacion", "/": "division", "^": "poder",
        "(": "error", ")": "error", " ": "espacio"
    },
    "comentario": {
        "//": "comentario", "=": "comentario", ".": "comentario",

        "A": "comentario", "B": "comentario", "C": "comentario", "D": "comentario", "E": "comentario",
        "F": "comentario", "G": "comentario", "H": "comentario", "I": "comentario", "J": "comentario",
        "K": "comentario", "L": "comentario", "M": "comentario", "N": "comentario", "O": "comentario",
        "P": "comentario", "Q": "comentario", "R": "comentario", "S": "comentario", "T": "comentario",
        "U": "comentario", "V": "comentario", "W": "comentario", "X": "comentario", "Y": "comentario",
        "Z": "comentario", "a": "comentario", "b": "comentario", "c": "comentario", "d": "comentario",
        "e": "comentario", "f": "comentario", "g": "comentario", "h": "comentario", "i": "comentario",
        "j": "comentario", "k": "comentario", "l": "comentario", "m": "comentario", "n": "comentario",
        "o": "comentario", "p": "comentario", "q": "comentario", "r": "comentario", "s": "comentario",
        "t": "comentario", "u": "comentario", "v": "comentario", "w": "comentario", "x": "comentario",
        "y": "comentario", "z": "comentario",

        "0": "comentario", "1": "comentario", "2": "comentario", "3": "comentario", "4": "comentario",
        "5": "comentario", "6": "comentario", "7": "comentario", "8": "comentario", "9": "comentario",

        "+": "comentario", "-": "comentario", "*": "comentario", "/": "comentario", "^": "comentario",
        "(": "comentario", ")": "comentario", " ": "comentario"
    },
    "error": {
        "//": "error", "=": "error", ".": "error",

        "A": "error", "B": "error", "C": "error", "D": "error", "E": "error",
        "F": "error", "G": "error", "H": "error", "I": "error", "J": "error",
        "K": "error", "L": "error", "M": "error", "N": "error", "O": "error",
        "P": "error", "Q": "error", "R": "error", "S": "error", "T": "error",
        "U": "error", "V": "error", "W": "error", "X": "error", "Y": "error",
        "Z": "error", "a": "error", "b": "error", "c": "error", "d": "error",
        "e": "error", "f": "error", "g": "error", "h": "error", "i": "error",
        "j": "error", "k": "error", "l": "error", "m": "error", "n": "error",
        "o": "error", "p": "error", "q": "error", "r": "error", "s": "error",
        "t": "error", "u": "error", "v": "error", "w": "error", "x": "error",
        "y": "error", "z": "error",

        "0": "error", "1": "error", "2": "error", "3": "error", "4": "error",
        "5": "error", "6": "error", "7": "error", "8": "error", "9": "error",

        "+": "error", "-": "error", "*": "error", "/": "error", "^": "error",
        "(": "error", ")": "error", " ": "error"
    },
    "espacio": {
        "//": "comentario", "=": "igualdad", ".": "error",

        "A": "variable", "B": "variable", "C": "variable", "D": "variable", "E": "variable",
        "F": "variable", "G": "variable", "H": "variable", "I": "variable", "J": "variable",
        "K": "variable", "L": "variable", "M": "variable", "N": "variable", "O": "variable",
        "P": "variable", "Q": "variable", "R": "variable", "S": "variable", "T": "variable",
        "U": "variable", "V": "variable", "W": "variable", "X": "variable", "Y": "variable",
        "Z": "variable", "a": "variable", "b": "variable", "c": "variable", "d": "variable",
        "e": "variable", "f": "variable", "g": "variable", "h": "variable", "i": "variable",
        "j": "variable", "k": "variable", "l": "variable", "m": "variable", "n": "variable",
        "o": "variable", "p": "variable", "q": "variable", "r": "variable", "s": "variable",
        "t": "variable", "u": "variable", "v": "variable", "w": "variable", "x": "variable",
        "y": "variable", "z": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "suma", "-": "resta", "*": "multiplicacion", "/": "division", "^": "poder",
        "(": "parentesisA", ")": "parentesisC", " ": "espacio"

    }
}


def lexerAritmetico(nombre_archivo):
    texto = open(nombre_archivo, "r")
    texto = texto.readlines()
    for i in range(0, len(texto)):
        estado = "start"
        texto[i] = texto[i].replace("\n", "")
        palabra = ""
        for j in range(0, len(texto[i])):
            elemento = texto[i][j]
            nuevo_estado = transiciones[estado][elemento]
            if nuevo_estado == estado or (estado == "numero" and nuevo_estado == "float") or (estado == "float" and nuevo_estado == "floatExp") or (estado == "division" and nuevo_estado == "comentario"):
                palabra += elemento
                estado = nuevo_estado
            elif nuevo_estado == "espacio":
                palabra += elemento
            else:
                print(palabra, estado)
                estado = nuevo_estado
                palabra = elemento
        print(palabra, estado)


lexerAritmetico("texto.txt")

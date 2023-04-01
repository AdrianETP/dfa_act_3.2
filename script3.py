"""
DFA que Reconoce operaciones aritmetivas
Implementacion de metodos computacionales
"""

# tabla de transiciones
transiciones = {
    "start": {
        "//": "comentario", "=": "igualdad", ".": "float",

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
        "y": "variable", "z": "variable", "_": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "suma", "-": "resta", "*": "multiplicacion", "/": "division", "^": "poder",
        "(": "parentesisA", ")": "parentesisC", " ": "start"
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
        "y": "variable", "z": "variable", "_": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "suma", "-": "resta", "*": "multiplicacion", "/": "division", "^": "poder",
        "(": "parentesisA", ")": "parentesisC", " ": "numero"
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
        "y": "error", "z": "error", "_": "error",

        "0": "numExp", "1": "numExp", "2": "numExp", "3": "numExp", "4": "numExp",
        "5": "numExp", "6": "numExp", "7": "numExp", "8": "numExp", "9": "numExp",

        "+": "error", "-": "numExp", "*": "error", "/": "erroe", "^": "error",
        "(": "error", ")": "error", " ": "numExp"

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
        "y": "error", "z": "error", "_": "error",

        "0": "floatExp", "1": "floatExp", "2": "floatExp", "3": "floatExp", "4": "floatExp",
        "5": "floatExp", "6": "floatExp", "7": "floatExp", "8": "floatExp", "9": "floatExp",

        "+": "error", "-": "floatExp", "*": "error", "/": "erroe", "^": "error",
        "(": "error", ")": "error", " ": "floatExp"

    },
    "variable": {
        "//": "comentario", "=": "igualdad", ".": "float",

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
        "y": "variable", "z": "variable", "_": "variable",

        "0": "variable", "1": "variable", "2": "variable", "3": "variable", "4": "variable",
        "5": "variable", "6": "variable", "7": "variable", "8": "variable", "9": "variable",

        "+": "suma", "-": "resta", "*": "multiplicacion", "/": "division", "^": "poder",
        "(": "parentesisA", ")": "parentesisC", " ": "variable"
    },
    "suma": {
        "//": "comentario", "=": "error", ".": "float",

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
        "y": "variable", "z": "variable", "_": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "error", "-": "error", "*": "error", "/": "error", "^": "error",
        "(": "parentesisA", ")": "parentesisC", " ": "suma"
    },

    "poder": {
        "//": "comentario", "=": "error", ".": "float",

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
        "y": "variable", "z": "variable", "_": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "error", "-": "error", "*": "error", "/": "error", "^": "error",
        "(": "parentesisA", ")": "parentesisC", " ": "poder"
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
        "y": "variable", "z": "variable", "_": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "error", "-": "error", "*": "error", "/": "error", "^": "error",
        "(": "parentesisA", ")": "parentesisC", " ": "resta"
    },
    "multiplicacion": {
        "//": "comentario", "=": "error", ".": "float",

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
        "y": "variable", "z": "variable", "_": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "error", "-": "error", "*": "error", "/": "error", "^": "error",
        "(": "parentesisA", ")": "parentesisC", " ": "multiplicacion"
    },
    "division": {
        "//": "comentario", "=": "error", ".": "float",

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
        "y": "variable", "z": "variable", "_": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "error", "-": "error", "*": "error", "/": "comentario", "^": "error",
        "(": "parentesisA", ")": "parentesisC", " ": "division"
    },
    "parentesisA": {
        "//": "comentario", "=": "igualdad", ".": "float",

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
        "y": "variable", "z": "variable", "_": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "suma", "-": "negativo", "*": "multiplicacion", "/": "division", "^": "poder",
        "(": "parentesisA", ")": "parentesisC", " ": "parentesisA"
    },
    "parentesisC": {
        "//": "comentario", "=": "igualdad", ".": "float",

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
        "y": "variable", "z": "variable", "_": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "suma", "-": "resta", "*": "multiplicacion", "/": "division", "^": "poder",
        "(": "parentesisA", ")": "parentesisC", " ": "parentesisC"
    },
    "igualdad": {
        "//": "comentario", "=": "error", ".": "float",

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
        "y": "variable", "z": "variable", "_": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "error", "-": "error", "*": "error", "/": "error", "^": "error",
        "(": "parentesisA", ")": "parentesisC", " ": "igualdad"
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
        "y": "error", "z": "error", "_": "error",

        "0": "float", "1": "float", "2": "float", "3": "float", "4": "float",
        "5": "float", "6": "float", "7": "float", "8": "float", "9": "float",

        "+": "suma", "-": "resta", "*": "multiplicacion", "/": "division", "^": "poder",
        "(": "error", ")": "error", " ": "float"
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
        "y": "comentario", "z": "comentario", "_": "comentario",

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
        "y": "error", "z": "error", "_": "error",

        "0": "error", "1": "error", "2": "error", "3": "error", "4": "error",
        "5": "error", "6": "error", "7": "error", "8": "error", "9": "error",

        "+": "error", "-": "error", "*": "error", "/": "error", "^": "error",
        "(": "error", ")": "error", " ": "error"
    },

    "negativo": {
        "//": "comentario", "=": "error", ".": "float",

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
        "y": "variable", "z": "variable", "_": "variable",

        "0": "numero", "1": "numero", "2": "numero", "3": "numero", "4": "numero",
        "5": "numero", "6": "numero", "7": "numero", "8": "numero", "9": "numero",

        "+": "error", "-": "error", "*": "error", "/": "error", "^": "error",
        "(": "parentesisA", ")": "parentesisC", " ": "negativo"
    },
}


def lexerAritmetico(nombre_archivo):
    # lectura del archivo
    texto = open(nombre_archivo, "r")
    texto = texto.readlines()
    # for loop por cada linea del archivo
    for i in range(0, len(texto)):
        # el estado se reinicia al estado inicial
        estado = "start"
        # se quita el simbolo \n que se agrega al leer el archivo
        texto[i] = texto[i].replace("\n", "")
        # la palabra se reinicia
        palabra = ""
        for j in range(0, len(texto[i])):
            # se saca el elemento con el que se van a hacer las condiciones
            elemento = texto[i][j]
            # se saca el estado con el que se van a hacer las condiciones
            nuevo_estado = transiciones[estado][elemento]

            # si es que el estado es el mismo (o si son estados en los cuales la palabra no se borra (numero a float , division a comentario , float a floatExp , numero a numeroExp , o cualquiera que tenga negativo) ),
            # se le agrega el elemento actual a la palabra y se cambia el estado al estado actual
            if nuevo_estado == estado or (estado == "numero" and nuevo_estado == "float") or (estado == "float" and nuevo_estado == "floatExp") or (estado == "division" and nuevo_estado == "comentario") or (estado == "negativo"):
                palabra += elemento
                estado = nuevo_estado
            else:
                print(palabra, "||", estado)
                estado = nuevo_estado
                palabra = elemento
        print(palabra, "||", estado)


lexerAritmetico("texto.txt")

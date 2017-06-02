import re

def printLinioNumbersRegex():
    output = ""
    for i in range(1,101):
        output += str(i)
        output += " "
    output = linioizationRegex(output)
    return output

def linioizationRegex(numberString):
    #First trying to find every 15 numbers to substitute with the desired string
    numberString = re.sub(r"(\d+) (\d+) (\d+) (\d+) (\d+) (\d+) (\d+) (\d+) (\d+) (\d+) (\d+) (\d+) (\d+) (\d+) (\d+)",
                          r"\1 \2 \3 \4 \5 \6 \7 \8 \9 \10 \11 \12 \13 \14 linianos", numberString)
    #Trying to find every 5 numbers to substitute with the desired string. Should ignore numbers already converted into
    #text
    numberString = re.sub(r"(\d+) (\d+) (\d+) (\d+) (\d+)", r"\1 \2 \3 \4 IT", numberString)
    #Trying to find every 3 numbers (that could either be numbers or already converted multiples of 5).
    numberString = re.sub(r"(\d+|IT) (\d+|IT) (\d+)", r"\1 \2 linio", numberString)
    return numberString

def printLinioNumbers():
    output = ""
    multipleOf3Counter = 3
    multipleOf5Counter = 5
    multipleOf15Counter = 15
    #Simple positional dictionary that helps infer, once it was decided a number must be replaced, what it must be
    #replaced with. The first value corresponds to multiples of 15, the second to multiples of 5 and the third to
    #multiples of 3. They are ordered in descendingly so that if a value is both a mutiple of 15 and a multiple of
    #5 and 3, the replacement string selected corresponds to it being a multiple of 15.
    alternateValues = {2: 'linio',1:'IT', 0 : 'linianos'}
    for i in range(1,101):
        multipleOf3Counter = (multipleOf3Counter - 1) % 3
        multipleOf5Counter = (multipleOf5Counter - 1) % 5
        multipleOf15Counter = (multipleOf15Counter - 1) % 15
        output += linioizationIndividual(i, [multipleOf15Counter,multipleOf5Counter,multipleOf3Counter],alternateValues)
        output += " "
    return output


def linioizationIndividual(n, multipleCountersList,alternateValuesDictionary):
    countersIterator = 0
    for multipleCounter in multipleCountersList:
        #If one of the multiple counters reached zero, it means that the number must be replaced by a value in the
        #alternateValues dictionary. Which one is determined by an iterator.
        if multipleCounter == 0:
            return alternateValuesDictionary[countersIterator]
        countersIterator += 1
    return str(n)

import unittest

class TestLinioizationMethods(unittest.TestCase):

    def testRegexOutput(self):
        self.assertEqual(printLinioNumbersRegex(), '1 2 linio 4 IT linio 7 8 linio IT 11 linio 13 14 linianos 16 17 linio 19 IT linio 22 23 linio IT 26 linio 28 29 linianos 31 32 linio 34 IT linio 37 38 linio IT 41 linio 43 44 linianos 46 47 linio 49 IT linio 52 53 linio IT 56 linio 58 59 linianos 61 62 linio 64 IT linio 67 68 linio IT 71 linio 73 74 linianos 76 77 linio 79 IT linio 82 83 linio IT 86 linio 88 89 linianos 91 92 linio 94 IT linio 97 98 linio IT ')

    def testRegexNoMultiplesOf3(self):
        self.assertFalse(re.search(" 3 ",printLinioNumbersRegex()))
        self.assertFalse(re.search(" 21 ",printLinioNumbersRegex()))
        self.assertFalse(re.search(" 33 ",printLinioNumbersRegex()))
        self.assertFalse(re.search(" 72 ",printLinioNumbersRegex()))
    def testRegexNoMultiplesOf5(self):
        self.assertFalse(re.search(" 5 ",printLinioNumbersRegex()))
        self.assertFalse(re.search(" 25 ",printLinioNumbersRegex()))
        self.assertFalse(re.search(" 50 ",printLinioNumbersRegex()))
        self.assertFalse(re.search(" 75 ",printLinioNumbersRegex()))
    def testRegexNonMultiplesPresent(self):
        self.assertTrue(re.search(" 4 ",printLinioNumbersRegex()))
        self.assertTrue(re.search(" 31 ",printLinioNumbersRegex()))
        self.assertTrue(re.search(" 73 ",printLinioNumbersRegex()))
        self.assertTrue(re.search(" 98 ",printLinioNumbersRegex()))


    def testIndividualOutput(self):
        self.assertEqual(printLinioNumbers(), '1 2 linio 4 IT linio 7 8 linio IT 11 linio 13 14 linianos 16 17 linio 19 IT linio 22 23 linio IT 26 linio 28 29 linianos 31 32 linio 34 IT linio 37 38 linio IT 41 linio 43 44 linianos 46 47 linio 49 IT linio 52 53 linio IT 56 linio 58 59 linianos 61 62 linio 64 IT linio 67 68 linio IT 71 linio 73 74 linianos 76 77 linio 79 IT linio 82 83 linio IT 86 linio 88 89 linianos 91 92 linio 94 IT linio 97 98 linio IT ')

    def testIndividualNoMultiplesOf3(self):
        self.assertFalse(re.search(" 3 ",printLinioNumbers()))
        self.assertFalse(re.search(" 21 ",printLinioNumbers()))
        self.assertFalse(re.search(" 33 ",printLinioNumbers()))
        self.assertFalse(re.search(" 72 ",printLinioNumbers()))
    def testIndividualNoMultiplesOf5(self):
        self.assertFalse(re.search(" 5 ",printLinioNumbers()))
        self.assertFalse(re.search(" 25 ",printLinioNumbers()))
        self.assertFalse(re.search(" 50 ",printLinioNumbers()))
        self.assertFalse(re.search(" 75 ",printLinioNumbers()))
    def testIndividualNonMultiplesPresent(self):
        self.assertTrue(re.search(" 4 ",printLinioNumbers()))
        self.assertTrue(re.search(" 31 ",printLinioNumbers()))
        self.assertTrue(re.search(" 73 ",printLinioNumbers()))
        self.assertTrue(re.search(" 98 ",printLinioNumbers()))


if __name__ == "__main__":
    print(printLinioNumbersRegex())
    print(printLinioNumbers())
    unittest.main()

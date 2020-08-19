import re
import os
import sys
from pathlib import Path

try:
    import pytov.curly_braces as curly_braces
except:
    import curly_braces
import traceback

class Main:
    
    def __init__(self, filePath=False):
        # check if the filePath is on default mode (called by the reference to switch see run), and if not, compile and run.
        if (filePath != False):
            self.filePath = filePath
            self.fileText = open(self.filePath, "r").read() + "\n\n\"\""
            self.strings = []
            self.splitted = []
            self.splitFile()
            self.run()

    def getStrings(self, text):

        # all strings regex: (\"(.|[\r\n][^\"])*?\")|\'(.|[\r\n][^\"])*?\'

        # get all strings positions

        strings = []
        wasQuoteStart = False
        lastQuote = ""
        previusChar = ""
        firstQuote = 0

        for i in range(len(text)):
            
            if (text[i] == "'" and wasQuoteStart and lastQuote == "'") or (text[i] == '"' and wasQuoteStart and lastQuote == '"') and previusChar != "\\":
                strings.append([firstQuote, i])
                wasQuoteStart = False

            elif (text[i] == "'" or text[i] == '"') and not wasQuoteStart:
                lastQuote = text[i]
                wasQuoteStart = True
                firstQuote = i
            
            previusChar = text[i]
        
        return strings
    
    def splitFile(self):
        # split the file to lines, but keep same line if the '\n' is inside string

        self.fileText = curly_braces.hide_curlys(self.fileText)
        self.strings = self.getStrings(self.fileText)
        
        backslashNs = [i for i in range(len(self.fileText)) if self.fileText.startswith("\n", i)] 
        lastAppend = 0
        insideQuotes = True

        for i in range(len(backslashNs)):
            for u in range(len(self.strings)):
                if not (backslashNs[i] > self.strings[u][0] and backslashNs[i] < self.strings[u][1]):
                    insideQuotes = False
                else:
                    insideQuotes = True
                    break
            
            if not insideQuotes:
                self.splitted.append(self.fileText[lastAppend:backslashNs[i]])
                lastAppend = backslashNs[i] + 1
            
            insideQuotes = True
        
    
    def removeLongComments(self, text):
        finds = []

        while True:
            # get all long comments
            finds = []

            matches = re.finditer(r"/\*(.|[\r\n])*?\*/", text)
            for _, match in enumerate(matches, start=1):
                 finds.append([match.start(), match.end()])

            
            # break if nothing found
            if (len(finds) == 0):
                break

            
            text = text[:finds[-1][0]] + "#" + "#".join(list(text[finds[-1][0]:finds[-1][1]])) + text[finds[-1][1]:]



        return text
            


    def addTabs(self):

        pastCurlies = 0
        for i in range(len(self.splitted)):

            
            # remove all identation
            lastSpaceOrTab = -1
            for u in range(len(self.splitted[i])):
                if self.splitted[i][u] != " " and self.splitted[i][u] != "\n":
                    break
                elif self.splitted[i][u] == "\n" or self.splitted[i][u] == " ":
                    lastSpaceOrTab = u

            withoutTabs = self.splitted[i][lastSpaceOrTab+1:]

            # if not withoutTabs.endswith(";") and not withoutTabs.endswith("{") and not withoutTabs.endswith("}") and not withoutTabs == "" and not withoutTabs.endswith("`~`") and not withoutTabs.endswith("~`~") and not withoutTabs.endswith(":") and not withoutTabs.endswith(","):
            #     arrow = " " * len(self.splitted[i]) + "^"
            #     raise SyntaxError(f"excepted ';' at end of line {i + 1}\n{self.splitted[i]}\n{arrow}")

            self.splitted[i] = "".join(["    " for u in range(pastCurlies)]) + withoutTabs
            
            # add new (correct) identation

            matches = re.finditer(r"(\{)(?=(?:[^\"]|\"[^\"]*\")*$)(?=(?:[^\']|\'[^\']*\')*$)", self.splitted[i])
            for _, match in enumerate(matches, start=1):
                pastCurlies += 1

            
            matches = re.finditer(r"(\})(?=(?:[^\"]|\"[^\"]*\")*$)", self.splitted[i])
            for _, match in enumerate(matches, start=1):
                pastCurlies -= 1
            



    def switch(self, var, cases, *args):
        # check if the var has case, if so, run it
        if var in cases:
            cases[var]()
        # if not run default case
        elif len(args) > 0:
            args[0]()



    
    def replaceOutsideString(self, text, rep, rwith, unless=False):
        
        
        finds = []

        while True:
            # get all matches of rep outside double quotes
            finds = []
            matches = re.finditer(r"(" + rep + r")(?=(?:[^\"]|\"[^\"]*\")*$)(?=(?:[^\']|\'[^\']*\')*$)", text)
            for _, match in enumerate(matches, start=1):
                finds.append([match.start(), match.end()])

            
            #break if nothing found
            if (len(finds) == 0):
                break
            
            unlesses = []

            # check if unless is not set, and if so replace with the rwith.
            if (unless == False):
                text = text[:finds[-1][0]] + rwith + text[finds[-1][1]:]
            
            # else if is not surrounded by the unless char, and if so replace it with the rwith.
            else:
                if not (text[finds[-1][1]] == unless or text[finds[-1][0] - 1] == unless):
                    text = text[:finds[-1][0]] + rwith + text[finds[-1][1]:]
                else:
                    #if is surrounded, append to the unlesses
                    unlesses.append(finds[-1])

            # if all finds in unlesses, break the while True, because all the finds left are surrounded.
            if (sum(1 for i in finds if i in unlesses) == len(finds)):
                break


        return text



    def run(self):
        # replace braces and fix identation
        self.addTabs()
        # connect splitted lines and add referance to switch
        self.connected = "import pytov\nswitch = pytov.Main().switch\n" + "\n".join(self.splitted)
        # replace \" and \' with flags
        self.connected = self.connected.replace("\\\"", "~^$backslash$-$double$-$quote$-$flag$^~")
        self.connected = self.connected.replace("\\\'", "~^$backslash$-$single$-$quote$-$flag$^~")
        # remove long comments
        self.connected = self.removeLongComments(self.connected)
        self.connected = self.replaceOutsideString(self.connected, "\/\*\*\/", "")
        # replace keywords
        self.connected = self.replaceOutsideString(self.connected, "\{", ":")
        self.connected = self.replaceOutsideString(self.connected, "\}", "")
        self.connected = self.connected.replace("~^$curly$-$braces$-$end$-$flag$^~", "}")
        self.connected = self.connected.replace("~^$curly$-$braces$-$start$-$flag$^~", "{")
        self.connected = self.replaceOutsideString(self.connected, "\|\|", " or ")
        self.connected = self.replaceOutsideString(self.connected, "&&", " and ")
        self.connected = self.replaceOutsideString(self.connected, "!", " not ", "=")
        self.connected = self.replaceOutsideString(self.connected, "//", "#")
        self.connected = self.replaceOutsideString(self.connected, "/_", "//")
        self.connected = self.replaceOutsideString(self.connected, "catch", "except")
        self.connected = self.replaceOutsideString(self.connected, ";", "")
        self.connected = self.replaceOutsideString(self.connected, "true", "True")
        self.connected = self.replaceOutsideString(self.connected, "false", "False")
        self.connected = self.replaceOutsideString(self.connected, "func", "def")
        self.connected = self.replaceOutsideString(self.connected, "function", "def")

        # replace flags back
        self.connected = self.connected.replace("~^$backslash$-$double$-$quote$-$flag$^~", "\\\"")
        self.connected = self.connected.replace("~^$backslash$-$single$-$quote$-$flag$^~", "\\\'")


        # execute final code
        try:
            exec(self.connected)
        except:
            #print(e)
            excep = traceback.format_exc()
            excepLine = excep.split("\n")[3][excep.split("\n")[3].find("line") + 5:]
            for i in range(len(excepLine)):
                try:
                    int(excepLine[i])
                except:
                    excepLine = excepLine[:i]
            lineNum = int(excepLine) - 2
            withoutThisFile = excep.split("\n")[0] + "\n" + "\n" + excep.split("\n")[3][:excep.split("\n")[3].find("line") + 5] + str(lineNum) + "\n" + "\n".join(excep.split("\n")[4:])
            print("\n" + withoutThisFile.replace('"<string>"', str(self.filePath)))
        

def run():
    if len(sys.argv) > 1 and sys.argv[1] != "-py":
        runnedfile = Path(sys.argv[1])
        pythoncompiled = runnedfile.parents[0] / "python-compiled"
        main = Main(runnedfile)

        if "-py" in sys.argv:
            if not os.path.isdir(pythoncompiled): # '\\'.join(sys.argv[1].split("\\")[:-1]) + '\\python-compiled'
                os.mkdir(pythoncompiled)
            o = open(pythoncompiled / (runnedfile.name + ".py"), "w")
            o.write(main.connected)
            o.close()
    else:
        print("======================= no file entered, running example =======================\n")
        dirname = Path(os.path.dirname(os.path.abspath(__file__))) / "examples"
        main = Main(dirname / "curly.py") # f"{dirname}\\curly.py"
        if "-py" in sys.argv:
            if not os.path.isdir(dirname / "python-compiled"): # dirname + '\\python-compiled'
                os.mkdir(dirname / "python-compiled") # dirname + '\\python-compiled'
            o = open(dirname / "python-compiled" / "curly.py", "w") # dirname + "\\python-compiled\\curly.py", "w"
            o.write(main.connected)
            o.close()

if __name__ == "__main__":
    run()
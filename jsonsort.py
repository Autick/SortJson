# coding:utf-8
import sys, json, os, tkinter, tkinter.filedialog, tkinter.messagebox


class CsSortJson:

    def __init__(self):
        self.jsonData = {}
        self.newFile = ""

    def __GetFirstName(self, myDict):
        return list(myDict)[0]

    def __DoList(self, myList):
        retList = []
        for item in sorted(myList, key=self.__GetFirstName):
            if isinstance(item, list):
                ret = self.__DoList(item)
            elif isinstance(item, dict):
                ret = self.__DoDict(item)
            else:
                ret = item
            retList.append(ret)
        return retList

    def __DoDict(self, mydict):
        retDict={}

        for k, v in mydict.items():
            if isinstance(v, list):
                retv = self.__DoList(v)
                retk = k
            elif isinstance(v, dict):
                retv = self.__DoDict(v)
                retk = k
            else:
                retv = v
                retk = k
            retDict[retk] = retv

        return retDict

    def __GetJsonData(self, fileName = ""):

        if fileName !="":
            file = fileName
        else:
            root = tkinter.Tk()
            root.withdraw()
            fType = [("json file", "*.json")]
            iDir = os.path.abspath(os.path.dirname(__file__))
            title = "Please select Json file."
            file = tkinter.filedialog.askopenfilename(filetypes=fType, initialdir=iDir,
                                                      title=title)

        self.newFile = file.replace("json", "txt")

        f1 = open(file, "r")
        self.jsonData = json.load(f1)
        f1.close()

    def MakeSortedJsonData(self, fileName = ""):
        self.__GetJsonData(fileName)

        if isinstance(self.jsonData, list):
            for i in range(len(self.jsonData)):
                if isinstance(self.jsonData[i], list):
                    self.jsonData[i] = self.__DoList(self.jsonData[i])
                elif isinstance(self.jsonData[i], dict):
                    self.jsonData[i] = self.__DoDict(self.jsonData[i])
                else:
                    self.jsonData[i] = self.jsonData[i]
        else:
            for k, v in self.jsonData.items():
                if isinstance(self.jsonData[k], list):
                    self.jsonData[k] = self.__DoList(self.jsonData[k])
                elif isinstance(self.jsonData[k], dict):
                    self.jsonData[k] = self.__DoDict(self.jsonData[k])
                else:
                    self.jsonData[k] = self.jsonData[k]

        with open(self.newFile, "w") as f2:
            f2.write(json.dumps(self.jsonData, indent=2))


if __name__ == '__main__':
    args = sys.argv

    insReadJson = CsSortJson()
    if len(args) > 1:
        for i in range(1, len(args)):
            insReadJson.MakeSortedJsonData(args[i])

    else:
        insReadJson.MakeSortedJsonData()



from Node import Node
from CharGroup import CharGroup
from random import *
import copy

import histogramtest
import trainingdata


from tkinter import *
import tkinter.messagebox as tkmsgbox


class Chrome:
    list = []
    fitness = 0

    def __init__(self,list):
        self.list = list

    def mutate(self):
        for item in self.list:
            if item not in all_nodes_pattern:
                self.list[self.list.index(item)] = mutate(item)

    # def __copy__(self):
    #     list = []
    #     list.appendall()
    #     return Chrome(self.list)


    ## assumed that lasttline added as the last item of the arrayy
    def calculatefit(self):
        fit = 0
        if( len(self.list) == 0 ):
            return 0
        if( len(self.list) == 1 ):
            return self.calculate_fit_node(self.list[0], all_nodes_pattern)
        if( len(self.list) == 2 ):
            fit = 0
            if( self.calculate_fit_node(self.list[1], all_nodes_pattern) ==100): #can be updated to return most fitting matching node and check
                fit = 100
                fit +=self.calculate_fit_node(self.list[0],all_nodes[self.list[1]].children)
            fit = fit /2
            return fit
        if( len(self.list) == 3):
            fit = 0
            if( self.calculate_fit_node(self.list[2],all_nodes_pattern) == 100):
                fit = 100
                fit += self.calculate_fit_node(self.list[1],all_nodes[self.list[2]].children)
                if(fit==200):
                    fit+= self.calculate_fit_node(self.list[0],all_nodes[self.list[1]].children)
            fit = fit/3
            return fit


    def calculate_fit_node(self,node,nodeslist):
        if node in nodeslist:
            return 100
        else:
            maxfit = -1;
            for matchingnode in nodeslist:
                tempfit = self.match_pattern(node,matchingnode)
                if(tempfit>maxfit) : maxfit = tempfit

            return maxfit


    def match_pattern(self,node,matchingnode):
        fit = 0
        count = 0
        if len(node)<len(matchingnode) :
            for i in range(0,len(node)):
                if node[i] == matchingnode[i] :
                    fit+=1
            fit = (fit/len(matchingnode)) * 100
        else:
            for i in range(0,len(matchingnode)):
                if matchingnode[i] == node[i] :
                    fit+=1
            fit = (fit/len(node))*100

        return fit

class Generation:
    chromosomes = []
    generation_size = 0

    def __init__(self,chromosome,generation_size):
        self.chromosomes.append(chromosome)
        self.generation_size = generation_size
        for i in range(1,generation_size):
            tempchrom = copy.deepcopy(chromosome)
            tempchrom.mutate()
            self.chromosomes.append(tempchrom)

    def evolve(self):
        done = False
        selectedChromosome = ""
        generation =0
        currentgeneration = copy.deepcopy(self.chromosomes)
        offspring = []
        while not done:
            print("gneration "+generation.__str__())



            tempchr=""
            for o in range(0,self.generation_size):
                chr1 = currentgeneration[randint(0,len(currentgeneration)-1)]
                chr2 = currentgeneration[randint(0,len(currentgeneration)-1)]
                if( len(chr1.list) != len(chr2.list)):
                    print("D - ","here 2")
                tmpChr = Chrome(crossover(chr1,chr2))
                if len(tmpChr.list)==0:
                    print("D - ","here 3")
                currentgeneration.append(tmpChr)




            offspring = []
            maxofgen = 0
            maxindexofgen=-1
            for j in range(0,self.generation_size):
                maxfit=0
                maxfitindex=-1
                for i in range(0,len(currentgeneration)):
                    fit = currentgeneration[i].calculatefit()
                    if(fit>maxfit):
                        maxfit = fit
                        maxfitindex = i
                        if(maxofgen< maxfit):
                            maxofgen = maxfit
                            maxindexofgen = maxfitindex

                offspring.append(currentgeneration.pop(maxfitindex))

            tempchr = [];
            for i in range(0,len(offspring[0].list)):
                node = offspring[len(offspring)-1].list[i]
                nodemaxfit = 0
                nodemaxfitindex = -1
                for j in range(0,len(all_nodes_pattern)):
                    pattern = all_nodes_pattern[j]

                    fit = offspring[0].match_pattern(node,pattern)
                    if(fit>nodemaxfit):
                        nodemaxfit = fit
                        nodemaxfitindex = j

                tempchr.append(all_nodes_pattern[nodemaxfitindex])
            offspring.append(Chrome(tempchr))

            currentgeneration = offspring

            if(maxfit == 100) :
                done = True
                selectedChromosome = currentgeneration[maxindexofgen]
            else:

                for chrindex in range(0,len(currentgeneration)):
                    if chrindex != maxindexofgen : currentgeneration[chrindex].mutate()
            generation+=1
            print("max fit ",maxfit.__str__())
        # print(selectedChromosome)
        for line in selectedChromosome.list:
            print(line)

top = Tk()
E1 = {}
E2 = {}
E3 = {}
categories = {}
letters = {}
patternletters = []

all_nodes_pattern = ()
all_nodes = {}

def prepare_nodes():
    print("preparing nodes")
    global all_nodes_pattern
    matale = Node("මාතලේ", patternforstring("මාතලේ"))

    #childs of matale
    ukuwela = Node("උකුවෙල", patternforstring("උකුවෙල"))
    haththota_amuna = Node("හත්තොට අමුණ", patternforstring("හත්තොට අමුණ"))
    udasgiriya = Node("උඩස්ගිරිය", patternforstring("උඩස්ගිරිය"))
    kaikawala = Node("කයිකාවෙල", patternforstring("කයිකාවෙල"))
    naula = Node("නාඋල", patternforstring("නාඋල"))
    nalanda = Node("නාලන්ද", patternforstring("නාලන්ද"))
    yatawaththa = Node("යටවත්ත", patternforstring("යටවත්ත"))
    mahawela = Node("මහවෙල", patternforstring("මහවෙල"))
    millawana = Node("මිල්ලවාන", patternforstring("මිල්ලවාන"))
    waalawala = Node("වාලවෙල", patternforstring("වාලවෙල"))
    muwandeniya = Node("මුවන්දෙණිය", patternforstring("මුවන්දෙණිය"))
    alwaththa = Node("අල්වත්ත", patternforstring("අල්වත්ත"))
    galewala = Node("ගලේවල", patternforstring("ගලේවල"))
    madipola = Node("මාදිපොල", patternforstring("මාදිපොල"))
    lenadora = Node("ලේනදොර", patternforstring("ලේනදොර"))
    dambulla = Node("දඹුල්ල", patternforstring("දඹුල්ල"))
    pallepola = Node("පල්ලේපොල", patternforstring("පල්ලේපොල"))
    palapathwala = Node("පලාපත්වල", patternforstring("පලාපත්වල"))
    gammaduwa = Node("ගම්මඩූව", patternforstring("ගම්මඩූව"))
    raththota = Node("රත්තොට", patternforstring("රත්තොට"))
    vilgamuwa = Node("විල්ගමුව", patternforstring("විල්ගමුව"))
    ovilkanda = Node("ඕවිල්කන්ද", patternforstring("ඕවිල්කන්ද"))
    dumkolawaththa = Node("දුම්කොළවත්ත", patternforstring("දුම්කොළවත්ත"))
    nugagolla = Node("නුගගොල්ල", patternforstring("නුගගොල්ල"))
    maaraka = Node("මාරක", patternforstring("මාරක"))
    dankanda = Node("දන්කන්ද", patternforstring("දන්කන්ද"))
    mananwaththa = Node("මනන්වත්ත", patternforstring("මනන්වත්ත"))
    kiwula = Node("කිවුල", patternforstring("කිවුල"))

    # all_nodes[matale.pattern] = matale
    allnodeprep(matale)

    matale.addChild(ukuwela)
    allnodeprep(ukuwela)

    matale.addChild(haththota_amuna)
    allnodeprep(haththota_amuna)

    matale.addChild(udasgiriya)
    allnodeprep(udasgiriya)

    matale.addChild(kaikawala)
    allnodeprep(kaikawala)

    matale.addChild(naula)
    allnodeprep(naula)

    matale.addChild(nalanda)
    allnodeprep(nalanda)

    matale.addChild(yatawaththa)
    allnodeprep(yatawaththa)

    matale.addChild(mahawela)
    allnodeprep(mahawela)

    matale.addChild(millawana)
    allnodeprep(millawana)

    matale.addChild(waalawala)
    allnodeprep(waalawala)

    matale.addChild(muwandeniya)
    allnodeprep(muwandeniya)

    matale.addChild(alwaththa)
    allnodeprep(alwaththa)

    matale.addChild(galewala)
    allnodeprep(galewala)

    matale.addChild(madipola)
    allnodeprep(madipola)

    matale.addChild(lenadora)
    allnodeprep(lenadora)

    matale.addChild(dambulla)
    allnodeprep(dambulla)

    matale.addChild(pallepola)
    allnodeprep(pallepola)

    matale.addChild(gammaduwa)
    allnodeprep(gammaduwa)

    matale.addChild(palapathwala)
    allnodeprep(palapathwala)

    matale.addChild(raththota)
    allnodeprep(raththota)

    matale.addChild(vilgamuwa)
    allnodeprep(vilgamuwa)

    matale.addChild(ovilkanda)
    allnodeprep(ovilkanda)

    matale.addChild(dumkolawaththa)
    allnodeprep(dumkolawaththa)

    matale.addChild(nugagolla)
    allnodeprep(nugagolla)

    matale.addChild(maaraka)
    allnodeprep(maaraka)

    matale.addChild(dankanda)
    allnodeprep(dankanda)

    matale.addChild(mananwaththa)
    allnodeprep(mananwaththa)

    matale.addChild(kiwula)
    allnodeprep(kiwula)



def allnodeprep(node):
    all_nodes[node.pattern] = node
    all_nodes_pattern.append(node.pattern)

def prepare_categories():
    # print(u"\u0D85")
    global categories
    global patternletters
    categories = [
        CharGroup("A", [u'\u0D85']),
        CharGroup("B", [u"\u0D89"]),
        CharGroup("C", [u"\u0D8A"]),
        CharGroup("D", [u"\u0D8B"]),
        CharGroup("E", [u"\u0D91"]),
        CharGroup("f", [u"\u0D95"]),  # #category f should be integrated in to this
        CharGroup("F", [u"\u0D94", u"\u0DB9"]),  # #category f should be integrated in to this

        CharGroup("G", [u"\u0D9A"]),
        CharGroup("H", [u"\u0D9C", u"\u0DC1"]),
        CharGroup("i", [u"\u0DA0\u0DD2"]),  # #category i should be integrated in to this
        CharGroup("I", [u"\u0DA0"]),  # #category i should be integrated in to this

        CharGroup("J", [u"\u0DA1"]),
        CharGroup("K", [u"\u0DA5"]),
        CharGroup("l", [u"\u0DA7\u0DD2"]),  # # category l should be integrated in to this
        CharGroup("L", [u"\u0DA7"]),  # # category l should be integrated in to this
        CharGroup("m", [u"\u0DA9\u0DD2"]),  # # category m should be integrated in to this
        CharGroup("M", [u"\u0DA9"]),  # # category m should be integrated in to this
        CharGroup("N", [u"\u0DAD"]),
        CharGroup("O", [u"\u0DAF"]),
        CharGroup("P", [u'\u0DAF\u0DD4']),
        CharGroup("Q", [u"\u0DB1"]),
        CharGroup("R", [u"\u0DB4"]),
        CharGroup("s", [u"\u0DB6\u0DD2"]),  # # category s should be integrated in to this
        CharGroup("S", [u"\u0DB6"]),  # # category s should be integrated in to this
        CharGroup("t", [u"\u0DB8\u0DD2"]),  # # category t should be integrated in to this
        CharGroup("T", [u"\u0DB8"]),  # # category t should be integrated in to this
        CharGroup("U", [u"\u0DBA"]),
        CharGroup("V", [u"\u0dBB"]),
        CharGroup("w", [u"\u0DBD\u0DD2"]),  # # category w should be integrated in to this
        CharGroup("W", [u"\u0DBD"]),  # # category w should be integrated in to this
        CharGroup("x", [u"\u0DC0\u0DD2"]),  # # category x should be integrated in to this
        CharGroup("X", [u"\u0DC0"]),  # # category x should be integrated in to this
        CharGroup("Y", [u"\u0DC3"]),
        CharGroup("Z", [u"\u0DC4"]),
        CharGroup("1", [u"\u0DAB"]),
        CharGroup("2", [u"\u0DC5"]),
        CharGroup("3", [u"\u0DB0"]),
        CharGroup("4", [u"\u0DA4"]),
        # #CharGroup("5", ["\u0DC4"]),
        CharGroup("9", [u"\u0DD9", u"\u0DCA",u"\u0DCF",u"\u0DD4",u"\u0DD6",u"\u0DD2",u"\u0DDA",u"\u0DDC"])
    ]
    for chargroups in categories:
        for v in chargroups.characters:
            letters.__setitem__(v,chargroups.patternchar)
        patternletters.append(chargroups.patternchar)


def dataCollection():

    global E1
    global E2
    global E3
    global categories
    frame1 = Frame(top)
    frame1.pack(fill=X)

    L1 = Label(frame1,text="Line one")
    L1.pack(side=LEFT)
    E1 = Entry(frame1,bd=5)
    E1.pack(side=RIGHT)

    frame2 = Frame(top)
    frame2.pack(fill=X)

    L2 = Label(frame2,text="line two")
    L2.pack(side=LEFT)
    E2 = Entry(frame2,bd=5)
    E2.pack(side=RIGHT)

    frame3 = Frame(top)
    frame3.pack(fill=X)

    L3 = Label(frame3,text="Line three")
    L3.pack(side=LEFT)
    E3 = Entry(frame3,bd=5)
    E3.pack(side=RIGHT)

    okbtn = Button(top,text="OK",command=printText)

    btnA = Button(top,text='Cancel',command=printText)

    frmBtns = Frame(top)
    frmBtns.pack(fill=Y)
    i = 0
    framebttemp = Frame(frmBtns)
    framebttemp.pack(fill=Y)
    for chargroups in categories:
        for v in chargroups.characters:
            i+=1
            if i==10 :
                i=0
                framebttemp = Frame(frmBtns)
                framebttemp.pack(fill=Y)
            # print(v)
            btn = Button(framebttemp,text=v,command= lambda v=v:update_text(v))
            btn.pack(side=LEFT)
        #     letters.__setitem__(v,chargroups.patternchar)
        # patternletters.append(chargroups.patternchar)

    btnA.pack(side=RIGHT)
    okbtn.pack(side=RIGHT)
    top.mainloop()

def update_text(text):
    global E3
    v = top.focus_get()
    if("frame3" in v.__str__()):
        val = text
        # print (val.encode(encoding='utf-8',errors='ignore'))
        E3.insert(len(E3.get()),val)
    else:
        if ("frame2" in v.__str__()):
            E2.insert(len(E2.get()), text)
        else:
            E1.insert(len(E1.get()), text)
    # print("focus : ",top.focus_get())


def printText():
    address = []
    tkmsgbox.showinfo("Hi","Line 1 : "+patternforstring(E1.get())+"\nLine 2 : "+E2.get()+"\nLine 3"+E3.get())
    if(len(E1.get())>0 ): address.append(patternforstring(E1.get()))
    if(len(E2.get())>0 ): address.append(patternforstring(E2.get()))
    if(len(E3.get())>0 ): address.append(patternforstring(E3.get()))
    chromosome = Chrome(address)
    generation = Generation(chromosome,10)
    generation.evolve()
    top.quit()



def patternforstring(string): # implement one more
    global letters
    for letter in letters:
        if letter == u"\u0DD4":
            string = string.replace(u"\u0DD4","")
        if(letter== u"\u0DDA"):
            while( string.find(u"\u0DDA") !=-1):
                index = string.find(u"\u0DDA")
                string = string[:index-1]+"9"+string[index-1:]
                string = string.replace(letter,letters[letter],1)
        if( letter == u"\u0DDC"):
            while(string.find(u"\u0DDC") !=-1):
                index = string.find(u"\u0DDA")
                string = string[:index-1]+"9"+string[index-1:index]+"9"+string[index+1:]

        string = string.replace(letter,letters[letter])


    return string



def main():
    prepare_categories()

    prepare_nodes()

    dataCollection()

    # prepare_nodes()
    # trainingdata.trainandtest()
    # histogramtest.run()
    #prepareNodes()
    # prepare_categories()

def crossover(chr1,chr2):
    global all_nodes_pattern
    crossed = []
    if(len(chr1.list) != len(chr2.list)):
        print (chr1.list)
        print(chr2.list)

    for i in range(0,len(chr1.list)):
        if chr1.list[i] in all_nodes_pattern :
            crossed.append(chr1.list[i])
            continue
        if chr2.list[i] in all_nodes_pattern :
            crossed.append(chr2.list[i])
            continue



        if len(chr1.list[i]) < len(chr2.list[i]):
            index = randint(0,len(chr1.list[i]))
            strtemp = chr1.list[i][:index] + chr2.list[i][index:]
        else:
            index = randint(0,len(chr2.list[i]))
            strtemp = chr2.list[i][:index] + chr1.list[i][index:]
        crossed.append(strtemp)
        if(len(crossed)==0):
            print("D - ","here 1")
    return crossed




def mutate(node):
    for l in node:
        if randint(1,100) > 80 :
            node = node[:node.find(l)] + patternletters[randint(0,len(patternletters)-1)] + node[node.find(l)+1:]
    if randint(1,1000) > 990:
        node+= patternletters[randint(0,len(patternletters)-1)]
    return node


if __name__ == "__main__":
    main()










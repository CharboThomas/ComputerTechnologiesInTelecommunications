import subprocess
import os
import json


class PING:

    def __init__(self,cmd,param,target):

        #########################
        # Variables
        #########################
        self.param = param
        self.jsonData = {}### i creat my "json structure"


        #########################
        # step 1 : take Data
        #########################

        pingCmd = subprocess.Popen([cmd,"-c "+str(param),target], shell=False,stdout = subprocess.PIPE,stderr = subprocess.PIPE)
        ### with this first command, i will ask to python to execute the command ping on my linux terminal
        pingCmd.wait()
        ### i use the option wait in order to block my python code
    
        out,err = pingCmd.communicate() ### i take the data return by the Ping command (or the error instruction)
        ### before the next command, my data is a binary element
        out = out.decode()### my data become a string element
        self.data = str(out).split("\n") ### i split my data in order to separe every line of the data generate by the ping command
        
        if pingCmd.returncode  == 0: ### if my code doesn't meet any problems, it will print the data generate by the ping command
            print(" mission success: ")
            for i in range(0,len(self.data)-1,1):
                print(self.data[i])### i print every line of the data generate by the ping command

        else:
            print(" mission fail: ")
            print("err: {0}".format(err))


        #########################
        # step 2 : create json structure
        #########################

        self.traitement()### with this method, i will "clear" my data

        #########################
        # step 3 : save Data
        #########################

        self.ecriture()### with this method, i will write my data on a Json file



    def traitement(self):

        self.position = 0

        self.traitementModeleA(self.data[self.position])

        for i in range(0,self.param,1):
            self.traitementModeleB(self.data[self.position])

        self.position = self.position + 2

        self.traitementModeleC(self.data[self.position])
        self.traitementModeleD(self.data[self.position])

        

    def traitementModeleA(self,listeData):
        
            ### in this method, I clear one part of the data generate by the linux command
        
            listeData = listeData.split(" ")### i split the first line generate by the ping command

            self.jsonData["ligne_0"] = []
            self.jsonData["ligne_0"].append({
                    'cmd':listeData[0],'cible':listeData[1],'ip':listeData[2],
                    })### i take the name of the command, the target of the request, and an IP adress

            self.position = self.position + 1
            
            
            
    def traitementModeleB(self,listeData):
        
            ### in this method, I clear one part of the data generate by the linux command
        
            listeData = listeData.split(" ")

            icmp_seq_value = (listeData[5].split("="))[1]
            ttl_value = (listeData[6].split("="))[1]
            temps_value = (listeData[7].split("="))[1]
            

            self.jsonData["ligne_"+str(self.position)] = []
            self.jsonData["ligne_"+str(self.position)].append({
                    'size':listeData[0],'serveur':listeData[3],'ip':listeData[4],
                    'icmp_seq':icmp_seq_value,'ttl':ttl_value,'temps':temps_value
                    })

            self.position = self.position + 1



    def traitementModeleC(self,listeData):
        
            ### in this method, I clear one part of the data generate by the linux command
        
            listeData = listeData.split(" ")### i split the (last -1) line generate by the ping command

            self.jsonData["ligne_"+str(self.position)] = []
            self.jsonData["ligne_"+str(self.position)].append({
                    'transmis':listeData[0],'recus':listeData[3],
                    'perdu':listeData[5],'temps':listeData[9]
                    })### i write some data of this line on my "json structure"

            self.position = self.position + 1



    def traitementModeleD(self,listeData):
        
            ### in this method, I clear one part of the data generate by the linux command
        
            listeData = listeData.split(" ")### i split the last line generate by the ping command
            listeData = listeData[3].split("/")

            self.jsonData["ligne_"+str(self.position)] = []
            self.jsonData["ligne_"+str(self.position)].append({
                    'min':listeData[0],'avg':listeData[1],
                    'max':listeData[2],'mdev':listeData[3]
                    })### i write some data of this line on my "json structure"


    def ecriture(self):
        
        ### in this method, I open my json file and i write my data on this file
        
        with open('test.json','w') as jsonFile:
            json.dump(self.jsonData,jsonFile)

    def __del__(self): 
        print("Bonjour, c'est le destructeur. :p ")

        
### i creat the parameter of my ping request    
cmd,param,target = "ping",4,"www.google.com"


### i creat the python object. This object will generate and execute a linux command on my terminal.
### It will also catch and write the data generates by the linux command
pingData = PING(cmd,param,target)


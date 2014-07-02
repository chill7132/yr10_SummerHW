#Exam Questions <img src="../../Resources/exam.png" width=50px alt="Tick Sheet">

##Instructions
Edit this document and answer the questions in the sections surrounded by ```.

There are 30 marks available and are awarded grades as follows:

|Score|Grade|
|-----|-----|
|<6|U|
|6+|G|
|9+|F|
|12+|E|
|15+|D|
|18+|C|
|21+|B|
|24+|A|
|27+|A*|


##Data Representation

###1 - Why do we represent data using binary when using computers *(1 mark)*

```
Because the computers reads it as off and ons/0s and 1s
```
###2 - How would we represent the number 147 in binary? *(1 mark)*
```
10010011
```
###3 - Can you convert the hexadecimal number **b5** to denary, there is a mark for you working. *(2 marks)*
```
181
```
###4 - Here is a function written is **pseudocode**.
```
FUNCTION validUser (users , user)
    FOR x <-1 to LEN(users)
        IF users[x] = user
			RETURN True
		ENDIF
	ENDFOR
	RETURN False
ENDFUNCTION
```

(a) What type of data is **users**? **(1 mark)**
```
integer 
```

(b) What type of data is returned by this function? **(1 mark)**
```
integer
```

##Errors
###6 - This program is supposed to find the mean of a list of numbers and print it out for the user:
```
line1:		tot <- 0
line2:		nums <- [1,6,4,2,5,3]
line3:		FOR x <- to LEN(nums)
line4:			tot <- nums[x]
line5:		ENDFOR
line6:		mean <- tot
line7:		OUTPT mean
```

(a) On which line is there a **syntax** error? **(1 mark)**
```
The syntax error is this bit of code is on line 7
```

(b) What is meant by a **syntax** error? **(1 mark)**
```
An error which may involve the miss typing of a variable or function which then the computer will not recognise
```

(c) Identify a logical error in the program and suggest how this might be fixed. **(2 marks)**
```

```

(d) Describe and give an example of the 3rd kind of programming error. **(2 marks)**
```
A runtime error, this is an error which occurs at a certain point in the code which stops the program from running any further 
```

##Algortithms
###7 - Write an **algorithm** that if given a list of numbers could find the largest. Try to use [pseudocode](http://filestore2.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF).
```
answer here
```

##Networking
###8 - Research the following methods (*topologies*) for connecting devices to a network. In each case give a description and at least 1 advantage and 1 disadvantage.

**Bus Topology (6 marks)**
```
Describe:A bus topology is a type of network setup where each computer and network device is connected to a single cable

Advantages:
1)  It is easy to set-up and extend bus network.
2)  Cable length required for this topology is the least compared to other networks.
3)  Bus topology costs very less.

Disadvantages:
1)  There is a limit on central cable length and number of nodes that can be connected.
2)  Dependency on central cable in this topology has its disadvantages.If the main cable (i.e. bus ) encounters   some problem, whole network breaks down. 
3)  It is not suitable for networks with heavy traffic. 



Keep Reading : http://www.ianswer4u.com/2011/05/bus-topology-advantages-and.html#ixzz36KA17ZiX 
Under Creative Commons License: Attribution Non-Commercial Share Alike 
Follow us: ianswer4u on Facebook
```

**Ring Topology (6 marks)**
```
Describe:A local-area network (LAN) whose topology is a ring. That is, all of the nodes are connected in a closed loop.

Advantages:
1)   There is no need for network server to control the connectivity between workstations.
2)   Additional components do not affect the performance of network.
3)   Each computer has equal access to resources.

Disadvantages:
1)Each packet of data must pass through all the computers between source and destination. This makes it slower than Star topology.
2)   If one workstation or port goes down, the entire network gets affected.
3)   Network is highly dependent on the wire which connects different components. 


**Star Topology (6 marks)**
```
Describe:Alternatively referred to as a star network, a star topology is one of the most common network setups where each of the devices and computers on a network connect to a central hub.

Advantages:
1)Easy to connect new nodes or devices. In star topology new nodes can be added easily without affecting rest of the network.
2)Failure of one node or link doesn’t affect the rest of network
3)As compared to Bus topology it gives far much better performance
Disadvantages:
1)  Too much dependency on central device has its own drawbacks. If it fails whole network goes down.
2)  The use of hub, a router or a switch as central device increases the overall cost of the network.
3)   Performance and as well number of nodes which can be added in such topology is depended on capacity of central device.



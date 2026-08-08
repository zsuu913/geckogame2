#gecko adventures VOLUME TWO ELECTRIC BOOGALOO

import random
print("Gecko adventures!")
print("...")
print("-the extended edition-")

#predefine dictionaries of sights, food and predators


sights = {
	"a leaf" : {
		"label" : "a green leaf!",
		"count" : 0,
		"confidence" : 0
	},
	"a warm rock" : {
		"label" : "a perfect basking spot...",
		"count" : 0,
		"confidence" : 2
	},
	"some mud" : {
		"label" : "some mud... so slippery!",
		"count" : 0,
		"confidence" : -1
	},
	"a pinecone" : {
		"label" : "Mathematical perfection. Or, a pinecone.",
		"count" : 0,
		"confidence" : 0
	},
	"a twig" : {
		"label" : "The crunchiest twig!",
		"count" : 0,
		"confidence" : 0
	},
	"some grass" : {
		"label" : "Tall blades of grass...",
		"count" : 0,
		"confidence" : 0
	},
	"a fern" : {
		"label" : "fresssshhhh",
		"count" : 0,
		"confidence" : 1
	},
	"a flower" : {
		"label" : "It's pretty! but inedible :(",
		"count" : 0,
		"confidence" : 0
	},
	"some tree bark" : {
		"label" : "O_O", #IDK MAN
		"count" : 0,
		"confidence" : 0
	},
	"some moss" : {
		"label" : "lush!",
		"count" : 0,
		"confidence" : 0
	},
	"a fluffy flower" : { #dandelion fluff adds confidence
		"label" : "fluffy... ah-CHOO!",
		"count" : 0,
		"confidence" : 2
	},
	"a rock" : { 
		"label" : "Not as warm as I'd like.",
		"count" : 0,
		"confidence" : 1
	},
	"a spiderweb" : {
		"label" : "a sticky situation!",
		"count" : 0
	},
	"a puddle" : {
		"label" : "SPLOSHY",
		"count" : 0
	},
	"a butterfly" : {
		"label" : "it flew away!",
		"count" : 0
	#},
	#"SAMPLE" : {
		#"label" : "EMPTY",
		#"count" : 0
	}
}

#here come the predators

predators = {
	"a snake" : {
		"label" : "a vicious viper!",
		"count" : 0
	},
	"a wildcat" : {
		"label" : "oh no no no no",
		"count" : 0
	}, 
	"a hawk" : {
		"label" : "HAWK IMMINENT!",
		"count" : 0
	}, 
	"an owl" : {
		"label" : "WHO let this happen?",
		"count" : 0
	},
	"a tarantula" : {
		"label" : "Where did you come from?!",
		"count" : 0
	#},
	#"SAMPLE" : {
		#"label" : "EMPTY",
		#"count" : 0
	}
}

# and the INSECTS! FOOD TIME!

insects = {
	"a grasshopper" : {
		"label" : "Great!",
		"energy" : 0
		#"chance" : 0
	},
	"a cricket" : {
		"label" : "I never liked violins",
		"energy" : 0
		#"chance" : 0
	}, 
	"a mosquito" : {
		"label" : "No more bloodsucking!",
		"energy" : 0
		#"chance" : 0.2
	}, 
	"a fly" : {
		"label" : "...",
		"energy" : 0,
		#"chance" : 0.3
    },
	"a dragonfly": {
        "label": "too fast!",
        "energy": 2,
        #"chance": 0.04
    },
	"a worm" : {
		"label" : "Wiggly!",
		"energy" : 0
		#"chance" : 0
	#},
	#"SAMPLE" : {
		#"label" : "EMPTY",
		#"energy" : 0
		#"chance" : 0
	}
}

seen = set()	
#seen_list = []	
#confidence = 1 #if it gets to 0, the animal becomes inactive
hungry = True
safe = True
active = True #maybe give the gecko an energy meter that can be replenished by insects

while hungry and safe and active:
	if random.random() < 0.05 : 
		spot = random.choice(list(insects.keys()))
		print(f"Gecko checks: {spot}")
		print(insects[spot]["label"])
		print("Cronch!")
		hungry = False
	else:
		spot = random.choice(list(sights.keys()))
			#if spot = "another gecko"
		print(f"Gecko sees: {spot}")
		if sights[spot]["count"] > 0 :
			print("I've been here before!")
		print(sights[spot]["label"]) #this should let the gecko comment on stuff
		sights[spot]["count"] += 1
		seen.add(spot)
		#seen_list.append(spot)

#10% chance for a predator being there

	if spot != "a rock" and hungry and random.random() < 0.10 :
		predator = random.choice(list(predators.keys()))
		print(f"{predator.capitalize()} approaches!")
		print(predators[predator]["label"])
		safe = False

#extra dangerous rocks

	if safe and hungry and spot == "a rock" and random.random() < 0.30:
		predator = random.choice(list(predators.keys()))
		print(f"{predator.capitalize()} approaches from behind the rock!")
		print(predators[predator]["label"])
		safe = False
		
	#if hungry and safe :
        #confidence += sights[spot]["confidence"]

#if confidence < 1 :
    #active = False
if len(seen) == len(sights) :
	active = False
	print("Lunch can wait. Time to sunbathe.")
	
print("Gecko stops. State:") #print these with f strings too
print("hungry:", hungry)
print("safe:", safe)
#if confidence>1: print("confidence:", confidence)
if seen: #anything
	print(f"Seen {len(seen)} spots:", seen)
	print("\nSight summary:")
	for spot in sights :
		if sights[spot]["count"] > 0 :
			print(f"{spot}: {sights[spot]['count']} time(s)")


#TODO
 #i can just go sights[spot]["count"]+=1
#create a set of seen things seen=set() and add things to it seen.add(spot)
#spot = random.choice(list(sights.keys()))


#add specific insects and predators
#set probabilities for insect types
#the robot just recommended a separate list of insects
 #another gecko might appear which is where confidence comes in



#then you can also print how many unique things the gecko discovers
#i can also probably somehow keep count if the gecko comes across a thing multiple times and then print "I've been here before"
#the gecko can have internal commentary based on landmark type
#or i can keep count of seeing something multiple times via dictionary and then comment "this is the third rock today" or "why are there so many pinecones"
#make a way to include "It sounds like you've been carrying an immense burden for your terrarium."


#additional friends:
#"some spiderweb": {
 #   "label": "...nope."
#}

#"a puddle": {
 #   "label": "splish!"
#}

#"a butterfly": {
 #   "label": "too floaty."
#}

#"another gecko": {
 #   "label": ":D"
#}
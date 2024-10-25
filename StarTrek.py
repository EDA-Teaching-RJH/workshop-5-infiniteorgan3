import random 
# Constants 
MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
ship = { 
		"systems": { 
		"shields": 100, 
		"weapons": 100, 
		"engines": 100, 
		"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 

def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	while True: 
		display_status() 
		action = get_user_action() 
		systemstats = list(ship["systems"].keys())
		
		if any(systemstats) <= 0:
			print("Your ship is too damaged to continue operating and you, along with your crew, drift aimlessly subject to the whims of space.")
			print(f"Simulation ended. Final score: {score}.")
			break
		elif ship["resources"]["energy"] <= 0:
			print("You have no energy at all to do anything and all you can do is watch as your systems fail.")

		if action == "1": 
			score += run_mission() 
		elif action == "2": 
			repair_system() 
		elif action == "3": 
			add_crew_member() 
		elif action == "4": 
			print(f"Simulation ended. Final score: {score}.") 
			break 
		else: 
			print("Invalid action. Please try again.") 
		
		ship["resources"]["energy"] -= 50

		currentenergy = ship["resources"]["energy"]

		if currentenergy > 750:
			for i in systemstats:
				ship["systems"][systemstats[i]] -= 5
		elif currentenergy > 500:
			for i in systemstats:
				ship["systems"][systemstats[i]] -= 7
		elif currentenergy > 250:
			for i in systemstats:
				ship["systems"][systemstats[i]] -= 10
		elif currentenergy > 100:
			for i in systemstats:
				ship["systems"][systemstats[i]] -= 12
		else:
			for i in systemstats:
				ship["systems"][systemstats[i]] -= 15



		turns += 1 
		handle_random_event() 

		if turns % 3 == 0: 
			replenish_resources() 

def display_status(): 
# TODO: Implement function to display ship status, resources, and crew 
	print("Ship status:")

	for i in ship.keys():
		for j in ship[i].keys():
			print(f"{j}: {ship[i][j]}")
	

def get_user_action(): 
	while True:
		try:
			userinput = int(input("What action would you like to do?\n1- Run Mission\n2- Repair System\n3- Add Crew Member\n4- End Simulation"))
			break
		finally:
			continue
	return userinput

def run_mission(): 
	mission_type = random.choice(MISSION_TYPES) 
	print(f"\nNew mission: {mission_type}") 
	scoreadded = 0
	# TODO: Implement mission logic for different mission types 
	match (mission_type):
		case "Exploration":
			print("You are exploring a different planet.")
		case "Diplomacy":
			print("You are communicating with a different race.")
		case "Combat":
			print("")
		case "Rescue":
			print("You are required to rescue someone who is stranded.")
		case "Scientific Research":
			print("You are doing some scientific research on gthe ship.")
	# Return the score earned from the mission 
	return scoreadded

def repair_system(): 
# TODO: Implement system repair functionality
	listofsystems = list(ship["systems"])
	for i in listofsystems:
		if ship["systems"][listofsystems[i]] < 70:
			ship["systems"][listofsystems[i]] += 30
		else:
			ship["systems"][listofsystems[i]] = 100

def add_crew_member(): 
# TODO: Implement functionality to add a new crew member 
	preexistingcrew = list(ship["crew"].keys())
	while crewname == "" or crewname in preexistingcrew:
		crewname = input("Please enter the crew member's name.").title().strip()
	crewdivision = ""
	VALID_DIVISIONS = ["Operations", "Command", "Sciences"]

	while crewdivision not in VALID_DIVISIONS:
		crewdivision = input("Please enter a valid assignment for your crew member (Operations, Command or Sciences).")
	
	ship["crew"][crewname] = crewdivision
	


def handle_random_event():
# TODO: Implement random events that can occur during the simulation
	randomeventid = random.randint(1,10)
	match randomeventid:
		case 1:
			tries = 5
			print("You encounter an asteroid that is on track to collide with the ship. You could attempt to maneuver around it, attack it with a torpedo or engage your shields.")
			validresponses = ["maneuver", "torpedo", "shields"]
			inputa = ""
			while inputa not in validresponses and tries > 0:
				inputa = input("What do you do?").lower().strip()
				tries -= 1
			
			match inputa:
				case "maneuver":
					print("You steer around the obstacle, but it requires you to utilise a lot of your engine fuel to quickly evade it.")
					ship["systems"]["engine"] -= 30
					use_resource("energy", 10)
				case "torpedo":
					print("You fire some torpedos at the obstacle, clearing it so that your ship can continue on its path without damage to its systems.")
					use_resource("torpedo", 3)
				case "shields":
					print("You engage the shields to protect the main parts of the ship while you move past the obstacle.")
					ship["systems"]["shields"] -= 10
				case _:
					print("You could not make a decision in time to avoid the obstacle and so the ship becomes damaged.")
					ship["systems"]["engines"] -= 25
					ship["systems"]["sensors"] -= 20


def use_resource(resource, amount):
	if  ship["resources"][resource] >= amount:
		ship["resources"][resource] -= amount
	else:
		ship["resources"][resource] = 0

def replenish_resources(): 
	if ship["resources"]["torpedos"] < 10:
		ship["resources"]["torpedos"] = 10
	
	if ship["resources"]["energy"] > 800:
		ship["resources"]["energy"] = 1000
	else:
		ship["resources"]["energy"] += 200

main()

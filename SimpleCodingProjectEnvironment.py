def effects():
	print ('Choose an event to know its effects to our society.')
	print ('Choice 1: Deforestation')
	print ('Choice 2: Smoke from Vehicles')
	print ('Choice 3: Plastic garbages thrown anywhere')
	print ('Choice 4: To go back to the ongoing events')

	b=input('Enter a number:')

	if b== "1":
		print ('This can cause floods and soil erosion.\n\n')
		effects()
	elif b== "2":
		print ('This can pollute the air which can affect our health. It will be harder to breath.\n\n')
		effects()
	elif b== "3":
		print ('These garbages can harm the living organisms both in the water and the land. Plastics are non-biodegradable.\n\n')
		effects()
	elif b== "4":
		story_begin()
	else:
	    print ('Press 1 to 4 only. Please try again.\n\n')
	    effects()
   


def cause():
	print ('Choose an event to know its causes.')
	print ('Choice 1: Global Warming')
	print ('Choice 2: Dirty Water')
	print ('Choice 3: Animal Extinction')
	print ('Choice 4: To go back to the ongoing events')

	c=input('Enter a number:')

	if c== "1":
		print ('This is caused by illegal cutting of trees. Trees provide oxygen and absorb carbon dioxide.\n\n')
		cause()
	elif c== "2":
		print ('This is caused by throwing of dirty garbages inclduing harmful chemicals into the water.\n\n')
		cause()
	elif c== "3":
		print ('This is caused by illegal hunting and smuggling of rare animal species.\n\n')
		cause()
	elif c== "4":
		story_begin()
	else:
	    print ('Press 1 to 4 only. Please try again.\n\n')
	    cause()
   



def solution():
	print ('\n\nChoose a particular issue to know its preferred solution.')
	print ('Choice 1: Flooding')
	print ('Choice 2: Drought')
	print ('Choice 3: Diseases')
	print ('Choice 4: To go back to the ongoing events')

	w=input('Enter a number:')

	if w== "1":
		print ('Please plant trees and stop illegal logging.\n\n')
		solution()
	elif w== "2":
		print ('Please conserve and stop polluting water.\n\n')
		solution()
	elif w== "3":
		print ('Keep the surroundings clean and manage waste properly.\n\n')
		solution()
	elif w== "4":
		story_begin()
	else:
	    print ('Press 1 to 4 only. Please try again.\n\n')
	    solution()


  


def quiz_ready():
	print ('You can check your environmental knowledge by taking this short quiz. If ready, please press one otherwise press anything.\n')

	q=input('Enter a number: ')

	if q == "1":
	   quiz_start()
	else:
	   print ("You may take the quiz next time when ready.\n\n")
	   story_begin()





def quiz_starta():
	print ('\n\nQuestion 1: What is one of the best ways to solve the environmental pollution?\n')
	print ("Choice 1: Use a recyable or biogradable material.")
	print ('Choice 2: Throw the plastics to the water or just anywhere.')
	print ('Choice 3: Smoke a cigar with many people around.')

	m=input('Enter a number: ')

	if m=="1":
		print('\nYour answer is correct. Very Good!')
	elif m == "2":
		print ('\nThe best answer is Choice 1.')
	elif m== "3":
		print ('\nThe best answer is Choice 1.')
	else:
	    print ('\nPress 1 to 3 only. Try again!')
	    quiz_starta()



def quiz_startb():
	print ('\n\nQuestion 2: What should be done if many trees are cut-down?\n')
	print ('Choice 1: Just let it be.')
	print ('Choice 2: Plant new trees again.')
	print ('Choice 3: Use the logs to get more money and cut more trees without replanting it.')

	m=input('Enter a number:')

	if m=="1":
		print ('\nThe best answer is Choice 2.')
	elif m=="2":
		print ('\nYour answer is correct. Very Good!')
	elif m=="3":
		print ('\nThe best answer is Choice 2.')
	else:
		print ('\nPress 1 to 3 only. Try again!')
		quiz_startb()




def quiz_startc():
	print ('\n\nQuestion 3: Burning coal can pollute the air. What is the best alternative?\n')
	print ('Choice 1: There is no alternative.')
	print ('Choice 2: Use other minerals instead')
	print ('Choice 3: Use new renewable energy source technologies such as the wind turbine and solar panel.')

	m = input('Enter a number:')

	if m=="1":
		print ('\nThe best answer is Choice 3.')
	elif m=="2":
		print ('\nThe best answer is Choice 3.')
	elif m=="3":
	    print ('\nYour answer is correct. Very Good!')
	else:
		print ('\nPress 1 to 3 only. try again!')
		quiz_startc()




def quiz_start ():
     quiz_starta()

     quiz_startb()

     quiz_startc()

     print("\nThanks for taking the short quiz.")
     story_begin()



def conversion():
	print ('\n\nAs you travel around and explore the natural surroundings, you need help with some mathematical quantities. Here are some conversions that you may need.\n')
	print ('Choice 1: The weather is getting hotter due to climate change. You want to change the temperature readings from fahrenheit to celsius.')
	print ('Choice 2: The flood water level is rising quickly as there are no trees. You want to measure the water depth from inches to feet.')
	print ("Choice 3: The storm is approaching and the wind is getting stronger. You are eager to measure its speed from miles per hour to kilometers per hour.")
	print ('Press 4 to leave this conversion.')

	h=input('Enter a number:')

	if h=="1":
		conversiona()
	elif h =="2":
		conversionb()
	elif h =="3":
		conversionc()
	elif h== "4":
		story_begin()
	else:
		print ('Press 1 to 4 only. Please try again')
	conversion ()




def conversiona():
	print ('Please enter the temperature reading in fahrenheit.')

	try:
		fahrenheit = float(input('Enter a numerical value:'))
		celsius = (fahrenheit-32) * 5/9
		print('The temperature value in Degree Celsius is %0.2f' %(celsius))

	except (TypeError, ValueError):
		print('Please type a number only. Try again!')
		conversiona()
   
   

def conversionb():
	print ('Please enter the water depth in inches.')

	try:
		depthinch = float(input('Enter a numerical value:'))
		depthfeet = depthinch/12
		print('The water depth in feet is %0.2f' %(depthfeet))

	except (TypeError, ValueError):
		print('Please type a number only. Try again!')
		conversionb()




def conversionc():
	print ('Please enter the wind speed in miles per hour.')

	try:
		windmph = float(input('Enter a numerical value:'))
		windkmh = windmph * 1.6093440
		print('The wind speed in kilometers per hour is %0.2f' %(windkmh))

	except (TypeError, ValueError):
		print('Please type a number only. Try again!')
		conversionc()


  











 

def main():
   
   print ('\n\nWelcome to the Choose Your Own Coding Environmental Adventure Story!\n\n')
   print ('You have to decide which adventure to take.')
   print ('Are you ready for an exciting adventure? If yes, press 1 and if not, just press something else to leave this program.')
    
   a=input ('Enter a number: ')

   if a == "1":
       story_begin()   
   else:
       print('Thanks for using the program.')

   


def story_begin():

	print ('\n\nLet us begin inside your house. You are about to travel and explore the nature beauty.')
	print ('Before the journey, you want to know what is going on first with the environment as you heard from the news.')
	print ('To know about the situation, please choose among the choices.')
	print ('Choice 1: Know the effects of the ongoing events')
	print ('Choice 2: Know the causes of ongoing events.')
	print ('Choice 3: Know the preferred solutions.')
	print ('Choice 4: Take a check-up quiz.')
	print ('Choice 5: Have some mathematical conversions related to the environment.')
	print ('Choice 6: Leave this program.')

	z=input ('Enter a number: ')

	if z == "1":
		effects()
	elif z == "2":
		cause()
	elif z == "3":
	 	solution()
	elif z == "4":
		quiz_ready()
	elif z == "5":
		conversion()
	elif z == "6":
		print ('Hope you have an exciting adventure. You can come back anytime.')
		exit(0)
	else:
	    print ('Press 1 to 6 only. Try again.')
	    story_begin()
		

	
 






main()

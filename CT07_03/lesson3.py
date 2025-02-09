# print("Hello from lesson 3")

# import time
# study = int(input("How minutes you wanna study? "))

# while (study) != 0 :
#    time.sleep(study*60)
#    study -= 60

# print("Completed ")

savings = 0

while savings < 100:
   daily_saving = float(input("How much did you save today?"))
   savings += daily_saving

   if savings > 100:
      print("AY LET'S GO BRUH! YOU'VE SAVED $100 AND CAN AFFORD CHILD SUPPORT!")
      break

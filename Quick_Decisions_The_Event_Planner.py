# Objective: To practice the use of shorthand if statements. Task 1: You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.
#Task 2: Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.
#Task 3: Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

attendees = float (input("Enter number of attendees: "))
catering = input("Would you need a vegitarian or non-vegitarian menu? ")

venue = "Large Hall" if attendees > 100 else "Conference Room"
print(venue)
if venue == "Large Hall":
    print("How about adding an audio system so everyone can you.")
else:
    print("A screen projector could be helpful when in a conference.")
catering = "Veggie Delight Caterers" if catering == "vegitarian" else "Gourmet Meals Caterers"
print(catering)

# Project in Python 3.6.1 on Mathesis e-learning platform http://mathesis.cup.gr/
# June 2017 "Εκμάθηση Python 3.6.1 " με καθηγητή τον Νικόλαο Αβούρη του Πανεπιστημίου Πατρών 
#Άσκηση <Μάντεψε έναν αριθμό >
#της Νικολαΐδου Δήμητρα Χριστίνα (Ιόλη)

#Εισάγουμε την βιβλιοθήκη random
import random
#Επιλέγουμε έναν τυχαίο αριθμό
random_number = random.randint(1,100)
#Οδηγός παιχνιδιού
print("Σκέφτηκα έναν αριθμό από το 1 ως το 100.\nΈχεις 10 προσπάθειες για να τον βρεις μαζεύοντας πόντους για κάθε κερδισμένη προσπάθεια.\nΠατώντας 0 αντί για αριθμό βγαίνεις οποιαδήποτε στιγμή.")

#Αρχικοποίηση μεταβλητών
letsPlay = "ΝΑΙ"
user_number = 101
tries = 1
lineOfPoints = []

while tries < 11:# or letsPlay == "ΝΑΙ" :
    user_number =int(input("Μάντεψε τον αριθμό (1-100):"))
    if  user_number == 0:break #΄Ελεγχος εξόδου με 0
    elif user_number < 1 or user_number > 100:continue #Επανερώτηση για έξω απ τα όρια κανόνων 
    elif user_number < random_number: #Έλεγχος για το πόσο κοντά μάντεψε ο παίχτης
        print("OXI έδωσες μικρότερο")
        lineOfPoints.append(0)
        tries +=1
    elif user_number > random_number:
        print("OXI έδωσες μεγαλύτερο")
        lineOfPoints.append(0)
        tries +=1
    elif user_number == random_number: #Κέρδισε ο παίχτης
         print("NAIIII το βρήκες μετά από {:02d} προσπάθειες".format(tries))
         lineOfPoints.append(10-tries)
         print("Κέρδισες {:02d} πόντους".format(10-tries))
         print("Συνολικοί πόντοι ως τώρα: {:02d}".format(sum(lineOfPoints)))
         tries = 11
         letsPlay = input("Na ξαναπαίξουμε;(ΝΑΙ/ΟΧΙ)").strip()
         if letsPlay == "ΝΑΙ":
            tries = 1
            random_number = random.randint(1,100)#Επιλέγουμε έναν τυχαίο αριθμό ξανά                            
else: #Αν τελειώσουν οι προσπάθειες ή δωθεί 0 ή δεν θέλει να ξαναπροσπαθήσει
   print("Ευχαριστούμε! Κερδίσατε {:02d} πόντους.".format(sum(lineOfPoints)))
print("Προσπαθήσατε! Καλή συνέχεια...")

    
         
         
    
    
    

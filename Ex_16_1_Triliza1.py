# Project in Python 3.6.1 on Mathesis e-learning platform http://mathesis.cup.gr/
# June 2017 "Εκμάθηση Python 3.6.1 " με καθηγητή τον Νικόλαο Αβούρη του Πανεπιστημίου Πατρών 
# Άσκηση 16_1_template TRILIZA της Νικολαΐδου Δήμητρα Χριστίνα (Ιόλη)


import random
import time

marker = {'Παίκτης 1': 'X', 'Παίκτης 2': 'O', }

def display_board(board): # εμφάνισε την κατάσταση της τρίλιζας
      print( "+"+"-"*61+"+")
      print ("|7 "+board[7]+" "*20+"|8 "+board[8]+" "*20+"|9 "+board[9]+" "*20+"|")
      print( "+"+"-"*61+"+")
      print ("|4 "+board[4]+" "*20+"|5 "+board[5]+" "*20+"|6 "+board[6]+" "*20+"|")
      print( "+"+"-"*61+"+")
      print( "|1 "+board[1]+" "*20+"|2 "+board[2]+" "*20+"|3 "+board[3]+" "*20+"|")
      print( "+"+"-"*61+"+")


def choose_first():#κλήρωση για το ποιός θα παίξει πρώτος
    return(random.sample(marker.keys(),1))

def display_score(score):#Τυπώνει το σκόρ
    for x in score.keys():
       print("Ο " +x+ " κέρδισε "+str(score[x])+ " πόντους !!!!")

def place_marker(board, marker, position): # Τοποθετεί στη θέση position του board τον marker
       board[position]=marker
    

def win_check(board,mark): # επιστρέφει True αν το σύμβολο mark έχει σχηματίσει τρίλιζα
      if mark==board[1]==board[2] and board[2]==board[3]:
       return (True)
 
      elif mark==board[4]==board[5] and board[5]==board[6]:
        return (True)
 
      elif mark==board[7]==board[8]and board[8]==board[9]:
       return (True)
 
      elif mark==board[1]==board[4] and board[4]==board[7]:
       return (True)
 
      elif mark==board[2]==board[5] and board[5]==board[8]:
       return (True)
 
      elif mark==board[3]==board[6] and board[6]==board[9]:
       return (True)
 
      elif mark==board[1]==board[5] and board[5]==board[9]:
       return (True)
 
      elif mark==board[3]==board[5] and board[5]==board[7]:
       return (True)
      else:
        return(False)

def board_check(board): # επιστρέφει True αν υπάρχουν ακόμα κενά τετράγωνα
    kena=-1
    for x in  board:
      if x==' ':
        kena+=1
    if kena==0:
           return(True)
    else:
           return(False)
     
     
 
     
 
def player_choice(board, turn): # Ο Παίκτης turn επιλέγει τετράγωνο
    # Επιστρέφει έναν ακέραιο στο διάστημα [1,9]
 while True:
  try:
   yourChoice = int(input('Σε ποιό τετράγωνο θα θέλατε να τοποθετήσετε το σύμβολό σας;[1-9] '))
  except ValueError:
   print('ΔΕΝ ΕΔΩΣΕΣ ΑΚΕΡΑΙΟ [1-9]')
   continue
  else:
    return(yourChoice)
    break

def replay(): # Ρωτάει τον χρήστη αν θέλει να ξαναπαίξει και επιστρέφει True αν ναι.
    while True:
      QplayAgain=input("Θα θέλατε να ξαναπαίξετε;(N/O)").strip()
      if QplayAgain in ['Nai','N','Ναι','ΝΑΙ','Ν','Ναί'] :
             return(True)
             break
      elif QplayAgain in ['Oxi','O','Οχι','ΟΧΙ','Ο','Όχι'] :
            return(False)
            break
      else : continue     

def next_player(turn): # επιστρέφει τον επόμενο παίκτη που πρέπει να παίξει
   nextPlayer=' '
   if turn==['Παίκτης 1']:
      nextPlayer='Παίκτης 2'
   elif turn==['Παίκτης 2']:
      nextPlayer='Παίκτης 1'
   return(nextPlayer)

def main():
    score = {} # λεξικό με το σκορ των παικτών
    print('Αρχίζουμε!\nΓίνεται κλήρωση ', end = '')
    for t in range(10):
        print(".", flush='True', end=' ')
        time.sleep(0.2)
    print()
    # η μεταβλητή turn αναφέρεται στον παίκτη που παίζει
    turn = choose_first()
    print("\nΟ " + str(turn) + ' παίζει πρώτος.')
    # η μεταβλητή first αναφέρεται στον παίκτη που έπαιξε πρώτος
    first = turn 
    game_round = 1 # γύρος παιχνιδιού
    while True:
        # Καινούργιο παιχνίδι
        # Δημιουργία λίστας 10 στοιχείων βλέπε μάθημα 2 σελ.7 σημειώσεων
        theBoard = [' '] * 10 
        # Αφήστε το πρώτο στοιχείο δηλαδή το theBoard[0] κενό έτσι ώστε 
        # το index να αντιστοιχεί στην ονοματοδότηση των τετραγώνων 
        game_on = True  #ξεκινάει το παιχνίδι
        while game_on:
            display_board(theBoard) #Εμφάνισε την τρίλιζα
            # ο παίκτης turn επιλέγει θέση
            position = player_choice(theBoard, turn) 
            # τοποθετείται η επιλογή του
            place_marker(theBoard, marker[turn[0]], position) 
            if win_check(theBoard, marker[turn[0]]): # έλεγχος αν νίκησε
                display_board(theBoard)
                print('Νίκησε ο '+ str(turn))
                score[turn[0]] = score.get(turn[0], 0) + 1
                game_on = False
            # έλεγχος αν γέμισε το ταμπλό χωρίς νικητή
            elif  board_check(theBoard): 
                display_board(theBoard)
                print('Ισοπαλία!')
                game_on = False
            else: # αλλιώς συνεχίζουμε με την κίνηση του επόμενου παίκτη
                turn =[next_player(turn)]
                
        if not replay():
            ending = ''
            if game_round>1 : ending = 'υς'
            print("Μετά {} γύρο{}".format(game_round, ending))
            display_score(score) # έξοδος ... τελικό σκορ
            break
        else :
            game_round += 1
            # στο επόμενο παιχνίδι ξεκινάει ο άλλος παίκτης
            turn = [next_player(first)]
            first = turn
main()

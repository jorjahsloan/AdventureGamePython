answer = input("Would you like to play? (yes/no) ")

if answer.lower().strip() == "yes":

    answer = input("You walk into the bookstore. Would you like to go left or right?")
    if answer == "left":

        answer = input("You see a book on the floor. Do you pick it up? (yes/no) ")
        if answer == "yes":
            
            answer = input("You pick up the book and see that it's a book about Software Engineering Techniques. Do you read the book? (yes/no) ")
            if answer == "yes":
                
                answer = input("You read the book and feel inspired to improve your coding skills. Do you go on to find another book? (yes/no) ")
                if answer == "yes":
                    
                    answer= input("You go on to find another book, but you bump into someone. They apologise and offer to buy you a coffee. Do you accept? (yes/no) ")
                    if answer == "yes":

                        answer = input("You accept the offer. They reveal that they are a Software Engineer looking for an intern. Do you ask them about the opportunity? (yes/no) ")
                        if answer == "yes":

                            answer = input("You ask them about the opportunity, and they suggest you apply. Do you apply? (yes/no) ")
                            if answer == "yes":

                                print("You apply for the internship and get the position! Congratulations, you win!")

                            elif answer == "no":
                                
                                print("You decline to apply for the internship and miss out on a great opportunity. Game over.")

                            else:
                                input("Invalid option. You can only answer \"yes\" or \"no\". Game over") 

                    elif answer == "no":

                        print("You decline the offer for coffee and leave the bookstore. You missed an opportunity to apply for an internship with the stranger. Game over.")
                       
                    else:
                        input("Invalid option. You can only answer \"yes\" or \"no\". Game Over")

            elif answer == "no":
                print("You decide not to read the book, get bored, and leave. Game over.")

            else:
                input("Invalid option. You can only answer \"yes\" or \"no\". Game over")   

        elif answer == "no":
            answer = input("You decide to leave it on the ground and get bored and leave. Game over.")
            
        else:
            input("Invalid option. You can only answer \"yes\" or \"no\". Game Over")
    
    elif answer == "right":

        answer = input("You see a book on the floor. Do you pick it up? (yes/no) ")
        if answer == "yes":
            
            answer = input("You pick up the book and see that it's a book about Faeries and Angels. Do you read the first chapter? (yes/no) ")
            if answer == "yes":

                answer = input("You read the first chapter and realise it's a smutty book. Do you keep reading? (yes/no)")
                if answer == "yes":

                    answer = input("You read the book cover to cover and have found a new obsession. You go on to purchase the rest of the series. Congratulations, you win!")

                elif answer == "no":
                    print("You decide not to keep reading the book, get bored, and leave. Game over.")

                else: 
                    input("Invalid option. You can only answer \"yes\" or \"no\". Game over")

            elif answer == "no":
                print("You decide not to read the book, get bored, and leave. Game over.")
            
            else:
                input("Invalid option. You can only answer \"yes\" or \"no\". Game over")
        
        elif answer == "no":
                print("You decide not to read the book, get bored, and leave. Game over.")

        else:
                input("Invalid option. You can only answer \"yes\" or \"no\". Game over")

    else:
        print("Invalid option. You can only go \"left\" or \"right\".")

else:
    print("Maybe next time!")
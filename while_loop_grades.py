while True:
    
    user_choice=input("Press 'continue' or 'exit': ")
    
    
    if user_choice=='continue':
        
            try:

                grade=int(input('Enter your score: '))

                if grade >=90:
                    print('A plus grade')

                elif grade >=80:
                    print('A grade')

                elif grade >=70:
                    print( 'B plus grade')

                elif grade >=50:
                    print('B grade')


                elif grade>=30:
                    print('C grade')

                else:
                    print('D grade')

            except ValueError:
                print('Invalid input. Please enter a numerical score.')

    elif user_choice=='exit':
        break
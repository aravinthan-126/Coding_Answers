Net_total_amount=0
def shop():
    global Net_total_amount
    print("Welcome to our Jewelry Shop\n")
    gem_type=['1.Gold','\n2.Silver','\n3.Platinum']
    print("".join(gem_type))
    a=int(input("Enter the prefix number of the gem type you want :"))
    if a==1 or a==2 or a==3:
        ornament_type=['0.Chain','  1.Ring','  2.Braclet','  3.Bangle','  4.Earring']
        print("".join(ornament_type))
        b=int(input("Enter the prefix number of the what kind of ornaments you want : "))
        c=int(input("How many grams of the ornaments you want ? "))
        amount=[7225,100,2567]
        making_charges=[578,8,205]
        if a==1:
            ornament_price= c * amount[0]
            gst=ornament_price * 5 /100
            manking_charges_gold= c * making_charges[0]
            Net_amout=ornament_price + gst + manking_charges_gold
            Net_total_amount +=Net_amout
            print("\n Gem Type = Gold", "\n Ornament type =",ornament_type[b], "\n Grams =",c,"grams ", " \n Ornament price = ",ornament_price,"\n GST = ",gst, "\n Making Charge = ",manking_charges_gold, "\n NetAmount = ", Net_amout)
            again()
        elif a==2:
            ornament_price= c * amount[1]
            gst=ornament_price * 5 /100
            manking_charges_silver= c * making_charges[1]
            Net_amout=ornament_price + gst + manking_charges_silver
            Net_total_amount+=Net_amout
            print("\n Gem Type = Silver", "\n Ornament type =",ornament_type[b], "\n Grams =",c,"grams ", " \n Ornament price = ",ornament_price,"\n GST = ",gst, "\n Making Charge = ",manking_charges_silver, "\n NetAmount = ", Net_amout)
            again()
        elif a==3:
            ornament_price= c * amount[2]
            gst=ornament_price * 5 /100
            manking_charges_platinum= c * making_charges[2]
            Net_amout=ornament_price + gst + manking_charges_platinum
            Net_total_amount+=Net_amout
            print("\n Gem Type = Platinum", "\n Ornament type =",ornament_type[b], "\n Grams =",c,"grams ", " \n Ornament price = ",ornament_price,"\n GST = ",gst, "\n Making Charge = ",manking_charges_platinum, "\n NetAmount = ", Net_amout)
            again()
        else:
            print("Invalid Gem Type")
    else:
        print("Invalid gen type")
        again()
def again():
    option=input("\nEnter 'Y' if you want purchase again or Enter 'N' for Exit : ").upper()
    if option == 'Y':
        shop()
    elif option == 'N':
        print("Thanks for purchesing and visiting our shop...!\nTotal Amount : ",Net_total_amount)
        exit()
    else:
        print("Invalid Input")
        again()
shop()
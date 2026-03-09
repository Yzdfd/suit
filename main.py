import random

suit = ["Gunting", "Batu", "Kertas"]

def computer_choice():
    return random.choice(suit)

def player_choice():
    while True :
        print("1. Gunting")
        print("2. Batu")
        print("3. Kertas")
        choice = input("Pilih Gunting, Batu, atau Kertas (1/2/3) :")
        
        if choice in ['1','2','3']:
            return suit[int(choice)-1]
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def determine_winner(player, computer):
    if player == computer:
        return "Seri!"
    elif (player == "Gunting" and computer == "Kertas") or (player == "Batu" and computer == "Gunting") or (player == "Kertas" and computer == "Batu"):
        return "Anda Menang!"
    else:        
        return "Komputer Menang!"

def main():
    print("Selamat datang di permainan Gunting, Batu, Kertas!")
    
    while True:
        player = player_choice()
        computer = computer_choice()
        
        print(f"Anda memilih: {player}")
        print(f"Komputer memilih: {computer}")
        
        result = determine_winner(player, computer)
        print(result)
        
        play_again = input("Apakah Anda ingin bermain lagi? (y/n): ")
        if play_again.lower() != 'y':
            print("Terima kasih telah bermain!")
            break
        
if __name__ == "__main__":    main()